// Create base sphere
polySphere -r 3 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
move -r -os -wd 0 3 0;

// Create middle sphere
polySphere -r 2 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
move -r -os -wd 0 7 0;

// Create head sphere
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
move -r -os -wd 0 9.5 0;

polyCone -r 1 -h 2 -sx 20 -sy 1 -sz 0 -ax 0 1 0 -rcp 0 -cuv 3 -ch 1;
move -r -os -wd 0 9.5 0;
rotate -r -os -fo 73.692452 0 0 ;
move -r 0 0 1.253218 ;
scale -r 0.598521 0.598521 0.598521 ;
rotate -r -os -fo 14.149248 0 0 ;
scale -r 0.638346 1 1 ;
scale -r 1 1 0.645102 ;

polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
move -r 0 9.458782 0 ;
move -r 0 9.458782 0 ;
select -r pSphere4 ;
scale -r 0.276548 0.276548 0.276548 ;
move -r -0.570121 0 0 ;
move -r 0 0 0.818761 ;
move -r 0 0.570983 0 ;
move -r 0.265973 0 0 ;
move -r -0.240212 0 0 ;
move -r 0 0 -0.140005 ;
move -r 0 -0.192598 0 ;
scale -r 0.779849 0.779849 0.779849 ;
duplicate -smartTransform;

move -r 1.0624 0 0 ;
select -r pSphere5 pSphere4 ;
move -r 0 -9.356789 0 ;
select -cl  ;
select -r pSphere5 ;
select -cl  ;
select -r pSphere2 ;
select -cl  ;
CreatePolygonSphere;
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere6 polySphere5
move -r 0 7.764419 0 ;
move -r 0 0 1.538736 ;
scale -r 0.42947 0.42947 0.42947 ;
move -r 0 0.35021 0 ;
move -r 0 0 -0.26042 ;
scale -r 0.636087 0.636087 0.636087 ;
move -r 0 0 0.448707 ;
duplicate -smartTransform;
// Result: pSphere7
move -r 0 -0.854105 0 ;
move -r 0 0 0.216492 ;
duplicate -smartTransform;
// Result: pSphere8
move -r 0 0 -0.338963 ;
select -tgl pSphere7 ;
select -tgl pSphere6 ;
move -r 0 0 -0.0844291 ;
move -r 0 0 0.0772543 ;
// Undo: move -r 0 0 0.0772543 
select -cl  ;
select -r pSphere6 ;
doDelete;
