"""Cross-check the classroom forwarding trace and destination-rooted shortest paths."""
from collections import deque
import json
from pathlib import Path
import re
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / 'code/visualizations/packet_routing.html'


def model(checks):
    node = shutil.which('node')
    if node is None:
        pytest.skip('Node.js is needed to verify the browser model')
    script = re.search(r'<script id="routing-model">(.*?)</script>', PAGE.read_text(), re.S).group(1)
    result = subprocess.run([node, '-e', "const assert=require('node:assert/strict');\n" + script + '\nconst M=PacketRoutingModel;\n' + checks], check=True, capture_output=True, text=True, timeout=30)
    return result.stdout


def test_forwarding_paths_delays_and_stage_boundaries():
    model("""
const old=M.stageFrames.given, fresh=M.stageFrames.new;
assert.deepEqual(old.at(-1).path,['S','N1','N3','N2','N4','T']);
assert.deepEqual(fresh.at(-1).path,['S','N1','N2','N4','T']);
assert.equal(old.at(-1).elapsed,20);assert.equal(old.at(-1).hops,3);
assert.equal(fresh.at(-1).elapsed,12);assert.equal(fresh.at(-1).hops,2);
for(const frames of [old,fresh]){
 assert.deepEqual(frames[0].path,['S']);assert.equal(frames[0].elapsed,0);
 for(let i=1;i<frames.length;i++){
  const f=frames[i],p=frames[i-1];
  if(f.phase==='lookup')assert.equal(f.elapsed-p.elapsed,M.delays[f.at]);
  else assert.equal(f.elapsed,p.elapsed);
  if(f.phase==='read'||f.phase==='arrive')assert.equal(f.next,null);
  if(f.phase==='arrive')assert.equal(f.tableOwner,null);
  if(f.phase==='send'&&f.at!=='N1'&&f.at!=='T')assert.ok(M.neighbors(f.tableOwner).includes(f.at));
 }
 const checkpoint=frames.find(f=>f.checkpoint);
 assert.deepEqual(checkpoint.path,['S','N1']);assert.equal(checkpoint.next,null);
 assert.equal(checkpoint.elapsed,0);assert.equal(checkpoint.phase,'arrive');
}
assert.throws(()=>M.forwarding({...M.given,N1:'N4'}),/相邻/);
assert.throws(()=>M.forwarding({...M.given,N2:'N3'}),/环路/);
""")


def test_dijkstra_against_independent_bfs_and_each_relaxation():
    output = model("console.log(JSON.stringify({links:M.links,frames:M.routing(),table:M.newTable}));")
    data = json.loads(output)
    adjacent = {n: [] for n in ['N1', 'N2', 'N3', 'N4']}
    for a, b in data['links']:
        adjacent[a].append(b)
        adjacent[b].append(a)
    dist = {'N4': 0}
    queue = deque(['N4'])
    while queue:
        node = queue.popleft()
        for other in adjacent[node]:
            if other not in dist:
                dist[other] = dist[node] + 1
                queue.append(other)
    final = data['frames'][-1]
    assert final['dist'] == dist == {'N4': 0, 'N2': 1, 'N1': 2, 'N3': 2}
    assert data['table'] == {'N1': 'N2', 'N2': 'N4', 'N3': 'N2', 'N4': 'T'}
    assert final['settled'] == ['N4', 'N2', 'N1', 'N3']
    for node, hop in data['table'].items():
        if node != 'N4':
            assert hop in adjacent[node]
            assert dist[node] == dist[hop] + 1
    frames = data['frames']
    for before, after in zip(frames, frames[1:]):
        if after['phase'] == 'compare':
            assert after['dist'] == before['dist']
            assert after['prev'] == before['prev']
            assert after['checkpoint']
        if after['phase'] == 'relax':
            source, target = after['edge']
            expected = before['dist'][source] + 1
            assert after['dist'][target] == min(before['dist'][target] or float('inf'), expected)
        if not after['done']:
            assert 'table' not in after


def test_rewind_replay_reset_and_new_table_gate():
    model("""
let s=M.createState();assert.deepEqual(M.act(s,{type:'stage',stage:'new'}),s);
s=M.act(s,{type:'stage',stage:'routing'});
for(let i=0;i<M.stageFrames.routing.length-2;i++)s=M.act(s,{type:'next'});
assert.equal(s.routeReady,false);
assert.deepEqual(M.act(s,{type:'stage',stage:'new'}),s);
s=M.act(s,{type:'next'});assert.equal(s.routeReady,true);
const end=JSON.stringify(M.frame(s));
s=M.act(s,{type:'back'});assert.equal(s.routeReady,false);
s=M.act(s,{type:'next'});assert.equal(JSON.stringify(M.frame(s)),end);
s=M.act(s,{type:'stage',stage:'new'});
assert.deepEqual(M.frame(s).path,['S']);assert.equal(M.frame(s).elapsed,0);
for(let i=0;i<M.stageFrames.new.length+2;i++)s=M.act(s,{type:'next'});
assert.equal(M.frame(s).elapsed,12);
s=M.act(s,{type:'reset'});assert.equal(M.frame(s).elapsed,0);
s=M.act(s,{type:'stage',stage:'routing'});assert.equal(s.routeReady,false);
assert.equal(M.frame(s).phase,'initial');assert.deepEqual(M.frame(s).settled,[]);
for(const stage of ['given','routing']){
 let a=M.act(M.createState(),{type:'stage',stage});
 const initial=JSON.stringify(M.frame(a));a=M.act(a,{type:'back'});
 assert.equal(JSON.stringify(M.frame(a)),initial);
 for(let i=0;i<8;i++)a=M.act(a,{type:'next'});
 const saved=JSON.stringify(M.frame(a));
 for(let i=0;i<8;i++)a=M.act(a,{type:'back'});
 for(let i=0;i<8;i++)a=M.act(a,{type:'next'});
 assert.equal(JSON.stringify(M.frame(a)),saved);
}
""")


def test_offline_assets_and_script_syntax():
    html = PAGE.read_text()
    assert not re.search(r'<(?:script|img|iframe)\b[^>]*\bsrc\s*=', html, re.I)
    assert not re.search(r'<link\b[^>]*\bhref\s*=', html, re.I)
    assert not re.search(r'\b(?:fetch|WebSocket|XMLHttpRequest)\s*\(', html)
    assert "connect-src 'none'" in html
    assert 'prefers-reduced-motion' in html
    node = shutil.which('node')
    if node:
        for script in re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>', html, re.S):
            subprocess.run([node, '--check'], input=script, text=True, check=True, capture_output=True)


def test_expanded_topology_shortest_paths_ties_and_switch_isolation():
    model("""
const E=PacketRoutingModel.create('expanded');
assert.equal(E.routers.length,7);assert.equal(E.links.length,12);assert.equal(E.root,'N7');
assert.deepEqual(E.stageFrames.given.at(-1).path,['S','N1','N3','N2','N5','N4','N6','N7','T']);
assert.equal(E.stageFrames.given.at(-1).elapsed,35);
assert.deepEqual(E.stageFrames.new.at(-1).path,['S','N1','N2','N4','N7','T']);
assert.equal(E.stageFrames.new.at(-1).elapsed,15);
assert.equal(E.stageFrames.new.at(-1).hops,3);
// Independent BFS and enumeration of equally short choices.
const d={N7:0},q=['N7'];for(let i=0;i<q.length;i++)for(const n of E.neighbors(q[i]))if(!(n in d)){d[n]=d[q[i]]+1;q.push(n);}
assert.deepEqual(E.stageFrames.routing.at(-1).dist,d);
for(const n of E.routers)if(n!==E.root){assert.ok(E.neighbors(n).includes(E.newTable[n]));assert.equal(d[n],d[E.newTable[n]]+1);}
assert.ok(E.routing().some(f=>f.message.includes('等长备选路径')));
assert.deepEqual(E.createState(),M.createState());
assert.equal(M.root,'N4');assert.equal(M.stageFrames.new.at(-1).elapsed,12);
assert.throws(()=>PacketRoutingModel.create('unknown'));
""")
