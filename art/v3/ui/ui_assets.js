// Scarlet Moon Never Sets — Version 3 Global UI Chrome (compact deterministic authoring source)
// Governing scope: issue #16, GLOBAL UI CHROME ONLY.
// Baseline: sprite-redesign @ 69d06766c0a6c165f26f71ded96d7b5bd8a122df
// "." = transparency. Existing PAL keys only. No palette extension requested.

export const UI_PAL_KEYS=Object.freeze({
r:"#e83a51",R:"#9a2438",w:"#fff0ce",W:"#d4c4a8",h:"#191528",H:"#2c2438",
f:"#f6b993",F:"#e08a72",k:"#080810",b:"#424d9d",B:"#2a3160",c:"#81d8ed",
C:"#c8f2ff",g:"#f5cb70",G:"#64b58a",p:"#ff93b4",P:"#c45a88",m:"#ae68d7",
M:"#6b3d9a",y:"#ffe08a",s:"#c8c8d8",S:"#8a8aa0",u:"#704638",o:"#c47a4a",
i:"#4aa0c8",n:"#171b39",e:"#21423e",d:"#3a2040",x:"#87243b",v:"#5a8f6a",
l:"#d0e8ff",t:"#8b5a3c",a:"#a9a4b6",z:"#ffd0e0"
});
const A=(w,h,ch=".")=>Array.from({length:h},()=>Array(w).fill(ch));
const rows=m=>m.map(r=>r.join(""));
const mh=rs=>rs.map(r=>[...r].reverse().join(""));
const mv=rs=>[...rs].reverse();
const put=(m,x,y,pat,t=".")=>pat.forEach((r,yy)=>[...r].forEach((ch,xx)=>{
  if(ch!==t&&m[y+yy]&&m[y+yy][x+xx]!==undefined)m[y+yy][x+xx]=ch;
}));

const tl=[
"rrrrrrrr","rRRRRRRR","rR......","rR.gg...","rR.g....","rR......","rR......","rR......"];
const tr=mh(tl),bl=mv(tl),br=mv(tr);
const top=["rrrrrrrr","RRRRRRRR","........","........","........","........","........","........"];
const bottom=mv(top);
const left=Array(8).fill("rR......"),right=mh(left);

const life=["..rrr...",".rwwRr..","rwrrwwr.","rwrRrwr.","rwwrrwr.",".rRwwr..","..rrr...","...R...."];
const bomb=["...g....",".g.r.g..","..rrr...","grrwrgg.","..rwr...",".g.rr.g.","...g....","..R.R..."];
const powerOn=["rrrrrrrr","rggggggr","rgyyyggr","rgyrrggr","rgyrrggr","rgyyyggr","rggggggr","rrrrrrrr"];
const powerOff=["HHHHHHHH","HBBBBBBH","HBhhhhBH","HBhBBhBH","HBhBBhBH","HBhhhhBH","HBBBBBBH","HHHHHHHH"];
const lake=[
"kkkkkkkkkkkkkkkk","kkkkkkkkkaakkkkk","kkkkkkkkaaaakkkk","kkkkkkkaaaaaakkk","kBkkkkkaaaaaakkk",
"BBkkBBkkaaaakkkk","BBBBBBBBBBBBBBBB","BbbBbbBbbBbbBbbB","bbibbbbibbbbibbb","bbbbccbbbbccbbbb",
"bbbbbCbbbbCbbbbb","bbbbccbbbbccbbbb","bBibbbbbBibbbbbb","bbbbbbbbbbbbbbbb","BbbBbbBbbBbbBbbB","BBBBBBBBBBBBBBBB"];
const forest=[
"kkkkkkkkkkkkkkkk","kkekkeekkkekkkkk","keeeevveeeevvkkk","eevevvveevvvvvkk","eveeGveeevGevvek",
"eevvvvvvvvvvvvve","evveeeevveeeevve","kkkkueeekkuuekkk","kkkkuuukkuuukkkk","kkkkutukkuutkkkk",
"kkkkuutukuuukkkk","kkkeeueekueeekkk","kkeeeeeeueeeeekk","keeeevveeeevvkkk","eevvvvvvvvvvvvek","kkkkkkkkkkkkkkkk"];
const mansion=[
"kkkkkkkkkkkkkkkk","kkkkkkkxxkkkkkkk","kkkkkkxxxxkkkkkk","kkkkkxxxxxxkkkkk","kkkHHHHHHHHHHkkk",
"kkHHBBBBBBBBHHkk","kkHBxxxxxxxxBHkk","kkHBxrrxxrrxBHkk","kkHBxrrxxrrxBHkk","kkHBxxxxxxxxBHkk",
"kkHBxxHBBHxxBHkk","kkHBxxHkkHxxBHkk","kkHBxxHkkHxxBHkk","kkHBxxHkkHxxBHkk","kkHHHHHHHHHHHHkk","kkkkkkkkkkkkkkkk"];

const titleTab=(()=>{
  const m=A(32,8);for(let x=4;x<28;x++)m[0][x]="r";
  m[1][3]=m[1][28]="r";for(let x=4;x<28;x++)m[1][x]="R";
  m[2][2]="r";m[2][3]="R";m[2][28]="R";m[2][29]="r";
  m[3][1]="r";m[3][2]="R";m[3][29]="R";m[3][30]="r";[7,8,23,24].forEach(x=>m[3][x]="g");
  m[4][0]="r";m[4][1]="R";m[4][30]="R";m[4][31]="r";[6,25].forEach(x=>m[4][x]="g");
  m[5][1]="R";m[5][30]="R";return rows(m);
})();
const hudDiv=(()=>{
  const m=A(56,8);for(let x=0;x<56;x++)m[3][x]="H";
  [0,1,2,53,54,55].forEach(x=>{m[2][x]="r";m[3][x]="r";m[4][x]="R"});
  [6,7,8,47,48,49].forEach(x=>m[3][x]="g");return rows(m);
})();
const hudPanel=(()=>{
  const m=A(64,240,"k");
  for(let y=0;y<240;y++){m[y][0]="r";m[y][1]="R";m[y][2]=(y>=5&&y<11)||(y>=229&&y<235)?"g":"H";m[y][62]="R";m[y][63]="r"}
  for(let x=0;x<64;x++){m[0][x]="r";m[1][x]="R";m[238][x]="R";m[239][x]="r"}
  for(let y=8;y<232;y+=8){m[y][4]="B";m[y][59]="B"}
  put(m,0,0,tl);put(m,56,0,tr);put(m,0,232,bl);put(m,56,232,br);
  [56,114,174,228].forEach(y=>put(m,4,y-3,hudDiv));
  for(let x=6;x<58;x++)m[145][x]="H";
  [6,7,56,57].forEach(x=>{m[144][x]="R";m[145][x]="r";m[146][x]="R"});
  for(let x=21;x<43;x++){m[204][x]="H";m[225][x]="H"}for(let y=204;y<226;y++){m[y][21]="H";m[y][42]="H"}
  m[204][21]=m[204][42]=m[225][21]=m[225][42]="r";m[205][22]=m[205][41]=m[224][22]=m[224][41]="g";
  return rows(m);
})();
const dialogue=(()=>{
  const m=A(248,62,"k");
  for(let x=0;x<248;x++){m[0][x]="r";m[1][x]="R";m[60][x]="R";m[61][x]="r"}
  for(let y=0;y<62;y++){m[y][0]="r";m[y][1]="R";m[y][246]="R";m[y][247]="r"}
  for(let x=6;x<242;x++){m[3][x]="H";m[58][x]="H"}for(let y=6;y<56;y++){m[y][3]="H";m[y][244]="H"}
  put(m,0,0,tl);put(m,240,0,tr);put(m,0,54,bl);put(m,240,54,br);
  [..."rrrgg"].forEach((ch,x)=>m[5][10+x]=ch);m[6][10]="r";m[7][10]="R";
  [..."ggrrr"].forEach((ch,x)=>m[56][233+x]=ch);m[54][237]="r";m[55][237]="R";
  return rows(m);
})();
const bezel=(()=>{
  const m=A(40,40);
  for(let x=0;x<40;x++){m[0][x]="r";m[1][x]="R";m[38][x]="R";m[39][x]="r"}
  for(let y=0;y<40;y++){m[y][0]="r";m[y][1]="R";m[y][38]="R";m[y][39]="r"}
  for(let x=3;x<37;x++){m[3][x]="w";m[36][x]="w"}for(let y=3;y<37;y++){m[y][3]="w";m[y][36]="w"}
  [[2,2],[35,2],[2,35],[35,35]].forEach(([x,y])=>m[y][x]="g");
  [[5,1],[6,1],[1,5],[1,6],[33,1],[34,1],[38,5],[38,6],[5,38],[6,38],[1,33],[1,34],[33,38],[34,38],[38,33],[38,34]]
    .forEach(([x,y])=>m[y][x]="r");
  return rows(m);
})();
const asset=(width,height,rows)=>Object.freeze({width,height,palette:[...new Set(rows.join(""))].filter(c=>c!==".").sort().join(""),rows:Object.freeze(rows)});
export const UI_ASSETS=Object.freeze({
ui_frame_corner_tl:asset(8,8,tl),ui_frame_corner_tr:asset(8,8,tr),ui_frame_corner_bl:asset(8,8,bl),ui_frame_corner_br:asset(8,8,br),
ui_frame_edge_top:asset(8,8,top),ui_frame_edge_bottom:asset(8,8,bottom),ui_frame_edge_left:asset(8,8,left),ui_frame_edge_right:asset(8,8,right),
ui_frame_title_tab:asset(32,8,titleTab),ui_hud_divider:asset(56,8,hudDiv),ui_hud_panel:asset(64,240,hudPanel),
ui_life_icon:asset(8,8,life),ui_bomb_icon:asset(8,8,bomb),ui_power_cell_on:asset(8,8,powerOn),ui_power_cell_off:asset(8,8,powerOff),
ui_stage_thumb_lake:asset(16,16,lake),ui_stage_thumb_forest:asset(16,16,forest),ui_stage_thumb_mansion:asset(16,16,mansion),
ui_dialogue_frame:asset(248,62,dialogue),ui_portrait_bezel:asset(40,40,bezel)
});
export const UI_LAYOUT_NOTES=Object.freeze({
ui_hud_panel:{logicalBox:"x=192..255, y=0..239",dividerY:[56,114,145,174,228],stageThumbnailSeat:"20x20 bracket local x=21..42,y=204..225; 16x16 thumb at x=23,y=206"},
ui_dialogue_frame:{logicalBox:"248x62; current placement x=4,y=174",contentInterior:"local x=4..243,y=4..57"},
ui_portrait_bezel:{opening:"32x32 transparent opening local x=4..35,y=4..35"},
sharedFrameLanguage:{tiles:["ui_frame_corner_tl","ui_frame_corner_tr","ui_frame_corner_bl","ui_frame_corner_br","ui_frame_edge_top","ui_frame_edge_bottom","ui_frame_edge_left","ui_frame_edge_right","ui_frame_title_tab"],use:"Pause / How To Play / Continue; fill interior with PAL k."}
});
export function validateUiAssets(){
  const allowed=new Set([".",...Object.keys(UI_PAL_KEYS)]),errors=[];
  for(const [name,a] of Object.entries(UI_ASSETS)){if(a.rows.length!==a.height)errors.push(`${name}: height ${a.rows.length} != ${a.height}`);
    a.rows.forEach((r,y)=>{if(r.length!==a.width)errors.push(`${name}: row ${y} width ${r.length} != ${a.width}`);for(const ch of r)if(!allowed.has(ch))errors.push(`${name}: illegal ${ch} at ${y}`)})}
  return Object.freeze({ok:!errors.length,errors});
}
