import test from 'node:test';
import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {RULES,createState,routeMetrics,crossesZone,start,tick,setNetwork,setPower,pending,report,countAlerts,executionTrace} from './model.mjs';

function until(s,predicate,limit=500){for(let i=0;i<limit&&!predicate(s);i++)tick(s);assert.ok(predicate(s),'bounded simulation should reach checkpoint');}
test('合规航程、时间、能耗与解析规则一致；直达冲突、第三方案漏检',()=>{
  for(const route of ['safe','direct','missed']){
    const s=createState({route});start(s);until(s,s=>s.status==='returned');const m=routeMetrics(route);
    assert.ok(Math.abs(s.distance-m.length)<1e-8);assert.ok(Math.abs(s.used-m.energy)<1e-8);assert.equal(s.time,m.seconds);assert.equal(s.crossed,m.conflict);assert.deepEqual(s.covered,m.covered);
  }
  assert.equal(routeMetrics('safe').conflict,false);assert.equal(routeMetrics('direct').conflict,true);assert.equal(routeMetrics('missed').covered.length,2);
  assert.equal(crossesZone([-10,-10],[10,-10]),true);
});
test('断网 → 本地继续记录 → 暂停冻结 → 恢复按序补传 → 返航',()=>{
  const s=createState();start(s);until(s,s=>s.covered.includes('P1'));assert.equal(s.records.filter(r=>r.delivered).length,1);
  setNetwork(s,false);until(s,s=>s.covered.includes('P2'));assert.equal(s.records.length,2);assert.equal(s.records.filter(r=>r.delivered).length,1);assert.equal(pending(s),1);
  s.running=false;const paused=JSON.stringify(s);tick(s);assert.equal(JSON.stringify(s),paused);
  setNetwork(s,true);assert.equal(pending(s),1);start(s);tick(s);assert.equal(pending(s),0);assert.ok(s.records[1].deliveredAt>s.records[1].time);
  until(s,s=>s.status==='returned');assert.equal(s.records.length,3);assert.equal(pending(s),0);assert.equal(report(s).count,2);assert.equal(report(s).ready,false);
  Object.assign(s,{originalSeen:true,regionSeen:true,extraSeen:true,review:'reinspect'});assert.equal(report(s).ready,true);
  s.review='crack';assert.equal(report(s).ready,false);
});
test('岸站指令失联仅阻止推进；本地停机阻止感知计算和补传',()=>{
  const s=createState({autonomy:false});start(s);until(s,s=>s.covered.includes('P1'));setNetwork(s,false);const pos=[...s.position],used=s.used;
  for(let i=0;i<5;i++)tick(s);assert.deepEqual(s.position,pos);assert.equal(s.records.length,1);assert.ok(s.used>used);
  setNetwork(s,true);tick(s);assert.notDeepEqual(s.position,pos);
  setPower(s,false);const stopped=[...s.position],recorded=s.records.length;for(let i=0;i<5;i++)tick(s);assert.deepEqual(s.position,stopped);assert.equal(s.records.length,recorded);
  setPower(s,true);until(s,s=>s.status==='returned');
});
test('断网直到返航时记录保留；停机不补传；恢复后每秒一条且不重复',()=>{
  const s=createState({network:false});start(s);until(s,s=>s.status==='returned');assert.equal(pending(s),3);
  setNetwork(s,true);setPower(s,false);start(s);tick(s);assert.equal(pending(s),3);
  setPower(s,true);for(const expected of [2,1,0]){tick(s);assert.equal(pending(s),expected);}
  assert.equal(s.records.length,3);assert.equal(s.running,false);
});
test('低电量无法返航；缺测不被写成正常温度；复位无旧数据',()=>{
  const low=createState({capacity:30});start(low);until(low,s=>s.status==='depleted');assert.ok(low.used<=low.capacity);assert.equal(report(low).ready,false);
  const missing=createState({temperatureSensor:false});start(missing);until(missing,s=>s.status==='returned');assert.equal(missing.covered.length,3);assert.equal(report(missing).received.length,0);assert.equal(report(missing).ready,false);assert.equal(report(missing).count,0);
  const fresh=createState();assert.equal(fresh.records.length,0);assert.equal(fresh.time,0);assert.equal(fresh.review,'pending');
});
test('JavaScript 与实际 Python 对照，追踪结果与统计规则一致',()=>{
  const python=spawnSync(process.env.USV_PYTHON||'python3',['-c', 'import json,runpy,sys; m=runpy.run_path(sys.argv[1]); print(json.dumps(m["verify"]()))',new URL('./verify_count.py',import.meta.url).pathname],{encoding:'utf8'});
  assert.equal(python.status,0,python.stderr);
  for(const c of JSON.parse(python.stdout)){assert.equal(countAlerts(c.readings,c.threshold),c.actual);assert.equal(executionTrace(c.readings,c.threshold,'>=').at(-1).count,c.actual);}
  assert.equal(countAlerts([65,80,81],80,'>'),1);assert.equal(executionTrace([65,80,81],80,'>').at(-1).count,1);
});

// 课堂检查点只读取同一个航次状态，不预写成功结果。
import { newLesson, snapshot, checkpoint, isFlightStep, rememberStep, pillarStep } from './learning.mjs';
test('课堂检查点覆盖本地执行与岸站等待两种配置',()=>{
  for(const autonomy of [true,false]){
    const s=createState({autonomy}),c=newLesson();c.step='sailing';start(s);
    until(s,s=>s.covered.includes('P1'));assert.equal(checkpoint(c,s),true);assert.equal(c.step,'network');assert.equal(s.running,false);
    c.before=snapshot(s);c.offlineStart=s.time;c.step='offline-run';setNetwork(s,false);start(s);
    until(s,()=>{checkpoint(c,s);return c.step==='offline';});
    assert.equal(c.offline.local,autonomy?2:1);assert.equal(c.offline.shore,1);assert.equal(c.offline.queue,autonomy?1:0);
    if(!autonomy)assert.deepEqual(c.offline.position,c.before.position);
    c.recoveryStart=s.time;c.step='recovery-run';setNetwork(s,true);start(s);tick(s);assert.equal(checkpoint(c,s),true);
    assert.equal(c.step,'recovered');assert.equal(c.recovered.queue,0);assert.equal(c.recovered.shore,autonomy?2:1);
    assert.equal(c.offline.shore,1); // 恢复不能改写断网证据
    c.step='returning';start(s);until(s,s=>s.status==='returned');checkpoint(c,s);assert.equal(c.step,'data');
  }
});
test('暂停不推进课堂阶段；故障终止进入依据不足的报告',()=>{
  const s=createState(),c=newLesson();c.step='sailing';start(s);tick(s);s.running=false;const before=JSON.stringify(s);
  tick(s);assert.equal(checkpoint(c,s),false);assert.equal(JSON.stringify(s),before);
  const low=createState({capacity:30});start(low);until(low,s=>s.status==='depleted');assert.equal(checkpoint(c,low),true);assert.equal(c.step,'report');assert.equal(report(low).ready,false);
  assert.equal(isFlightStep('data'),false);assert.equal(isFlightStep('offline-run'),true);
});
test('新的课堂与观测快照不共享可变的证据或船位',()=>{
  const c=newLesson(),other=newLesson();c.dataEvidence.push({prediction:1,count:2});assert.equal(other.dataEvidence.length,0);
  const s=createState(),before=snapshot(s);start(s);tick(s);assert.notDeepEqual(before.position,s.position);assert.equal(before.time,0);
});
test('四种思维均能独立进入；导航不伪造巡检记录或重置作答',()=>{
  const s=createState(),c=newLesson(),before=JSON.stringify(s);
  assert.equal(pillarStep(c,s,'computation'),'route');
  assert.equal(pillarStep(c,s,'system'),'system-intro');
  assert.equal(pillarStep(c,s,'data'),'data');
  assert.equal(pillarStep(c,s,'intelligence'),'image-intro');
  c.guess=2;rememberStep(c,'data-result');rememberStep(c,'system-intro');
  assert.equal(pillarStep(c,s,'data'),'data-result');assert.equal(c.guess,2);
  assert.equal(JSON.stringify(s),before);assert.equal(report(s).ready,false);
  assert.equal(c.missionStep,'route');assert.deepEqual(newLesson().steps,{});
});
test('断网途中跳到其他章节后，恢复原航次和补传检查点',()=>{
  const s=createState(),c=newLesson();rememberStep(c,'sailing');start(s);
  until(s,s=>s.covered.includes('P1'));checkpoint(c,s);rememberStep(c,c.step);
  c.before=snapshot(s);c.offlineStart=s.time;setNetwork(s,false);rememberStep(c,'offline-run');start(s);tick(s);
  s.running=false;const paused=JSON.stringify(s);rememberStep(c,'data');tick(s);
  assert.equal(JSON.stringify(s),paused);assert.equal(c.missionStep,'offline-run');
  assert.equal(pillarStep(c,s,'computation'),'route-summary');
  rememberStep(c,pillarStep(c,s,'system'));assert.equal(c.step,'offline-run');start(s);
  until(s,()=>{checkpoint(c,s);return c.step==='offline';});
  assert.equal(c.offline.time,31);assert.equal(c.offline.queue,1);
  assert.equal(pillarStep(c,s,'intelligence'),'image');
  setNetwork(s,true);start(s);until(s,s=>s.status==='returned');
  assert.equal(pillarStep(c,s,'system'),'system-summary');assert.equal(s.records.length,3);
});
