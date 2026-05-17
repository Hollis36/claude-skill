---
name: review-paper-writing
description: Comprehensive guide to writing literature review / survey papers using Claude Code skills, MCP bio-research tools, scientific writing plugins, and 2025-2026 AI research tools (Semantic Scholar, OpenAlex, Elicit, Research Rabbit, Consensus, Scite.ai)
version: "2.0"
license: Apache-2.0
---

# Review Paper Writing

A comprehensive skill for writing literature review and survey papers using Claude Code. Combines MCP bio-research tools for literature search, scientific writing plugins for drafting, AI-powered research tools (2025-2026), and structured workflows for every phase from topic definition to submission.

## Quick Start

```bash
# Step 1: Install the Scientific Writer plugin
/plugin marketplace add https://github.com/K-Dense-AI/claude-scientific-writer
/plugin install claude-scientific-writer
# Restart Claude Code, then:
/scientific-writer:init

# Step 2: Use the built-in paper skill
/paper

# Step 3: Initialize Bio-Research MCP tools (pre-installed)
/bio-research:start
```

> See [references/tools-installation.md](references/tools-installation.md) for detailed tool comparison and installation instructions.
> See [references/mcp-bio-research.md](references/mcp-bio-research.md) for MCP tool API reference.

---

## Review Paper Writing Workflow (7 Phases)

### Phase 1: Topic Definition & Scope

**Goal**: Define research questions and scope.

**Tools**: `/paper`, Scientific Writing skill

**Steps**:
1. Define 2-3 core research questions
2. Identify key terms and synonyms for search
3. Set inclusion/exclusion criteria
4. Choose review type (narrative, systematic, scoping, meta-analysis)

### Phase 2: Literature Search & Collection（增强版）

**Goal**: Systematically find and collect relevant papers using AI-powered tools.

**Tools**: PubMed MCP, bioRxiv MCP, Semantic Scholar, OpenAlex, Elicit, Research Rabbit, Connected Papers, Consensus, Scite.ai

#### 主要文献数据库

| 数据库 | 领域 | 特点 |
|--------|------|------|
| **PubMed / MEDLINE** | 生物医学 | 3300万+文献，MeSH词汇 |
| **Web of Science** | 综合 | 引用分析权威 |
| **Scopus** | 综合 | 欧洲偏重，指标丰富 |
| **Google Scholar** | 综合 | 覆盖最广，含灰色文献 |
| **Semantic Scholar** | 综合 | AI语义搜索，200M+论文 |
| **OpenAlex** | 综合 | 完全开源，250M+文献 |
| **Dimensions** | 综合 | 含专利和临床试验 |
| **IEEE Xplore** | 工程/CS | IEEE/IET出版物 |
| **ACM Digital Library** | CS | ACM出版物 |
| **arXiv** | CS/物理/数学/生物 | 预印本，最新成果 |
| **bioRxiv / medRxiv** | 生物医学 | 生物医学预印本 |
| **ChemRxiv** | 化学 | 化学预印本 |

#### AI 辅助文献工具（2025-2026最新）

```
# Semantic Scholar - 语义搜索 + TLDR摘要
访问: https://api.semanticscholar.org/graph/v1/paper/search
特点: 免费API，自动生成TLDR摘要，引用图谱分析
用法: 输入概念性查询，获取语义相似论文

# OpenAlex - 开源学术元数据
访问: https://api.openalex.org/works?search=<query>
特点: 完全免费，250M+文献，机构/概念分析
用法: 系统性检索，支持引用网络分析

# Elicit - AI结构化数据提取
访问: https://elicit.com
特点: 自动提取研究人群、方法、结果等结构化数据
用法: 输入研究问题，自动分析相关论文并提取关键信息

# Research Rabbit - 引用网络映射
访问: https://researchrabbitapp.com
特点: 从种子论文扩展发现相关工作，可视化引用网络
用法: 导入已知关键论文，探索相关论文空间

# Connected Papers - 图谱化文献发现
访问: https://www.connectedpapers.com
特点: 基于引用相似度的图谱化文献关联
用法: 输入核心论文，发现相关文献簇

# Consensus - 科学共识检查
访问: https://consensus.app
特点: 快速了解特定研究问题的学术共识
用法: 输入具体问题，获取文献支持的答案

# Scite.ai - 引用质量验证
访问: https://scite.ai
特点: 区分"支持"/"反驳"/"提及"三类引用关系
用法: 验证关键声明的文献支持度，发现争议性研究
```

**Steps**:
1. 在主要数据库运行系统性检索（使用标准化检索策略）
2. 用 Semantic Scholar 进行语义检索，捕获传统关键词可能遗漏的相关文献
3. 用 Research Rabbit 从关键种子论文扩展发现相关工作
4. 用 Connected Papers 发现主题相近的文献簇
5. 用 Elicit 自动提取结构化数据（人群、方法、结果）
6. 用 Scite.ai 验证关键引用的可靠性
7. 检查 arXiv/bioRxiv 获取最新预印本成果
8. 导出引用并按主题分类整理

> See [Multi-Database Search Workflow](references/mcp-bio-research.md#multi-database-search-workflow) for detailed steps.

### Phase 3: Literature Organization & Synthesis

**Goal**: Read, categorize, and synthesize findings.

**Tools**: Literature Review skill, Citation Management skill, PDF skill

**Steps**:
1. Organize papers by theme (NOT by individual study)
2. Create a comparison matrix (see [Paper Comparison Matrix](#paper-comparison-matrix) template)
3. Identify consensus, contradictions, and gaps
4. Build citation database (BibTeX format)

**Key Principles**:
- Synthesize across studies, compare and contrast
- Critically evaluate quality and consistency
- Note what is missing or understudied
- Track how the field has evolved over time

### Phase 4: Outline & Structure

**Goal**: Create a detailed outline.

**Tools**: Scientific Writing skill, Academic Writing Standards skill

### Phase 5: Writing

**Goal**: Draft the full paper.

**Tools**: Scientific Writer CLI/Plugin, Content Research Writer

**Tips**:
- Write one section at a time
- Use active voice where possible
- Ensure every claim has a citation
- Maintain consistent terminology throughout

### Phase 6: Review & Refinement

**Goal**: Polish to publication quality.

**Tools**: Peer Review skill, Scholar Evaluation skill (8-dimension scoring), Academic Writing Standards

**Steps**:
1. Run peer review evaluation
2. Check citation completeness and accuracy
3. Verify all figures and tables are referenced
4. Ensure logical flow between sections
5. Check for redundancy and gaps
6. Polish language and formatting

### Phase 7: Formatting & Submission

**Goal**: Format for target venue and prepare submission.

**Tools**: Scientific Writer venue templates, LaTeX Research Posters skill, Scientific Slides skill

**Steps**:
1. Select target journal/conference template
2. Format according to submission guidelines
3. Prepare cover letter
4. Generate supplementary materials if needed
5. Final proofreading

---

## Scientific Writer Skills Reference (16+)

### Writing & Research

| # | Skill | Purpose |
|---|-------|---------|
| 1 | Scientific Writing | IMRaD structure, citation styles, figure/table formatting, reporting standards |
| 2 | Literature Review | Cross-database search, citation organization, thematic synthesis, gap identification |
| 3 | Peer Review | Manuscript evaluation, methodology assessment, journal compliance |
| 4 | Scholar Evaluation | 8-dimension scoring (originality, methodology, clarity, significance, technical soundness, presentation, reproducibility, impact) |
| 5 | Research Grants | NSF/NIH/DOE/DARPA proposals, budget templates |
| 6 | Clinical Reports | CARE-compliant case reports, HIPAA compliance |
| 7 | Clinical Decision Support | GRADE framework, treatment plans, cohort analyses |
| 8 | Market Research Reports | Market sizing, competitive landscapes |

### Presentation & Visual

| # | Skill | Purpose |
|---|-------|---------|
| 9 | LaTeX Research Posters | beamerposter/tikzposter frameworks |
| 10 | Scientific Slides | 5-60 min talks, timing guidance, AI visuals |
| 11 | Scientific Schematics | TikZ publication-quality figures and flowcharts |

### Document Manipulation

| # | Skill | Purpose |
|---|-------|---------|
| 12 | MarkItDown | PDF/DOCX/PPTX/XLSX/images to Markdown |
| 13 | DOCX | Word document processing |
| 14 | PDF | PDF extraction and generation |
| 15 | PPTX | PowerPoint creation and editing |
| 16 | XLSX | Spreadsheet data and analysis |

### Recommended Skill Combination by Phase

```
Phase 1 (Topic & Scope):   Scientific Writing
Phase 2 (Search):          Literature Review + Bio-Research MCP + Semantic Scholar + Elicit
Phase 3 (Organize):        Citation Management + Literature Review
Phase 4 (Outline):         Scientific Writing + Academic Writing Standards
Phase 5 (Write):           Scientific Writing + Literature Review
Phase 6 (Review):          Peer Review + Scholar Evaluation + Scite.ai
Phase 7 (Format):          Scientific Writing (venue templates)
```

---

## Templates & Checklists

### Systematic Review Structure（PRISMA 2020 Updated）

PRISMA 2020 是目前最新的系统综述报告规范，相比2009版有重要更新：
- 新增数据库以外来源（citation searching, grey literature）的报告
- 更新流程图（现包含4个阶段：Identification, Screening, Eligibility, Included）
- 增加偏倚风险评估要求

```
1. Title
   - PRISMA 2020 compliant title (include "systematic review" or "meta-analysis")
2. Abstract (structured: background, objectives, eligibility criteria,
   information sources, risk of bias, synthesis methods, results, limitations,
   conclusions, systematic review registration)
3. Introduction
   - Rationale
   - Objectives
   - Research questions (PICO format)
4. Methods
   - Eligibility criteria (PICO + study design)
   - Information sources (all databases + dates searched)
   - Search strategy (full search strategy for at least one database)
   - Selection process (screening steps, software used)
   - Data extraction process
   - Study risk of bias assessment (tool used, e.g., RoB 2, ROBINS-I)
   - Effect measures
   - Synthesis methods (narrative/quantitative)
   - Reporting bias assessment
   - Certainty of evidence (e.g., GRADE)
5. Results
   - Study selection (PRISMA 2020 flow diagram with 4 phases)
   - Study characteristics
   - Risk of bias in studies
   - Results of individual studies
   - Results of syntheses
   - Reporting biases
   - Certainty of evidence
6. Discussion
   - Summary of evidence
   - Limitations
   - Implications
7. Other information
   - Registration and protocol
   - Support/funding
   - Competing interests
8. References
```

### Meta-Analysis 工作流

```python
# 效应量计算 (使用 Python meta-analysis 库)
# pip install pymare

from pymare import Dataset
import numpy as np

# 基本效应量计算
def cohens_d(mean1, mean2, sd1, sd2, n1, n2):
    """计算Cohen's d效应量
    
    Args:
        mean1: 干预组/实验组均值
        mean2: 对照组均值
        sd1:   干预组标准差
        sd2:   对照组标准差
        n1:    干预组样本量
        n2:    对照组样本量
    
    Returns:
        float: Cohen's d效应量（正值表示干预组更高）
    """
    pooled_sd = np.sqrt(((n1-1)*sd1**2 + (n2-1)*sd2**2) / (n1+n2-2))
    return (mean1 - mean2) / pooled_sd

# 森林图绘制 (使用 forestplot 库)
# pip install forestplot
import forestplot as fp

# 数据格式: DataFrame with columns [estimate, ll, hl, label]
fp.forestplot(
    df,
    estimate='effect_size',
    ll='lower_ci',
    hl='upper_ci',
    varlabel='study',
    xlabel='Effect Size (Cohen\'s d)',
    annote=['n', 'p_value'],
    annoteheaders=['N', 'P-value'],
    rightannote=['weight'],
    right_annoteheaders=['Weight (%)'],
    figsize=(8, 6)
)
```

```r
# R语言Meta-Analysis（推荐工具）
library(meta)
library(metafor)

# 连续型数据meta分析
meta_result <- metacont(
  n.e = n_treatment,    # 干预组样本量
  mean.e = mean_treatment,
  sd.e = sd_treatment,
  n.c = n_control,      # 对照组样本量
  mean.c = mean_control,
  sd.c = sd_control,
  studlab = study_label,
  data = meta_data,
  sm = "SMD",           # 标准化均差
  method.tau = "REML"   # 随机效应模型
)

# 森林图
forest(meta_result, sortvar = TE)

# 漏斗图（偏倚检测）
funnel(meta_result)

# Egger's test（发表偏倚检验）
metabias(meta_result, method.bias = "linreg")

# 异质性分析
print(meta_result$I2)  # I²统计量
print(meta_result$Q)   # Cochran's Q
```

### Narrative Review Structure

```
1. Title
2. Abstract
3. Introduction
   - Background
   - Scope and purpose
4. Body (thematic sections)
   - Theme 1: [Topic]
     - Current state of knowledge
     - Key findings across studies
     - Contradictions and debates
   - Theme 2: [Topic]
   - Theme 3: [Topic]
5. Discussion
   - Synthesis of findings
   - Research gaps identified
   - Methodological challenges
   - Future directions
6. Conclusion
7. References
```

### Literature Search Strategy Template

```markdown
## Search Terms
Primary terms: [term1], [term2], [term3]
Secondary terms: [term4], [term5]
Boolean operators: (term1 OR term2) AND (term3 OR term4)

## Databases to Search
- [ ] PubMed / MEDLINE
- [ ] Web of Science
- [ ] Scopus
- [ ] Google Scholar
- [ ] Semantic Scholar
- [ ] OpenAlex
- [ ] arXiv (preprints: CS/Physics/Math/Biology)
- [ ] bioRxiv / medRxiv (biomedical preprints)
- [ ] IEEE Xplore (engineering/CS)
- [ ] ACM Digital Library (CS)
- [ ] Dimensions
- [ ] Domain-specific databases

## Inclusion Criteria
- Publication date: [start] to [end]
- Language: [languages]
- Study type: [types]
- Population: [if applicable]

## Exclusion Criteria
- [criterion 1]
- [criterion 2]

## Search Record
| Database | Date | Query | Results | After Dedup | Selected |
|----------|------|-------|---------|-------------|----------|
| PubMed   |      |       |         |             |          |
| Semantic Scholar |  |   |         |             |          |
| arXiv    |      |       |         |             |          |
```

### Paper Comparison Matrix

```markdown
| # | Author(s) | Year | Title | Method | Sample/Data | Key Findings | Limitations | Quality |
|---|-----------|------|-------|--------|-------------|--------------|-------------|---------|
| 1 |           |      |       |        |             |              |             | H/M/L   |
| 2 |           |      |       |        |             |              |             | H/M/L   |
```

Quality: H = High, M = Medium, L = Low

### Academic Writing Checklist

**Structure**:
- [ ] Clear thesis / research questions stated
- [ ] Logical flow between sections
- [ ] Each paragraph has a topic sentence
- [ ] Transitions connect ideas smoothly
- [ ] Conclusion summarizes and extends (not just repeats)

**Language**:
- [ ] Formal academic tone throughout
- [ ] No contractions (don't -> do not)
- [ ] No colloquialisms or slang
- [ ] Precise vocabulary (avoid vague terms)
- [ ] Active voice preferred where appropriate
- [ ] Consistent tense usage

**Citations**:
- [ ] Every claim backed by a citation
- [ ] No "orphan" citations (cited but not discussed)
- [ ] Citation format consistent throughout
- [ ] All references in bibliography are cited in text
- [ ] All in-text citations appear in bibliography
- [ ] DOIs included where available
- [ ] Key citations verified via Scite.ai

**Figures & Tables**:
- [ ] Every figure/table referenced in text
- [ ] Captions are self-explanatory
- [ ] High resolution (300+ DPI)
- [ ] Consistent styling across all figures
- [ ] Data clearly labeled with units

**Common Mistakes to Avoid**:
- Plagiarism (even unintentional)
- Over-reliance on a single source
- Citation clusters without synthesis
- Listing studies without comparing them
- Missing recent publications (last 2-3 years)
- Ignoring contradictory evidence

## AI 辅助综述伦理指南

> **AI辅助文献综述的使用规范（2025-2026）**

### 允许的AI辅助用途
- 文献检索辅助（Semantic Scholar, Elicit等）
- 论文摘要理解（SciSpace等）
- 写作润色和语法纠错
- 格式规范化

### 必须由人工完成的工作
- 文献纳入/排除决策（必须基于研究者判断）
- 数据提取的准确性验证（AI提取数据必须人工核实）
- 结果解读和分析综合
- 结论的形成

### 透明披露要求
- 说明使用了哪些AI辅助工具
- 描述AI在文献筛选/数据提取中的具体角色
- 按目标期刊政策进行适当披露（参考COPE指南）

### 引用验证
- 禁止将AI生成的虚假引用纳入综述
- 使用Scite.ai验证关键引用的支持关系
- 对争议性声明进行原文核查

### Citation Style Quick Reference

**APA 7th Edition**:
```
In-text: (Author, Year) or Author (Year)
Reference: Author, A. A. (Year). Title. Journal, Volume(Issue), Pages. https://doi.org/xxx
```

**IEEE**:
```
In-text: [1], [2], [3]
Reference: [1] A. Author, "Title," Journal, vol. X, no. Y, pp. Z-Z, Month Year.
```

**Nature**:
```
In-text: Superscript numbers: text^1
Reference: 1. Author, A. A. Title. Journal Vol, Pages (Year).
```

**Chicago (Author-Date)**:
```
In-text: (Author Year, Page)
Reference: Author, First. Year. "Title." Journal Volume (Issue): Pages.
```
