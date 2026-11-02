#!/usr/bin/env node
// Builds the printable rundown (Markdown) from demo.config.json + steps.json, so paper and panel never drift.
// Follows the format: "demo" (minimal panel, so the printout carries the presenter's talking points) or "fgd" (adds note tables).
// Usage: node build-script.mjs path/to/demo.config.json [--format demo|fgd] > Rundown.md
import fs from 'node:fs';
import path from 'node:path';

const configPath=path.resolve(process.argv[2]||'demo.config.json'),base=path.dirname(configPath);
const config=JSON.parse(fs.readFileSync(configPath,'utf8'));
const steps=JSON.parse(fs.readFileSync(path.resolve(base,config.steps||'steps.json'),'utf8'));
const Q=typeof config.questions==='string'?JSON.parse(fs.readFileSync(path.resolve(base,config.questions),'utf8')):config.questions||{};
const roles=config.roles||[],who=key=>roles.find(r=>r.key===key)||{name:key};
const cell=s=>String(s??'').replace(/\|/g,'\\|').replace(/\n/g,' ');
const flag=process.argv.indexOf('--format'),format=flag>0?process.argv[flag+1]:config.format;
const client=config.client||'klien',port=config.port||4000,out=[],fgd=format!=='demo',GUIDE=fgd?'Panduan FGD':'Panduan Demo';

out.push(`# Rundown ${fgd?'FGD':'Demo'} ${config.title||''}`.trim(),'',
 fgd?`Naskah pendamping ${GUIDE} di layar. Isi langkah sama dengan panel (sumber: steps.json).`:`Naskah pembawa untuk ${GUIDE}. Panel di layar hanya berisi tombol langkah, Sebelumnya/Berikutnya dan Catatan, jadi tujuan, poin bicara dan instruksi klik ada di naskah ini (sumber: steps.json).`,'',
 '## Persiapan','',
 `1. Jalankan aplikasinya, lalu proxy demo: \`node demo-proxy.mjs ${path.basename(configPath)}${format!==config.format?' --format '+format:''}\`.`,
 `2. Buka http://localhost:${port}/demo lalu klik **Mulai ${GUIDE} ▶**.`,
 ...(fgd?[
 '3. Panel menempel di bawah layar. Tombol nomor **0, 1, 2, …** untuk lompat langkah, **‹ Sebelumnya / Berikutnya ›** atau panah kiri/kanan untuk berurutan, **▾** untuk mengecilkan.',
 `4. **Info pembawa** (menit, pembawa, poin bicara, instruksi klik) mati secara bawaan karena layar dilihat ${client}; nyalakan hanya di layar tim penyaji.`,
 '5. **Sorot** meredupkan layar di luar bagian yang sedang dibahas; matikan bila peserta ingin melihat keseluruhan.',
 `6. Ketik masukan peserta di kolom **Perlu diubah (masukan ${client})** dan kesepakatan di **Sudah diubah / disepakati**. Di akhir sesi klik **Unduh catatan (.md / .csv)**.`,
 '7. Uji coba sekali dari awal sampai akhir sebelum hari-H, lalu restart dan klik **Kosongkan catatan** agar sesi mulai bersih.']:[
 '3. Panel menempel di bawah layar dalam satu baris: tombol nomor **0, 1, 2, …** untuk lompat langkah, **‹ Sebelumnya / Berikutnya ›** atau panah kiri/kanan untuk berurutan, dan **×** untuk menutup. Bagian layar yang dibahas otomatis disorot.',
 '4. Pegang naskah ini di samping laptop: tujuan, poin bicara dan instruksi klik tiap langkah tidak tampil di layar.',
 '5. Klik **Catatan** untuk membuka kolom tulis masukan langkah itu; jumlahnya muncul sebagai badge di nomor langkah. Unduh .md / .csv dari kolom itu atau dari halaman /demo.',
 '6. Uji coba sekali dari awal sampai akhir sebelum hari-H, lalu restart agar data kembali bersih dan hapus file catatan uji.',
 '7. Pertanyaan (bila ada) ada di naskah ini, tidak di layar.']),
 `8. Peserta yang mencoba sendiri: WiFi yang sama, buka http://<IP-laptop>:${port}/demo, pilih peran di **Masuk bebas sebagai peran**.`,'');
if(config.durationMinutes)out.push(`Durasi: ${config.durationMinutes} menit.`,'');

out.push('## Pemeran','','| Peran | Nama | Kelompok |','|---|---|---|',...roles.map(r=>`| ${cell(r.role)} | ${cell(r.name)} | ${cell(r.group)} |`),'');
out.push('## Ringkasan rundown','','| # | Menit | Langkah | Pembawa | Masuk sebagai | Pertanyaan |','|---|---|---|---|---|---|',
 ...steps.map((s,i)=>`| ${i} | ${cell(s.min)} | ${cell(s.title)} | ${cell(s.who)} | ${cell(who(s.as).name)} | ${cell((s.q||[]).filter(c=>Q[c]).join(', '))} |`),'');

steps.forEach((s,i)=>{
 const r=who(s.as);
 out.push(`## ${i}. ${s.title}${s.min?` (menit ${s.min})`:''}`,'');
 if(s.goal)out.push(`**Tujuan:** ${s.goal}`,'');
 out.push(`**Masuk sebagai:** ${r.name}${r.group?' · '+r.group:''}${s.who?` · **Dibawakan:** ${s.who}`:''}`,'');
 if(s.show?.length)out.push('**Tampilkan:**',...s.show.map(x=>'- '+x),'');
 if(s.q?.length)out.push('**Pertanyaan:**',...s.q.map(c=>Q[c]?`- **${c}** ${Q[c]}`:'- '+c),'');
 if(s.say?.length)out.push('**Sampaikan (pembawa):**',...s.say.map(x=>'- '+x),'');
 if(s.do)out.push(`**Lakukan (pembawa):** ${s.do}`,'');
 out.push(...(fgd?[`| Perlu diubah (masukan ${client}) | Sudah diubah / disepakati |`,'|---|---|','| | |']:['**Catatan:** ______________________________']),'');
});

const used=new Set(steps.flatMap(s=>s.q||[]));const unused=Object.keys(Q).filter(c=>!used.has(c));
if(unused.length)out.push(fgd?'## Pertanyaan cadangan':'## Pertanyaan lain','',...unused.map(c=>`- **${c}** ${Q[c]}`),'');
if(config.notes?.length)out.push('## Catatan untuk pembawa','',...config.notes.map(n=>'- '+n),'');
process.stdout.write(out.join('\n'));
