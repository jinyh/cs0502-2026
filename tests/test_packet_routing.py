"""Verify the slide-style packet header / local table / output-interface linkage."""
from pathlib import Path
import re
import shutil
import subprocess

import pytest

PAGE = Path(__file__).resolve().parents[1] / 'code/visualizations/packet_routing.html'


def model(checks):
    node = shutil.which('node')
    if node is None:
        pytest.skip('Node.js is required to verify the browser model')
    script = re.search(r'<script id="packet-model">(.*?)</script>', PAGE.read_text(), re.S).group(1)
    subprocess.run([node, '-e', "const assert=require('node:assert/strict');\n" + script + '\nconst M=PacketForwardingModel;\n' + checks], check=True, capture_output=True, text=True, timeout=30)


def test_every_table_entry_names_an_actual_local_interface():
    model("""
const expected={R1:['A','B','R2','R3'],R2:['C','R1','R3','R5'],R3:['R1','R2','R4','R5'],R4:['D','E','R3','R5'],R5:['F','R2','R3','R4']};
for(const router of M.routers){
 assert.deepEqual(M.neighbors(router),expected[router]);
 assert.equal(M.tables[router].length,6);
 assert.deepEqual(M.tables[router].map(r=>r.dest),M.hosts);
 for(const row of M.tables[router])assert.equal(expected[router][row.port-1],row.next);
}
assert.equal(M.links.length,13); // Seven router links and six host links.
""")


def test_all_destinations_have_correct_paths_and_unchanged_packet_contents():
    model("""
const paths={A:['C','R2','R1','A'],B:['C','R2','R1','B'],D:['C','R2','R3','R4','D'],E:['C','R2','R3','R4','E'],F:['C','R2','R5','F']};
for(const [dest,path] of Object.entries(paths)){
 const frames=M.frames(dest);assert.deepEqual(frames.at(-1).path,path);
 assert.equal(frames.at(-1).at,dest);assert.equal(frames.at(-1).done,true);
 for(const f of frames){
  assert.equal(f.source,'C');assert.equal(f.destination,dest);assert.equal(f.payload,'hello');
  assert.deepEqual(f.path,path.slice(0,f.path.length));
  if(f.edge)assert.ok(M.neighbors(f.edge[0]).includes(f.edge[1]));
  if(f.output)assert.equal(M.neighbors(f.owner)[f.port-1],f.next);
 }
}
assert.equal(M.tables.R2.find(r=>r.dest==='D').port,M.tables.R2.find(r=>r.dest==='E').port);
assert.notEqual(M.tables.R2.find(r=>r.dest==='D').port,M.tables.R2.find(r=>r.dest==='F').port);
""")


def test_each_hop_reads_matches_and_chooses_in_order_without_early_answer():
    model("""
const frames=M.frames('D');assert.equal(frames[0].owner,null);assert.deepEqual(frames[0].path,['C']);
for(let i=0;i<frames.length;i++){
 const f=frames[i];
 if(f.phase==='arrive'){
  assert.equal(f.owner,f.at);assert.equal(f.matched,false);assert.equal(f.next,null);
  assert.equal(frames[i+1].phase,'read');assert.equal(frames[i+2].phase,'match');
  assert.equal(frames[i+3].phase,'choose');assert.equal(frames[i+4].phase,'send');
 }
 if(f.phase==='read'){
  assert.equal(f.checkpoint,true);assert.equal(f.header,true);
  assert.equal(f.matched,false);assert.equal(f.output,false);assert.equal(f.next,null);assert.equal(f.port,null);
 }
 if(f.phase==='match'){assert.equal(f.matched,true);assert.equal(f.output,false);}
 if(f.phase==='send'&&f.owner){assert.equal(f.owner,f.edge[0]);assert.equal(f.at,f.edge[1]);}
}
assert.deepEqual(frames.filter(f=>f.checkpoint).map(f=>f.owner),['R2','R3','R4']);
""")


def test_rewind_replay_reset_destination_change_and_invalid_destinations():
    model("""
let s=M.create();for(let i=0;i<8;i++)s=M.act(s,{type:'next'});
const saved=JSON.stringify(M.frame(s));
for(let i=0;i<8;i++)s=M.act(s,{type:'back'});
assert.deepEqual(s,M.create());s=M.act(s,{type:'back'});assert.deepEqual(s,M.create());
for(let i=0;i<8;i++)s=M.act(s,{type:'next'});assert.equal(JSON.stringify(M.frame(s)),saved);
s=M.act(s,{type:'destination',value:'F'});assert.deepEqual(s,M.create('F'));
assert.equal(M.frame(s).owner,null);assert.equal(M.frame(s).port,null);assert.deepEqual(M.frame(s).path,['C']);
for(let i=0;i<100;i++)s=M.act(s,{type:'next'});assert.equal(M.frame(s).done,true);
s=M.act(s,{type:'reset'});assert.deepEqual(s,M.create('F'));
for(const value of ['C','G','',null,undefined,'<script>'])assert.throws(()=>M.frames(value));
assert.throws(()=>M.act(s,{type:'missing'}));
""")


def test_offline_resources_and_all_script_syntax():
    html = PAGE.read_text()
    assert not re.search(r'<(?:script|img|iframe)\b[^>]*\bsrc\s*=', html, re.I)
    assert not re.search(r'<link\b[^>]*\bhref\s*=', html, re.I)
    assert not re.search(r'\b(?:fetch|WebSocket|XMLHttpRequest)\s*\(', html)
    assert "connect-src 'none'" in html
    assert 'prefers-reduced-motion' in html
    assert 'aria-live="polite"' in html
    assert '教学补充' in html
    node = shutil.which('node')
    if node:
        for script in re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>', html, re.S):
            subprocess.run([node, '--check'], input=script, text=True, check=True, capture_output=True)
