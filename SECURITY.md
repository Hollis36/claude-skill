# Security Policy

## Reporting Security Issues

The Claude Skills Collection team takes security seriously. If you discover a security vulnerability, please report it responsibly.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by:
1. Opening a security advisory on GitHub
2. Or sending an email with details to the repository maintainers

Please include:
- Type of vulnerability
- Affected skill(s) or component(s)
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| Older   | :x:                |

## Security Update Process

When a security vulnerability is reported:

1. **Acknowledgment**: We'll acknowledge receipt within 48 hours
2. **Assessment**: We'll assess the vulnerability and its impact
3. **Fix**: We'll work on a fix and test it thoroughly
4. **Disclosure**: We'll coordinate disclosure with the reporter
5. **Release**: We'll release a patch and update documentation

## Best Practices for Users

When using Claude Skills:

1. **Review Skills**: Always review skill content before using it
2. **Sensitive Data**: Never include sensitive data (API keys, passwords, personal information) in skills
3. **Code Execution**: Be cautious when skills involve code execution
4. **External Resources**: Verify external resources referenced by skills
5. **Updates**: Keep track of skill updates and security advisories

## Security Considerations for Skill Creators

If you're creating or contributing skills:

1. **No Secrets**: Never include API keys, tokens, or sensitive data
2. **Input Validation**: Validate and sanitize all inputs
3. **Safe Commands**: Avoid commands that could be harmful
4. **Dependencies**: Keep dependencies updated and secure
5. **Documentation**: Document security considerations in your skill

## Security Features

This repository includes:

- `.gitignore` to prevent accidental commit of sensitive files
- License information for each skill
- Clear documentation and examples
- Code review process for contributions

## Known Security Considerations

Skills in this repository:
- Are templates and prompts, not executable code by default
- May reference external tools or libraries (verify before use)
- Should be reviewed before use in production environments
- May require secure handling of user data

## Contact

For security concerns, please use GitHub's security advisory feature or contact the repository maintainers through GitHub.

## Updates

This security policy may be updated periodically. Check back for the latest version.

---

Last Updated: 2026-02-17
