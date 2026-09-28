const fs=require('fs'),vm=require('vm');
class Canvas{constructor(){this.width=256;this.height=240;this.style={};this.ctx=new Context(this)}getContext(){return this.ctx}addEventListener(){}focus(){}}
class Context{
 constructor(c){this.c=c;this.buf=new Uint8Array(256*240*4);this.t=[1,1,0,0];this.bounds=[0,0,256,240];this.stack=[];this.fillStyle='#000000'}
 ensure(){if(this.buf.length!==this.c.width*this.c.height*4){this.buf=new Uint8Array(this.c.width*this.c.height*4);this.bounds=[0,0,this.c.width,this.c.height]}}
 save(){this.stack.push([[...this.t],[...this.bounds],this.fillStyle])}restore(){[this.t,this.bounds,this.fillStyle]=this.stack.pop()}
 translate(x,y){this.t[2]+=x*this.t[0];this.t[3]+=y*this.t[1]}scale(x,y){this.t[0]*=x;this.t[1]*=y}
 beginPath(){this.path=null}rect(x,y,w,h){this.path=[x,y,x+w,y+h]}clip(){this.bounds=this.bounds.map((v,i)=>i<2?Math.max(v,this.path[i]):Math.min(v,this.path[i]))}
 fillRect(x,y,w,h){this.ensure();x=this.t[2]+x*this.t[0];y=this.t[3]+y*this.t[1];w*=this.t[0];h*=this.t[1];if(w<0){x+=w;w=-w}if(h<0){y+=h;h=-h}let col=this.fillStyle;if(!/^#[a-f0-9]{6}$/i.test(col))throw Error('color '+col);let rgb=parseInt(col.slice(1),16);let a=this.bounds;for(let yy=Math.max(0,a[1],Math.round(y));yy<Math.min(this.c.height,a[3],Math.round(y+h));yy++)for(let xx=Math.max(0,a[0],Math.round(x));xx<Math.min(this.c.width,a[2],Math.round(x+w));xx++){let p=(yy*this.c.width+xx)*4;this.buf[p]=rgb>>16;this.buf[p+1]=(rgb>>8)&255;this.buf[p+2]=rgb&255;this.buf[p+3]=255}}
 drawImage(c,...v){this.ensure();let sx=0,sy=0,sw=c.width,sh=c.height,dx,dy,dw,dh;if(v.length===2){[dx,dy]=v;dw=sw;dh=sh}else if(v.length===4){[dx,dy,dw,dh]=v}else [sx,sy,sw,sh,dx,dy,dw,dh]=v;const b=c.ctx.buf.slice();for(let y=0;y<dh;y++)for(let x=0;x<dw;x++){const xx=dx+x,yy=dy+y;if(xx<0||xx>=this.c.width||yy<0||yy>=this.c.height||xx<this.bounds[0]||yy<this.bounds[1]||xx>=this.bounds[2]||yy>=this.bounds[3])continue;const src=(Math.floor(sy+y*sh/dh)*c.width+Math.floor(sx+x*sw/dw))*4,dst=(yy*this.c.width+xx)*4;if(b[src+3])this.buf.set(b.subarray(src,src+4),dst)}}
}
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
