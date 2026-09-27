"""Verify the actual self-contained page's algorithm trace with Node.js."""

from pathlib import Path
import re
import shutil
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[1]


def test_graph_search_trace_preserves_stack_and_queue_semantics():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required to execute the browser algorithm model")
    html = (ROOT / "code/visualizations/graph_search.html").read_text(encoding="utf-8")
    model = re.search(r'<script id="search-model">(.*?)</script>', html, re.DOTALL).group(1)
    checks = r"""
const assert = require('node:assert/strict');
const dfs = buildTrace('dfs'), bfs = buildTrace('bfs');
assert.deepEqual(dfs.at(-1).seen, ['A','B','D','C','E']);
assert.deepEqual(bfs.at(-1).seen, ['A','B','C','D','E']);
assert.deepEqual(bfs.at(-1).distances, {A:0,B:1,C:1,D:2,E:3});
assert.deepEqual(dfs.at(-1).stack, []);
assert.deepEqual(bfs.at(-1).queue, []);
const dc = dfs.filter(s=>s.checkpoint), bc = bfs.filter(s=>s.checkpoint);
assert.equal(dc.length,1);assert.equal(bc.length,1);
assert.deepEqual(dc[0].stack.map(f=>f.node),['A','B','D','C']);
assert.deepEqual(bc[0].queue,['C','D']);
const returned = dfs[dfs.indexOf(dc[0])+1];
assert.equal(returned.current,'D');
assert.deepEqual(returned.stack.map(f=>f.node),['A','B','D']);
assert.deepEqual(returned.seen, dc[0].seen); // Returning is not rediscovery.
assert.equal(bfs[bfs.indexOf(bc[0])+1].current,'C');
assert.equal(bfs.filter(s=>s.kind==='标记并入队' && s.seen.at(-1)==='D').length,1);
for(const trace of [dfs,bfs]) {
  assert.deepEqual([...trace.at(-1).done].sort(),['A','B','C','D','E']);
  for(let i=0;i<trace.length;i++) {
    const s=trace[i], prev=trace[i-1];
    assert.equal(new Set(s.seen).size,s.seen.length);
    assert.equal(new Set(s.done).size,s.done.length);
    assert(s.done.every(v=>s.seen.includes(v)));
    assert.equal(s.tree.length,Math.max(0,s.seen.length-1));
    for(const [a,b] of s.tree) assert(GRAPH[a].includes(b));
    if(prev) assert.deepEqual(s.seen.slice(0,prev.seen.length),prev.seen);
    if(trace===dfs) {
      const chain=s.stack.map(f=>f.node);
      assert(chain.every(v=>s.seen.includes(v)&&!s.done.includes(v)));
      for(let k=1;k<chain.length;k++) assert(GRAPH[chain[k-1]].includes(chain[k]));
      assert.equal(s.current,chain.at(-1)||null);
      assert(s.stack.every(f=>f.next>=0&&f.next<=GRAPH[f.node].length));
      if(s.kind==='压栈 / push') assert.deepEqual(chain.slice(0,-1),prev.stack.map(f=>f.node));
      if(s.kind==='弹栈 / pop') assert.deepEqual(chain,prev.stack.slice(0,-1).map(f=>f.node));
    } else {
      assert.equal(new Set(s.queue).size,s.queue.length);
      assert(s.queue.every(v=>s.seen.includes(v)&&!s.done.includes(v)&&v!==s.current));
      for(let k=1;k<s.queue.length;k++) assert(s.distances[s.queue[k-1]]<=s.distances[s.queue[k]]);
      if(s.kind==='出队 / dequeue') {
        assert.equal(s.current,prev.queue[0]);
        assert.deepEqual(s.queue,prev.queue.slice(1));
      }
      if(s.kind==='标记并入队') {
        assert.deepEqual(s.queue.slice(0,-1),prev.queue);
        assert(!prev.seen.includes(s.queue.at(-1)));
      }
    }
  }
}
// Generating or inspecting a second trace must not modify previous snapshots.
assert.deepEqual(dfs[0].seen,[]);
assert.deepEqual(bfs[0].queue,[]);
assert.deepEqual(buildTrace('dfs'),dfs);
assert.deepEqual(buildTrace('bfs'),bfs);
"""
    subprocess.run([node, "-e", model + checks], check=True, capture_output=True, text=True)
