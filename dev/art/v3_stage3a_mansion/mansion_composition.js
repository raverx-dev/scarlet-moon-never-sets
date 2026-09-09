'use strict';

const operations = [];
const tileRect = (asset, x, y, width, height) => operations.push({ op: 'tile_rect', asset, x, y, width, height });
const place = (asset, x, y) => operations.push({ op: 'place', asset, x, y });

tileRect('mansion_wall_plain', 0, 0, 192, 240);
tileRect('mansion_wall_damask_a', 0, 0, 48, 240);
tileRect('mansion_wall_damask_b', 144, 0, 48, 240);
tileRect('mansion_carpet_center', 64, 0, 64, 240);
place('mansion_carpet_motif', 88, 40);
place('mansion_carpet_motif', 96, 104);
place('mansion_carpet_motif', 88, 176);
tileRect('mansion_carpet_edge_l', 56, 0, 8, 240);
tileRect('mansion_carpet_edge_r', 128, 0, 8, 240);
tileRect('mansion_masonry_shadow', 48, 0, 8, 240);
tileRect('mansion_masonry_shadow', 136, 0, 8, 240);

for (const y of [72, 152, 224]) {
  tileRect('mansion_molding_horizontal', 0, y, 56, 8);
  tileRect('mansion_molding_horizontal', 136, y, 56, 8);
}

for (const x of [0, 40, 136, 176]) {
  place('mansion_pillar_cap', x, 0);
  for (const y of [16,32,48,64,80,96,112,128,144,160,176,192]) place('mansion_pillar_mid', x, y);
  place('mansion_pillar_base', x, 208);
}

for (const [asset,x,y] of [
  ['mansion_window_gothic_a',16,16], ['mansion_window_gothic_b',152,16],
  ['mansion_window_gothic_b',16,88], ['mansion_window_gothic_a',152,88],
  ['mansion_sconce_single',0,40], ['mansion_sconce_double',32,40],
  ['mansion_sconce_double',144,40], ['mansion_sconce_single',176,40],
  ['mansion_sconce_double',0,112], ['mansion_sconce_single',32,112],
  ['mansion_sconce_single',144,112], ['mansion_sconce_double',176,112],
  ['mansion_sconce_single',16,184], ['mansion_sconce_single',160,184],
  ['mansion_painting_frame',16,56], ['mansion_painting_frame',160,56],
  ['mansion_side_table',16,72], ['mansion_vase_flowers',16,64],
  ['mansion_side_table',160,72], ['mansion_vase_flowers',160,64],
  ['mansion_drape_banner',32,128], ['mansion_drape_banner',144,128],
  ['mansion_bust_statue',40,168], ['mansion_side_table',40,184],
  ['mansion_bust_statue',136,168], ['mansion_side_table',136,184],
  ['mansion_chandelier',8,4], ['mansion_chandelier',152,4],
  ['mansion_door_arch_l',48,208], ['mansion_door_arch_r',128,208],
  ['mansion_door_side_l',48,224], ['mansion_door_side_r',128,224],
  ['mansion_corridor_threshold',0,208], ['mansion_corridor_threshold',176,208],
]) place(asset, x, y);

for (const x of [0,16,32,144,160,176]) place('mansion_railing', x, 144);
for (const x of [8,24,152,168]) {
  place('mansion_bookcase', x, 160);
  place('mansion_bookcase', x, 176);
}
for (const x of [64,80,96,112]) {
  place('mansion_corridor_shadow', x, 208);
  place('mansion_corridor_shadow', x, 224);
}

module.exports = Object.freeze({
  width: 192,
  height: 240,
  operations: Object.freeze(operations.map(Object.freeze)),
  rule: 'Every visible proof pixel is copied from exact mansion_* matrices; no external art or scene primitives.',
});
