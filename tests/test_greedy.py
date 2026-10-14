"""Execute the classroom page's actual algorithm model and check independent optima."""

from pathlib import Path
import re
import shutil
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[1]


def test_greedy_visualization_traces_and_counterexamples():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required to execute the browser algorithm model")
    html = (ROOT / "code/visualizations/greedy.html").read_text(encoding="utf-8")
    model = re.search(r'<script id="greedy-model">(.*?)</script>', html, re.DOTALL).group(1)
    checks = r"""
const assert = require('node:assert/strict');
const originalActivities=structuredClone(ACTIVITIES), originalEdges=structuredClone(BASE_EDGES);
const stamps=coinTrace(COIN_PRESETS.stamps.faces,140), small=coinTrace([4,3,1],6);
assert.deepEqual(stamps.states.at(-1).chosen,[100,34,1,1,1,1,1,1]);
assert.deepEqual(stamps.optimum,{count:2,chosen:[70,70]});
assert.deepEqual(small.states.at(-1).chosen,[4,1,1]);
assert.deepEqual(small.optimum,{count:2,chosen:[3,3]});
for(const trace of [stamps,small]){
  assert.equal(trace.states.filter(s=>s.checkpoint).length,1);
  for(const [i,s] of trace.states.entries()){
    assert.equal(s.remaining+s.chosen.reduce((a,b)=>a+b,0),trace.target);
    assert(s.remaining>=0);
    if(s.kind==='作出选择'){
      const before=trace.states[i-1];
      assert.equal(s.chosen.at(-1),trace.faces.find(face=>face<=before.remaining));
      assert.deepEqual(s.chosen.slice(0,-1),before.chosen);
    }
  }
  assert.deepEqual(trace.states[0].chosen,[]);
}
// An independent breadth-first search checks minimum coin counts, including unreachable amounts.
function coinBfs(faces,target){const queue=[[0,0]],seen=new Set([0]);while(queue.length){const [amount,n]=queue.shift();if(amount===target)return n;for(const face of faces){const next=amount+face;if(next<=target&&!seen.has(next)){seen.add(next);queue.push([next,n+1]);}}}return Infinity;}
for(const faces of [[1,3,4],[2,5],[3,7],[1,5,10]])for(let target=0;target<=35;target++){
  const result=minimumCoins(faces,target);
  assert.equal(result.count,coinBfs(faces,target));
  if(Number.isFinite(result.count)){assert.equal(result.chosen.length,result.count);assert.equal(result.chosen.reduce((a,b)=>a+b,0),target);}
}
assert.equal(coinTrace([3,4],6).states.at(-1).remaining,2); // Greedy can get stuck despite a feasible solution.
assert.throws(()=>minimumCoins([0],6));
const schedule=Object.fromEntries(['finish','start','duration'].map(rule=>[rule,activityTrace(ACTIVITIES,rule)]));
assert.deepEqual(schedule.finish.states.at(-1).chosen,['B','D','E']);
assert.deepEqual(schedule.start.states.at(-1).chosen,['A']);
assert.deepEqual(schedule.duration.states.at(-1).chosen,['C','E']);
assert.deepEqual(schedule.finish.optimum,['B','D','E']);
for(const trace of Object.values(schedule))for(const s of trace.states){
  const chosen=ACTIVITIES.filter(a=>s.chosen.includes(a.id));
  assert.equal(new Set(s.chosen).size,s.chosen.length);
  assert(chosen.every((a,i)=>chosen.slice(i+1).every(b=>compatible(a,b))));
  assert(s.chosen.every(id=>!s.rejected.includes(id)));
  assert.equal(s.inspected.length,s.chosen.length+s.rejected.length);
}
// Earliest finish must match exhaustive optimum over many different small interval sets.
let seed=2026;function rand(n){seed=(seed*1664525+1013904223)>>>0;return seed%n;}
for(let trial=0;trial<45;trial++){
  const activities=Array.from({length:7},(_,i)=>{const start=rand(10);return{id:String(i),start,end:start+1+rand(6)};});
  const trace=activityTrace(activities,'finish');
  assert.equal(trace.states.at(-1).chosen.length,bestActivities(activities).length);
}
// Shortest paths are checked against Bellman-Ford rather than another Dijkstra implementation.
function bellman(vertices,edges,source){const d=Object.fromEntries(vertices.map(v=>[v,Infinity]));d[source]=0;for(let i=1;i<vertices.length;i++)for(const [a,b,w] of edges)d[b]=Math.min(d[b],d[a]+w);return d;}
for(let weight=0;weight<=12;weight++){
  const edges=graphEdges(weight),trace=dijkstraTrace(VERTICES,edges,'s','t'),final=trace.states.at(-1);
  assert.deepEqual(final.distance,bellman(VERTICES,edges,'s'));
  assert.equal(trace.path[0],'s');assert.equal(trace.path.at(-1),'t');
  const sum=trace.path.slice(1).reduce((total,v,i)=>total+edges.find(([a,b])=>a===trace.path[i]&&b===v)[2],0);
  assert.equal(sum,final.distance.t);
  for(const [i,s] of trace.states.entries()){
    assert(s.candidates.every(v=>!s.done.includes(v)));
    assert.equal(s.candidates.length+s.done.length,VERTICES.length);
    for(let j=1;j<s.candidates.length;j++)assert(s.distance[s.candidates[j-1]]<=s.distance[s.candidates[j]]);
    if(i){const before=trace.states[i-1];for(const v of before.done)assert.equal(s.distance[v],before.distance[v]);}
    if(s.kind==='确定距离'){
      const before=trace.states[i-1];
      assert.equal(s.focus,before.candidates[0]);
      assert.equal(s.done.length,before.done.length+1);
    }
  }
}
const dijkstra=dijkstraTrace(VERTICES,BASE_EDGES,'s','t');
assert.deepEqual(dijkstra.states.at(-1).distance,{s:0,b:5,c:6,d:7,e:9,t:12});
assert.deepEqual(dijkstra.states.at(-1).done,['s','b','c','d','e','t']);
assert.deepEqual(dijkstra.path,['s','c','d','e','t']);
assert(dijkstra.states.some(s=>s.kind==='松弛 / 更新'&&s.changed==='d'&&s.distance.d===7));
assert(dijkstra.states.some(s=>s.kind==='松弛 / 更新'&&s.changed==='t'&&s.distance.t===12));
assert.deepEqual(dijkstra.states[0].done,[]);assert.equal(dijkstra.states[0].distance.t,Infinity);
const unreachable=dijkstraTrace(['s','a','t'],[['s','a',2]],'s','t');
assert.equal(unreachable.states.at(-1).distance.t,Infinity);assert.deepEqual(unreachable.path,[]);
assert.throws(()=>dijkstraTrace(['s','t'],[['s','t',-1]],'s','t'),/非负/);
assert.deepEqual(ACTIVITIES,originalActivities);assert.deepEqual(BASE_EDGES,originalEdges);
assert.deepEqual(dijkstraTrace(VERTICES,BASE_EDGES,'s','t'),dijkstra);
"""
    subprocess.run([node, "-e", model + checks], check=True, capture_output=True, text=True)
