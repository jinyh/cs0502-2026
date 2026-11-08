"""Check the four-letter teaching model, including reciprocal operation and stepping."""
from pathlib import Path
import re
import shutil
import subprocess

import pytest

PAGE = Path(__file__).resolve().parents[1] / "code/visualizations/enigma.html"


def run_model(checks):
    node = shutil.which("node")
    if node is None:
        pytest.skip("需要Node.js核对浏览器中的模型")
    source = re.search(r'<script id="enigma-model">(.*?)</script>', PAGE.read_text(), re.S).group(1)
    subprocess.run([node, "-e", "const assert=require('node:assert/strict');\n" + source + "\nconst E=EnigmaModel;\n" + checks], check=True, capture_output=True, text=True, timeout=30)


def test_default_vectors_and_carry():
    run_model("""
const c={initial:[0,0,0],plug:'ab',freeze:false};
assert.equal(E.transform('AAAA',c).output,'BDBC');
assert.equal(E.transform('BDBC',c).output,'AAAA');
assert.equal(E.transform('AAAA',{...c,freeze:true}).output,'DDDD');
assert.deepEqual(E.advance([3,0,0]),[0,1,0]);
assert.deepEqual(E.advance([3,3,0]),[0,0,1]);
assert.deepEqual(E.advance([3,3,3]),[0,0,0]);
assert.deepEqual(E.advance([3,3,3],true),[3,3,3]);
const encoded=E.transform('AAAA',c);
assert.notEqual(E.transform(encoded.output,{...c,initial:encoded.positions}).output,'AAAA');
""")


def test_reciprocity_and_trace_for_all_settings():
    run_model("""
for(let a=0;a<4;a++)for(let b=0;b<4;b++)for(let c=0;c<4;c++)
 for(const plug of Object.keys(E.plugs))for(const freeze of [false,true]){
  const cfg={initial:[a,b,c],plug,freeze},snapshot=JSON.stringify(cfg);
  for(const letter of E.ABC){
   const t=E.trace(letter,cfg.initial,cfg);
   assert.notEqual(t.output,letter); // paired reflector has no fixed point
   assert.equal(E.trace(t.output,cfg.initial,cfg).output,letter);
   assert.equal(t.values.length,10);
   assert.equal(E.ABC[t.values[0]],letter);
   assert.equal(E.ABC[t.values[9]],t.output);
   assert.ok(t.values.every(x=>Number.isInteger(x)&&x>=0&&x<4));
  }
  for(const input of ['ABCD','AAAABBBBCCCCDDDD','ABCD'.repeat(8)]){
   const enc=E.transform(input,cfg);
   assert.equal(E.transform(enc.output,cfg).output,input);
   assert.deepEqual(enc.positions,freeze?cfg.initial:E.advance(E.transform(input.slice(0,-1),cfg).positions));
  }
  assert.equal(JSON.stringify(cfg),snapshot);
 }
""")


def test_input_validation_and_offline_page():
    run_model("""
assert.equal(E.normalize('a b\ncd'),'ABCD');
for(const value of ['', 'E', 'A1', '中文', 'A'.repeat(33)])assert.throws(()=>E.normalize(value));
for(const cfg of [{initial:[4,0,0],plug:'ab',freeze:false},{initial:[0,0],plug:'ab',freeze:false},{initial:[0,0,0],plug:'x',freeze:false}])assert.throws(()=>E.transform('A',cfg));
""".replace("'a b\ncd'", "'a b\\ncd'"))
    html = PAGE.read_text()
    assert not re.search(r"<(?:script|img|iframe)\b[^>]*\bsrc\s*=", html, re.I)
    assert not re.search(r"<link\b[^>]*\bhref\s*=", html, re.I)
    assert not re.search(r"\b(?:fetch|WebSocket|XMLHttpRequest)\s*\(", html)
    assert "connect-src 'none'" in html
