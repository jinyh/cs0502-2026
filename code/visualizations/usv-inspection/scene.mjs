import * as THREE from 'three';
import { OrbitControls } from './vendor/OrbitControls.js';
import { POINTS, ROUTES, ZONE, active, propulsion } from './model.mjs';

import { PARTS } from './parts.mjs';

export function createScene(host, labelHost, onSelect, onFail) {
  const renderer = new THREE.WebGLRenderer({antialias:true,alpha:true});
  renderer.setPixelRatio(Math.min(devicePixelRatio,2));
  renderer.setClearColor(0x000000,0); renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.05;renderer.shadowMap.enabled=true; renderer.shadowMap.type=THREE.PCFSoftShadowMap;
  host.appendChild(renderer.domElement);
  renderer.domElement.addEventListener('webglcontextlost', e=>{e.preventDefault();onFail();});
  const scene=new THREE.Scene(), camera=new THREE.PerspectiveCamera(38,1,.1,600);
  const controls=new OrbitControls(camera,renderer.domElement); controls.enableDamping=true; controls.dampingFactor=.1; controls.maxPolarAngle=Math.PI*.48;
  scene.add(new THREE.HemisphereLight(0xffffff,0x798897,2.8));
  const light=new THREE.DirectionalLight(0xfffbeb,3.2); light.position.set(-30,70,25);light.castShadow=true;light.shadow.mapSize.set(2048,2048);Object.assign(light.shadow.camera,{left:-70,right:70,top:65,bottom:-65,near:.1,far:180});light.shadow.bias=-.001;scene.add(light);
  const material = (color, extra={}) => new THREE.MeshStandardMaterial({color,roughness:.7,metalness:.15,...extra});
  function box(parent, size, pos, color, extra={}) { const m=new THREE.Mesh(new THREE.BoxGeometry(...size),material(color,extra));m.position.set(...pos);m.castShadow=true;m.receiveShadow=true;parent.add(m);return m; }
  function cylinder(parent,radius,height,pos,color){const m=new THREE.Mesh(new THREE.CylinderGeometry(radius,radius,height,24),material(color));m.position.set(...pos);m.castShadow=true;parent.add(m);return m;}
  const world=new THREE.Group();scene.add(world);
  box(world,[114,.6,86],[0,-2,0],0x839db7,{metalness:0,roughness:.85});box(world,[114,1,86],[0,-3,0],0x778a9e);
  const grid=new THREE.GridHelper(110,22,0xb7c3cf,0xc4ced9);grid.position.y=-1.65;world.add(grid);
  const zone=new THREE.Mesh(new THREE.PlaneGeometry(ZONE.maxX-ZONE.minX,ZONE.maxZ-ZONE.minZ),material(0xe5b585,{transparent:true,opacity:.45,side:THREE.DoubleSide}));zone.rotation.x=-Math.PI/2;zone.position.set(0,-1.55,(ZONE.minZ+ZONE.maxZ)/2);world.add(zone);
  for(let x=-8;x<=8;x+=4){box(world,[.12,.15,21],[x,-1.4,-20.5],0xc68f5c);}
  for(const key of ['P1','P2','P3']){
    const [x,z]=POINTS[key];const pier=new THREE.Group();pier.position.set(x,0,z-5);world.add(pier);
    box(pier,[10,1.2,5],[0,.4,0],0xd4caba);for(const dx of [-3.5,3.5])cylinder(pier,.65,6,[dx,1.2,0],0x9ea3a9);
    box(pier,[11,.6,1.4],[0,4,0],0xa8b0b9);box(pier,[2.2,2.4,.4],[0,2.5,2.6],key==='P2'?0xcda06f:0x667a8e);
  }
  box(world,[18,1.7,9],[-42,-.1,35],0xcacabc);box(world,[6,5,4],[-47,3,36],0xe7e6d6);box(world,[3,2,.15],[-47,3.5,33.9],0x54687d);
  cylinder(world,.16,9,[-42,4,36],0x4e6072);cylinder(world,.8,.4,[-42,8.6,36],0xd5dce2);
  const routeLine=new THREE.Line(new THREE.BufferGeometry(),new THREE.LineDashedMaterial({color:0x28425d,dashSize:2,gapSize:1.4}));world.add(routeLine);
  const trailLine=new THREE.Line(new THREE.BufferGeometry(),new THREE.LineBasicMaterial({color:0x072f58}));world.add(trailLine);
  const ship=new THREE.Group();scene.add(ship);const structure=new THREE.Group();ship.add(structure);
  for(const x of [-3.4,3.4]){
    const shape=new THREE.Shape();shape.moveTo(-1.3,-6);shape.lineTo(-1.3,3.8);shape.lineTo(0,6.8);shape.lineTo(1.3,3.8);shape.lineTo(1.3,-6);shape.closePath();
    const hull=new THREE.Mesh(new THREE.ExtrudeGeometry(shape,{depth:1.7,bevelEnabled:true,bevelThickness:.2,bevelSize:.2,bevelSegments:2,steps:1}),material(0x1e4369));hull.rotation.x=Math.PI/2;hull.position.set(x,1.6,0);hull.castShadow=true;structure.add(hull);
    box(structure,[2.15,.12,8.4],[x,1.75,-.5],0xe1e3d3);
  }
  box(structure,[7,.4,8],[0,1.6,-.2],0xf1eee0);box(structure,[7.2,.18,.8],[0,1.9,2.5],0x425970);
  const parts=new Map(), propellers=[];
  for(const p of PARTS){
    const g=new THREE.Group();g.position.set(...p.pos);g.userData.part=p.id;parts.set(p.id,g);(p.id==='shore'?scene:ship).add(g);
    if(p.id==='camera') {box(g,[1.7,1.25,1.1],[0,0,0],p.color);const lens=cylinder(g,.43,.35,[0,0,.7],0x112539);lens.rotation.x=Math.PI/2;box(g,[.4,1,.4],[0,-.7,0],0x86929f);}
    else if(p.id==='gps'){cylinder(g,.9,.3,[0,.3,0],p.color);cylinder(g,.15,1,[0,-.3,0],0x5b6c7e);}
    else if(p.id==='radio'){cylinder(g,.1,4.5,[0,1.8,0],p.color);cylinder(g,.5,.15,[0,3.9,0],0xdce2e9);box(g,[1.2,.8,1],[0,-.1,0],p.color);}
    else if(p.id==='temp'){cylinder(g,.28,1,[0,0,0],p.color);box(g,[.9,.5,.6],[0,-.5,0],0x4d5864);}
    else if(p.id==='propulsion'){for(const dx of [-3.4,3.4]){const hub=cylinder(g,.45,1,[dx,0,0],p.color);hub.rotation.x=Math.PI/2;const prop=new THREE.Group();prop.position.set(dx,0,-.7);box(prop,[1.8,.22,.14],[0,0,0],0x96a6b6);box(prop,[.22,1.8,.14],[0,0,0],0x96a6b6);g.add(prop);propellers.push(prop);}}
    else if(p.id==='shore'){box(g,[5,4,3],[0,0,0],0xd5dce2);box(g,[3.8,2.5,.15],[0,.3,1.58],0x2c4660);box(g,[2.8,.7,.17],[0,-.8,1.7],0x9cb8d5);cylinder(g,.1,5,[3,1,0],0x44596e);}
    else {box(g,p.id==='battery'?[3.2,1.1,2.2]:p.id==='computer'?[2.7,1,2.4]:[1.1,.7,1.8],[0,0,0],p.color);for(let i=0;i<4;i++)box(g,[.09,.08,1.5],[-.7+i*.45,.55,0],0xcdd6e0);}
    g.traverse(o=>{if(o.isMesh)o.userData.part=p.id;});
  }
  const flowGroup=new THREE.Group();scene.add(flowGroup);
  const links=[['camera','computer'],['gps','computer'],['temp','computer'],['computer','storage'],['storage','radio'],['radio','shore'],['computer','propulsion'],['battery','computer']];
  const arrows=links.map(()=>{const a=new THREE.ArrowHelper(new THREE.Vector3(1,0,0),new THREE.Vector3(),1,0x466a8f,.7,.35);flowGroup.add(a);return a;});
  let view='mission',selected='computer',currentState,explode=0;
  const labelElements=new Map();function label(id,text){const el=document.createElement('span');el.className='scene-label';el.textContent=text;labelHost.append(el);labelElements.set(id,el);}
  for(const key of ['B','P1','P2','P3'])label(key,key==='B'?'基地 / 岸站':`${key} 巡检点`);label('zone','施工禁行');for(const p of PARTS)label(p.id,p.name);
  const systemFit=aspect=>Math.max(1,1.9/aspect);
  function resetView(){
    if(host.clientWidth&&host.clientHeight){camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix();}
    controls.target.set(view==='system'?2:0,view==='system'?4:0,0);camera.position.set(...(view==='system'?[21,19,27]:[88,99,117]));
    if(view==='system')camera.position.sub(controls.target).multiplyScalar(systemFit(camera.aspect)).add(controls.target);
    controls.minDistance=view==='system'?10:45;controls.maxDistance=view==='system'?100:230;controls.update();
  }
  resetView();
  const observer=new ResizeObserver(()=>{const w=host.clientWidth,h=host.clientHeight;if(!w||!h)return;renderer.setSize(w,h);if(view==='system')camera.position.sub(controls.target).multiplyScalar(systemFit(w/h)/systemFit(camera.aspect)).add(controls.target);camera.aspect=w/h;camera.updateProjectionMatrix();});observer.observe(host);
  const raycaster=new THREE.Raycaster();let down;
  renderer.domElement.addEventListener('pointerdown',e=>{down=[e.clientX,e.clientY];});
  renderer.domElement.addEventListener('pointerup',e=>{if(view!=='system'||!down||Math.hypot(e.clientX-down[0],e.clientY-down[1])>6)return;const r=renderer.domElement.getBoundingClientRect();raycaster.setFromCamera(new THREE.Vector2((e.clientX-r.left)/r.width*2-1,-(e.clientY-r.top)/r.height*2+1),camera);const hits=raycaster.intersectObjects([...parts.values()],true);if(hits[0])onSelect(hits[0].object.userData.part);});
  function update(s,newView,amount,part){
    currentState=s;selected=part;explode=amount/100;
    if(newView!==view){view=newView;resetView();}
    world.visible=view==='mission';flowGroup.visible=view==='system';
    ship.position.set(...(view==='mission'?[s.position[0],0,s.position[1]]:[-3,0,0]));ship.rotation.y=view==='mission'?s.heading:0;ship.scale.setScalar(view==='mission'?.67:1);
    for(const p of PARTS){const g=parts.get(p.id);g.visible=p.id!=='shore'||view==='system';g.position.set(...p.pos.map((v,i)=>v+(view==='system'?p.spread[i]*explode:0)));g.traverse(o=>{if(o.material?.emissive){o.material.emissive.setHex(view==='system'&&p.id===selected?0x274f78:0x000000);o.material.emissiveIntensity=.38;}});}
    propellers.forEach(p=>{p.rotation.z=s.distance*1.8;});
    const routePoints=ROUTES[s.route].nodes.map(n=>new THREE.Vector3(POINTS[n][0],-.8,POINTS[n][1]));routeLine.geometry.dispose();routeLine.geometry=new THREE.BufferGeometry().setFromPoints(routePoints);routeLine.computeLineDistances();
    trailLine.geometry.dispose();trailLine.geometry=new THREE.BufferGeometry().setFromPoints(s.trail.map(p=>new THREE.Vector3(p[0],-.6,p[1])));
    ship.updateMatrixWorld(true);
    links.forEach(([a,b],i)=>{const from=parts.get(a).getWorldPosition(new THREE.Vector3()),to=parts.get(b).getWorldPosition(new THREE.Vector3());const d=to.clone().sub(from);arrows[i].position.copy(from);arrows[i].setDirection(d.clone().normalize());arrows[i].setLength(d.length(),.6,.3);const enabled=active(s)&&(a!=='radio'||s.network)&&(a!=='temp'||s.temperatureSensor)&&(b!=='propulsion'||propulsion(s));arrows[i].setColor(enabled?0x395f85:0xc68055);arrows[i].line.material.transparent=true;arrows[i].line.material.opacity=enabled? .65+.3*(s.time%2):.28;});
  }
  function labels(){
    const placed=[];
    for(const [id,el] of labelElements){const isPart=parts.has(id);el.hidden=view==='system'?(!isPart||![selected,'camera','computer','radio','shore'].includes(id)):isPart;if(el.hidden)continue;
      let p;if(isPart){p=parts.get(id).getWorldPosition(new THREE.Vector3());p.y+=id==='radio'?4.8:1.7;}else if(id==='zone')p=new THREE.Vector3(0,.5,-25);else p=new THREE.Vector3(POINTS[id][0],6,POINTS[id][1]);
      p.project(camera);let x=(p.x*.5+.5)*host.clientWidth,y=(-p.y*.5+.5)*host.clientHeight;
      for(let tries=0;tries<6&&placed.some(a=>Math.abs(a.x-x)<85&&Math.abs(a.y-y)<26);tries++)y+=26;
      y=Math.min(host.clientHeight-30,Math.max(view==='system'?90:30,y));placed.push({x,y});el.style.left=`${x}px`;el.style.top=`${y}px`;el.style.display=Math.abs(p.x)>1||Math.abs(p.y)>1.25||p.z>1?'none':'';el.style.borderColor=id===selected&&view==='system'?'#235689':'';
    }
  }
  let disposed=false;function draw(){if(disposed)return;requestAnimationFrame(draw);if(host.hidden||!host.clientWidth)return;controls.update();labels();renderer.render(scene,camera);}draw();
  return { update,resetView,rotate(){const offset=camera.position.clone().sub(controls.target);offset.applyAxisAngle(new THREE.Vector3(0,1,0),Math.PI/9);camera.position.copy(controls.target).add(offset);controls.update();},zoom(factor){camera.position.sub(controls.target).multiplyScalar(factor).add(controls.target);controls.update();},focus(){const target=parts.get(selected).getWorldPosition(new THREE.Vector3());controls.target.copy(target);camera.position.copy(target).add(new THREE.Vector3(13,12,18));controls.update();},dispose(){disposed=true;observer.disconnect();controls.dispose();renderer.dispose();},get status(){return {view,selected,time:currentState?.time,explode};} };
}
