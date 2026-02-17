#!/usr/bin/env python3
"""
Validate SKILL.md files to ensure they follow the correct structure.

This script checks:
1. YAML frontmatter exists and is valid
2. Required frontmatter fields are present
3. File structure is consistent
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple


def validate_skill_file(file_path: Path) -> Tuple[bool, List[str]]:
    """
    Validate a single SKILL.md file.
    
    Returns:
        Tuple of (is_valid, error_messages)
    """
    errors = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, [f"Failed to read file: {e}"]
    
    # Check for YAML frontmatter
    frontmatter_pattern = r'^---\n(.*?)\n---'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if not match:
        errors.append("Missing YAML frontmatter (should start with --- and end with ---)")
        return False, errors
    
    frontmatter = match.group(1)
    
    # Check for required fields
    required_fields = ['name', 'description']
    for field in required_fields:
        if not re.search(rf'^{field}:\s*.+', frontmatter, re.MULTILINE):
            errors.append(f"Missing required frontmatter field: {field}")
    
    # Check for license field (recommended but not required)
    if not re.search(r'^license:\s*.+', frontmatter, re.MULTILINE):
        errors.append("Warning: Missing recommended frontmatter field: license")
    
    # Check if file has content after frontmatter
    content_after_frontmatter = content[match.end():].strip()
    if not content_after_frontmatter:
        errors.append("No content found after frontmatter")
    
    return len(errors) == 0, errors


def find_skill_files(base_path: Path) -> List[Path]:
    """Find all SKILL.md files in the repository."""
    skill_files = []
    
    # Check skills/ directory
    skills_dir = base_path / 'skills'
    if skills_dir.exists():
        skill_files.extend(skills_dir.glob('*/SKILL.md'))
    
    # Check root-level skill directories
    for skill_dir in ['graphical-abstract', 'scientific-plotting']:
        skill_file = base_path / skill_dir / 'SKILL.md'
        if skill_file.exists():
            skill_files.append(skill_file)
    
    return skill_files


def main():
    """Main validation function."""
    base_path = Path(__file__).parent.parent
    
    print("🔍 Validating SKILL.md files...\n")
    
    skill_files = find_skill_files(base_path)
    
    if not skill_files:
        print("⚠️  No SKILL.md files found!")
        return 1
    
    all_valid = True
    total_files = len(skill_files)
    valid_files = 0
    
    for skill_file in skill_files:
        relative_path = skill_file.relative_to(base_path)
        is_valid, errors = validate_skill_file(skill_file)
        
        if is_valid:
            print(f"✅ {relative_path}")
            valid_files += 1
        else:
            print(f"❌ {relative_path}")
            for error in errors:
                print(f"   - {error}")
            all_valid = False
        print()
    
    print(f"\n{'='*60}")
    print(f"Results: {valid_files}/{total_files} files passed validation")
    print(f"{'='*60}\n")
    
    return 0 if all_valid else 1


if __name__ == '__main__':
    sys.exit(main())
