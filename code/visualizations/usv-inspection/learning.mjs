import { ROUTES, routeMetrics, pending, countAlerts, report } from './model.mjs';

export const PILLARS = [
  {id:'computation',name:'计算思维',question:'怎样把任务变成可执行的步骤？'},
  {id:'system',name:'系统思维',question:'哪个环节中断，影响哪些能力？'},
  {id:'data',name:'数据思维',question:'这个统计数有什么依据？'},
  {id:'intelligence',name:'智能思维',question:'什么新证据能改变判断？'},
];
const flightSteps=['sailing','offline-run','recovery-run','returning'];
export const isFlightStep=step=>flightSteps.includes(step);
export function newLesson(){return {step:'route',steps:{},missionStep:'route',choice:null,networkGuess:null,guess:null,initialImage:null,conclusion:null,offlineStart:0,recoveryStart:0,before:null,offline:null,recovered:null,routeEvidence:null,dataEvidence:[],imageEvidence:null};}
export function lessonPillar(step){
  if(['route','route-result','route-summary','sailing'].includes(step))return 0;
  if(['system-intro','system-summary','network','offline-run','offline','recovery-run','recovered','returning'].includes(step))return 1;
  if(['data','data-result','strict','strict-result'].includes(step))return 2;
  return step==='report'?4:3;
}
export function rememberStep(c,step){
  c.step=step;
  const index=lessonPillar(step);
  if(index<4)c.steps[index]=step;
  if(['route','route-result','network','offline','recovered',...flightSteps].includes(step))c.missionStep=step;
}
// 导航只选择教学页面，不生成记录、不移动船位，也不改写以前的实验。
export function pillarStep(c,s,id){
  switch(id){
    case 'computation':return s.status==='ready'?(c.steps[0]||'route'):'route-summary';
    case 'system':return ['returned','depleted'].includes(s.status)?'system-summary':(c.steps[1]||(s.covered.includes('P1')?'network':'system-intro'));
    case 'data':return c.steps[2]||'data';
    case 'intelligence':return s.covered.includes('P2')?(c.steps[3]&&c.steps[3]!=='image-intro'?c.steps[3]:'image'):'image-intro';
    default:throw new Error('Unknown thinking pillar');
  }
}
export function snapshot(s){return {time:s.time,local:s.records.length,shore:s.records.filter(r=>r.delivered).length,queue:pending(s),autonomy:s.autonomy,position:[...s.position],power:s.power,network:s.network};}
export function checkpoint(c,s){
  if(!isFlightStep(c.step))return false;
  const old=c.step;
  if(s.status==='depleted'){c.step='report';s.running=false;}
  else if(s.status==='returned'&&c.step!=='recovery-run'){c.step='data';s.running=false;}
  else if(c.step==='sailing'&&s.covered.includes('P1')){c.step='network';s.running=false;}
  else if(c.step==='offline-run'&&((s.autonomy&&s.covered.includes('P2'))||(!s.autonomy&&s.time-c.offlineStart>=5))){c.offline=snapshot(s);c.step='offline';s.running=false;}
  else if(c.step==='recovery-run'&&s.network&&s.power&&pending(s)===0&&s.time>c.recoveryStart){c.recovered=snapshot(s);c.step='recovered';s.running=false;}
  return old!==c.step;
}
const esc=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const distance=(a,b)=>Math.hypot(a.position[0]-b.position[0],a.position[1]-b.position[1]);
const countText=o=>o?`${o.time} s · 船上 ${o.local} 条 / 岸站 ${o.shore} 条 / 待交回 ${o.queue} 条`:'尚无该时刻的证据';
const imageNames={crack:'更像裂纹',surface:'更像涂层边缘或阴影',unknown:'暂时保留多个候选'};
export function createClassroom({context,command,layout}){
  const $=id=>document.getElementById(id);
  let c=newLesson(),enabled=true,drawKey='',optionsKey='',dataKey='';
  const homes=new Map();
  function move(node,target){if(!homes.has(node)){const marker=document.createComment('classroom resource home');node.before(marker);homes.set(node,marker);}if(node.parentElement!==target)target.append(node);}
  function home(node){const marker=homes.get(node);if(marker&&node.parentNode!==marker.parentNode)marker.after(node);}
  const scene=document.querySelector('.scene-column'),photo=document.querySelector('.evidence-frame'),program=document.querySelector('.program-panel'),readings=document.querySelector('.readings-panel'),transport=document.querySelector('.transport'),status=document.querySelector('.right-panel'),parts=$('parts-panel'),reportPanel=$('bench-report'),battery=$('battery');
  const shell=document.createElement('section');shell.id='classroom';shell.className='classroom';
  shell.innerHTML=`<nav id="class-progress" class="class-progress" aria-label="课堂进度"></nav><header class="class-heading"><div><p id="class-kicker" class="eyebrow"></p><h1 id="class-title"></h1><p id="class-lead"></p></div><button id="class-settings-open" class="quiet">实验设置</button></header><div class="class-layout"><div id="class-visual" class="class-visual"></div><aside class="class-action"><div id="class-choices" class="class-choices"></div><div id="class-result" class="class-result" role="status"></div><div id="class-concept" class="class-concept"></div><button id="class-next" class="primary"></button><p id="class-footnote" class="small"></p></aside></div><details id="class-why" class="class-extra"><summary>看看为什么 · 表示与步骤</summary><div id="class-why-copy"></div><div id="class-parts"></div></details><details id="class-data-extra" class="class-extra" hidden><summary>更多数据与规则</summary><div id="class-readings"></div></details><details id="class-program" class="class-extra" hidden><summary>第二讲 · 展开 Python 程序追踪</summary><div id="class-program-body"></div></details><section id="class-summary" hidden><div id="class-cards" class="class-cards"></div><label class="field" for="class-reflection">最后想一想：换成无人机或机床，你会用哪种思维检查什么？</label><textarea id="class-reflection" rows="2" placeholder="选一种思维，写出你会检查的条件、部件关系或证据。也可以先口头讨论。"></textarea><div class="class-report-actions"><a class="button primary" id="class-download" download="CS0502-USV-教学报告.txt">下载报告与复盘 ↗</a><button id="class-free">继续自由探索</button></div><details id="class-report-details" class="class-extra"><summary>查看完整航次记录与报告</summary><div id="class-report-body"></div></details></section><dialog id="class-settings"><div class="dialog-heading"><h2>实验设置</h2><button id="class-settings-close">关闭设置 ×</button></div><p class="small">暂停、单步与倍速只改变观察过程；更复杂的故障组合可在自由探索中比较。</p><div id="class-controls"></div><label class="field" for="battery">出航电量 / Wh</label><div id="class-battery-control"></div><div id="class-state-controls"></div><button id="class-advanced">进入自由探索 · 保留本航次</button></dialog>`;
  document.querySelector('.intro').before(shell);
  $('class-progress').setAttribute('aria-label','四种思维导航');
  $('class-progress').innerHTML=PILLARS.map((p,i)=>`<button data-pillar="${p.id}" aria-label="${p.name}" aria-controls="class-title"><b aria-hidden="true">0${i+1}</b>${p.name}</button>`).join('');
  function pillar(){return lessonPillar(c.step);}
  function change(step){rememberStep(c,step);drawKey='';$('class-why').open=false;$('class-data-extra').open=false;$('class-program').open=false;}
  function navigate(id){
    const target=pillarStep(c,context().state,id);
    if(target===c.step)return;
    change(target);
    command('pause');
    if(target==='image')command('evidence','region');
    if(pillar()===2&&!dataKey)dataKey=readingsKey();
    command('render');
  }
  function resumeMission(){
    const s=context().state;
    if(s.status==='depleted')change('report');
    else if(s.status==='returned')navigate('system');
    else change(c.missionStep);
  }
  function readingsKey(){const x=context();return JSON.stringify([x.readings,x.operator,x.threshold,x.dataSource]);}
  function completeData(){const x=context();c.dataEvidence.push({source:x.sourceName,readings:[...x.readings],operator:x.operator,threshold:x.threshold,prediction:c.guess,count:countAlerts(x.readings,x.threshold,x.operator)});dataKey=readingsKey();}
  function config(){
    const x=context(),s=x.state,m=routeMetrics(s.route,s.capacity),r=report(s,x.threshold,x.operator);
    const base={options:[],selected:null,result:'',concept:'',footnote:'简化教学模型 · m / s / Wh，非真实航行预测',next:'下一步',disabled:false};
    switch(c.step){
      case 'route-summary':return {...base,title:'回看路线：步骤和约束是否都满足？',lead:`本航次采用${ROUTES[s.route].name}。出航后保留原路线，切换章节不会重跑航次。`,result:`<p>${ROUTES[s.route].nodes.join(' → ')}</p><p>当前覆盖 ${s.covered.length}/3 · ${s.time} s</p><p>${m.conflict?'存在禁区冲突':'避开禁区'} · 预计返航剩余 ${m.margin.toFixed(1)} Wh</p>`,concept:'计算思维：表示任务、分解步骤，用约束检查结果。',next:s.status==='returned'?'回看系统实验':'继续当前课堂任务'};
      case 'system-intro':return {...base,title:'断网切断的是哪一段信息流？',lead:'先查看船上部件和岸站的分工。断网实验在完成 P1 采集后开展，现有任务会保留。',result:counter(s),concept:'系统思维：沿着部件之间的连接，判断一个环节失效会影响哪些能力。',next:s.status==='ready'?'进入出航步骤':'继续任务至断网实验'};
      case 'system-summary':return {...base,title:'回看系统：断网与恢复改变了什么？',lead:c.offline?`断网证据：${countText(c.offline)}。`:'本航次尚未留下断网实验记录。',result:counter(s),concept:c.recovered?`恢复证据：${countText(c.recovered)}。传感、计算和存储是否继续工作，取决于部件分工与任务配置。`:'系统思维：分别检查感知、计算、存储和通信，不能把断网与停机混为一谈。',next:'查看数据统计'};
      case 'image-intro':return {...base,title:'疑似裂纹，需要什么证据才能判断？',lead:'本航次尚未采集 P2 图像。完成采集后，依次查看原图、疑似区域和补拍，判断证据是否充分。',result:`<p>P2 图像：尚未采集</p><p>当前覆盖 ${s.covered.length}/3</p>`,concept:'智能思维：提出候选，用新证据验证，再更新判断。没有图像时先补齐证据。',next:'继续任务，采集 P2 图像'};
      case 'route':return {...base,title:'先预测：哪条路线能完成巡检？',lead:'从基地 B 出发，巡检 P1、P2、P3 后返航；必须避开施工禁区，并保留至少 6 Wh。',options:[['direct','A · 依次直达 P1、P2、P3'],['safe','B · 经 W1、W2 绕行'],['missed','C · 经 P1、P3 返航']],selected:c.choice,next:'检查这条路线',disabled:!c.choice};
      case 'route-result':return {...base,title:m.conflict||m.covered.length<3||!m.enough?'这条路线漏掉了什么条件？':'这条路线通过了哪些检查？',lead:'把自然语言任务变成逐项可判断的条件，才能检查程序是否完成了任务。',result:`<div class="check-results"><p>${m.covered.length===3?'✓':'×'} 覆盖 ${m.covered.length} / 3 个点</p><p>${m.conflict?'× 穿越禁区':'✓ 避开禁区'}</p><p>${m.enough?'✓':'×'} 预计返航剩余 ${m.margin.toFixed(1)} Wh</p></div>`,concept:'计算思维：把任务表示成数据，分解成步骤，再用明确约束检查结果。',next:m.conflict||m.covered.length<3||!m.enough?'换条路线再检查':'按这条路线出航'};
      case 'sailing':return {...base,title:'按步骤执行：驶向 P1，采集并记录',lead:'船正在执行选定路线。到达 P1 后会自动暂停，进入断网实验。',next:s.running?'暂停观察':'继续航行',result:`<p class="big-number">${s.time}<small> s</small></p><p>当前覆盖 ${s.covered.length} / 3</p>`};
      case 'network':return {...base,title:'断网后，新采集的记录会怎样？',lead:`P1 已完成。当前配置：${s.autonomy?'具备本地任务执行能力':'依赖岸站指令'}。现在只切断无线通信。`,options:[['stop','所有设备停止，无法记录'],['local','船上可记录，岸站暂时收不到'],['shore','岸站仍会收到新记录']],selected:c.networkGuess,next:'切断通信并观察',disabled:!c.networkGuess};
      case 'offline-run':return {...base,title:'通信已断开，观察船和记录的变化',lead:s.autonomy?'船上继续执行任务；到 P2 后自动暂停，再对照记录数量。':'依赖岸站指令的配置将等待 5 个教学秒，再对照船位与记录。',result:counter(s),next:s.running?'暂停观察':'继续观察'};
      case 'offline':return {...base,title:s.autonomy?'岸站没收到，船上有记录吗？':'船为什么停在原地？',lead:`断网前：${countText(c.before)}。`,result:counter(s),concept:c.offline&&c.before?(s.autonomy?`系统思维：船上新增 ${c.offline.local-c.before.local} 条记录。无线链路中断，船载计算和本地存储仍可工作。`:`系统思维：失联 ${c.offline.time-c.before.time} s，船位变化 ${distance(c.offline,c.before).toFixed(1)} m。推进等待岸站指令，感知与本地存储能力仍保留。`):'沿着感知、计算、存储与通信的连接，解释故障影响。',next:'恢复通信，观察交回'};
      case 'recovery-run':return {...base,title:'通信恢复，留意岸站的记录数量',lead:'每个教学秒最多交回一条排队记录；已有记录不会重复计数。',result:counter(s),next:s.running?'暂停观察':'继续观察'};
      case 'recovered':return {...base,title:c.offline?.queue?'旧记录交回了，采集时间变了吗？':'通信恢复后，任务能继续了吗？',lead:`断网时：${countText(c.offline)}。`,result:counter(s),concept:c.offline?.queue?'系统思维：记录先在船上保存，恢复后再传给岸站。采集时间与交回时间不同。':'系统思维：恢复的是跨网络的连接。没有待交回的记录，就不会凭空生成补传数据。',next:'继续巡检并返航'};
      case 'returning':return {...base,title:'把三个巡检点的证据带回基地',lead:'返航后，接着检查报告中的温度统计。',result:counter(s),next:s.running?'暂停观察':'继续返航'};
      case 'data':case 'strict':return {...base,title:c.step==='strict'?'改变比较规则后，次数会变吗？':'先预测：这些温度有几次满足条件？',lead:`${x.sourceName}。当前规则：temperature ${x.operator} ${x.threshold} °C。`,options:[0,1,2,3].map(n=>[String(n),`${n} 次`]),selected:c.guess===null?null:String(c.guess),next:'验证我的预测',disabled:c.guess===null,footnote:'同一推进电机 M1 · 不同时刻的温度记录 · °C'};
      case 'data-result':case 'strict-result':{const count=countAlerts(x.readings,x.threshold,x.operator);return {...base,title:x.readings.length?'这个统计数，到底数的是什么？':'返回 0，就代表设备正常吗？',lead:`初始预测 ${c.guess} 次；按当前规则计算得到 ${count} 次。`,result:`<p class="big-number">${count}<small> 次</small></p><p>${x.readings.length?`${x.readings.length} 条有效温度记录`:'没有记录'}</p>`,concept:x.readings.length?'数据思维：先确认来源、完整性和规则。这里数的是满足条件的记录次数，不能当作故障设备数量。':'数据思维：没有记录时程序返回 0，但设备状态仍然缺少依据。',next:c.step==='data-result'?'改变比较规则，再预测一次':'检查 P2 的图像证据',footnote:'第一讲先理解统计依据；第二讲可在下方展开程序追踪。'};}
      case 'image':return {...base,title:'先看原图：一条暗线可能是什么？',lead:'AI 教学示例提出“疑似裂纹”。请看原图与圈出的区域，保留一个候选判断。',options:Object.entries(imageNames),selected:c.initialImage,next:'改变光照，查看补拍',disabled:!c.initialImage,footnote:'虚拟设施 · 教学构造图像 · 预设 AI 判断，未运行真实模型'};
      case 'image-evidence':return {...base,title:'补拍增加了什么证据？现在怎样下结论？',lead:'斜光下可见涂层边缘，内部结构仍不可见。请选择当前证据支持的结论。',options:[['crack','已经确认结构裂纹'],['clear','已经排除风险'],['reinspect','保留疑点，安排进一步复检']],selected:c.conclusion,next:'用这个结论检查报告',disabled:!c.conclusion,footnote:'补拍与原图来自同一虚拟设施，不是独立检测结果。'};
      case 'image-result':return {...base,title:c.conclusion==='reinspect'?'证据还不充分，下一步做什么？':'这个结论超出了现有证据',lead:c.conclusion==='reinspect'?'保留待复检结论，并安排能够检查内部结构的进一步检测。':'表面图像不足以确认内部裂纹，也不足以排除风险。',result:`<p>初始候选：${imageNames[c.initialImage]}</p><p>补拍：涂层边缘可见，内部结构未定</p>`,concept:'智能思维：提出候选，选择新证据来验证，再更新判断与下一步行动。',next:c.conclusion==='reinspect'?'生成任务报告':'根据证据重新判断',footnote:'判断可以修正；报告保留初始候选和最终结论。'};
      default:return {...base,title:r.ready?'船回来了，这份教学报告可以交':'这份报告还缺什么依据？',lead:r.ready?'报告应明确保留“P2 待进一步复检”。回看同一次任务中的四种思维。':r.issues.join('；'),next:'',footnote:''};
    }
  }
  function counter(s){return `<div class="class-counter"><div><span>船上已存</span><strong>${s.records.length}</strong></div><span>${s.network?'→':'×'}</span><div><span>岸站已收</span><strong>${s.records.filter(r=>r.delivered).length}</strong></div></div><p>待交回 ${pending(s)} 条 · 教学时间 ${s.time} s</p>`;}
  function primary(){
    const x=context(),s=x.state;
    if(isFlightStep(c.step)){command(s.running?'pause':'run');return;}
    switch(c.step){
      case 'route-summary':case 'system-intro':case 'image-intro':resumeMission();break;
      case 'system-summary':navigate('data');break;
      case 'route':c.routeEvidence={route:s.route,...routeMetrics(s.route,s.capacity)};change('route-result');break;
      case 'route-result':{const m=routeMetrics(s.route,s.capacity);if(m.conflict||m.covered.length<3||!m.enough)change('route');else{c.routeEvidence={route:s.route,...m};change('sailing');command('run');}break;}
      case 'network':c.before=snapshot(s);c.offlineStart=s.time;change('offline-run');command('network',false);command('run');break;
      case 'offline':c.recoveryStart=s.time;change('recovery-run');command('network',true);command('run');break;
      case 'recovered':change('returning');command('run');break;
      case 'data':case 'strict':{const step=c.step;completeData();change(step==='strict'?'strict-result':'data-result');break;}
      case 'data-result':c.guess=null;change('strict');command('operator',x.operator==='>='?'>':'>=');dataKey=readingsKey();break;
      case 'strict-result':navigate('intelligence');break;
      case 'image':change('image-evidence');command('evidence','extra');break;
      case 'image-evidence':command('review',c.conclusion);change('image-result');break;
      case 'image-result':if(c.conclusion!=='reinspect'){c.conclusion=null;change('image-evidence');}else{c.imageEvidence={initial:c.initialImage,conclusion:c.conclusion};change('report');}break;
    }
    update();command('render');
  }
  function cards(){
    const r=c.routeEvidence,datum=c.dataEvidence.slice(-2);
    const descriptions=[r?`${ROUTES[r.route].nodes.join(' → ')}。覆盖 ${r.covered.length}/3；${r.conflict?'存在禁区冲突':'避开禁区'}；预计返航余量 ${r.margin.toFixed(1)} Wh。`:'本轮尚未检查路线。',c.offline?`初始预测：${{stop:'全部停止',local:'船上可记录，岸站暂收不到',shore:'岸站继续收到'}[c.networkGuess]}。断网时 ${countText(c.offline)}；恢复后 ${countText(c.recovered)}。`:'本轮尚无完整断网证据。',datum.length?(c.dataEvidence.length>2?'展示最近两次比较，完整过程见报告。':'')+datum.map(d=>`[${d.readings.join(', ')}] ${d.operator} ${d.threshold}：预测 ${d.prediction} 次，实际 ${d.count} 次。来源：${d.source}。`).join(' '):'本轮尚未完成统计预测。',c.imageEvidence?`初始候选：${imageNames[c.imageEvidence.initial]}。补拍后保留疑点，安排进一步复检。`:'本轮图像结论尚未完成。'];
    return PILLARS.map((p,i)=>`<article><p class="eyebrow">0${i+1} / ${p.name}</p><h2>${p.question}</h2><p>${esc(descriptions[i])}</p></article>`).join('');
  }
  function update(){
    enabled=context().mode==='guided';document.body.dataset.mode=enabled?'guided':'free';shell.hidden=!enabled;
    if(!enabled){for(const node of homes.keys())home(node);return;}
    move(battery,$('class-battery-control'));move(transport,$('class-controls'));move(status,$('class-state-controls'));move(program,$('class-program-body'));move(readings,$('class-readings'));move(parts,$('class-parts'));move(reportPanel,$('class-report-body'));
    if(['data','strict','data-result','strict-result'].includes(c.step)&&dataKey&&readingsKey()!==dataKey){
      // 改参数时保留展开区和输入焦点，让学生可以连续输入；旧预测仍保存在证据中。
      if(c.step.endsWith('-result'))rememberStep(c,c.step==='strict-result'?'strict':'data');
      drawKey=c.step;c.guess=null;dataKey=readingsKey();$('class-program').open=false;
    }
    const spatial=['route','route-result','route-summary','system-intro','system-summary','image-intro',...flightSteps,'network','offline','recovered'].includes(c.step),images=c.step.startsWith('image')&&c.step!=='image-intro',isData=['data','strict','data-result','strict-result'].includes(c.step),done=c.step==='report';
    const why=$('class-why').open&&pillar()===1;
    layout(why||c.step==='system-intro'||c.step==='system-summary'?'system':isData?'data':'mission');
    shell.classList.toggle('why-open',why);shell.classList.toggle('is-report',done);shell.classList.toggle('data-unrevealed',['data','strict'].includes(c.step));
    if(spatial){home(photo);move(scene,$('class-visual'));}else{home(scene);if(images)move(photo,$('class-visual'));else home(photo);}
    const configNow=config(),stepChanged=drawKey!==c.step;
    const completed=[!!c.routeEvidence,!!c.offline&&!!c.recovered,c.dataEvidence.length>=2,!!c.imageEvidence];
    $('class-progress').querySelectorAll('button').forEach((b,i)=>{b.setAttribute('aria-pressed',i===pillar());b.classList.toggle('passed',completed[i]);b.querySelector('b').textContent=completed[i]?'✓':String(i+1).padStart(2,'0');});
    $('class-kicker').textContent=done?'任务报告 / 四种思维串起同一次巡检':`0${pillar()+1} / ${PILLARS[pillar()].name}`;
    $('class-title').textContent=configNow.title;$('class-lead').textContent=configNow.lead;
    const options=configNow.options.map(([value,text])=>`<button data-class-choice="${value}" aria-pressed="${configNow.selected===value}">${text}</button>`).join('');
    if(options!==optionsKey){const focused=document.activeElement?.dataset.classChoice;$('class-choices').innerHTML=options;optionsKey=options;if(focused)$('class-choices').querySelector(`[data-class-choice="${focused}"]`)?.focus({preventScroll:true});}
    $('class-result').innerHTML=configNow.result;$('class-result').hidden=!configNow.result;$('class-concept').textContent=configNow.concept;$('class-concept').hidden=!configNow.concept;
    $('class-next').textContent=configNow.next;$('class-next').disabled=configNow.disabled;$('class-footnote').textContent=configNow.footnote;
    $('class-why').hidden=!spatial||pillar()>1;$('class-why').querySelector('summary').textContent=pillar()===0?'看看为什么 · 任务的表示与步骤':'看看为什么 · 拆开船体，追踪信息流';
    $('class-why-copy').innerHTML=pillar()===0?'<p><b>表示：</b>把巡检点变成坐标，把路线变成有序列表。<b>分解：</b>移动、采集、记录。<b>算法（algorithm）：</b>对每个巡检点按顺序执行，最后返航。<b>约束：</b>覆盖、禁区与返航余量必须同时满足。</p>':'<p>感知 → 船载计算 → 本地存储留在船上；无线通信 → 岸站跨越网络。电池提供能量。选择部件或展开结构，查看它的职责。若推进依赖岸站指令，断网后会等待；本模型只在巡检点生成记录。</p>';
    $('class-parts').hidden=pillar()!==1;
    $('class-data-extra').hidden=!isData;$('class-program').hidden=!isData||['data','strict'].includes(c.step);$('class-summary').hidden=!done;document.querySelector('.class-layout').hidden=done;
    let diagram=$('class-data-visual');
    if(isData){if(!diagram){diagram=document.createElement('div');diagram.id='class-data-visual';$('class-visual').append(diagram);}const x=context(),revealed=['data-result','strict-result'].includes(c.step);diagram.innerHTML=`<p class="eyebrow">${esc(x.sourceName)}</p><div class="class-temperatures">${x.readings.length?x.readings.map((t,i)=>`<div class="${revealed&&countAlerts([t],x.threshold,x.operator)?'alert':''}"><small>时刻 ${i+1}</small><strong>${t}<small> °C</small></strong>${revealed?`<b>${countAlerts([t],x.threshold,x.operator)?'满足条件':'不满足条件'}</b>`:''}</div>`).join(''):'<div class="empty-record"><strong>∅</strong><p>没有有效温度记录</p></div>'}</div><p class="class-rule">temperature <b>${esc(x.operator)}</b> ${x.threshold} °C</p><p>同一推进电机 M1 · 统计对象是采集记录</p>`;}else diagram?.remove();
    if(done){$('class-cards').innerHTML=cards();reportPanel.hidden=false;}
    if(stepChanged){drawKey=c.step;if(!isFlightStep(c.step)&&c.step!=='route'){$('class-title').tabIndex=-1;$('class-title').focus({preventScroll:true});if(!$('class-settings').open)shell.scrollIntoView({block:'start',behavior:'smooth'});}}
  }
  $('class-choices').onclick=e=>{const b=e.target.closest('[data-class-choice]');if(!b)return;const v=b.dataset.classChoice;if(c.step==='route'){c.choice=v;command('route',v);}else if(c.step==='network')c.networkGuess=v;else if(c.step==='data'||c.step==='strict')c.guess=Number(v);else if(c.step==='image')c.initialImage=v;else if(c.step==='image-evidence')c.conclusion=v;update();};
  $('class-next').onclick=primary;
  $('class-progress').onclick=e=>{const button=e.target.closest('[data-pillar]');if(button)navigate(button.dataset.pillar);};
  $('class-why').ontoggle=()=>{if(enabled)command('render');};
  $('class-settings-open').onclick=()=>$('class-settings').showModal();$('class-settings-close').onclick=()=>$('class-settings').close();
  for(const id of ['class-advanced','class-free'])$(id).onclick=()=>{if($('class-settings').open)$('class-settings').close();command('free');};
  $('class-reflection').oninput=e=>{$('reflection').value=e.target.value;command('render');};
  $('class-download').onclick=()=>{command('render');$('class-report-details').open=true;};
  function afterTick(){const previous=c.step;if(checkpoint(c,context().state)){change(c.step);if(c.step==='data'&&previous!=='data'){c.guess=null;command('data-defaults');dataKey=readingsKey();}}}
  function reset(){c=newLesson();dataKey='';drawKey='';optionsKey='';$('class-reflection').value='';$('class-report-details').open=false;$('class-why').open=false;$('class-program').open=false;$('class-data-extra').open=false;}
  function exportText(){return '\n课堂过程记录（自动保留预测与模型证据，不代表学习效果评分）\n'+(c.routeEvidence?`计算思维：${ROUTES[c.routeEvidence.route].name}，覆盖 ${c.routeEvidence.covered.length}/3，禁区冲突 ${c.routeEvidence.conflict?'有':'无'}，预计返航 ${c.routeEvidence.margin.toFixed(1)} Wh。\n`:'计算思维：尚未检查路线。\n')+`系统思维：初始预测 ${{stop:'全部停止',local:'船上可记录，岸站暂收不到',shore:'岸站继续收到'}[c.networkGuess]||'未作答'}；断网前 ${countText(c.before)}；断网时 ${countText(c.offline)}；恢复后 ${countText(c.recovered)}。\n`+c.dataEvidence.map(d=>`数据思维：${d.source} [${d.readings.join(', ')}] °C，${d.operator} ${d.threshold}；初始预测 ${d.prediction}，实际 ${d.count} 次。\n`).join('')+`智能思维：初始候选 ${imageNames[c.initialImage]||'未作答'}；最终结论 ${c.imageEvidence?'保留疑点，安排进一步复检':'待完成'}。\n`;}
  return {update,afterTick,reset,exportText,canRun:()=>isFlightStep(c.step),step:()=>c.step};
}
