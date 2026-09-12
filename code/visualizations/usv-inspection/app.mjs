import { RULES, POINTS, ROUTES, ZONE, routeMetrics, createState, event, active, propulsion, setNetwork, setPower, pending, start, remainingMargin, tick, countAlerts, executionTrace, report } from './model.mjs';

import { createClassroom } from './learning.mjs';

import { PARTS } from './parts.mjs';

const $ = id => document.getElementById(id);
// 在课程站内返回当前站点；独立启动时链接公开课程主页。
if(location.pathname.includes('/code/visualizations/usv-inspection/'))$('course-home').href='../../../';
const $$ = selector => [...document.querySelectorAll(selector)];
const escapeHTML = value => String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let state=createState(), mode='guided', view='mission', bench='records', scene=null, parts=PARTS, selectedPart='computer', explode=0, evidenceView='original';
let fallback=new URLSearchParams(location.search).get('view')==='2d', webglFailed=false, speed=4, accumulator=0;
let dataSource='standard', threshold=80, operator='>=', traceIndex=-1, traceSignature='';
const samples={standard:[65,80,81],ordinary:[65,81],boundary:[80],empty:[]};
const sourceNames={standard:'标准课堂数据 · M1 的三个时刻',ordinary:'独立统计样例 · 普通值',boundary:'独立统计样例 · 边界值',empty:'独立统计样例 · 空记录',mission:'当前航次 · 岸站已收的有效温度'};
let noticeTimer, learning=null;
function notify(text){$('notice').textContent=text;clearTimeout(noticeTimer);noticeTimer=setTimeout(()=>$('notice').textContent='',4500);}
function currentReadings(){return dataSource==='mission'?state.records.filter(r=>r.delivered&&r.temperature!==null).map(r=>r.temperature):samples[dataSource];}
function applyView(next){view=next;$$('[data-view]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.view===view));$('spatial').hidden=view==='data';$('data-view').hidden=view!=='data';$('route-panel').hidden=view==='system';$('parts-panel').hidden=view!=='system';$('explode-tools').hidden=view!=='system';}
function switchView(next){applyView(next);render();}
function switchBench(next,scroll=false){bench=next;$$('[data-bench]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.bench===bench));for(const name of ['records','image','report','model'])$(`bench-${name}`).hidden=bench!==name;render();if(scroll)$(`bench-${bench}`).scrollIntoView({behavior:'smooth',block:'start'});}
function setFallback(on){fallback=on;const show=on||webglFailed;$('render-host').hidden=show;$('fallback').toggleAttribute('hidden',!show);$('scene-labels').hidden=show;$('fallback-toggle').setAttribute('aria-pressed',show);$('fallback-toggle').textContent=show?'切回三维':'二维备用';$('renderer-status').textContent=show?(webglFailed?'二维备用 · 三维不可用':'二维备用 · 相同任务状态'):'THREE.JS r180 · 本地资源';for(const id of ['rotate-left','zoom-in','zoom-out','reset-view','focus-part'])$(id).disabled=show;renderFallback();}
function run(){if(mode==='guided'&&!learning?.canRun()){notify('请使用当前问题下方的主要按钮继续课堂任务。');return;}start(state);accumulator=0;render();}
function reset(baseline=false){
  const options=baseline?{}:{route:state.route,capacity:state.capacity,autonomy:state.autonomy,network:state.network,power:state.power,temperatureSensor:state.temperatureSensor};
  state=createState(options);accumulator=0;traceIndex=-1;evidenceView='original';$('reflection').value='';
  if(baseline){dataSource='standard';threshold=80;operator='>=';speed=mode==='guided'?4:1;explode=0;selectedPart='computer';$('speed').value=String(speed);$('threshold').value='80';$('operator').value='>=';$('explode').value='0';scene?.resetView();}
  learning?.reset();$('battery').value=String(state.capacity);$('autonomy').value=state.autonomy?'local':'shore';$('sensor').checked=state.temperatureSensor;render();
}
function advance(){tick(state);if(mode==='guided')learning?.afterTick();render();}
function renderRoutes(){
  for(const [key,route] of Object.entries(ROUTES)){
    const m=routeMetrics(key,state.capacity),b=document.querySelector(`[data-route="${key}"]`);
    b.setAttribute('aria-pressed',key===state.route);b.disabled=state.status!=='ready';b.innerHTML=`<strong>${key==='safe'?'B':key==='direct'?'A':'C'} / ${route.name}</strong><span>${route.note}</span><span class="route-numbers">${m.length.toFixed(0)} m · ${m.seconds} s · ${m.energy.toFixed(1)} Wh</span>`;
  }
  const m=routeMetrics(state.route,state.capacity);$('route-result').textContent=`${m.conflict?'路线穿越禁区': '路线避开禁区'} · 覆盖 ${m.covered.length}/3 点。预计返航剩余 ${m.margin.toFixed(1)} Wh${m.enough?'，达到 6 Wh 保留量。':'，低于 6 Wh 保留量。'}`;
  $('route-result').classList.toggle('warn',m.conflict||m.covered.length<3||!m.enough);
  $('battery').disabled=$('autonomy').disabled=state.status!=='ready';
}
function renderStatus(){
  const alive=active(state), moving=propulsion(state), received=state.records.filter(r=>r.delivered).length;
  let label=state.status==='ready'?'基地待命':state.status==='returned'?'已返航 · 待核报告':state.status==='depleted'?'能量耗尽 · 未返航':!state.running?'任务暂停':!state.power?'船载停机':!state.autonomy&&!state.network?'等待岸站指令':'巡检航行中';
  $('mission-status').textContent=label;$('coverage').innerHTML=`${state.covered.length}<small> / 3</small>`;$('energy').innerHTML=`${Math.max(0,state.capacity-state.used).toFixed(1)}<small> Wh</small>`;
  $('energy-bar').style.width=`${Math.max(0,100*(1-state.used/state.capacity))}%`;
  $('energy-bar').style.background=remainingMargin(state)<RULES.reserveWh?'#c36536':'';
  $('margin').textContent=`预计返航余量 ${remainingMargin(state).toFixed(1)} Wh / 保留量 6 Wh`;
  const statuses=[['感知',alive?'就绪':'停机',alive],['计算',alive?'运行':'停机',alive],['本地记录',alive?'可写入':'保留旧记录',alive],['无线链路',alive&&state.network?'连通':'中断',alive&&state.network],['推进',moving?'执行':'停止',moving],['温度记录',alive&&state.temperatureSensor?'有效':'缺测',alive&&state.temperatureSensor]];
  $('signals').innerHTML=statuses.map(([name,value,on])=>`<span>${name}<b class="${on?'':'off'}">${value}</b></span>`).join('');
  $('local-count').textContent=state.records.length;$('shore-count').textContent=received;$('transfer-arrow').textContent=state.network&&alive?'→':'×';$('queue').textContent=`待补传 ${pending(state)} 条${!state.running?' · 时间已冻结':''}`;
  $('network').textContent=`通信：${state.network?'已连接':'已断开'}`;$('network').setAttribute('aria-pressed',state.network);
  $('power').textContent=`船载：${state.power?'已上电':'已停机'}`;$('power').setAttribute('aria-pressed',state.power);
  $('clock').innerHTML=`${String(state.time).padStart(3,'0')} <small>s</small>`;
  $('start').textContent=state.status==='ready'?'▶ 开始任务':state.status==='returned'&&pending(state)?'▶ 继续补传':'▶ 继续任务';$('start').disabled=state.running||state.status==='depleted'||(state.status==='returned'&&!pending(state));$('pause').disabled=!state.running;$('step').disabled=state.running||state.status==='depleted'||(state.status==='returned'&&!pending(state));
}
function renderScene(){
  $('scene-title').textContent=view==='system'?'感知、计算与存储怎样协作':'从基地到证据';$('scene-kicker').textContent=view==='system'?'SYSTEM / 结构与信息流':'INSPECTION WATER / 教学港区';
  document.querySelector('.scene-key').innerHTML=view==='system'?'<span><i class="teal"></i> 信息 / 控制 / 供电</span><span><i class="orange"></i> 中断或停用</span>':'<span><i class="teal"></i> 实际航迹</span><span><i class="dash"></i> 候选路线</span><span><i class="orange"></i> 禁行水域</span>';
  $('explode-value').textContent=`${explode}%`;
  const part=parts.find(p=>p.id===selectedPart);
  $('scene-note').innerHTML=view==='system'&&part?`<span class="number">↗</span><p><strong>${part.name}：</strong>${part.role}<br><b>${part.flow}</b></p>`:`<span class="number">↗</span><p>${fallback||webglFailed?'二维备用与三维共享任务。':'拖动旋转 · 滚轮缩放。'}虚线是所选路线，实线是已走航迹；P1—P3 是设施巡检点，温度来自同一台推进电机。</p>`;
  $$('[data-part]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.part===selectedPart));
  if(view!=='data')scene?.update(state,view,explode,selectedPart);
  if(fallback||webglFailed)renderFallback();
}
function renderFallback(){
  if(!fallback&&!webglFailed)return;
  const svg=$('fallback');
  if(view==='system'){
    svg.setAttribute('viewBox','0 0 600 390');
    const nodes=[['camera',80,145,'摄像头'],['gps',80,205,'定位'],['temp',80,265,'温度'],['computer',270,200,'船载计算机'],['storage',440,145,'本地存储'],['radio',440,220,'无线通信'],['shore',440,320,'岸站'],['battery',270,95,'电池'],['propulsion',270,320,'推进 / 执行']];
    svg.innerHTML=`<defs><marker id="arrow2d" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6" fill="none" stroke="#436587"/></marker></defs>`+[[80,145,270,200],[80,205,270,200],[80,265,270,200],[270,200,440,145],[440,145,440,220],[440,220,440,320],[270,95,270,200],[270,200,270,320]].map((p,i)=>`<path d="M${p[0]} ${p[1]}L${p[2]} ${p[3]}" stroke="${i===5&&!state.network?'#c36536':'#436587'}" stroke-width="2" ${i===5&&!state.network?'stroke-dasharray="5 6"':''} marker-end="url(#arrow2d)"/>`).join('')+nodes.map(([id,x,y,name])=>`<g transform="translate(${x},${y})"><rect x="-55" y="-19" width="110" height="38" rx="6" fill="${id===selectedPart?'#c4d4e5':'#f6f8fa'}" stroke="#6b849d"/><text text-anchor="middle" y="5" font-size="13" fill="#23374b">${name}</text></g>`).join('');
    return;
  }
  svg.setAttribute('viewBox','-60 -55 120 110');
  svg.innerHTML=`<defs><pattern id="grid2d" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M10 0H0V10" fill="none" stroke="#c3ced9" stroke-width=".2"/></pattern><pattern id="hatch" width="3" height="3" patternUnits="userSpaceOnUse"><path d="M0 3L3 0" stroke="#ce9c6e" stroke-width=".3"/></pattern></defs><rect x="-56" y="-36" width="112" height="75" rx="2" fill="url(#grid2d)"/><rect x="${ZONE.minX}" y="${ZONE.minZ}" width="18" height="21" fill="url(#hatch)" stroke="#cb9563" stroke-width=".4"/><text x="0" y="-33" font-size="2.8" text-anchor="middle" fill="#aa612b">施工禁行</text><polyline points="${ROUTES[state.route].nodes.map(n=>POINTS[n].join(',')).join(' ')}" fill="none" stroke="#71879d" stroke-width=".5" stroke-dasharray="2 1.5"/><polyline points="${state.trail.map(p=>p.join(',')).join(' ')}" fill="none" stroke="#13467a" stroke-width="1"/>`+['B','P1','P2','P3'].map(n=>`<g transform="translate(${POINTS[n]})"><rect x="-5" y="-7" width="10" height="4" fill="#9ea6ae" rx=".5"/><circle r="1.2" fill="${state.covered.includes(n)?'#164d84':'#fafbf4'}" stroke="#5b738c" stroke-width=".4"/><text y="-9" text-anchor="middle" font-size="3.5" fill="#283b4f">${n==='B'?'基地 / 岸站':n}</text></g>`).join('')+`<g transform="translate(${state.position}) rotate(${-state.heading*180/Math.PI})"><path d="M-1.8-2L-1.8 2.5L0 4L1.8 2.5L1.8-2Z" fill="#133a61" stroke="#fff" stroke-width=".3"/><rect x="-.7" y="-1" width="1.4" height="2.7" fill="#d3dee8"/></g>`;
}
function renderProgram(){
  const readings=currentReadings(),signature=JSON.stringify([readings,threshold,operator,dataSource]);if(signature!==traceSignature){traceIndex=-1;traceSignature=signature;}
  const frames=executionTrace(readings,threshold,operator),frame=frames[traceIndex];
  const code=['def count_alerts(readings, threshold):','    count = 0','    for temperature in readings:',`        if temperature ${operator} threshold:`,'            count = count + 1','    return count','',`readings = [${readings.join(', ')}]`,`print(count_alerts(readings, ${threshold}))`];
  $('python-code').innerHTML=code.map((line,i)=>`<span class="code-line ${frame?.line===i+1?'current':''}" ${frame?.line===i+1?'aria-current="step"':''}><span class="line-no">${i+1}</span>${escapeHTML(line)||' '}</span>`).join('');
  $('trace-temp').textContent=frame?.temperature==null?'—':`${frame.temperature} °C`;$('trace-count').textContent=frame?.count??0;$('trace-condition').textContent=frame?.condition??'尚未开始';$('trace-step').disabled=traceIndex>=frames.length-1;
  const count=countAlerts(readings,threshold,operator);$('data-source').textContent=sourceNames[dataSource];$('stat-count').textContent=count;
  $('stat-explanation').textContent=readings.length?`${readings.length} 条有效记录，按 temperature ${operator} ${threshold} °C 统计。${count===0?'未出现满足条件的记录；不能据此认定设备正常。':''}`:'没有记录。返回 0，不代表设备正常。';
  $('reading-bars').innerHTML=readings.length?readings.map((n,i)=>`<div class="bar-wrap"><div class="temp-bar ${countAlerts([n],threshold,operator)?'alert':''}" style="height:${Math.max(6,n)}px"><b>${n} °C</b></div><small>时刻 ${i+1}</small></div>`).join(''):'<p class="muted">∅ 没有记录可供判断</p>';
}
function renderRecords(){
  $('record-badge').textContent=String(state.records.length).padStart(2,'0');
  $('record-rows').innerHTML=state.records.length?state.records.map(r=>`<tr><td>${r.point} / M1</td><td>${r.time} s</td><td>${r.temperature===null?'缺测':r.temperature}</td><td>${r.delivered?`已交回 · ${r.deliveredAt} s`:'船上已存 · 待补传'}</td></tr>`).join(''):'<tr><td colspan="4">尚未采集。请先预测，再开始任务。</td></tr>';
  $('events').innerHTML=state.events.length?[...state.events].reverse().map(e=>`<li class="${e.type}"><time>${String(e.time).padStart(3,'0')} s</time><span>${escapeHTML(e.text)}</span></li>`).join(''):'<li>任务就绪。改变一个条件，观察整个信息链。</li>';
}
function renderEvidence(){
  const available=state.covered.includes('P2');for(const id of ['original','region','extra','review'])$(id).disabled=!available;
  $('evidence-image').src=evidenceView==='extra'?'./evidence/followup.svg':'./evidence/original.svg';
  $('evidence-image').alt=evidenceView==='extra'?'教学构造补拍：斜光下涂层边缘与暗线，内部结构不可见':'教学构造原图：涂装钢板接缝附近有一条暗线';
  $('evidence-image').style.opacity=available?'1':'.24';$('roi').toggleAttribute('hidden',evidenceView!=='region'||!available);
  $('evidence-note').textContent=available?`证据已查看：原图 ${state.originalSeen?'✓':'—'} / 疑似区域 ${state.regionSeen?'✓':'—'} / 补拍 ${state.extraSeen?'✓':'—'}`:'请先完成 P2 巡检，再查看本航次证据。';
  $('review').value=state.review;
  $('review-feedback').textContent=state.review==='crack'?'当前图像不足以证实结构裂纹。报告将保留“待复核”。':state.review==='clear'?'没有看清裂纹不等于排除风险。报告将保留“待复核”。':state.review==='reinspect'?'已选择安排复检。查看全部证据后，可形成注明局限的巡检报告。':'请依据图像选择结论，不把预设 AI 判断当作事实。';
  $('evidence-caption').textContent=$('evidence-image').getAttribute('src').endsWith('followup.svg')?'补拍：斜向光照下，部分暗线沿涂层边缘变化；内部材料状态仍不可见。':'原图：正面光照下的涂装表面暗线，可能来自裂纹、涂层接缝或阴影。';
}
function reportText(){const r=report(state,threshold,operator);return `CS0502 无人船巡检教学报告\n教学模型，非真实航行或检测报告\n路线：${ROUTES[state.route].name}\n状态：${state.status==='returned'?'已返航':'未返航'}；覆盖 ${state.covered.join('、')||'无'}\n时间 ${state.time} s；航程 ${state.distance.toFixed(1)} m；耗能 ${state.used.toFixed(1)} Wh；剩余 ${(state.capacity-state.used).toFixed(1)} Wh\n船上 ${state.records.length} 条；岸站 ${state.records.filter(x=>x.delivered).length} 条；待交回 ${pending(state)} 条\n有效温度（岸站）：[${r.received.map(x=>x.temperature).join(', ')}] °C\n规则：temperature ${operator} ${threshold}；满足条件 ${r.count} 次${r.received.length?'':'；没有记录，不代表设备正常'}\n图像结论：${r.evidenceReady&&state.review==='reinspect'?'保留疑点，安排进一步复检':'待复核；现有证据不支持定论'}\n检查结果：${r.ready?'可交教学报告，P2 需进一步复检':r.issues.join('；')}\n\n记录\n${state.records.map(x=>`${x.point} M1 / ${x.time} s / ${x.temperature??'缺测'} °C / ${x.delivered?'已交回':'待补传'}`).join('\n')}\n\n事件\n${state.events.map(e=>`${e.time} s ${e.text}`).join('\n')}\n\n复盘\n${$('reflection').value}\n${learning?.exportText()||''}`;}
function renderReport(){
  const r=report(state,threshold,operator);$('report-title').textContent=r.ready?'可交教学报告 · P2 仍需复检':'巡检报告草稿 · 依据待补齐';
  const cells=[['路线与覆盖',`${state.covered.length} / 3 巡检点`,state.crossed||routeMetrics(state.route).conflict?'路线穿越禁区':`已覆盖 ${state.covered.join('、')||'无'}；路线避开禁区`,state.covered.length<3||state.crossed||routeMetrics(state.route).conflict],['返航与资源',state.status==='returned'?'已返航':'尚未返航',`航程 ${state.distance.toFixed(1)} m · ${state.time} s；剩余 ${(state.capacity-state.used).toFixed(1)} Wh`,state.status!=='returned'||state.capacity-state.used<6],['记录完整性',`${r.received.length} 条岸站有效温度`,`船上 ${state.records.length} 条；已交回 ${state.records.filter(x=>x.delivered).length} 条；待补传 ${pending(state)} 条`,r.received.length<3],['温度统计依据',`${r.count} 次满足条件`,`[${r.received.map(x=>x.temperature).join(', ')}] ${operator} ${threshold} °C${r.received.length?'':'；没有记录，不代表正常'}`,!r.received.length],['图像复核',r.evidenceReady&&state.review==='reinspect'?'保留疑点，安排复检':'结论待复核',r.evidenceReady?'已查看原图、疑似区域和补拍；不能确认内部结构状态':'本航次 P2 证据尚未完整查看',!r.evidenceReady||state.review!=='reinspect'],['故障与恢复',`${state.events.filter(e=>e.type==='fault').length} 个故障事件`,state.events.filter(e=>e.type==='fault'||e.type==='recovery').map(e=>`${e.time} s ${e.text}`).join('；')||'本航次未注入故障',false]];
  $('report-content').innerHTML=`<div class="report-grid">${cells.map(([name,title,text,warn])=>`<div class="report-cell ${warn?'warn':''}"><span>${name}</span><strong>${escapeHTML(title)}</strong><p>${escapeHTML(text)}</p></div>`).join('')}</div>${r.issues.length?`<ul class="issue-list">${r.issues.map(i=>`<li>${i}</li>`).join('')}</ul>`:'<p class="note">任务记录齐全，可以交付带“P2 待进一步复检”结论的教学报告。满足温度阈值不等于诊断设备故障。</p>'}`;
  syncReportExport();
  const baseline=routeMetrics('safe');
  $('report-content').insertAdjacentHTML('beforeend',`<p class="small">基准对照（合规绕行 / 60 Wh / 无等待）：${baseline.seconds} s · 耗能 ${baseline.energy.toFixed(1)} Wh · 剩余 ${baseline.margin.toFixed(1)} Wh。${state.status==='returned'?`本航次相对基准：时间差 ${(state.time-baseline.seconds).toFixed(0)} s，耗能差 ${Number((state.used-baseline.energy).toFixed(1))} Wh。`:'本航次尚未返航，暂不比较总时间与总耗能。'}</p>`);
}
function render(){learning?.update();renderRoutes();renderStatus();renderScene();renderRecords();renderProgram();renderEvidence();renderReport();}
function enterFree(){mode='free';$('guided').setAttribute('aria-pressed','false');$('free').setAttribute('aria-pressed','true');applyView('mission');switchBench('records');notify('自由探索保留当前航次，全部控件已展开。');}
learning=createClassroom({
  context:()=>({state,mode,readings:currentReadings(),threshold,operator,dataSource,sourceName:sourceNames[dataSource]}),
  layout:applyView,
  command:(action,value)=>{
    if(action==='route'){state.route=value;render();}
    if(action==='run')run();
    if(action==='pause'){state.running=false;accumulator=0;render();}
    if(action==='network'){setNetwork(state,value);render();}
    if(action==='operator'){operator=value;$('operator').value=value;traceIndex=-1;render();}
    if(action==='data-defaults'){dataSource='mission';threshold=80;operator='>=';$('threshold').value='80';$('operator').value='>=';traceIndex=-1;}
    if(action==='evidence'){if(value==='region'){state.originalSeen=true;state.regionSeen=true;}else if(value==='extra')state.extraSeen=true;evidenceView=value;render();}
    if(action==='review'){state.review=value;render();}
    if(action==='free')enterFree();
    if(action==='render')render();
  },
});

for(const key of Object.keys(ROUTES)){const b=document.createElement('button');b.className='route-card';b.dataset.route=key;$('routes').append(b);b.onclick=()=>{state.route=key;render();};}
$$('[data-view]').forEach(b=>b.onclick=()=>switchView(b.dataset.view));$$('[data-bench]').forEach(b=>b.onclick=()=>switchBench(b.dataset.bench));
$('report-jump').onclick=()=>switchBench('report',true);
$('guided').onclick=()=>{if(mode==='guided')return;mode='guided';reset(true);switchView('mission');$('guided').setAttribute('aria-pressed','true');$('free').setAttribute('aria-pressed','false');notify('课堂引导从基准重新开始。');};
$('free').onclick=enterFree;
$('battery').onchange=e=>{state.capacity=Number(e.target.value);render();};$('autonomy').onchange=e=>{state.autonomy=e.target.value==='local';render();};
$('network').onclick=()=>{setNetwork(state,!state.network);render();};
$('power').onclick=()=>{setPower(state,!state.power);render();};$('sensor').onchange=e=>{state.temperatureSensor=e.target.checked;event(state,e.target.checked?'recovery':'fault',e.target.checked?'温度记录恢复有效；旧缺测值不回填':'温度传感器缺测；后续记录保留空值');render();};
$('start').onclick=run;$('pause').onclick=()=>{state.running=false;accumulator=0;render();};$('step').onclick=()=>{run();if(state.running){advance();state.running=false;render();}};$('speed').onchange=e=>{speed=Number(e.target.value);};$('rerun').onclick=()=>{reset();notify('已清空航次，保留当前配置。');};$('baseline').onclick=()=>{reset(true);notify('基准已恢复，航次、统计规则与复盘已复位。');};
$('fallback-toggle').onclick=()=>{if(webglFailed){notify('当前三维不可用，二维可完成全部核心活动。');return;}setFallback(!fallback);renderScene();};$('rotate-left').onclick=()=>scene?.rotate();$('zoom-in').onclick=()=>scene?.zoom(.85);$('zoom-out').onclick=()=>scene?.zoom(1.18);$('reset-view').onclick=()=>scene?.resetView();$('focus-part').onclick=()=>scene?.focus();$('explode').oninput=e=>{explode=Number(e.target.value);renderScene();};
$('standard').onclick=()=>{dataSource='standard';traceIndex=-1;render();};$$('[data-sample]').forEach(b=>b.onclick=()=>{dataSource=b.dataset.sample;traceIndex=-1;render();});
$('operator').onchange=e=>{operator=e.target.value;render();};
function readThreshold(input){const value=Number(input.value);if(input.value===''||!Number.isFinite(value)||value< -50||value>200)return false;threshold=value;render();return true;}
$('threshold').oninput=e=>{readThreshold(e.target);};$('threshold').onchange=e=>{if(!readThreshold(e.target)){e.target.value=String(threshold);notify('阈值请输入 -50 到 200 的有限数值。');}};
$('trace-step').onclick=()=>{traceIndex++;renderProgram();};$('trace-reset').onclick=()=>{traceIndex=-1;renderProgram();};
$('original').onclick=()=>{state.originalSeen=true;evidenceView='original';render();};
$('region').onclick=()=>{state.regionSeen=true;evidenceView='region';render();};$('extra').onclick=()=>{state.extraSeen=true;evidenceView='extra';render();};$('review').onchange=e=>{state.review=e.target.value;render();};
document.querySelector('.report-preview').ontoggle=()=>{if(document.querySelector('.report-preview').open)syncReportExport();};
for(const type of ['input','change','click'])document.addEventListener(type,()=>{if(document.querySelector('.report-preview').open)syncReportExport();});
function syncReportExport(){const text=reportText();$('report-text').value=text;const url='data:text/plain;charset=utf-8,'+encodeURIComponent(text);$('download-report').href=url;if($('class-download'))$('class-download').href=url;}
$('download-report').onclick=()=>{syncReportExport();document.querySelector('.report-preview').open=true;};
$('route-comparison').innerHTML=`<div class="table-wrap"><table><thead><tr><th>基准：60 Wh</th><th>距离 m</th><th>时间 s</th><th>能耗 Wh</th><th>返航余量 Wh</th></tr></thead><tbody>${Object.entries(ROUTES).map(([key,r])=>{const m=routeMetrics(key);return `<tr><td>${r.name}</td><td>${m.length.toFixed(1)}</td><td>${m.seconds}</td><td>${m.energy.toFixed(1)}</td><td>${m.margin.toFixed(1)}</td></tr>`;}).join('')}</tbody></table></div>`;

// 逻辑固定步长 1 s；倍速仅改变每真实秒执行几步。后台页面不追赶丢失的时间。
let last=performance.now();function loop(now){const delta=Math.min((now-last)/1000,.2);last=now;if(!document.hidden&&state.running){accumulator+=delta*speed;while(accumulator>=1&&state.running){accumulator-=1;advance();}}else accumulator=0;requestAnimationFrame(loop);}requestAnimationFrame(loop);
document.addEventListener('visibilitychange',()=>{last=performance.now();accumulator=0;});
$('speed').value=String(speed);render();
$('parts').innerHTML=parts.map((p,i)=>`<button class="part" data-part="${p.id}"><span>${String(i+1).padStart(2,'0')}</span>${p.name}<b>↗</b></button>`).join('');$$('[data-part]').forEach(b=>b.onclick=()=>{selectedPart=b.dataset.part;renderScene();});
try{const module=await import('./scene.mjs');
  try{scene=module.createScene($('render-host'),$('scene-labels'),id=>{selectedPart=id;renderScene();},()=>{webglFailed=true;setFallback(true);});}catch{webglFailed=true;}
}catch{webglFailed=true;}
setFallback(fallback);render();
