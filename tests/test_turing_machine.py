"""核对课堂页面的真实模型、Python 示例和课件关键配置。"""

import importlib.util
import itertools
import json
from pathlib import Path
import re
import shutil
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "code/visualizations/turing_machine.html"


def example():
    spec = importlib.util.spec_from_file_location(
        "turing_example", ROOT / "code/examples/08_turing_machine.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_python_examples_and_backward_compatible_trace():
    machine = example()
    output, trace = machine.run_machine(machine.FLIP_BITS, "0110")
    assert output == "1001"
    assert trace == [
        (0, "scan", 0, "0"),
        (1, "scan", 1, "1"),
        (2, "scan", 2, "1"),
        (3, "scan", 3, "0"),
        (4, "scan", 4, "_"),
        (5, "halt", 5, "_"),
    ]
    assert machine.run_machine(machine.FLIP_BITS, "") == (
        "", [(0, "scan", 0, "_"), (1, "halt", 1, "_")]
    )
    for x, y in itertools.product(range(6), repeat=2):
        total, trace = machine.run_unary_addition(x, y)
        assert total == x + y
        assert trace[-1][0:2] == (x + y + 3, "halt")
    _, trace = machine.run_unary_addition(3, 4)
    assert [(trace[i][1], trace[i][2]) for i in [3, 4, 8, 9, 10]] == [
        ("q1", 4), ("q2", 5), ("q2", 9), ("q3", 8), ("halt", 9)
    ]
    for pair in [(-1, 4), (1.5, 4), ("3", 4), (True, 4)]:
        with pytest.raises(ValueError, match="非负整数"):
            machine.run_unary_addition(*pair)


def test_python_halt_missing_rule_and_step_limit_are_distinct():
    machine = example()
    assert machine.run_machine({}, "", start="halt", max_steps=0) == (
        "", [(0, "halt", 0, "_")]
    )
    with pytest.raises(ValueError, match="没有转移规则"):
        machine.run_machine({}, "0")
    loop = {("scan", "_"): ("scan", "_", "R")}
    with pytest.raises(TimeoutError, match="本次未观察到停机"):
        machine.run_machine(loop, "", max_steps=2)
    with pytest.raises(ValueError, match="移动方向"):
        machine.run_machine({("scan", "0"): ("scan", "1", "invalid")}, "0")


def test_browser_model_matches_python_and_transition_invariants():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required to execute the page's model")
    html = PAGE.read_text(encoding="utf-8")
    model = re.search(r'<script id="turing-model">(.*?)</script>', html, re.S).group(1)
    flips = [
        "".join(bits)
        for length in range(6)
        for bits in itertools.product("01", repeat=length)
    ] + ["01" * 16]
    pairs = list(itertools.product(range(6), repeat=2)) + [(20, 20)]
    inputs = [{"mode": "flip", "input": {"text": text}} for text in flips]
    inputs += [{"mode": "addition", "input": {"x": x, "y": y}} for x, y in pairs]
    checks = r"""
const assert = require('node:assert/strict');
const results = inputs.map(({mode,input}) => {
  let config = createMachine(mode,input);
  const snapshots = [config], original = JSON.stringify(config);
  while(config.status === 'running') {
    const before = config, tapeBefore = JSON.stringify(before.tape);
    config = stepMachine(before,MACHINE_RULES[mode]);
    assert.equal(JSON.stringify(before.tape),tapeBefore);
    assert.equal(config.step,before.step+1);
    assert.equal(Math.abs(config.head-before.head),1);
    const keys = new Set([...Object.keys(before.tape),...Object.keys(config.tape)]);
    for(const key of keys) {
      if(Number(key)!==before.head) assert.equal(config.tape[key],before.tape[key]);
    }
    assert.equal(config.tape[before.head],config.last.write);
    assert.equal(config.state,config.last.next);
    assert.equal(config.head,before.head+(config.last.move==='R'?1:-1));
    snapshots.push(config);
    assert(snapshots.length < 100);
  }
  assert.equal(config.status,'halted');
  assert.equal(JSON.stringify(snapshots[0]),original);
  assert.deepEqual(stepMachine(config,MACHINE_RULES[mode]),config);
  // 回看旧配置后再次执行，应得到同一条后续轨迹。
  for(let i=0;i<snapshots.length-1;i++)
    assert.deepEqual(stepMachine(snapshots[i],MACHINE_RULES[mode]),snapshots[i+1]);
  return {
    mode,input,output:tapeContents(config),
    trace:snapshots.map(s=>[s.step,s.state,s.head,readSymbol(s)]),
    checkpoints:snapshots.filter(s=>predictionQuestion(mode,s)).map(s=>s.step)
  };
});
const sample=results.find(r=>r.mode==='flip'&&r.input.text==='0110');
assert.equal(sample.output,'1001');
assert.deepEqual(sample.checkpoints,[0,4]);
const addition=results.find(r=>r.mode==='addition'&&r.input.x===3&&r.input.y===4);
assert.deepEqual(addition.checkpoints,[0,3,8,9]);
assert.equal(addition.output,'▷1111111◁');
assert.equal(stepMachine(createMachine('flip',{text:'0'}),[]).status,'missing_rule');
const loop=[{state:'scan',read:'_',write:'_',move:'R',next:'scan'}];
let config=createMachine('flip',{text:''});
config=stepMachine(config,loop,1);
const limited=stepMachine(config,loop,1);
assert.equal(limited.status,'step_limit');
assert.equal(limited.step,1);
assert(limited.message.includes('本次未观察到停机'));
assert.equal(stepMachine(createMachine('flip',{text:''}),MACHINE_RULES.flip,1).status,'halted');
// 支持纸带负下标，改写仍发生在原位置。
const left=stepMachine(createMachine('flip',{text:'0'}),[
  {state:'scan',read:'0',write:'1',move:'L',next:'halt'}
]);
assert.equal(left.head,-1);assert.equal(left.tape[0],'1');assert.equal(readSymbol(left),'_');
for(const text of ['2','0102','0'.repeat(33),'01\n',' '])
  assert.throws(()=>createMachine('flip',{text}));
for(const input of [{x:-1,y:0},{x:21,y:0},{x:1.5,y:0},{x:NaN,y:0},{x:true,y:0}])
  assert.throws(()=>createMachine('addition',input));
process.stdout.write(JSON.stringify(results));
"""
    completed = subprocess.run(
        [node, "-e", model + "\nconst inputs=" + json.dumps(inputs) + ";\n" + checks],
        check=True, capture_output=True, text=True,
    )
    machine = example()
    for result in json.loads(completed.stdout):
        if result["mode"] == "flip":
            text = result["input"]["text"]
            output, trace = machine.run_machine(machine.FLIP_BITS, text)
            assert output == text.translate(str.maketrans("01", "10"))
            assert trace[-1][0] == len(text) + 1
        else:
            x, y = result["input"]["x"], result["input"]["y"]
            output, trace = machine.run_machine(
                machine.UNARY_ADDITION, "▷" + "1" * x + "0" + "1" * y + "◁",
                start="q1", start_head=1,
            )
            assert output == "▷" + "1" * (x + y) + "◁"
            assert trace[-1][0] == x + y + 3
        assert result["output"] == output
        assert result["trace"] == [list(row) for row in trace]
