// Native integer source inspection adapter; no runtime files are edited.
const path=require('path'),crypto=require('crypto');
const root=path.resolve(__dirname,'../../..');
const out=__dirname;
fs.mkdirSync(out+'/inputs',{recursive:true});
const setup="frame=16;stage=3;stageTick=1800;state='play';sceneKind='';boss=null;dialogue=null;sakuyaDone=false;resetPlayer();player.x=96;player.y=200;player.power=1;player.inv=0;player.lives=3;player.bombs=2;score=123450;hiscore=250000;graze=128;muted=false;enemies=[{type:'familiar',x:56,y:64,t:1},{type:'familiar',x:136,y:64,t:1}];bullets=[{x:40,y:112,c:C.pink},{x:64,y:128,c:C.pink},{x:88,y:144,c:C.pink},{x:112,y:144,c:C.cyan},{x:136,y:128,c:C.cyan},{x:160,y:112,c:C.cyan},{x:48,y:168,c:C.pink},{x:144,y:168,c:C.cyan}];shots=[];effects=[];items=[];lasers=[];bombTimer=0;paused=false;";
for(const v of ['v3','v4']){
 const canvas=new Canvas(),box={document:{getElementById:()=>canvas,createElement:()=>new Canvas(),addEventListener(){}},innerWidth:256,innerHeight:240,addEventListener(){},requestAnimationFrame(){},sessionStorage:{getItem(){return 0}},console,Math};box.window=box;vm.createContext(box);
 const source=fs.readFileSync(root+'/versions/'+(v==='v3'?'sprite-redesign':'v4')+'/index.html','utf8');vm.runInContext(source.match(/<script>([\s\S]*?)<\/script>/)[1],box);
 for(const pose of ['neutral','fire']){
  vm.runInContext(setup+(pose==='fire'?"keys.z=true;shots=[{x:96,y:164},{x:96,y:140}];":"keys.z=false;")+"drawPlay()",box);
  fs.writeFileSync(out+'/inputs/'+v+'-'+pose+'.rgba',canvas.ctx.buf);
 }
 fs.writeFileSync(out+'/inputs/'+v+'-data.json',JSON.stringify(vm.runInContext('({sprites:SPRITES,palette:PAL,ui:UI,colors:C})',box)));
}
