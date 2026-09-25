// Extract exact source-defined static matrices; never executes the game loop.
const fs=require('fs'),vm=require('vm'),path=require('path'),crypto=require('crypto');
const root=__dirname,repo=path.resolve(root,'../../..');
const result={source_commit:'d7054d2b9b111ff711f44cc3ee5b71268aca6ed8',versions:{}};
for(const [name,file] of [['v3','versions/sprite-redesign/index.html'],['v4','versions/v4/index.html']]){
 const src=fs.readFileSync(path.join(repo,file),'utf8');
 const c=src.match(/^const C=.*$/m)[0],pal=src.match(/^const PAL=.*$/m)[0];
 const sprites=src.slice(src.indexOf('const SPRITES='),src.indexOf('const UI='));
 const ui=src.slice(src.indexOf('const UI='),src.indexOf('const SHRINE='));
 const lake=src.slice(src.indexOf('const LAKE='),src.indexOf('const FOREST='));
 const context={document:{createElement:()=>({getContext:()=>({fillRect(){}})})}};
 vm.createContext(context);vm.runInContext(c+'\n'+pal+'\n'+sprites+'\n'+ui+'\n'+lake+'\nresult={C,PAL,SPRITES,UI,A:LAKE.A,placements:LAKE.placements}',context);
 const v=context.result;
 result.versions[name]={path:file,sha256:crypto.createHash('sha256').update(src).digest('hex'),palette:v.PAL,background:v.C.black,assets:v.A,placements:v.placements};
 if(name==='v4')result.witness={palette:v.PAL,sprites:Object.fromEntries(['reimu','reimuStoryA','cirno','p_cirno','fairyIce'].map(n=>[n,v.SPRITES[n]])),dialogue:v.UI.ui_dialogue_frame};
}
fs.writeFileSync(path.join(root,'evidence/source-matrices.json'),JSON.stringify(result));
console.log('Extracted V3/V4 canonical source matrices and static witness sprites');
