// Version 3 Stage 1 Misty Lake — 192x240 composition proof
// ART SOURCE ONLY. No runtime integration.
// Requires STAGE1_MISTY_LAKE from lake_stage1_assets.js.

function composeStage1MistyLakeReference() {
  const A = STAGE1_MISTY_LAKE.assets;
  const W = 192, H = 240;
  const centerSafeLane = [48, 143];
  const pixels = Array.from({length:H}, () => Array(W).fill('.'));
  const placements = [];
  const add = (asset,x,y,layer) => { placements.push({asset,x,y,layer}); };

  const centerCycle = ['lake_water_dark_a','lake_water_dark_b','lake_water_dark_c'];
  const edgeCycle = ['lake_water_dark_a','lake_water_dark_b','lake_water_dark_c','lake_water_edge_d'];
  for (let ty=0; ty<H; ty+=8) for (let tx=0; tx<W; tx+=8) {
    const col=tx>>3, cycle=(col>=6&&col<=17)?centerCycle:edgeCycle;
    add(cycle[(col+(ty>>3))%cycle.length],tx,ty,'base_water');
  }
  for (const ty of [24,56,96,136,176,216]) for (const tx of [0,16,32,136,152,168])
    add('lake_water_band_e',tx,ty+(((tx>>4)&1)*8),'water_band');
  for (const ty of [40,112,184]) for (const tx of [56,72,104,120]) add('lake_water_band_e',tx,ty,'water_band');

  for (let ty=24; ty<H; ty+=32) for (const tx of [0,16,160,176]) {
    add('lake_ripple_cool_a',tx+(((ty>>5)&1)*8),ty,'ripples');
    if (((ty>>5)&1)===0) add('lake_foam_edge_b',tx,ty+8,'foam');
  }
  for (let ty=32; ty<H; ty+=32) for (const tx of [56,80,104,128])
    add((((tx+ty)>>3)&1)===0?'lake_ripple_dim_a':'lake_ripple_dim_b',tx,ty,'ripples');
  for (const [x,y] of [[16,64],[160,72],[24,184],[152,192]]) add('lake_foam_spark_a',x,y,'foam');

  for (const [x,y,a] of [[88,32,'lake_moon_reflect_a'],[96,48,'lake_moon_reflect_b'],[88,64,'lake_moon_reflect_a'],[96,80,'lake_moon_reflect_b'],[88,96,'lake_moon_reflect_a']]) add(a,x,y,'moon_reflection');

  const mistGroups = [
    [8,20,['lake_mist_wisp_a','lake_mist_transition_d','lake_mist_wisp_b','lake_mist_wisp_a','lake_mist_wisp_b']],
    [152,12,['lake_mist_wisp_b','lake_mist_transition_d','lake_mist_wisp_a','lake_mist_wisp_b','lake_mist_wisp_a']],
    [56,40,['lake_mist_wisp_c','lake_mist_wisp_a','lake_mist_wisp_c','lake_mist_wisp_b']],
    [104,56,['lake_mist_wisp_c','lake_mist_wisp_b','lake_mist_wisp_c','lake_mist_wisp_a']]
  ];
  for (const [x0,y0,seq] of mistGroups) seq.forEach((a,i)=>add(a,x0+(i%2?8:0),y0+i*24,'mist'));

  for (const [x,ys,a] of [[0,[96,144,192,216],'lake_edge_cluster_c'],[16,[120,168,208],'lake_shore_stone_a'],[160,[104,152,200],'lake_shore_stone_b'],[176,[128,176,216],'lake_edge_cluster_c']])
    for (const y of ys) add(a,x,y,'shore');

  for (const [x,y,a] of [
    [0,112,'lake_reeds_a'],[16,184,'lake_reeds_b'],[160,120,'lake_reeds_b'],[176,184,'lake_reeds_a'],
    [16,72,'lake_lilypad_a'],[144,80,'lake_lilypad_a'],[24,168,'lake_lilypad_a'],[152,176,'lake_lilypad_a'],
    [8,88,'lake_shore_post'],[24,184,'lake_shore_post'],[168,96,'lake_shore_post'],[152,184,'lake_shore_post'],
    [24,96,'lake_lantern_dim'],[152,112,'lake_lantern_dim'],
    [32,56,'lake_ice_shard'],[144,56,'lake_ice_shard'],[16,152,'lake_ice_shard'],[168,160,'lake_ice_shard'],
    [24,64,'lake_ice_glint'],[152,72,'lake_ice_glint']
  ]) add(a,x,y,'edge_props');

  for (const p of placements) {
    const m=A[p.asset].matrix;
    for (let j=0;j<m.length;j++) for (let i=0;i<m[j].length;i++) {
      const ch=m[j][i]; if (ch==='.') continue;
      const x=p.x+i,y=p.y+j; if (x>=0&&x<W&&y>=0&&y<H) pixels[y][x]=ch;
    }
  }
  return { width:W, height:H, centerSafeLane, placements, matrix:pixels.map(r=>r.join('')) };
}

if (typeof module !== 'undefined') module.exports = composeStage1MistyLakeReference;
