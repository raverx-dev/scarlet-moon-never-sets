// Illustrative staging only. Reuse actual game actors, dialogue and frame.
// Background/donation overrides exist solely in this disposable VM.
const fs=require('fs'),path=require('path');
const {loadImage}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/@napi-rs/canvas');
const {game}=require('./capture_current.cjs');
const check=process.argv.includes('--check');
(async()=>{
 for(const [mode,id] of [['night','intro'],['morning','ending']]){
  const g=game('versions/v4/index.html');
  g.context.candidateBg=await loadImage(path.join(__dirname,mode==='night'?'night_native.png':'witnesses/morning_without_box.png'));
  g.context.candidateBox=await loadImage(path.join(__dirname,'assets/donation-box-'+mode+'.png'));
  g.run(`background=function(){ctx.drawImage(candidateBg,0,0)};
   donation=function(x,y){ctx.drawImage(candidateBox,Math.round(x)-16,Math.round(y)-11)};
   frame=120;showDialogue('${id}',()=>{},'${mode==='night'?'shrine':'morning'}');dialogue.print=999;drawDialogue();`);
  const out=path.join(__dirname,'witnesses',id+'_dialogue_native.png'),bytes=g.canvas.toBuffer('image/png');
  if(check){if(!fs.readFileSync(out).equals(bytes))throw Error(id+' witness differs')}
  else fs.writeFileSync(out,bytes);
 }
 console.log('Opening and ending staging witnesses: exact reproduction PASS');
})().catch(e=>{console.error(e);process.exit(1)});
