"""Verify the RSA classroom example, including non-coprime message values."""
from pathlib import Path
import re
import shutil
import subprocess

import pytest

PAGE = Path(__file__).resolve().parents[1] / "code/visualizations/rsa.html"


def run_model(checks):
    node = shutil.which("node")
    if node is None:
        pytest.skip("需要Node.js核对浏览器中的模型")
    source = re.search(r'<script id="rsa-model">(.*?)</script>', PAGE.read_text(), re.S).group(1)
    subprocess.run(
        [node, "-e", "const assert=require('node:assert/strict');\n" + source + "\nconst R=RSAModel;\n" + checks],
        check=True, capture_output=True, text=True, timeout=30,
    )


def test_classroom_vector_and_inverse():
    run_model("""
assert.equal(R.key.n,33);
assert.equal(R.key.phi,20);
assert.equal(R.inverse(7,20),3);
assert.equal((7*3)%20,1);
const t=R.transform(4);
assert.equal(t.c,16);
assert.equal(t.recovered,4);
assert.deepEqual(t.encryption.rows.map(r=>r.remainder),[4,16,31,25,1,4,16]);
assert.deepEqual(t.decryption.rows.map(r=>r.remainder),[16,25,4]);
assert.throws(()=>R.inverse(5,20));
""")


def test_every_legal_message_round_trips_and_can_be_recovered_from_public_data():
    # Python pow is independent of the browser's multiplication implementation.
    vectors = [(m, pow(m, 7, 33)) for m in range(33)]
    run_model("const vectors=" + str(vectors).replace("(", "[").replace(")", "]") + ";" + """
for(const [m,c] of vectors){
 const t=R.transform(m);
 assert.equal(t.c,c);
 assert.equal(t.recovered,m);
 assert.equal(t.encryption.rows.length,7);
 assert.equal(t.decryption.rows.length,3);
 const attack=R.recover({e:7,n:33},c);
 assert.deepEqual(attack,{p:3,q:11,phi:20,d:3,m});
}
assert.equal(R.transform(0).c,0);
assert.equal(R.transform(1).c,1);
assert.equal(R.gcd(3,33),3); // Non-coprime messages must work too.
assert.equal(R.transform(3).recovered,3);
assert.equal(R.powerTrace(4,0,33).value,1);
""")


def test_invalid_inputs_and_offline_resources():
    run_model("""
assert.equal(R.normalize(' 04 '),4);
for(const value of ['', ' ', '-1', '33', '4.2', '1e1', 'abc', '中文', 0.5, -1,33,NaN,Infinity,null,undefined])assert.throws(()=>R.normalize(value));
assert.throws(()=>R.powerTrace(2,-1,33));
assert.throws(()=>R.recover({n:33,e:7},33));
assert.throws(()=>R.factor(31));
""")
    html = PAGE.read_text()
    assert not re.search(r"<(?:script|img|iframe)\b[^>]*\bsrc\s*=", html, re.I)
    assert not re.search(r"<link\b[^>]*\bhref\s*=", html, re.I)
    assert not re.search(r"\b(?:fetch|WebSocket|XMLHttpRequest)\s*\(", html)
    assert "connect-src 'none'" in html
