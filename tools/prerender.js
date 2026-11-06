// Puts the rendered home page HTML inside <main id="app"> so crawlers that don't run JavaScript can read it.
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const f=path.resolve(__dirname,'..','index.html');
(async()=>{let src=fs.readFileSync(f,'utf8');
 src=src.replace(/<!--prerender-->[\s\S]*?<!--\/prerender-->/,'<!--prerender--><!--/prerender-->');
 fs.writeFileSync(f,src);
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:900}});
 await p.goto('file://'+f+'#home');await p.waitForTimeout(800);
 const inner=await p.evaluate(()=>document.getElementById('app').innerHTML);await b.close();
 src=src.replace('<!--prerender--><!--/prerender-->','<!--prerender-->'+inner.replace(/\$/g,'$$$$')+'<!--/prerender-->');
 fs.writeFileSync(f,src);console.log('prerendered',inner.length,'chars');})();
