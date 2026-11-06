// Reads the services and areas from index.html (as the browser builds them) into tools/data.json
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const root=path.resolve(__dirname,'..');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+root+'/index.html');await p.waitForTimeout(600);
const data=await p.evaluate(()=>({
  areas:AREAS, general:GENERAL_FAQ,
  services:SERVICES.map(s0=>{const s={intro:s0.short,includes:["Site visit and assessment","Clear written quote","Materials sourced on request","Clean-up after work","90-day workmanship warranty"],faq:[["How do I get a quote?","Send photos on WhatsApp or book a free site visit. You get a clear written quote before any work starts."]],process:PROCESS[s0.cat]||PROCESS.Technical,...s0};
   return {id:s.id,name:s.name,cat:s.cat,short:s.short,intro:s.intro,includes:s.includes,process:s.process,processTitle:s.processTitle||'How we work',finishes:s.finishes||null,finishesTitle:s.finishesTitle||null,faq:[...s.faq,...GENERAL_FAQ],photo:s.photo||null,photoAlt:s.photoAlt||s.name,photo2:s.photo2||null,photo2Alt:s.photo2Alt||'',time:s.time||''};})
}));
fs.writeFileSync(path.join(__dirname,'data.json'),JSON.stringify(data,null,1));console.log('services',data.services.length);await b.close();})();
