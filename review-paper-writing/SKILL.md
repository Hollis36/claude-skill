---
name: review-paper-writing
description: Comprehensive guide to writing literature review / survey papers using Claude Code skills, MCP bio-research tools, and scientific writing plugins
version: "1.0"
license: Apache-2.0
---

# Review Paper Writing

A comprehensive skill for writing literature review and survey papers using Claude Code. Combines MCP bio-research tools for literature search, scientific writing plugins for drafting, and structured workflows for every phase from topic definition to submission.

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

### Phase 2: Literature Search & Collection

**Goal**: Systematically find and collect relevant papers.

**Tools**: PubMed MCP, bioRxiv MCP, Open Targets MCP, ClinicalTrials MCP, Scientific Writer `research-lookup`

**Steps**:
1. Run systematic searches across multiple databases
2. Use `find_related_articles` to expand from key papers
3. Check preprints on bioRxiv for latest unpublished work
4. Use `search_published_preprints` to verify peer-review status
5. Export citations and organize by theme

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
Phase 2 (Search):          Literature Review + Bio-Research MCP
Phase 3 (Organize):        Citation Management + Literature Review
Phase 4 (Outline):         Scientific Writing + Academic Writing Standards
Phase 5 (Write):           Scientific Writing + Literature Review
Phase 6 (Review):          Peer Review + Scholar Evaluation
Phase 7 (Format):          Scientific Writing (venue templates)
```

---

## Templates & Checklists

### Systematic Review Structure (PRISMA-compliant)

```
1. Title
2. Abstract (structured: background, objectives, methods, results, conclusions)
3. Introduction
   - Rationale
   - Objectives
   - Research questions
4. Methods
   - Eligibility criteria
   - Information sources
   - Search strategy
   - Selection process
   - Data extraction
   - Quality assessment
5. Results
   - Study selection (PRISMA flow diagram)
   - Study characteristics
   - Synthesis of results
6. Discussion
   - Summary of evidence
   - Limitations
   - Implications
7. Conclusion
8. References
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
- [ ] bioRxiv / medRxiv (preprints)
- [ ] OpenAlex
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
| Database | Date | Query | Results | Selected |
|----------|------|-------|---------|----------|
| PubMed   |      |       |         |          |
| bioRxiv  |      |       |         |          |
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
