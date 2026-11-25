"""Verify the Slide14 clustering model (K-Means, Hierarchical, DBSCAN) and offline page invariants."""
from pathlib import Path
import re
import shutil
import subprocess

import pytest

PAGE = Path(__file__).resolve().parents[1] / "code/visualizations/clustering.html"


def run_model(checks):
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required to verify the browser clustering model")
    match = re.search(r'<script id="clustering-model">(.*?)</script>', PAGE.read_text(encoding="utf-8"), re.S)
    assert match, "clustering-model script block missing"
    script = match.group(1)
    code = (
        "const assert = require('node:assert/strict');\n"
        + script
        + "\nconst M = ClusteringModel;\n"
        + checks
    )
    proc = subprocess.run([node, "-e", code], capture_output=True, text=True, timeout=30)
    assert proc.returncode == 0, f"Node check failed:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"


def test_slide14_p28_kmeans_both_initializations():
    run_model("""
const ae = M.KMEANS_STEP_PRESETS.slide14_ae;
const runAE = M.runKMeans(ae.points, 2, ae.initIndices);
assert.equal(runAE.frames[0].phase, 'init');
assert.equal(runAE.frames.at(-1).phase, 'done');
assert.equal(runAE.frames.at(-1).stable, true);
assert.deepEqual(runAE.finalCenters, [{ x: 1, y: 5 }, { x: 9, y: 5 }]);
assert.equal(runAE.sse, 100);
assert.deepEqual(runAE.finalLabels, [0, 0, 0, 0, 1, 1, 1, 1]);

const ad = M.KMEANS_STEP_PRESETS.slide14_ad;
const runAD = M.runKMeans(ad.points, 2, ad.initIndices);
assert.deepEqual(runAD.finalCenters, [{ x: 5, y: 1.5 }, { x: 5, y: 8.5 }]);
assert.equal(runAD.sse, 130);
assert.deepEqual(runAD.finalLabels, [0, 0, 1, 1, 0, 0, 1, 1]);
assert.ok(runAD.sse > runAE.sse, 'A,D init should yield higher SSE local optimum');

// Outlier pull preset shifts cluster 2 centroid away from (6,6)
const out = M.KMEANS_STEP_PRESETS.outlier_pull;
const runOut = M.runKMeans(out.points, 2, out.initIndices);
assert.deepEqual(runOut.finalCenters[0], { x: 2, y: 3 });
assert.ok(runOut.finalCenters[1].x > 6.5 && runOut.finalCenters[1].y > 6.5);
""")


def test_slide14_p32_dbscan_exact_match_and_border_non_expansion():
    run_model("""
const p32 = M.DBSCAN_STEP_PRESETS.slide14_p32;
const res = M.runDBSCAN(p32.points, p32.eps, p32.minPts, p32.checkpointIds);
const byId = Object.fromEntries(p32.points.map((p, i) => [p.id, i]));
const nbrNames = id => res.neighbors[byId[id]].map(j => p32.points[j].id);

assert.deepEqual(nbrNames('A'), ['A', 'B', 'C', 'D']);
assert.deepEqual(nbrNames('B'), ['A', 'B', 'C']); // includes self -> 3; d^2(A,B)=4 <= 4
assert.deepEqual(nbrNames('C'), ['A', 'B', 'C']);
assert.deepEqual(nbrNames('D'), ['A', 'D']);
assert.deepEqual(nbrNames('E'), ['E', 'F', 'G']);
assert.deepEqual(nbrNames('F'), ['E', 'F', 'G']);
assert.deepEqual(nbrNames('G'), ['E', 'F', 'G']);
assert.deepEqual(nbrNames('H'), ['H']);
assert.equal(M.dist2(p32.points[byId.A], p32.points[byId.B]), 4);

const roleMap = Object.fromEntries(p32.points.map((p, i) => [p.id, res.roles[i]]));
assert.deepEqual(roleMap, {
  A: 'core', B: 'core', C: 'core', D: 'border',
  E: 'core', F: 'core', G: 'core', H: 'noise'
});
const clusters = res.clusters.map(c => c.map(i => p32.points[i].id));
assert.deepEqual(clusters, [['A', 'B', 'C', 'D'], ['E', 'F', 'G']]);
assert.deepEqual(res.noise.map(i => p32.points[i].id), ['H']);

// Border non-expansion preset (eps=2, MinPts=4)
const bp = M.DBSCAN_STEP_PRESETS.dbscan_border;
const bres = M.runDBSCAN(bp.points, bp.eps, bp.minPts, bp.checkpointIds);
const bRole = Object.fromEntries(bp.points.map((p, i) => [p.id, bres.roles[i]]));
assert.equal(bRole.E, 'border'); // touches core D and core F, but |N(E)|=3 < 4
assert.equal(bRole.J, 'border'); // touches core B and noise K, |N(J)|=3 < 4
assert.equal(bRole.K, 'noise');  // only neighbor is border J -> must remain noise!
assert.equal(bres.clusters.length, 2, 'border E must NOT bridge the two core clusters');
assert.deepEqual(bres.noise.map(i => bp.points[i].id), ['K']);
""")


def test_hierarchical_p30_topology_linkage_difference_and_cut_invariants():
    run_model("""
const six = M.HIER_STEP_PRESETS.hier_six;
for (const linkage of ['single', 'average', 'complete']) {
  const h = M.runHierarchical(six.points, linkage);
  assert.equal(h.merges.length, 5);
  // First 3 merges are (A,B), (C,D), (E,F)
  const pairs = h.merges.slice(0, 3).map(m => m.mergedMembers.map(i => six.points[i].id).join(''));
  assert.deepEqual(pairs, ['AB', 'CD', 'EF']);
  // 4th merge joins AB and CD -> ABCD
  assert.equal(h.merges[3].mergedMembers.map(i => six.points[i].id).join(''), 'ABCD');
  // Monotonic merge heights
  for (let i = 1; i < h.merges.length; i++) {
    assert.ok(h.merges[i].distance >= h.merges[i - 1].distance - 1e-9);
  }
  // Cut at every k produces exact k non-empty clusters
  for (let k = 1; k <= six.points.length; k++) {
    const cut = M.cutDendrogram(h, k);
    assert.equal(cut.groups.length, k);
    assert.equal(cut.sizes.reduce((a, b) => a + b, 0), six.points.length);
  }
}

// Parallel bars: Single linkage separates top vs bottom bar, Complete linkage separates left vs right square
const bars = M.HIER_STEP_PRESETS.hier_bridge;
const cutSingle = M.cutDendrogram(M.runHierarchical(bars.points, 'single'), 2);
const cutComplete = M.cutDendrogram(M.runHierarchical(bars.points, 'complete'), 2);
const fmt = cut => cut.groups.map(g => g.map(i => bars.points[i].id).join('')).sort();
assert.deepEqual(fmt(cutSingle), ['ABCD', 'EFGH']);
assert.deepEqual(fmt(cutComplete), ['ABEF', 'CDGH']);
""")


def test_compare_mode_five_datasets_and_voronoi():
    run_model("""
// 1. Blobs: all 3 algorithms find 3 clean clusters of 14 points each
const blobs = M.compareAll('blobs');
assert.deepEqual(blobs.db.clusters.map(c => c.length), [14, 14, 14]);
assert.equal(blobs.db.noise.length, 0);
assert.deepEqual(blobs.hcCut.sizes, [14, 14, 14]);
const kmBlobCounts = [0, 0, 0];
blobs.km.finalLabels.forEach(c => kmBlobCounts[c]++);
assert.deepEqual(kmBlobCounts.sort((a, b) => a - b), [14, 14, 14]);

// 2. Moons + 6 noise (P34): DBSCAN isolates exact 2 moons (21 each) + 6 noise; K-Means has 0 noise & mixes moons
const moons = M.compareAll('moons');
assert.deepEqual(moons.db.clusters.map(c => c.length).sort((a, b) => a - b), [21, 21]);
assert.equal(moons.db.noise.length, 6);
const moon0Labels = new Set(moons.points.slice(0, 21).map((_, i) => moons.km.finalLabels[i]));
assert.equal(moon0Labels.size, 2, 'K-Means must slice upper moon across both clusters');

// 3. Rings: DBSCAN & Single-linkage separate inner(16) vs outer(36); K-Means mixes outer ring
const rings = M.compareAll('rings');
assert.deepEqual(rings.db.clusters.map(c => c.length).sort((a, b) => a - b), [16, 36]);
assert.equal(rings.db.noise.length, 0);
assert.deepEqual([...rings.hcCut.sizes].sort((a, b) => a - b), [16, 36]);
const outerKm = new Set(rings.points.slice(16).map((_, i) => rings.km.finalLabels[16 + i]));
assert.equal(outerKm.size, 2, 'K-Means must split the outer ring');

// 4. Outliers: DBSCAN marks all 3 far outliers as noise and keeps the 3 real clusters
const outliers = M.compareAll('outliers');
assert.equal(outliers.db.noise.length, 3);
assert.deepEqual(outliers.db.clusters.map(c => c.length).sort((a, b) => a - b), [9, 14, 14]);

// 5. Varied density (DBSCAN limitation): small eps loses sparse cluster; large eps fuses dense pair; K-Means & Average HC find 3
const vdSmall = M.compareAll('varied_density', [], { dbEps: 0.85, dbMin: 4 });
assert.equal(vdSmall.db.clusters.length, 2);
assert.equal(vdSmall.db.noise.length, 10, 'Small eps should turn all 10 sparse points into noise');
const vdLarge = M.compareAll('varied_density', [], { dbEps: 2.00, dbMin: 4 });
assert.equal(vdLarge.db.clusters.length, 2, 'Large eps should fuse the two left dense clusters');
assert.equal(vdLarge.db.noise.length, 0);
const kmVdCounts = [0, 0, 0];
vdSmall.km.finalLabels.forEach(c => kmVdCounts[c]++);
assert.deepEqual(kmVdCounts.sort((a, b) => a - b), [10, 16, 16]);
assert.deepEqual([...vdSmall.hcCut.sizes].sort((a, b) => a - b), [10, 16, 16]);

// Custom point appending works cleanly across all 3 algorithms
const withExtra = M.compareAll('blobs', [{ x: 9.5, y: 0.5 }]);
assert.equal(withExtra.points.length, 43);
assert.equal(withExtra.db.noise.length, 1);

// Voronoi polygon clipping yields valid convex cells covering centers
const polys = M.voronoiPolygons(blobs.km.finalCenters);
assert.equal(polys.length, 3);
for (const poly of polys) assert.ok(poly.length >= 3);
""")


def test_offline_security_accessibility_and_script_syntax():
    html = PAGE.read_text(encoding="utf-8")
    assert not re.search(r"<(?:script|img|iframe)\b[^>]*\bsrc\s*=", html, re.I)
    assert not re.search(r"<link\b[^>]*\bhref\s*=", html, re.I)
    assert not re.search(r"\b(?:fetch|WebSocket|XMLHttpRequest)\s*\(", html)
    assert "connect-src 'none'" in html
    assert "prefers-reduced-motion" in html
    assert 'aria-live="polite"' in html
    assert "先预测" in html
    node = shutil.which("node")
    if node:
        scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.S)
        assert len(scripts) == 2
        for script in scripts:
            subprocess.run([node, "--check"], input=script, text=True, check=True, capture_output=True)
