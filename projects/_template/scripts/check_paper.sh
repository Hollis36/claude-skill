#!/usr/bin/env bash
# Pre-submission self-check.
# Run from project root: bash scripts/check_paper.sh [draft/main.pdf]
#
# Checks (each prints OK / WARN / FAIL with details):
#   1. Unfilled placeholders: [CITE: ...] [TODO: ...] [NEED EXP: ...]
#   2. BibTeX hygiene: duplicate keys, missing keys cited in tex
#   3. Figure files exist for every \includegraphics
#   4. matplotlib_settings used in every figure_*.py
#   5. results.csv schema intact (header + non-empty)
#   6. rebuttal-tracker not abandoned (no all-TODO rows if rebuttal/revising)
#   7. Optional: PDF page count if pdfinfo available
#
# Exit 0 if no FAIL; non-zero if any FAIL.
set -uo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

PDF="${1:-draft/main.pdf}"
FAILS=0
WARNS=0

red()    { printf '\033[31m%s\033[0m' "$1"; }
yellow() { printf '\033[33m%s\033[0m' "$1"; }
green()  { printf '\033[32m%s\033[0m' "$1"; }

ok()   { echo "  $(green OK)   $1"; }
warn() { echo "  $(yellow WARN) $1"; WARNS=$((WARNS+1)); }
fail() { echo "  $(red FAIL) $1"; FAILS=$((FAILS+1)); }

echo "=== Paper self-check: $PROJECT_ROOT ==="

# --- 1. Placeholders ---
echo
echo "[1/7] Unfilled placeholders in draft/"
if [ -d draft ]; then
  hits=$(grep -rn -E '\[(CITE|TODO|NEED EXP|FIXME):' draft/ 2>/dev/null || true)
  if [ -z "$hits" ]; then
    ok "no [CITE:] / [TODO:] / [NEED EXP:] markers"
  else
    n=$(echo "$hits" | wc -l)
    fail "$n unfilled placeholder(s):"
    echo "$hits" | head -10 | sed 's/^/      /'
    [ "$n" -gt 10 ] && echo "      ... ($((n-10)) more)"
  fi
else
  warn "draft/ directory missing"
fi

# --- 2. BibTeX hygiene ---
echo
echo "[2/7] BibTeX hygiene"
if [ -f refs/main.bib ]; then
  dup=$(grep -E '^@[A-Za-z]+\{' refs/main.bib | sed -E 's/^@[A-Za-z]+\{([^,]+),.*/\1/' \
        | sort | uniq -d || true)
  if [ -z "$dup" ]; then
    ok "no duplicate BibTeX keys"
  else
    fail "duplicate keys: $(echo "$dup" | tr '\n' ' ')"
  fi

  if [ -d draft ]; then
    cited=$(grep -rohE '\\cite[a-z]*\{[^}]+\}' draft/ 2>/dev/null \
            | sed -E 's/\\cite[a-z]*\{([^}]+)\}/\1/' | tr ',' '\n' \
            | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sort -u)
    defined=$(grep -E '^@[A-Za-z]+\{' refs/main.bib \
              | sed -E 's/^@[A-Za-z]+\{([^,]+),.*/\1/' | sort -u)
    missing=$(comm -23 <(echo "$cited") <(echo "$defined"))
    if [ -z "$missing" ]; then
      ok "all \\cite{} keys exist in refs/main.bib"
    else
      n=$(echo "$missing" | wc -l)
      fail "$n key(s) cited but not in main.bib:"
      echo "$missing" | head -5 | sed 's/^/      /'
    fi
  fi
else
  warn "refs/main.bib not found"
fi

# --- 3. Figure existence ---
echo
echo "[3/7] \\includegraphics references"
if [ -d draft ]; then
  refs=$(grep -rhoE '\\includegraphics(\[[^]]*\])?\{[^}]+\}' draft/ 2>/dev/null \
         | sed -E 's/.*\{([^}]+)\}/\1/' | sort -u)
  missing_figs=""
  for ref in $refs; do
    # Try common extensions / relative paths
    found=0
    for cand in "$ref" "$ref.pdf" "$ref.png" "../figures/$ref" \
                "figures/$(basename "$ref").pdf" "figures/$(basename "$ref").png"; do
      [ -f "$cand" ] && { found=1; break; }
    done
    [ "$found" -eq 0 ] && missing_figs="$missing_figs $ref"
  done
  if [ -z "${refs:-}" ]; then
    warn "no \\includegraphics found (check if figures referenced)"
  elif [ -z "$missing_figs" ]; then
    ok "all $(echo "$refs" | wc -l) figure reference(s) resolved"
  else
    fail "missing figure files:$missing_figs"
  fi
fi

# --- 4. Figure style consistency ---
echo
echo "[4/7] matplotlib_settings used in figures/"
if [ -d figures ]; then
  scripts=$(find figures -maxdepth 1 -name 'figure_*.py' 2>/dev/null)
  if [ -z "$scripts" ]; then
    warn "no figure_*.py scripts found"
  else
    skipped=""
    for s in $scripts; do
      grep -q 'matplotlib_settings' "$s" || skipped="$skipped $(basename "$s")"
    done
    if [ -z "$skipped" ]; then
      ok "all $(echo "$scripts" | wc -w) figure script(s) import matplotlib_settings"
    else
      warn "scripts without matplotlib_settings:$skipped"
    fi
  fi
fi

# --- 5. results.csv schema ---
echo
echo "[5/7] data/results.csv schema"
if [ -f data/results.csv ]; then
  expected="run_id,seed,dataset,method,metric_name,metric_value,std,n_samples,notes"
  header=$(head -1 data/results.csv)
  rows=$(($(wc -l < data/results.csv) - 1))
  if [ "$header" = "$expected" ] && [ "$rows" -gt 0 ]; then
    ok "schema match, $rows data row(s)"
  elif [ "$header" != "$expected" ]; then
    fail "header mismatch — expected: $expected"
    echo "      found: $header"
  else
    warn "results.csv has header but no data"
  fi
else
  warn "data/results.csv not found"
fi

# --- 6. Rebuttal tracker freshness ---
echo
echo "[6/7] rebuttal-tracker (if in rebuttal/revising)"
phase=$(grep -E '^phase:' README.md 2>/dev/null | head -1 | awk '{print $2}' || true)
if [[ "$phase" == "rebuttal" || "$phase" == "revising" ]]; then
  tracker="response/rebuttal-tracker.md"
  if [ -f "$tracker" ]; then
    todo_count=$(grep -c "TODO" "$tracker" || true)
    done_count=$(grep -c "DONE" "$tracker" || true)
    if [ "$todo_count" -gt 0 ] && [ "$done_count" -eq 0 ]; then
      warn "rebuttal-tracker has $todo_count TODO and no DONE — work not started?"
    elif [ "$todo_count" -gt 0 ]; then
      warn "$todo_count question(s) still TODO in rebuttal-tracker"
    else
      ok "rebuttal-tracker shows no remaining TODO"
    fi
  else
    fail "phase=$phase but $tracker missing"
  fi
else
  ok "phase=${phase:-unset}, skipping rebuttal-tracker check"
fi

# --- 7. PDF page count (optional) ---
echo
echo "[7/7] PDF page count"
if [ -f "$PDF" ]; then
  if command -v pdfinfo >/dev/null 2>&1; then
    pages=$(pdfinfo "$PDF" 2>/dev/null | awk '/^Pages:/ {print $2}')
    venue=$(grep -E '^target_venue:' README.md 2>/dev/null | head -1 | awk '{print $2}' || echo unknown)
    echo "  $PDF: $pages pages (target_venue: $venue)"
    case "$venue" in
      NeurIPS|ICML) limit=9 ;;
      ICLR) limit=10 ;;
      CVPR|ACL|EMNLP|NAACL) limit=8 ;;
      *) limit="" ;;
    esac
    if [ -n "$limit" ]; then
      if [ "$pages" -le "$limit" ]; then
        ok "within ${limit}-page main-text limit (refs/appendix may extend)"
      else
        warn "exceeds ${limit}-page main-text limit — check what counts toward limit"
      fi
    else
      ok "venue page limit not registered for $venue"
    fi
  else
    warn "pdfinfo not installed (apt install poppler-utils); skipping page count"
  fi
else
  warn "$PDF not found (build with latexmk first)"
fi

# --- Summary ---
echo
echo "=== Summary ==="
echo "FAIL: $FAILS    WARN: $WARNS"
if [ "$FAILS" -gt 0 ]; then
  echo
  echo "❌ Block submission until FAILs are resolved."
  exit 1
elif [ "$WARNS" -gt 0 ]; then
  echo
  echo "⚠️  Review WARNs; can still submit if intentional."
  exit 0
else
  echo
  echo "✅ Clean — ready to submit."
fi
