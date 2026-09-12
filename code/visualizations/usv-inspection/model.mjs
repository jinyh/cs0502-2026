// 所有视图共享的确定性教学模型。坐标 m，时间 s，能量 Wh；不模拟真实船舶水动力。
export const RULES = Object.freeze({ speed: 4, moveWh: 0.1, hotelWh: 0.05, sampleWh: 1, reserveWh: 6 });
export const POINTS = Object.freeze({ B: [-42, 28], P1: [-32, -20], P2: [20, -24], P3: [35, 22], W1: [-15, -4], W2: [15, -4] });
export const ZONE = Object.freeze({ minX: -9, maxX: 9, minZ: -31, maxZ: -10 });
export const ROUTES = Object.freeze({
  direct: { name: '直达航线', note: '基地 → P1 → P2 → P3 → 基地', nodes: ['B', 'P1', 'P2', 'P3', 'B'] },
  safe: { name: '合规绕行', note: '绕开施工水域，完成三个巡检点', nodes: ['B', 'P1', 'W1', 'W2', 'P2', 'P3', 'B'] },
  missed: { name: '少走一个点', note: '基地 → P1 → P3 → 基地，遗漏 P2', nodes: ['B', 'P1', 'P3', 'B'] },
});
export const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);
export function crossesZone(a, b) {
  // Liang–Barsky 线段裁剪；碰到禁区边界也算冲突。
  let lo = 0, hi = 1;
  for (const [origin, delta, min, max] of [[a[0], b[0]-a[0], ZONE.minX, ZONE.maxX], [a[1], b[1]-a[1], ZONE.minZ, ZONE.maxZ]]) {
    if (delta === 0) { if (origin < min || origin > max) return false; }
    else { const t1 = (min-origin)/delta, t2 = (max-origin)/delta; lo = Math.max(lo, Math.min(t1,t2)); hi = Math.min(hi, Math.max(t1,t2)); }
  }
  return lo <= hi;
}
export function routeMetrics(key, battery = 60) {
  const nodes = ROUTES[key].nodes;
  let length = 0, conflict = false;
  for (let i = 1; i < nodes.length; i++) { length += dist(POINTS[nodes[i-1]], POINTS[nodes[i]]); conflict ||= crossesZone(POINTS[nodes[i-1]], POINTS[nodes[i]]); }
  const covered = [...new Set(nodes.filter(n => n.startsWith('P')))];
  const seconds = Math.ceil(length / RULES.speed);
  const energy = length * RULES.moveWh + seconds * RULES.hotelWh + covered.length * RULES.sampleWh;
  return { length, conflict, covered, seconds, energy, margin: battery - energy, enough: battery - energy >= RULES.reserveWh };
}
export function createState(options = {}) {
  return { route: 'safe', capacity: 60, autonomy: true, network: true, power: true, temperatureSensor: true, ...options,
    time: 0, used: 0, distance: 0, position: [...POINTS.B], next: 1, heading: 0, status: 'ready', running: false,
    covered: [], records: [], trail: [[...POINTS.B]], events: [], crossed: false, review: 'pending', originalSeen: false, regionSeen: false, extraSeen: false,
  };
}
export function event(s, type, text) { s.events.push({ time: s.time, type, text }); }
export function active(s) { return s.power && s.used < s.capacity; }
export function propulsion(s) { return s.running && s.status === 'sailing' && active(s) && (s.autonomy || s.network); }
export function setNetwork(s, online) {
  if (s.network === online) return;
  s.network = online;
  event(s, online ? 'recovery' : 'fault', online ? `通信恢复；${pending(s)} 条记录等待按序补传` : '通信中断；岸站停止接收新数据');
}
export function setPower(s, on) {
  if (s.power === on) return;
  s.power = on;
  event(s, on ? 'recovery' : 'fault', on ? '船载设备重新上电；继续原任务' : '船载停机；感知、计算、记录和推进停止，已有记录保留');
}
export const pending = s => s.records.filter(r => !r.delivered).length;
export function start(s) {
  if (s.status === 'depleted' || (s.status === 'returned' && pending(s) === 0)) return;
  if (s.status === 'ready') { s.status = 'sailing'; event(s, 'task', `出航：${ROUTES[s.route].name}，${s.autonomy ? '本地执行' : '岸站指令'}配置`); }
  s.running = true;
}
export function remainingMargin(s) {
  if (s.status === 'returned') return s.capacity - s.used;
  const nodes = ROUTES[s.route].nodes;
  let length = dist(s.position, POINTS[nodes[s.next]]);
  for (let i = s.next + 1; i < nodes.length; i++) length += dist(POINTS[nodes[i-1]], POINTS[nodes[i]]);
  const samples = nodes.slice(s.next).filter(n => n.startsWith('P') && !s.covered.includes(n)).length;
  return s.capacity - s.used - length*RULES.moveWh - Math.ceil(length/RULES.speed)*RULES.hotelWh - samples*RULES.sampleWh;
}
export function tick(s) {
  if (!s.running || s.status === 'depleted') return;
  s.time += 1;
  const canMove = propulsion(s);
  if (s.status !== 'returned') s.used = Math.min(s.capacity, s.used + (s.power ? RULES.hotelWh : 0.01));
  if (canMove) {
    let budget = Math.min(RULES.speed, Math.max(0, (s.capacity - s.used) / RULES.moveWh));
    const nodes = ROUTES[s.route].nodes;
    while (budget > 1e-8 && s.status === 'sailing') {
      const targetName = nodes[s.next], target = POINTS[targetName];
      const distance = dist(s.position, target), travel = Math.min(budget, distance);
      const previous = [...s.position];
      s.heading = Math.atan2(target[0] - previous[0], target[1] - previous[1]);
      s.position = distance < 1e-8 ? [...target] : previous.map((v, i) => v + (target[i]-v)*travel/distance);
      s.distance += travel; s.used += travel*RULES.moveWh; budget -= travel;
      if (!s.crossed && crossesZone(previous, s.position)) { s.crossed = true; event(s, 'fault', '航迹进入禁行施工水域：路线违规'); }
      if (travel >= distance - 1e-8) {
        s.next += 1;
        if (targetName.startsWith('P') && !s.covered.includes(targetName)) {
          if (s.capacity - s.used >= RULES.sampleWh) {
            s.used += RULES.sampleWh; s.covered.push(targetName);
            const temperature = s.temperatureSensor ? { P1: 65, P2: 80, P3: 81 }[targetName] : null;
            s.records.push({ id: s.records.length+1, point: targetName, time: s.time, device: '推进电机 M1', temperature, delivered: false, deliveredAt: null });
            event(s, 'sample', `${targetName}：图像已采集；M1 温度${temperature === null ? '缺测' : ` ${temperature} °C`}；已存船上`);
          } else { event(s, 'fault', `${targetName}：采集能量不足，没有生成记录`); }
        }
        if (s.next === nodes.length) { s.status = 'returned'; s.running = false; event(s, 'task', '已返航；请分别检查覆盖、交回记录和图像证据'); }
        budget = Math.min(budget, Math.max(0, (s.capacity-s.used)/RULES.moveWh));
      }
    }
    s.trail.push([...s.position]);
  }
  if (s.used >= s.capacity - 1e-8 && s.status !== 'returned') { s.used = s.capacity; s.status = 'depleted'; s.running = false; event(s, 'fault', '能量耗尽；未返航，设备停止'); }
  // 可靠有序队列：每教学秒最多交回一条，避免断网被误画成记录丢失。
  if (s.network && active(s)) {
    const record = s.records.find(r => !r.delivered);
    if (record) { record.delivered = true; record.deliveredAt = s.time; event(s, 'transfer', `记录 ${record.id}（${record.point}）交回岸站`); }
  }
  if (s.status === 'returned' && pending(s) === 0) s.running = false;
}
export function countAlerts(readings, threshold = 80, operator = '>=') { return readings.reduce((count, t) => count + Number(operator === '>=' ? t >= threshold : t > threshold), 0); }
export function executionTrace(readings, threshold, operator) {
  let count = 0;
  const frames = [{line:8,count,temperature:null,condition:'准备输入'}, {line:9,count,temperature:null,condition:'调用函数'}, {line:2,count,temperature:null,condition:'初始化计数'}];
  for (const temperature of readings) {
    frames.push({line:3,count,temperature,condition:'取下一条记录'});
    const result = operator === '>=' ? temperature >= threshold : temperature > threshold;
    frames.push({line:4,count,temperature,condition:result ? 'True（成立）' : 'False（不成立）'});
    if (result) { count++; frames.push({line:5,count,temperature,condition:'count 加 1'}); }
  }
  frames.push({line:6,count,temperature:null,condition:readings.length ? '循环结束，返回结果' : '没有记录，返回 0'}, {line:9,count,temperature:null,condition:`输出 ${count}`});
  return frames;
}
export function report(s, threshold = 80, operator = '>=') {
  const local = s.records.filter(r => r.temperature !== null);
  const received = local.filter(r => r.delivered);
  const issues = [];
  if (s.status !== 'returned') issues.push('尚未返航');
  if (s.crossed || routeMetrics(s.route).conflict) issues.push('路线穿越禁区');
  if (s.covered.length < 3) issues.push(`漏检 ${['P1','P2','P3'].filter(p => !s.covered.includes(p)).join('、')}`);
  if (pending(s)) issues.push(`${pending(s)} 条记录尚未交回`);
  if (local.length < 3) issues.push('有效温度记录不足 3 条');
  if (s.capacity - s.used < RULES.reserveWh) issues.push('返航安全余量不足 6 Wh');
  const evidenceReady = s.originalSeen && s.regionSeen && s.extraSeen && s.covered.includes('P2');
  if (!evidenceReady || s.review !== 'reinspect') issues.push('P2 结论待复核');
  return { local, received, issues, ready: issues.length === 0, count: countAlerts(received.map(r => r.temperature), threshold, operator), evidenceReady };
}
