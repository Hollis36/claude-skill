# Scripts Documentation

This directory contains utility scripts for maintaining and validating the Claude Skills Collection.

## Available Scripts

### validate_skills.py

**Purpose**: Validate SKILL.md files for proper structure and required fields.

**Usage**:
```bash
python3 scripts/validate_skills.py
```

**What it checks**:
- YAML frontmatter exists and is properly formatted
- Required fields (name, description) are present
- License field is present (warning if missing)
- Content exists after frontmatter

**Exit codes**:
- `0`: All skills valid
- `1`: One or more skills failed validation

**Example output**:
```
🔍 Validating SKILL.md files...

✅ skills/paper/SKILL.md
✅ skills/docx/SKILL.md
❌ skills/example/SKILL.md
   - Missing YAML frontmatter

============================================================
Results: 18/19 files passed validation
============================================================
```

---

## Using the Makefile

The repository includes a Makefile for common tasks:

### Validate Skills
```bash
make validate
```
Runs the skill validation script.

### Lint Python Code
```bash
make lint
```
Runs flake8 on Python scripts (requires `pip install flake8`).

### Format Python Code
```bash
make format
```
Formats Python code with black (requires `pip install black`).

### Run All Checks
```bash
make check
```
Runs validation and linting.

### Clean Temporary Files
```bash
make clean
```
Removes `__pycache__`, `.pyc`, and other temporary files.

### Install Development Dependencies
```bash
make install
```
Installs flake8, black, and pytest for development.

---

## Skill-Specific Scripts

Many skills include their own utility scripts. Here's an overview:

### Document Skills

#### skills/docx/
No scripts currently.

#### skills/pptx/
- `scripts/inventory.py` - Inventory slides in a presentation
- `scripts/replace.py` - Replace text in presentations
- `scripts/rearrange.py` - Rearrange slides
- `scripts/thumbnail.py` - Generate slide thumbnails
- `scripts/html2pptx.js` - Convert HTML to PowerPoint

#### skills/pdf/
- `scripts/check_fillable_fields.py` - Check PDF form fields
- `scripts/fill_fillable_fields.py` - Fill PDF forms
- `scripts/check_bounding_boxes.py` - Check text bounding boxes
- `scripts/create_validation_image.py` - Create validation images

#### skills/xlsx/
No scripts currently.

### Scientific Skills

#### scientific-plotting/
- `scripts/setup_plotting.py` - Setup plotting environment

### Other Skills

Most other skills are primarily documentation-based and don't include scripts.

---

## Creating New Scripts

If you're adding a new script:

1. **Place it appropriately**:
   - Repository-wide utilities: `scripts/`
   - Skill-specific: `skills/{skill-name}/scripts/`

2. **Include proper documentation**:
   - Add docstrings to functions
   - Include usage examples
   - Document dependencies

3. **Follow coding standards**:
   - Use the `.editorconfig` settings
   - Run `make lint` to check style
   - Format with `make format`

4. **Add error handling**:
   - Handle missing files gracefully
   - Provide clear error messages
   - Exit with appropriate codes

5. **Make it executable** (optional):
   ```bash
   chmod +x scripts/your_script.py
   ```

6. **Add shebang** for direct execution:
   ```python
   #!/usr/bin/env python3
   ```

---

## Script Template

Here's a template for new Python scripts:

```python
#!/usr/bin/env python3
"""
Brief description of what this script does.

Usage:
    python3 script_name.py [arguments]

Example:
    python3 script_name.py --input file.txt
"""

import argparse
import sys
from pathlib import Path


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Script description"
    )
    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='Input file path'
    )
    
    args = parser.parse_args()
    
    try:
        # Script logic here
        print(f"Processing {args.input}...")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
```

---

## Testing Scripts

When adding or modifying scripts:

1. **Test with valid inputs**:
   ```bash
   python3 scripts/your_script.py --valid-input
   ```

2. **Test with invalid inputs**:
   ```bash
   python3 scripts/your_script.py --invalid-input
   # Should handle gracefully
   ```

3. **Test edge cases**:
   - Empty files
   - Missing files
   - Large files
   - Special characters

4. **Check exit codes**:
   ```bash
   python3 scripts/your_script.py; echo $?
   # Should be 0 for success, non-zero for failure
   ```

---

## Continuous Integration

Scripts are automatically tested via GitHub Actions:
- Validation runs on every push
- Linting checks code quality
- See `.github/workflows/validate.yml` for details

---

## Dependencies

### Core (included with Python):
- `os`, `sys`, `re`, `pathlib`

### Development:
- `flake8` - Linting
- `black` - Code formatting
- `pytest` - Testing

### Skill-specific:
Check each skill's documentation for specific requirements.

---

## Contributing Scripts

When contributing scripts:

1. Ensure they work on Linux, macOS, and Windows (if possible)
2. Use Python 3.8+ features
3. Include proper error handling
4. Add documentation
5. Test thoroughly
6. Update this README

---

## Questions?

- Check the [Contributing Guide](../CONTRIBUTING.md)
- Open an issue for bugs
- Start a discussion for questions

---

**Last Updated**: 2026-02-17
