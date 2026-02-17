# Troubleshooting Guide

Common issues and solutions when using Claude Skills.

## Table of Contents

- [General Issues](#general-issues)
- [Skill-Specific Issues](#skill-specific-issues)
- [Best Practices](#best-practices)
- [Getting Help](#getting-help)

---

## General Issues

### Issue: Skill output is too verbose

**Symptoms**: Claude provides too much explanation or detail.

**Solutions**:
1. Add "be concise" to your prompt
2. Ask Claude to "summarize the key points"
3. Request specific sections only: "Just give me the code, skip the explanation"

**Example**:
```
[Paste SKILL.md content]

Please be concise and focus on the code implementation only.
```

---

### Issue: Skill output doesn't match my requirements

**Symptoms**: Output doesn't fit your specific needs or context.

**Solutions**:
1. Provide more specific requirements upfront
2. Include examples of what you want
3. Specify format, style, or constraints explicitly
4. Break down complex requests into smaller steps

**Example**:
```
[Paste SKILL.md content]

Specific requirements:
- Output format: IEEE double-column
- Figure width: 3.5 inches
- Color scheme: colorblind-friendly
- Font size: 10pt minimum
```

---

### Issue: Skills not producing expected results

**Symptoms**: Output quality is lower than expected.

**Solutions**:
1. Check if you're using the right skill for your task
2. Provide complete context and data
3. Reference specific sections of the skill
4. Try rephrasing your request
5. Use multiple iterations to refine

**Example**:
```
Let's iterate on this. Start with the basic structure,
then we'll refine the details.
```

---

### Issue: Can't find the right skill

**Symptoms**: Not sure which skill to use for your task.

**Solutions**:
1. Check the [Skills Catalog](SKILLS_CATALOG.md) for descriptions
2. Look at the "Use when" section for each skill
3. Check [examples](examples/) for similar use cases
4. Consider combining multiple skills

**Quick Reference**:
- Academic writing → `skills/paper`
- Data visualization → `scientific-plotting`
- Web development → `skills/frontend-design` or `web-artifacts-builder`
- Document creation → `skills/docx`, `pptx`, or `pdf`
- Development tools → `skills/mcp-builder`

---

### Issue: Skill files are too large

**Symptoms**: SKILL.md file is too large to paste in context.

**Solutions**:
1. Use only relevant sections of the skill
2. Ask Claude to summarize the skill first
3. Break complex tasks into multiple conversations
4. Create a custom simplified version for your needs

**Example**:
```
Here's a summary of the skill: [brief description]

Now let's apply it to: [your specific task]
```

---

## Skill-Specific Issues

### Academic Skills (paper, graphical-abstract, scientific-plotting)

#### Issue: Citations not formatted correctly

**Solution**: Specify your citation style explicitly:
```
Use APA 7th edition citation style
```

#### Issue: Figures don't meet journal requirements

**Solution**: Provide journal-specific requirements:
```
Journal requirements:
- Format: EPS or PDF
- Resolution: 300 DPI minimum
- Size: 88mm (single column) or 180mm (double column)
- Fonts: Arial, 7pt minimum
```

#### Issue: Paper structure doesn't match target venue

**Solution**: Provide template or example:
```
Follow the ACL conference template structure:
- Abstract (200 words max)
- Introduction (1 page)
- Related Work
- ...
```

---

### Document Skills (docx, pptx, xlsx, pdf)

#### Issue: Generated code produces errors

**Solution**: 
1. Check if required libraries are installed
2. Verify file paths are correct
3. Provide sample data in correct format
4. Ask for error handling code

**Example**:
```
Include error handling and validation.
Check if files exist before opening.
```

#### Issue: Formatting not preserved

**Solution**: Be explicit about formatting requirements:
```
Preserve:
- Heading styles (Heading 1, 2, 3)
- Bold and italic text
- Bullet points and numbering
- Tables with borders
```

---

### Development Skills (mcp-builder, web-artifacts-builder)

#### Issue: Code doesn't run or has bugs

**Solutions**:
1. Ask for complete, runnable code
2. Request error handling
3. Ask for dependencies list
4. Request testing instructions

**Example**:
```
Provide:
1. Complete code with all imports
2. Dependencies (requirements.txt or package.json)
3. Setup instructions
4. Testing commands
```

#### Issue: MCP server not connecting

**Solutions**:
1. Check server is running
2. Verify port configuration
3. Check firewall settings
4. Review MCP configuration

---

### Design Skills (frontend-design, theme-factory, brand-guidelines)

#### Issue: Design looks generic or uninspired

**Solutions**:
1. Provide specific design references
2. Describe desired style in detail
3. Specify color palette
4. Give examples of designs you like

**Example**:
```
Design style:
- Modern, minimalist
- Color palette: #2D3748, #4299E1, #F7FAFC
- Typography: Inter for headings, system fonts for body
- Inspiration: Linear.app, Stripe.com
```

#### Issue: Components not responsive

**Solution**: Explicitly request responsive design:
```
Make it fully responsive:
- Mobile: 320px-768px
- Tablet: 768px-1024px
- Desktop: 1024px+
```

---

## Best Practices

### 1. Start Simple, Then Iterate
- Begin with basic requirements
- Review the initial output
- Refine with specific feedback
- Iterate until satisfied

### 2. Provide Complete Context
Always include:
- What you're trying to achieve
- Your constraints or requirements
- Target audience or use case
- Any relevant data or examples

### 3. Be Specific About Format
Specify:
- File formats
- Dimensions or sizes
- Color schemes
- Font requirements
- Output structure

### 4. Test and Validate
- Test generated code before using in production
- Validate outputs meet your requirements
- Check for edge cases
- Review for security issues

### 5. Use Examples
- Provide examples of desired output
- Reference similar work
- Show what you don't want
- Include edge cases

---

## Common Patterns

### Pattern: Iterative Refinement
```
1st iteration: Get basic structure
2nd iteration: Refine specific sections
3rd iteration: Polish and finalize
```

### Pattern: Modular Approach
```
Break large tasks into smaller pieces:
1. Structure/outline
2. Individual sections
3. Integration
4. Final polish
```

### Pattern: Template Customization
```
1. Use skill to generate template
2. Review and identify needed changes
3. Request specific modifications
4. Finalize and test
```

---

## Getting Help

### Before Asking for Help

1. Check this troubleshooting guide
2. Review the [Quick Start Guide](QUICKSTART.md)
3. Check skill-specific documentation
4. Look at [examples](examples/) for similar use cases

### How to Report Issues

When reporting issues, include:
1. **Which skill** you're using
2. **What you expected** to happen
3. **What actually happened**
4. **Your prompt** (if appropriate to share)
5. **Error messages** or unexpected output
6. **Environment details** (if relevant)

### Where to Get Help

- **Bug Reports**: [Create an issue](https://github.com/Hollis36/claude-skill/issues/new?template=bug_report.md)
- **Feature Requests**: [Request a feature](https://github.com/Hollis36/claude-skill/issues/new?template=feature_request.md)
- **New Skill Ideas**: [Propose a skill](https://github.com/Hollis36/claude-skill/issues/new?template=new_skill.md)
- **General Questions**: Open a discussion on GitHub

---

## Tips from the Community

### Tip: Save Successful Prompts
Keep a note of prompts that work well for future reference.

### Tip: Combine Skills Creatively
Don't limit yourself to one skill - combine them for complex workflows.

### Tip: Customize Skills
Feel free to modify skills for your specific needs.

### Tip: Share Your Experience
Help others by sharing what worked for you!

---

## Still Having Issues?

If you can't find a solution here:
1. Check if there's a similar issue already reported
2. Create a new issue with detailed information
3. Be patient - maintainers will respond as soon as possible

---

**Last Updated**: 2026-02-17

**Contributions Welcome**: If you've solved an issue not listed here, please contribute by opening a PR!
