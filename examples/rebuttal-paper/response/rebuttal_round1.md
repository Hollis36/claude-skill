# Response to Reviewers — NeurIPS 2026 Round 1

We thank all reviewers for their constructive feedback. We are encouraged that
R1 and R3 recognize the practical importance of our routing approach, and that
R3 highlights "the clearest motivation in this batch." Below we address each
concern; **bold** marks where new experiments or analyses have been added.

**Summary of changes** (preview): we will (a) add a 5-seed paired Wilcoxon
test to all main results, (b) clarify the router score function with a worked
example in §3.2, (c) include a router-head ablation, and (d) release anonymous
code with a one-command reproduction script.

---

## R1 (rating 6, confidence 4)

[TODO: R1-Q1 — Method §3.2 clarity]

[TODO: R1-Q2 — H2O 5-seed comparison; experiment 0042 is running, will fill
once complete with the exact mean ± std and Wilcoxon p-value from
`scripts/stats.py compare --method-a Ours --method-b H2O`]

[TODO: R1-Q3 — extend Limitations]

---

## R2 (rating 4, confidence 3)

[TODO: R2-Q1 — Novelty vs H2O. This is the most critical question.
Outline:
  - H2O routes via attention-score heuristic, fixed at inference;
  - Ours: learned, per-layer router with explicit sparsity supervision;
  - Quantitative gap: +6.3 pp on LongBench, +8.8 pp on RULER (Table 1);
  - Build comparison table similar to templates/rebuttal.md "Novelty" pattern]

**[R2-Q2] Statistical significance.** We re-ran main experiments with 5 random
seeds (previously 3). Improvements remain significant: on LongBench, Ours
achieves $84.5 \pm 0.2$ vs FlashAttention-2 $82.7 \pm 0.2$
($p = 0.031$, paired Wilcoxon signed-rank, one-sided, $n=5$). On RULER,
$73.7 \pm 0.3$ vs $71.3 \pm 0.2$ ($p = 0.031$). On InfiniteBench,
$58.8 \pm 0.2$ vs $56.2 \pm 0.2$ ($p = 0.031$). The Wilcoxon $p=0.031$ is the
minimum attainable at $n=5$, reflecting that Ours wins every paired comparison.
We updated Table 1 with mean ± std and significance annotations; the full
5-seed CSV is in the anonymous repository for verification.

[TODO: R2-Q3 — router head ablation; awaiting experiment]

[TODO: R2-Q4 — InfiniteBench performance. Reviewer interpreted Fig. 4 as
showing degraded performance; clarify that we report relative to baseline,
and Table 2 shows Ours absolute is highest. Cite Table 2 line directly.]

**[R2-Q5] Reproducibility.** We have prepared an anonymous repository at
https://anonymous.4open.science/r/attention-routing-rebuttal/ containing:
training scripts, evaluation configs, the exact 5-seed checkpoints, and a
one-command reproduction `bash scripts/reproduce_table_1.sh` that regenerates
Table 1 in approximately 6 hours on a single A100. The README provides the
exact PyTorch and CUDA versions used. The repository will be de-anonymized
upon acceptance.

---

## R3 (rating 7, confidence 5)

[TODO: R3-Q1 — Discussion of scaling to 70B. Approach:
  - Compute requirement: router adds ~0.3% params, scaling is linear;
  - We don't have 70B experiments due to compute; will commit to
    follow-up in camera-ready Discussion;
  - Cite the few existing 70B long-context papers for context]

[TODO: R3-Q2 — typo at §4.2 paragraph 3, will fix in camera-ready]
