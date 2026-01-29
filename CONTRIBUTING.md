# Contributing to Claude Skills Collection

Thank you for your interest in contributing to this collection! This document provides guidelines for adding new skills or improving existing ones.

## How to Contribute

### Adding a New Skill

1. **Plan Your Skill**
   - Read the skill creation guide: [`skills/skill-creator/SKILL.md`](skills/skill-creator/SKILL.md)
   - Ensure your skill provides unique value
   - Define clear use cases and workflows

2. **Create the Skill Directory**
   ```
   skills/your-skill-name/
   ├── SKILL.md          # Required: Main skill definition
   ├── LICENSE.txt       # Required: License information
   ├── references/       # Optional: Additional resources
   └── examples/         # Optional: Usage examples
   ```

3. **Write SKILL.md**
   
   Start with YAML frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: Brief description of what the skill does (one sentence)
   license: Complete terms in LICENSE.txt
   ---
   ```
   
   Then include:
   - Clear title and introduction
   - Workflows and procedures
   - Examples and templates
   - Best practices
   - Troubleshooting tips

4. **Follow Best Practices**
   - **Be Concise**: Context window is limited; only include essential information
   - **Use Examples**: Show, don't just tell
   - **Stay Focused**: One skill should do one thing well
   - **Test Thoroughly**: Ensure your skill works as intended

### Improving Existing Skills

1. Fork the repository
2. Create a feature branch (`git checkout -b improve-skill-name`)
3. Make your improvements
4. Test the changes
5. Submit a pull request with clear description

### Skill Quality Checklist

Before submitting a new skill, verify:

- [ ] SKILL.md has proper YAML frontmatter
- [ ] Description clearly explains when to use this skill
- [ ] Workflows are well-structured and logical
- [ ] Examples are practical and easy to follow
- [ ] LICENSE.txt is included
- [ ] No sensitive information is included
- [ ] Skill is concise and focused
- [ ] Documentation is clear in both English and Chinese (if applicable)

## Style Guidelines

### Formatting

- Use Markdown for all documentation
- Use code blocks with language tags for code examples
- Use tables for comparisons and reference data
- Use headers to organize content hierarchically

### Language

- Use clear, professional language
- Provide bilingual content (English/Chinese) when appropriate
- Use consistent terminology throughout

### Code Examples

```python
# Good: Include comments and context
def create_plot(data, title):
    """Create a publication-quality plot."""
    fig, ax = plt.subplots(figsize=(3.5, 2.5))
    ax.plot(data)
    ax.set_title(title)
    return fig
```

## Submission Process

1. **Fork** the repository
2. **Create** a new branch for your contribution
3. **Add/Modify** skills following the guidelines
4. **Test** your changes
5. **Commit** with clear, descriptive messages
6. **Push** to your fork
7. **Submit** a pull request

### Pull Request Guidelines

- Provide a clear title and description
- Explain what the skill does and why it's useful
- Include examples of usage
- Reference any related issues
- Ensure all files are properly formatted

## Questions or Issues?

- Open an issue for bugs or feature requests
- Start a discussion for general questions
- Check existing issues before creating new ones

## License

By contributing to this repository, you agree that your contributions will be licensed under the same license as the respective skill you're contributing to. Make sure to include appropriate license information with new skills.

Thank you for contributing! 🎉
