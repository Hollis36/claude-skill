# Tools Overview & Installation

Detailed installation and configuration instructions for all tools used in the review paper writing workflow.

## Skill Comparison

| Skill/Tool | Best For | Install Difficulty |
|------------|----------|-------------------|
| Scientific Writer | Full paper writing pipeline | Easy (plugin) |
| Scientific Skills (140+) | Database access + analysis | Medium (clone) |
| Literature Review (FastMCP) | Focused lit review methodology | Easy (skill file) |
| Academic Writing Standards | Style + citation compliance | Easy (skill file) |
| Content Research Writer | General research writing | Easy (skill file) |
| Bio-Research MCP | PubMed/bioRxiv data access | Already installed |

## Prerequisites

- Claude Code CLI installed and configured
- Python 3.10+ (for Scientific Writer CLI)
- `ANTHROPIC_API_KEY` environment variable set

---

## Claude Scientific Writer (Plugin - Recommended)

**Repository**: https://github.com/K-Dense-AI/claude-scientific-writer

AI-driven deep research with publication-ready outputs. Performs comprehensive literature search before writing, ensuring every claim is backed by real, verifiable sources.

**Key Features**:
- Real-time literature search via Perplexity Sonar Pro
- Intelligent paper detection and reference management
- Peer review feedback using ScholarEval (8-dimension scoring)
- Supports Nature, Science, NeurIPS, and other venue templates
- Auto-generates BibTeX citations
- Converts PDF, DOCX, PPTX, XLSX to Markdown
- AI-powered diagram generation (Nano Banana Pro)

**Installation**:

```bash
# Option A: As Claude Code Plugin (Easiest)
/plugin marketplace add https://github.com/K-Dense-AI/claude-scientific-writer
/plugin install claude-scientific-writer
# Restart Claude Code
/scientific-writer:init

# Option B: Via pip
pip install scientific-writer

# Option C: From source
git clone https://github.com/K-Dense-AI/claude-scientific-writer.git
cd claude-scientific-writer
uv sync  # or: pip install -e .
```

**Optional API Keys**:
- `OPENROUTER_API_KEY` - For Perplexity Sonar Pro real-time literature search
- `NANO_BANANA_API_KEY` - For AI-powered diagram generation

**Usage**:

```bash
# CLI
scientific-writer
> Create a comprehensive review paper on CRISPR delivery methods.
> Include data from knockout_efficiency.csv and figure1.png.

# In Claude Code
/scientific-writer:init
# Then: "Write a literature review on deep learning for medical image segmentation"
```

```python
# Python API
import asyncio
from scientific_writer import generate_paper

async def main():
    async for update in generate_paper(
        query="Create a review paper on transformer architectures in NLP",
        data_files=["results.csv", "comparison_table.png"]
    ):
        if update["type"] == "progress":
            print(f"[{update['stage']}] {update['message']}")

asyncio.run(main())
```

---

## Claude Scientific Skills (140+)

**Repository**: https://github.com/K-Dense-AI/claude-scientific-skills

### Scientific Databases (28+)

| Database | Type | Useful For |
|----------|------|------------|
| **OpenAlex** | Academic papers | Comprehensive literature search |
| **PubMed** | Biomedical literature | Medical/bio review papers |
| **bioRxiv** | Preprints | Latest unpublished research |
| **ChEMBL** | Drug/compound data | Pharmaceutical reviews |
| **UniProt** | Protein data | Protein/biochemistry reviews |
| **COSMIC** | Cancer mutations | Oncology reviews |
| **ClinicalTrials.gov** | Clinical trials | Clinical research reviews |
| **Open Targets** | Drug targets | Target identification reviews |
| **Ensembl** | Genomic data | Genomics reviews |
| **InterPro** | Protein families | Structural biology reviews |

### Analysis & Communication Tools (30+)

| Tool Category | Skills Included |
|---------------|----------------|
| Literature Review | Systematic search, synthesis, gap analysis |
| Scientific Writing | Paper drafting, formatting, style |
| Peer Review | Manuscript evaluation |
| Citation Management | BibTeX, reference formatting |
| Document Processing | PDF, DOCX, PPTX conversion |
| Poster Creation | LaTeX posters, conference materials |
| Slide Preparation | Scientific presentations |
| Schematic Design | Figures, diagrams, flowcharts |
| Hypothesis Generation | Research question formulation |
| Grant Writing | Proposal drafting |

### Python Packages (55+)

Data analysis (pandas, numpy, scipy), visualization (matplotlib, seaborn, plotly), bioinformatics (biopython, scanpy, scvi-tools), machine learning (scikit-learn, pytorch), statistics (statsmodels, lifelines).

**Installation**:

```bash
git clone https://github.com/K-Dense-AI/claude-scientific-skills.git
# Copy specific skills to your project
cp claude-scientific-skills/skills/literature-review.md .claude/skills/
cp claude-scientific-skills/skills/scientific-writing.md .claude/skills/
```

---

## Literature Review Skill (FastMCP)

**Source**: https://fastmcp.me/Skills/Details/89/literature-review

Core methodology:
- **Organize thematically** - Group by themes, not individual studies
- **Synthesize across studies** - Compare and contrast findings
- **Be critical** - Evaluate quality and consistency of evidence
- **Identify gaps** - Note what is missing or understudied

**Installation**:

```bash
# Global
cp literature-review.md ~/.claude/skills/
# Project-level
cp literature-review.md .claude/skills/
```

---

## Academic Writing Standards

**Source**: https://claude-plugins.dev/skills/@seabbs/claude-code-config/academic-writing-standards
**Repository**: https://github.com/seabbs/claude-code-config

Features: Citation integrity checking, style guide compliance (APA, MLA, Chicago, IEEE), academic tone enforcement, manuscript editing.

**Installation**:

```bash
git clone https://github.com/seabbs/claude-code-config.git /tmp/seabbs-config
cp /tmp/seabbs-config/academic-writing-standards.md ~/.claude/skills/
```

---

## Content Research Writer

**Source**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer/SKILL.md

Features: Research with verified citations, outline iteration, section-by-section writing with quality checks. Best for introductions, abstracts, structuring complex arguments.

**Installation**:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git /tmp/awesome-skills
cp -r /tmp/awesome-skills/content-research-writer/ ~/.claude/skills/
```

**Other Research Writing Tools**:
- **Article Writer**: https://github.com/wordflowlab/article-writer - Full article generation pipeline
- **Knowledge Extraction**: Converts unstructured documents into structured reports
- **Research Automation**: Automate paper collection, extraction, summarization

---

## Awesome Skill Collections

| Repository | URL |
|------------|-----|
| ComposioHQ/awesome-claude-skills | https://github.com/ComposioHQ/awesome-claude-skills |
| VoltAgent/awesome-agent-skills (200+) | https://github.com/VoltAgent/awesome-agent-skills |
| travisvn/awesome-claude-skills | https://github.com/travisvn/awesome-claude-skills |
| karanb192/awesome-claude-skills (50+) | https://github.com/karanb192/awesome-claude-skills |
| BehiSecc/awesome-claude-skills | https://github.com/BehiSecc/awesome-claude-skills |

## Skill Discovery Platforms

| Platform | URL |
|----------|-----|
| FastMCP Skills | https://fastmcp.me/Skills |
| Claude Plugins Dev | https://claude-plugins.dev |
| MCP Market | https://mcpmarket.com |

## How to Install Skills from Collections

```bash
# 1. Clone the repository
git clone https://github.com/<repo>.git

# 2. Copy skill files
cp path/to/SKILL.md ~/.claude/skills/skill-name.md    # Global
cp path/to/SKILL.md .claude/skills/skill-name.md       # Project-level

# 3. Restart Claude Code to load the new skill
```

## Verification

```bash
/plugin list                # List installed plugins
/scientific-writer:init     # Test scientific writer
/paper                      # Test built-in paper skill
/bio-research:start         # Test bio-research tools
```
