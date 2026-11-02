#!/usr/bin/env node
// Imports the user's question list (.md, .xlsx, .csv, .tsv) into questions.json ({"CODE": "question"}) for the demo panel.
// Usage: node import-questions.mjs <file> [--out questions.json] [--sheet "Nama sheet"]
// Prints a JSON summary (code, question, topic, row) on stdout so steps can be matched to topics. No dependencies.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';

const args=process.argv.slice(2),file=args.find(a=>!a.startsWith('--')&&args[args.indexOf(a)-1]!=='--out'&&args[args.indexOf(a)-1]!=='--sheet');
const opt=k=>{const i=args.indexOf(k);return i>=0?args[i+1]:null};
if(!file){console.error('Usage: node import-questions.mjs <file.md|.xlsx|.csv|.tsv> [--out questions.json] [--sheet name]');process.exit(2)}
const ext=path.extname(file).toLowerCase();

// Column aliases (case-insensitive, Indonesian and English).
const COLS={
 code:['kode','code','no','nomor','id','#'],
 text:['pertanyaan','question','questions','soal','pertanyaan diskusi','daftar pertanyaan'],
 topic:['langkah','step','topik','topic','bagian','fitur','modul','menu','halaman','tema','kategori','category','section']
};
const norm=s=>String(s??'').trim().toLowerCase().replace(/\s+/g,' ');
function fromRows(rows){
 rows=rows.map(r=>r.map(c=>String(c??'').trim())).filter(r=>r.some(Boolean));
 if(!rows.length)return [];
 const headerAt=rows.findIndex(r=>r.some(c=>COLS.text.includes(norm(c))));
 if(headerAt<0){
  // No header: a single text column, or code + text.
  return rows.map(r=>r.filter(Boolean)).map(r=>r.length>1&&/^[A-Za-z]{0,3}[-.]?\d+[a-z]?$/.test(r[0])?{code:r[0],text:r.slice(1).join(' ')}:{text:r.join(' ')});
 }
 const head=rows[headerAt].map(norm),col=k=>head.findIndex(h=>COLS[k].includes(h));
 const ci=col('code'),ti=col('text'),pi=col('topic');
 return rows.slice(headerAt+1).map((r,i)=>({code:ci>=0?r[ci]:'',text:r[ti]||'',topic:pi>=0?r[pi]:'',row:headerAt+i+2})).filter(q=>q.text);
}

function parseDelimited(text,sep){
 const rows=[];let row=[],cell='',q=false;
 for(let i=0;i<text.length;i++){const c=text[i];
  if(q){if(c==='"'&&text[i+1]==='"'){cell+='"';i++}else if(c==='"')q=false;else cell+=c;continue}
  if(c==='"')q=true;else if(c===sep){row.push(cell);cell=''}else if(c==='\n'||c==='\r'){if(c==='\r'&&text[i+1]==='\n')i++;row.push(cell);rows.push(row);row=[];cell=''}else cell+=c}
 if(cell||row.length){row.push(cell);rows.push(row)}
 return rows;
}

function parseMarkdown(text){
 const lines=text.replace(/^﻿/,'').split(/\r?\n/);
 // A Markdown table with a question column wins.
 const table=lines.filter(l=>/^\s*\|.*\|\s*$/.test(l)&&!/^\s*\|[\s:|-]+\|\s*$/.test(l)).map(l=>l.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim().replace(/\*\*/g,'')));
 if(table.length>1&&table[0].some(c=>COLS.text.includes(norm(c))))return fromRows(table);
 // Otherwise headings are topics and list items/lines are questions: "- A1: text", "1. text", "- **A1** text", "A1. text".
 const out=[];let topic='';
 for(const raw of lines){
  const l=raw.trim();if(!l)continue;
  const h=l.match(/^#{1,6}\s+(.*)$/);if(h){topic=h[1].replace(/\*\*/g,'').trim();continue}
  let m=l.match(/^(?:[-*+]\s+|\d+[.)]\s+)?(.*)$/),body=m[1].replace(/\*\*/g,'').trim();if(!body)continue;
  if(!/^[-*+]\s|^\d+[.)]\s/.test(l)&&!/\?$/.test(body)&&!/^[A-Za-z]{1,3}[-.]?\d+[a-z]?\s*[:.)]/.test(body))continue; // skip prose
  const c=body.match(/^\(?([A-Za-z]{1,3}[-.]?\d+[a-z]?)\)?\s*[:.)\-–]?\s+(.+)$/);
  out.push(c?{code:c[1],text:c[2],topic}:{text:body,topic});
 }
 return out;
}

// Minimal .xlsx reader: ZIP central directory + inflate, shared strings and the first (or named) worksheet.
function unzip(buf){
 let eocd=buf.length-22;while(eocd>=0&&buf.readUInt32LE(eocd)!==0x06054b50)eocd--;if(eocd<0)throw Error('Bukan file .xlsx yang valid.');
 const n=buf.readUInt16LE(eocd+10);let p=buf.readUInt32LE(eocd+16);const files={};
 for(let k=0;k<n;k++){
  const method=buf.readUInt16LE(p+10),size=buf.readUInt32LE(p+20),nameLen=buf.readUInt16LE(p+28),extra=buf.readUInt16LE(p+30),comment=buf.readUInt16LE(p+32),local=buf.readUInt32LE(p+42);
  const name=buf.toString('utf8',p+46,p+46+nameLen);p+=46+nameLen+extra+comment;
  const start=local+30+buf.readUInt16LE(local+26)+buf.readUInt16LE(local+28),data=buf.subarray(start,start+size);
  files[name]=()=>method===8?zlib.inflateRawSync(data):data;
 }
 return files;
}
const xmlText=s=>s.replace(/<[^>]+>/g,'').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/&apos;/g,"'").replace(/&#(\d+);/g,(_,d)=>String.fromCodePoint(+d)).replace(/&amp;/g,'&');
function parseXlsx(buf,sheetName){
 const z=unzip(buf),read=n=>z[n]?z[n]().toString('utf8'):'';
 const shared=[...read('xl/sharedStrings.xml').matchAll(/<si>([\s\S]*?)<\/si>/g)].map(m=>[...m[1].matchAll(/<t[^>]*>([\s\S]*?)<\/t>/g)].map(t=>xmlText(t[1])).join(''));
 const wb=read('xl/workbook.xml'),rels=read('xl/_rels/workbook.xml.rels');
 const sheets=[...wb.matchAll(/<sheet\b[^>]*name="([^"]*)"[^>]*r:id="([^"]*)"/g)].map(m=>({name:xmlText(m[1]),rid:m[2]}));
 const pick=(sheetName&&sheets.find(s=>s.name===sheetName))||sheets[0];
 const target=pick&&rels.match(new RegExp(`Id="${pick.rid}"[^>]*Target="([^"]*)"|Target="([^"]*)"[^>]*Id="${pick.rid}"`));
 const sheetPath=target?'xl/'+(target[1]||target[2]).replace(/^\/?xl\//,''):'xl/worksheets/sheet1.xml';
 const colIndex=ref=>{const l=ref.match(/^[A-Z]+/)[0];let n=0;for(const ch of l)n=n*26+ch.charCodeAt(0)-64;return n-1};
 const rows=[];
 for(const r of read(sheetPath).matchAll(/<row\b[^>]*>([\s\S]*?)<\/row>/g)){
  const row=[];
  for(const c of r[1].matchAll(/<c\b([^>]*?)(?:\/>|>([\s\S]*?)<\/c>)/g)){
   const attrs=c[1],inner=c[2]||'',ref=attrs.match(/r="([A-Z]+\d+)"/)?.[1],type=attrs.match(/t="(\w+)"/)?.[1];
   const v=inner.match(/<v>([\s\S]*?)<\/v>/)?.[1];
   const val=type==='s'?shared[+v]:type==='inlineStr'?xmlText(inner.match(/<is>([\s\S]*?)<\/is>/)?.[1]||''):v!==undefined?xmlText(v):'';
   row[ref?colIndex(ref):row.length]=val;
  }
  rows.push(Array.from(row,x=>x??''));
 }
 return {rows,sheet:pick?.name||'sheet1',sheets:sheets.map(s=>s.name)};
}

let items,meta={file:path.resolve(file)};
if(ext==='.md'||ext==='.markdown'||ext==='.txt')items=parseMarkdown(fs.readFileSync(file,'utf8'));
else if(ext==='.csv'){const t=fs.readFileSync(file,'utf8').replace(/^﻿/,'');items=fromRows(parseDelimited(t,(t.split('\n')[0].match(/;/g)||[]).length>(t.split('\n')[0].match(/,/g)||[]).length?';':','))}
else if(ext==='.tsv')items=fromRows(parseDelimited(fs.readFileSync(file,'utf8').replace(/^﻿/,''),'\t'));
else if(ext==='.xlsx'||ext==='.xlsm'){const x=parseXlsx(fs.readFileSync(file),opt('--sheet'));items=fromRows(x.rows);meta.sheet=x.sheet;meta.sheets=x.sheets}
else{console.error(`Format ${ext} belum didukung. Simpan sebagai .md, .xlsx, .csv atau .tsv (Google Sheets: File › Download).`);process.exit(2)}

if(!items.length){console.error('Tidak ada pertanyaan yang terbaca. Pastikan ada kolom "Pertanyaan" (Excel/CSV/tabel) atau daftar butir (Markdown).');process.exit(1)}
const questions={},seen=new Set;let auto=0;
const list=items.map(q=>{let code=(q.code||'').replace(/\s+/g,'');while(!code||seen.has(code))code='Q'+(++auto);seen.add(code);questions[code]=q.text.replace(/\s+/g,' ').trim();return {code,question:questions[code],topic:q.topic||'',row:q.row}});
const out=opt('--out')||'questions.json';
fs.writeFileSync(out,JSON.stringify(questions,null,1)+'\n');
console.log(JSON.stringify({...meta,out:path.resolve(out),count:list.length,topics:[...new Set(list.map(q=>q.topic).filter(Boolean))],questions:list},null,1));
