# Changelog

All notable changes to the Claude Skills Collection will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Community Infrastructure**
  - GitHub issue templates (bug reports, feature requests, new skill proposals)
  - Pull request template with comprehensive checklist
  - Code of Conduct (Contributor Covenant 2.0)
  - Security policy and guidelines
  - Contributors acknowledgment file

- **Validation & Quality Tools**
  - GitHub Actions workflow for automated validation
  - Python script to validate SKILL.md structure (scripts/validate_skills.py)
  - Makefile for common tasks (validate, lint, format, test, clean)
  - EditorConfig for consistent code style
  - setup.cfg for Python tool configuration (flake8, mypy, pytest)

- **Documentation Enhancements**
  - PROJECT_OVERVIEW.md - Comprehensive project guide
  - SKILL_COMPARISON.md - Skill selection guide with decision tree
  - TROUBLESHOOTING.md - Common issues and solutions
  - examples/ directory with practical use cases
  - scripts/README.md - Script documentation
  - Enhanced README with badges and table of contents
  - CHANGELOG.md for tracking changes

- **Repository Features**
  - Badges in README (license, stars, PRs welcome, CI status)
  - Validation status badge from GitHub Actions
  - Cross-references between all documentation
  - Comprehensive .gitignore improvements

### Changed
- **Bug Fixes**
  - Fixed typo "cluade_skill" → "claude-skill" in all documentation
  - Updated repository URL references throughout
  - Corrected repository name in ORGANIZATION_SUMMARY.md

- **Documentation Improvements**
  - Enhanced README structure with better navigation
  - Improved documentation index with all resources
  - Added table of contents to main documents
  - Bilingual section organization in README

- **Code Quality**
  - Added missing LICENSE.txt to skills/doc-coauthoring/
  - Updated doc-coauthoring SKILL.md with license field
  - All 19 skills now pass validation (100%)

### Fixed
- All internal documentation links verified and working
- Consistent formatting across all documentation files
- Proper frontmatter in all SKILL.md files

## [1.0.0] - 2026-01-29

### Added
- Initial comprehensive documentation
- README with bilingual (English/Chinese) content
- QUICKSTART guide
- SKILLS_CATALOG with detailed skill reference
- CONTRIBUTING guidelines
- LICENSE information
- .gitignore file
- LICENSE.txt files for graphical-abstract, scientific-plotting, and skills/paper
- commands/README.md explanation

### Changed
- Organized repository structure
- Added YAML frontmatter to skill files
- Improved navigation between documentation files

---

For more details, see the [commit history](https://github.com/Hollis36/claude-skill/commits/main).
