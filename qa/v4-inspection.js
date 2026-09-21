// V4-only authoring inspection. Never included in the shipped runtime.
const v4Tools=document.createElement('div');
v4Tools.innerHTML='<h3>V4 character evidence</h3><button id="v4-atlas">Character frame atlas</button><button id="v4-focus">Focus alignment</button><button id="v4-continue-clear">Continue clear card</button>';
inspection.prepend(v4Tools);
let v4Atlas=false;
const v4OriginalDraw=draw;
draw=function(){if(v4Atlas)drawV4Atlas();else v4OriginalDraw()};
const v4OriginalJump=document.querySelector('#audit-jump').onclick;
document.querySelector('#audit-jump').onclick=()=>{v4Atlas=false;v4OriginalJump()};
function drawV4Atlas(){
 auditFrozen=true;ctx.fillStyle=PAL.k;ctx.fillRect(0,0,256,240);
 const groups=[['reimuBack_idle_a','reimuBack_idle_b','reimuBack_focus','reimuBack_fire'],['cirno','cirnoB','cirnoFreeze'],['marisa','marisaB','marisaAttack'],['remilia','remiliaB','remiliaFinal']];
 groups.forEach((g,j)=>g.forEach((n,i)=>{const x=32+i*64,y=29+j*59;sprite(n,x,y,1);text(n.replace('reimuBack_','R-').replace('reimu','R').replace('cirno','C').replace('marisa','M').replace('remilia','V'),x-24,y+20,C.white)}));
 document.querySelector('#audit-meta').textContent=JSON.stringify({state:'character-atlas',groups});
};
document.querySelector('#v4-atlas').onclick=()=>{v4Atlas=true;auditFrozen=true;draw()};
document.querySelector('#v4-focus').onclick=()=>{v4Atlas=false;newRun();stage=1;startStage(1);setState('play');player.inv=0;player.focus=true;auditFrozen=true;frame=16;draw();auditMeta()};
document.querySelector('#v4-continue-clear').onclick=()=>{v4Atlas=false;newRun();continues=2;setState('theend');auditFrozen=true;draw();auditMeta()};
