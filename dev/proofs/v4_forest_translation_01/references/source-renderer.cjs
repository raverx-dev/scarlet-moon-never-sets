const fs=require('fs'),vm=require('vm');
class Canvas {
 constructor(){this.width=256;this.height=240;this.data=Buffer.alloc(256*240*4);this.style={};this.c=new Context(this)}
 getContext(){return this.c} addEventListener(){} focus(){}
}
class Context{
 constructor(canvas){this.canvas=canvas;this.fillStyle='#000000';this.t=[1,1,0,0];this.clipbox=[0,0,256,240];this.stack=[];this.globalAlpha=1}
 save(){this.stack.push([this.t.slice(),this.clipbox.slice(),this.fillStyle,this.globalAlpha])}
 restore(){[this.t,this.clipbox,this.fillStyle,this.globalAlpha]=this.stack.pop()}
 translate(x,y){this.t[2]+=x*this.t[0];this.t[3]+=y*this.t[1]}
 scale(x,y){this.t[0]*=x;this.t[1]*=y}
 beginPath(){} rect(x,y,w,h){this.pending=[x,y,x+w,y+h]} clip(){this.clipbox=this.pending}
 fillRect(x,y,w,h){let c=this.fillStyle,rgba;if(c[0]==='#'){if(c.length===4)c='#'+[...c.slice(1)].map(x=>x+x).join('');rgba=[parseInt(c.slice(1,3),16),parseInt(c.slice(3,5),16),parseInt(c.slice(5,7),16),255]}else{rgba=c.match(/[\d.]+/g).map(Number);rgba[3]=(rgba[3]??1)*255}let[a,b,tx,ty]=this.t;let x0=Math.min(x*a+tx,(x+w)*a+tx),x1=Math.max(x*a+tx,(x+w)*a+tx),y0=Math.min(y*b+ty,(y+h)*b+ty),y1=Math.max(y*b+ty,(y+h)*b+ty);for(let j=Math.max(0,y0,this.clipbox[1]);j<Math.min(240,y1,this.clipbox[3]);j++)for(let i=Math.max(0,x0,this.clipbox[0]);i<Math.min(256,x1,this.clipbox[2]);i++){let k=(j*256+i)*4,alpha=rgba[3]/255*this.globalAlpha;for(let n=0;n<3;n++)this.canvas.data[k+n]=Math.round(rgba[n]*alpha+this.canvas.data[k+n]*(1-alpha));this.canvas.data[k+3]=255}}
 drawImage(im,...args){let sx=0,sy=0,sw=im.width,sh=im.height,dx,dy,dw,dh;if(args.length===2){[dx,dy]=args;dw=sw;dh=sh}else [sx,sy,sw,sh,dx,dy,dw,dh]=args;for(let y=0;y<dh;y++)for(let x=0;x<dw;x++){let from=((sy+Math.floor(y*sh/dh))*256+sx+Math.floor(x*sw/dw))*4,to=((dy+y)*256+dx+x)*4;im.data.copy(this.canvas.data,to,from,from+4)}}
}
for(const name of ['v3','public-v4']){
const canvas=new Canvas(),dummy={textContent:'',addEventListener(){}};
const context={console,Math,performance:{now:()=>0},document:{getElementById:id=>id==='game'?canvas:dummy,createElement:()=>new Canvas(),addEventListener(){}},innerWidth:256,innerHeight:240,addEventListener(){},requestAnimationFrame(){},localStorage:{getItem(){return null},setItem(){}},window:{},setInterval(){},clearInterval(){}};
vm.createContext(context);let html=fs.readFileSync('source/'+name+'.html','utf8'),code=html.match(/<script>([\s\S]*?)<\/script>/)[1];vm.runInContext(code,context);
vm.runInContext("frame=60;stage=2;drawForest(60,256,0)",context);fs.writeFileSync('evidence/'+name+'-background.rgba',canvas.data);
vm.runInContext("showDialogue('marisa_before',()=>{},'');dialogue.print=999;frame=60;drawDialogue()",context);fs.writeFileSync('evidence/'+name+'-story.rgba',canvas.data);
vm.runInContext("newRun();startStage(2);setState('play');for(let i=0;i<900;i++){player.inv=999;tick()}draw()",context);fs.writeFileSync('evidence/'+name+'-gameplay.rgba',canvas.data);
}
