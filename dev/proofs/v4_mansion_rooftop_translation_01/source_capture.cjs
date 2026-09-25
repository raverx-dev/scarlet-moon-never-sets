const fs=require('fs'),vm=require('vm');const {createCanvas}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/@napi-rs/canvas');
const path=require('path');const root=path.resolve(__dirname,'../../..');const out=path.join(__dirname,'current/');
const main=createCanvas(256,240);main.style={};main.focus=()=>{};main.addEventListener=()=>{};
const document={getElementById:id=>id==='game'?main:{textContent:'',style:{}},createElement:type=>createCanvas(256,240),addEventListener:()=>{}};
const context={document,innerWidth:768,innerHeight:720,addEventListener:()=>{},requestAnimationFrame:()=>{},performance:{now:()=>0},console,localStorage:{getItem:()=>null,setItem:()=>{}},setTimeout:()=>0,clearTimeout:()=>{},navigator:{getGamepads:()=>[]}};context.window=context;vm.createContext(context);
let code=fs.readFileSync(path.join(root,'versions/v4/index.html'),'utf8').split('<script>')[1].split('</script>')[0];
code=code.replaceAll('{alpha:false}','{alpha:true}'); // harness-only transparent output
vm.runInContext(code,context);
const reset=`newRun();stage=3;frame=120;stateTick=120;ctx.clearRect(0,0,256,240);`;
const cmds={gameplay:`drawRoof(120,192,0)`,story:`drawRoof(120,256,0)`,before:`showDialogue('remilia_before',()=>{},'roof');dialogue.print=999;drawDialogue()`,after:`showDialogue('remilia_after',()=>{},'roof');dialogue.print=999;drawDialogue()`,boss:`startBoss('remilia');phaseGap=0;for(let i=0;i<240;i++){player.inv=999;tick()}drawPlay()`,defeat:`startBoss('remilia');sceneKind='remilia';state='defeat';stateTick=45;draw()`,attract:`state='attract';stateTick=1045;draw()`};
for(const [kind,cmd]of Object.entries(cmds)){vm.runInContext(reset+cmd,context);fs.writeFileSync(out+kind+'.png',main.toBuffer('image/png'));}
// Witnesses render the unchanged game actor/UI/bullet code onto a transparent canvas.
// Override only the background dispatcher; alpha=true is a harness setting, not a game edit.
vm.runInContext(`background=()=>{};`,context);
for(const [kind,cmd]of [['story_overlay',cmds.before],['gameplay_overlay',cmds.boss]]){vm.runInContext(reset+cmd,context);fs.writeFileSync(out+kind+'.png',main.toBuffer('image/png'));}
fs.writeFileSync(out+'source_inventory.json',JSON.stringify(vm.runInContext(`({dialogueActors:[[56,124],[200,124]],dialoguePanelY:174,remiliaFrames:['remilia','remiliaB','remiliaFinal'],gameplayMode:'boss remilia / stage3 after 70s',sourceRoofSizes:[[192,240],[256,240]],attractTick:1045,defeatTick:45})`,context),null,2));
console.log('Captured exact source render paths and illustrative overlays');

// Main canvases above are 256 wide. Only gameplay proof and its overlay use 192.
for(const name of ['gameplay','gameplay_overlay']){const {loadImage}=require(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES+'/@napi-rs/canvas');loadImage(out+name+'.png').then(im=>{const c=createCanvas(192,240);c.getContext('2d').drawImage(im,0,0);fs.writeFileSync(out+name+'.png',c.toBuffer('image/png'));});}
