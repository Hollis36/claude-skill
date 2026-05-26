# Skill Comparison Guide

Not sure which skill to use? This guide helps you choose the right skill for your needs.

## Quick Decision Tree

```
What do you want to do?
│
├─ Write academic content
│  ├─ Research paper → skills/paper
│  ├─ Create figures → scientific-plotting
│  └─ TOC graphic → graphical-abstract
│
├─ Create documents
│  ├─ Word document → skills/docx
│  ├─ PowerPoint → skills/pptx
│  ├─ Excel spreadsheet → skills/xlsx
│  └─ PDF → skills/pdf
│
├─ Design & Creative
│  ├─ Generative art → skills/algorithmic-art
│  ├─ Visual designs → skills/canvas-design
│  ├─ Web UI → skills/frontend-design
│  ├─ Color themes → skills/theme-factory
│  └─ Brand guidelines → skills/brand-guidelines
│
├─ Develop software
│  ├─ MCP server → skills/mcp-builder
│  ├─ Web components → skills/web-artifacts-builder
│  └─ Test web apps → skills/webapp-testing
│
└─ Communication
   ├─ Documentation → skills/doc-coauthoring
   ├─ Internal comms → skills/internal-comms
   └─ Slack GIFs → skills/slack-gif-creator
```

---

## Document Creation Skills Comparison

### When to use docx vs pptx vs xlsx vs pdf

| Feature | docx | pptx | xlsx | pdf |
|---------|------|------|------|-----|
| **Best for** | Reports, papers, memos | Presentations, slides | Data, calculations | Forms, fixed layouts |
| **Editing** | ✅ Easy | ✅ Easy | ✅ Easy | ⚠️ Limited |
| **Formatting** | ✅ Rich text | ✅ Layouts | ⚠️ Basic | ✅ Preserved |
| **Data analysis** | ❌ No | ❌ No | ✅ Yes | ❌ No |
| **Collaboration** | ✅ Track changes | ✅ Comments | ✅ Yes | ⚠️ Annotations |
| **File size** | Medium | Large | Small | Medium |

**Choose docx when:**
- Writing reports, proposals, or documentation
- Need rich text formatting
- Want tracked changes and comments
- Collaborative editing needed

**Choose pptx when:**
- Creating presentations
- Need slide layouts and transitions
- Visual storytelling
- Speaker notes needed

**Choose xlsx when:**
- Working with tabular data
- Need formulas and calculations
- Data analysis required
- Charts from data

**Choose pdf when:**
- Need fixed layout
- Filling forms
- Final distribution format
- Print-ready documents

---

## Design Skills Comparison

### frontend-design vs canvas-design vs algorithmic-art

| Feature | frontend-design | canvas-design | algorithmic-art |
|---------|----------------|---------------|-----------------|
| **Output** | Web UI code | Static images | Interactive art |
| **Language** | HTML/CSS/React | Python/Design | p5.js |
| **Interactive** | ✅ Yes | ❌ No | ✅ Yes |
| **Best for** | Apps, websites | Posters, prints | Generative art |
| **Skill level** | Intermediate | Beginner | Intermediate |

**Choose frontend-design when:**
- Building web applications
- Need interactive UI components
- React/Tailwind stack
- Production-ready code needed

**Choose canvas-design when:**
- Creating posters or artwork
- Need static visual designs
- Print materials
- Don't need interactivity

**Choose algorithmic-art when:**
- Creating generative art
- Want parametric designs
- Interactive visualizations
- Code-based art

---

## Academic Skills Comparison

### paper vs graphical-abstract vs scientific-plotting

| Feature | paper | graphical-abstract | scientific-plotting |
|---------|-------|-------------------|-------------------|
| **Focus** | Writing | Visual summary | Data visualization |
| **Output** | LaTeX/Text | Image files | Charts/plots |
| **Use case** | Full paper | TOC figure | Data figures |
| **Complexity** | High | Medium | Medium |

**Workflow**: Use all three together!
1. Write paper with `skills/paper`
2. Create data figures with `scientific-plotting`
3. Design TOC graphic with `graphical-abstract`

---

## Development Skills Comparison

### mcp-builder vs web-artifacts-builder

| Feature | mcp-builder | web-artifacts-builder |
|---------|------------|---------------------|
| **Purpose** | Backend integration | Frontend components |
| **Output** | MCP server | Web artifacts |
| **Language** | Python/TypeScript | React/HTML |
| **Complexity** | High | Medium |

**Choose mcp-builder when:**
- Integrating external APIs
- Building LLM tool servers
- Backend service needed
- Protocol-based communication

**Choose web-artifacts-builder when:**
- Creating interactive web UI
- Building user-facing components
- Single-page applications
- Claude.ai artifacts

---

## Communication Skills Comparison

### doc-coauthoring vs internal-comms

| Feature | doc-coauthoring | internal-comms |
|---------|-----------------|----------------|
| **Focus** | Collaborative writing | Company communications |
| **Formality** | Variable | Professional |
| **Templates** | General | Company-specific |

**Choose doc-coauthoring when:**
- Writing documentation collaboratively
- Technical specs or proposals
- General documentation needs

**Choose internal-comms when:**
- Company announcements
- Team updates
- Internal newsletters
- Following company style

---

## Combining Skills

Many tasks benefit from combining multiple skills. Here are common combinations:

### Research Paper Workflow
```
skills/paper + scientific-plotting + graphical-abstract
```
- Write the paper
- Create data visualizations
- Design TOC figure

### Web Application
```
skills/frontend-design + web-artifacts-builder + webapp-testing
```
- Design the UI
- Build components
- Test functionality

### Business Documentation
```
skills/doc-coauthoring + docx + pptx
```
- Draft content
- Create Word document
- Make presentation

### Brand Development
```
skills/brand-guidelines + theme-factory + frontend-design
```
- Define brand identity
- Create color themes
- Apply to web design

---

## Skill Selection Checklist

Ask yourself:

1. **What's the output format?**
   - Document → docx, pptx, xlsx, pdf
   - Code → mcp-builder, web-artifacts-builder, frontend-design
   - Visual → canvas-design, algorithmic-art, graphical-abstract

2. **What's the purpose?**
   - Academic → paper, scientific-plotting, graphical-abstract
   - Business → doc-coauthoring, internal-comms, docx, pptx
   - Development → mcp-builder, web-artifacts-builder
   - Creative → algorithmic-art, canvas-design, theme-factory

3. **What's your skill level?**
   - Beginner → canvas-design, docx, theme-factory
   - Intermediate → frontend-design, algorithmic-art, scientific-plotting
   - Advanced → mcp-builder, paper

4. **Do you need interactivity?**
   - Yes → frontend-design, web-artifacts-builder, algorithmic-art
   - No → docx, pptx, canvas-design, pdf

5. **Is this for production?**
   - Yes → Add thorough testing, validation
   - No → Can be more exploratory

---

## Still Not Sure?

1. Check the [Skills Catalog](SKILLS_CATALOG.md) for detailed descriptions
2. Look at [examples](examples/) for similar use cases
3. Read skill's "Use when" section
4. Try the skill on a small test case
5. Ask in discussions or issues

---

## Skill Recommendations by Use Case

### Academic Research
- **Primary**: skills/paper
- **Supporting**: scientific-plotting, graphical-abstract

### Web Development
- **Primary**: frontend-design, web-artifacts-builder
- **Supporting**: webapp-testing, theme-factory

### Business Reports
- **Primary**: doc-coauthoring, docx
- **Supporting**: xlsx (for data), pptx (for presentation)

### Data Science
- **Primary**: scientific-plotting, xlsx
- **Supporting**: pdf (for reports)

### Creative Work
- **Primary**: algorithmic-art, canvas-design
- **Supporting**: theme-factory, brand-guidelines

### API Integration
- **Primary**: mcp-builder
- **Supporting**: webapp-testing (for testing)

---

**Need help choosing?** Open a [discussion](https://github.com/Hollis36/claude-skill/discussions) and describe your use case!
