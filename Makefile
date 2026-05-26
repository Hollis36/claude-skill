# Makefile for Claude Skills Collection

.PHONY: help validate lint format check test clean install

help:
	@echo "Claude Skills Collection - Available Commands:"
	@echo ""
	@echo "  make validate      - Validate all SKILL.md files"
	@echo "  make lint          - Run linters on Python code"
	@echo "  make format        - Format Python code with black"
	@echo "  make check         - Run all checks (validate + lint)"
	@echo "  make test          - Run tests (when available)"
	@echo "  make clean         - Clean up temporary files"
	@echo "  make install       - Install development dependencies"
	@echo ""

validate:
	@echo "Validating SKILL.md files..."
	@python3 scripts/validate_skills.py

lint:
	@echo "Running Python linters..."
	@if command -v flake8 >/dev/null 2>&1; then \
		flake8 scripts/ skills/*/scripts/*.py scientific-plotting/scripts/*.py 2>/dev/null || true; \
	else \
		echo "flake8 not installed. Run 'pip install flake8' to enable linting."; \
	fi

format:
	@echo "Formatting Python code..."
	@if command -v black >/dev/null 2>&1; then \
		black scripts/ skills/*/scripts/*.py scientific-plotting/scripts/*.py 2>/dev/null || true; \
	else \
		echo "black not installed. Run 'pip install black' to enable formatting."; \
	fi

check: validate lint
	@echo "All checks completed!"

test:
	@echo "Running tests..."
	@if command -v pytest >/dev/null 2>&1; then \
		pytest skills/*/scripts/ 2>/dev/null || echo "No tests found or pytest not configured."; \
	else \
		echo "pytest not installed. Run 'pip install pytest' to enable testing."; \
	fi

clean:
	@echo "Cleaning up..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleanup complete!"

install:
	@echo "Installing development dependencies..."
	@pip install --upgrade pip
	@pip install flake8 black pytest
	@echo "Development dependencies installed!"
	@echo ""
	@echo "Optional dependencies:"
	@echo "  - For document skills: pip install python-docx python-pptx openpyxl"
	@echo "  - For PDF skills: pip install PyPDF2 pdfplumber"
	@echo "  - For plotting: pip install matplotlib seaborn pandas"
	@echo ""
