# /check — 投稿前自查

跑 `projects/<name>/scripts/check_paper.sh` + 额外的英文风格扫描。投稿 / 提交 rebuttal 前必做。

## 流程

### Step 1：跑结构检查脚本
```bash
bash scripts/check_paper.sh [draft/main.pdf]
```

输出 7 段：
1. 未填占位符（`[CITE:]` / `[TODO:]` / `[NEED EXP:]`）
2. BibTeX 重复 / 未定义 key
3. `\includegraphics` 文件是否存在
4. 图脚本是否都 import 共享 `matplotlib_settings`
5. `data/results.csv` schema 完整性
6. Rebuttal tracker 完成度（仅 rebuttal / revising phase）
7. PDF 页数（vs venue 限制）

任一 FAIL → 阻断提交，agent 列出具体位置 + 修复建议。

### Step 2：英文风格扫描（在 `draft/sections/` 下）

按 `knowledge/methods/writing-style-checks.md` 跑：

```bash
# 弱词
grep -rn -i -E 'delve into|in order to|utilize|leverage' draft/sections/

# 含糊量词
grep -rn -E '\bvery |\bextensive(ly)?\b|\bvarious\b|\bseveral\b' draft/sections/

# 过度被动 / 套话
grep -rn -E '\bIt is .+ that\b|\bhas been\b|\bcan be\b' draft/sections/

# 长句（>40 词）
awk -v thresh=40 '
  /^\s*%/ {next}
  {
    gsub(/[^.!?]+\./, "&\n", $0)
    while ((p=index($0,".")) > 0) {
      s = substr($0,1,p)
      n = split(s, w, " ")
      if (n > thresh) print FILENAME ":" NR ": " n " words"
      $0 = substr($0, p+1)
    }
  }' draft/sections/*.tex
```

每条命中要：
- **报告位置**（file:line）
- **建议替换**（参考 writing-style-checks.md 表格）
- 不强制改 — flag 给 Hollis 决定

### Step 3：数字一致性抽查

每个表格 / 摘要中的关键数字（accuracy、parameter count、speedup），grep 全文：
```bash
grep -rn "87.3" draft/   # 看是否多处出现，是否一致
```

不一致 → FAIL（致命）。

### Step 4：报告

按以下格式：
```
=== /check report ===

STRUCTURE (scripts/check_paper.sh):
  FAIL: N | WARN: M
  [details]

STYLE (draft/sections/):
  Weak words: 5 hits (delve into ×2, utilize ×3)
  Vague quantifiers: 3 hits (various, several)
  Passive voice candidates: 12 hits (need manual review)
  Long sentences (>40w): 2 hits

NUMBER CONSISTENCY:
  ✓ "87.3" appears 4× consistently
  ✗ "76.5" in abstract vs "76.4" in §4.2 — RESOLVE

VERDICT: block / warn / clean
```

### 红线

- **任何 FAIL 都要阻断**，不能"应该没事吧"放行
- **数字不一致是致命**，必须 resolve
- **不自动改**：agent 报告 → Hollis 决定 → 才修

$ARGUMENTS
