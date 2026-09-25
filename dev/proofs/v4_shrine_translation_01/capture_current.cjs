// Execute the unmodified game's actual drawing functions in a headless Canvas2D.
// These are source-rendered static witnesses, not browser/gameplay QA captures.
const fs=require('fs'),path=require('path'),vm=require('vm');
const {createCanvas}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/@napi-rs/canvas');
const root=path.resolve(__dirname,'../../..');
const outputs=path.join(__dirname,'current');fs.mkdirSync(outputs,{recursive:true});
function game(version){
 const source=fs.readFileSync(path.join(root,version),'utf8');
 const canvas=createCanvas(256,240);canvas.style={};canvas.addEventListener=()=>{};canvas.focus=()=>{};
 const dummy={style:{},addEventListener(){},textContent:''};
 const document={addEventListener(){},getElementById:id=>id==='game'?canvas:dummy,createElement:tag=>tag==='canvas'?createCanvas(256,240):dummy};
 const sandbox={document,innerWidth:256,innerHeight:240,addEventListener(){},requestAnimationFrame(){},sessionStorage:{getItem(){return null}},console,Math,performance:{now(){return 0}}};
 sandbox.window=sandbox;const context=vm.createContext(sandbox);
 vm.runInContext(source.match(/<script>([\s\S]*?)<\/script>/)[1],context);
 return {canvas,context,run:s=>vm.runInContext(s,context)};
}
if(require.main===module)for(const [name,file] of [['v4','versions/v4/index.html'],['v3','versions/sprite-redesign/index.html']]){
 const g=game(file);
 for(const morning of [false,true]){
  g.run(`frame=120;shrine(${morning},120);`);
  fs.writeFileSync(path.join(outputs,`${name}_${morning?'morning':'night'}.png`),g.canvas.toBuffer('image/png'));
 }
 for(const [id,code] of Object.entries({opening:"showDialogue('intro',()=>{},'shrine');dialogue.print=999;draw()",ending:"showDialogue('ending',()=>{},'morning');dialogue.print=999;draw()",notice:"state='notice';stateTick=120;draw()",dawn:"state='dawn';stateTick=250;draw()",ending_scene:"state='endingScene';stateTick=400;draw()",ending_exit:"state='endingExit';stateTick=80;draw()",the_end:"state='theend';stateTick=100;draw()"})){
  g.run(code);fs.writeFileSync(path.join(outputs,`${name}_${id}.png`),g.canvas.toBuffer('image/png'));
 }
 fs.writeFileSync(path.join(outputs,`${name}_dialogue.json`),g.run('JSON.stringify({intro:DIALOGUE.intro,ending:DIALOGUE.ending},null,2)'));
}
module.exports={game};
