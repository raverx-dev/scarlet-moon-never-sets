// Version 3 Stage 2 Forest of Magic — 192x240 composition proof
// ART SOURCE ONLY. No runtime integration.
// Requires FOREST_STAGE2_ASSETS from forest_stage2_assets.js.
// Assembled exclusively from exact authored matrices using FOREST_STAGE2_META
// placement rules and the accepted validation fingerprint:
//   central lane x=56..135 mean Rec.709 luminance 29.08
//   outer side columns x=0..15 and x=176..191 mean Rec.709 luminance 85.65
// Do not paint non-path assets into the central bullet lane.

function composeStage2ForestReference() {
  const A = FOREST_STAGE2_ASSETS;
  const W = 192, H = 240;
  const centerSafeLane = [56, 135];
  const pixels = Array.from({length: H}, () => Array(W).fill('.'));
  const placements = [];
  const add = (asset, x, y, layer) => { placements.push({asset, x, y, layer}); };

  const lane = ['forest_path_lane_a', 'forest_path_lane_b', 'forest_path_lane_c'];
  for (let ty = 0; ty < H; ty += 8) for (let tx = 0; tx < W; tx += 8)
    add(lane[((tx >> 3) + (ty >> 3)) % 3], tx, ty, 'path');

  for (let ty = 0; ty < H; ty += 8) {
    add('forest_ground_edge', 48, ty, 'path_edge');
    add('forest_ground_edge', 136, ty, 'path_edge');
  }

  for (const [i, tx] of [0, 16, 32, 144, 160, 176].entries()) {
    if (tx === 0 || tx === 176) add('forest_distant_pines_moonlit', tx, 0, 'pines');
    else add(i % 2 ? 'forest_distant_pines_b' : 'forest_distant_pines_a', tx, 0, 'pines');
  }

  for (let ty = 0; ty < H; ty += 16) {
    for (const tx of [0, 16, 32, 144, 160, 176]) {
      if (ty === 0 && (tx === 0 || tx === 176)) add('forest_canopy_moonlit', tx, ty, 'canopy');
      else if (tx === 32 || tx === 144) add('forest_canopy_shadow', tx, ty, 'canopy');
      else add(((tx >> 4) + (ty >> 4)) % 2 === 0 ? 'forest_canopy_a' : 'forest_canopy_b', tx, ty, 'canopy');
    }
  }

  for (let ty = 16; ty < 224; ty += 16) {
    add((ty >> 4) % 2 === 0 ? 'forest_trunk_straight' : 'forest_trunk_knotted', 0, ty, 'trunk');
    add((ty >> 4) % 2 === 0 ? 'forest_trunk_knotted' : 'forest_trunk_straight', 176, ty, 'trunk');
  }
  add('forest_root_left', 0, 224, 'trunk');
  add('forest_root_right', 176, 224, 'trunk');

  for (const [x, y, a] of [
    [16, 40, 'forest_mushroom_red'], [16, 104, 'forest_mushroom_violet'], [16, 168, 'forest_mushroom_red'],
    [160, 56, 'forest_mushroom_violet'], [160, 120, 'forest_mushroom_red'], [160, 184, 'forest_mushroom_violet'],
    [0, 72, 'forest_mushroom_cluster'], [0, 200, 'forest_mushroom_cluster'],
    [176, 48, 'forest_mushroom_cluster'], [176, 136, 'forest_mushroom_cluster']
  ]) add(a, x, y, 'mushroom');

  for (const y of [24, 88, 152, 216]) {
    add('forest_lantern_small', 4, y, 'light');
    add('forest_lantern_small', 180, y, 'light');
  }
  for (const [i, y] of [16, 36, 56, 76, 96, 116, 136, 156, 176, 196, 216].entries())
    add(i % 2 === 0 ? 'forest_firefly_a' : 'forest_firefly_b', i % 2 === 0 ? 8 : 176, y, 'light');
  for (const [x, y] of [[24, 32], [160, 64], [8, 128], [176, 160], [24, 192], [160, 208]])
    add('forest_wisp', x, y, 'light');

  for (const y of [48, 112, 176]) {
    add('forest_fern', 16, y, 'vegetation');
    add('forest_fern', 160, y, 'vegetation');
  }
  for (const y of [32, 96, 160, 224]) {
    add('forest_shrub', 16, y, 'vegetation');
    add('forest_shrub', 160, y, 'vegetation');
  }
  for (const y of [16, 80, 144, 208]) {
    add('forest_grass_tuft', 40, y, 'vegetation');
    add('forest_grass_tuft', 136, y, 'vegetation');
  }
  for (const y of [0, 16, 32]) {
    add('forest_vine_hanging', 16, y, 'vegetation');
    add('forest_vine_hanging', 160, y, 'vegetation');
  }
  for (const y of [64, 128, 192]) {
    add('forest_path_edge_stone', 40, y, 'ground');
    add('forest_path_edge_stone', 136, y, 'ground');
  }
  for (let i = 0, y = 8; y < 232; y += 16, i++) {
    add(['forest_leaf_a', 'forest_leaf_b', 'forest_leaf_c'][i % 3], 24, y, 'foliage');
    add(['forest_leaf_c', 'forest_leaf_a', 'forest_leaf_b'][i % 3], 160, y, 'foliage');
  }
  for (const [x, y] of [[0, 8], [184, 24], [0, 88], [184, 120], [0, 168], [184, 200]])
    add('forest_leaf_moonlit', x, y, 'foliage');

  for (const p of placements) {
    const m = A[p.asset];
    const path = p.asset.indexOf('forest_path_lane') === 0;
    for (let j = 0; j < m.length; j++) for (let i = 0; i < m[j].length; i++) {
      const ch = m[j][i]; if (ch === '.') continue;
      const x = p.x + i, y = p.y + j;
      if (x < 0 || x >= W || y < 0 || y >= H) continue;
      if (!path && x >= centerSafeLane[0] && x <= centerSafeLane[1]) continue;
      pixels[y][x] = ch;
    }
  }
  return { width: W, height: H, centerSafeLane, placements, matrix: pixels.map(r => r.join('')) };
}

if (typeof module !== 'undefined') module.exports = composeStage2ForestReference;
