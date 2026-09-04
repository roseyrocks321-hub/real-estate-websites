#!/usr/bin/env python3
"""
GTR Heading Structure Audit & Fix Script
Audits HTML files for heading sequence violations, missing H2s, and duplicate H2s.
Usage: python3 fix-headings.py <directory_or_file>
"""
import os, re, sys, glob
from collections import Counter

def analyze_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all headings with their positions
    headings = []
    for m in re.finditer(r'<(h[1-6])[^>]*>(.*?)</\1>', content, re.I | re.S):
        tag = m.group(1).lower()
        text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        headings.append((m.start(), tag, text))

    headings.sort(key=lambda x: x[0])
    issues = []

    if not headings:
        return {"file": path, "issues": ["No headings found"], "headings": []}

    # Check for H1
    h1s = [h for h in headings if h[1] == 'h1']
    if len(h1s) == 0:
        issues.append("Missing H1")
    elif len(h1s) > 1:
        issues.append(f"Multiple H1s ({len(h1s)})")

    # Check for missing H2
    h2s = [h for h in headings if h[1] == 'h2']
    if len(h2s) == 0 and len(h1s) > 0:
        issues.append("Missing H2 (has H1 but no H2)")

    # Check sequence violations
    seen = set()
    for pos, tag, text in headings:
        level = int(tag[1])
        if level == 1:
            seen.add(1)
        elif level == 2:
            if 1 not in seen:
                issues.append(f"H2 before H1: '{text[:50]}'")
            seen.add(2)
        elif level == 3:
            if 2 not in seen:
                issues.append(f"H3 before H2: '{text[:50]}'")
            seen.add(3)
        elif level == 4:
            if 3 not in seen:
                issues.append(f"H4 before H3: '{text[:50]}'")

    return {
        "file": path,
        "issues": issues,
        "headings": [(tag, text[:70]) for pos, tag, text in headings]
    }

def main(target):
    results = []
    all_h2_texts = []

    if os.path.isfile(target):
        files = [target]
    else:
        files = glob.glob(os.path.join(target, '**/*.html'), recursive=True)

    for f in files:
        result = analyze_file(f)
        results.append(result)
        all_h2_texts.extend([h[1] for h in result["headings"] if h[0] == 'h2'])

    # Print per-file issues
    print("=== GTR Heading Audit Results ===\n")
    has_issues = False
    for r in results:
        if r["issues"]:
            has_issues = True
            print(f"FILE: {r['file']}")
            for issue in r["issues"]:
                print(f"  [ISSUE] {issue}")
            for tag, text in r["headings"]:
                print(f"    <{tag}> {text}")
            print()

    if not has_issues:
        print("No heading issues found!\n")

    # Check for duplicate H2s across files
    print("=== Duplicate H2 Analysis ===")
    counts = Counter(all_h2_texts)
    duplicates = {text: count for text, count in counts.items() if count > 1}
    if duplicates:
        for text, count in sorted(duplicates.items(), key=lambda x: -x[1]):
            print(f"  DUPLICATE ({count}x): '{text}'")
            # Show which files
            for r in results:
                file_h2s = [h[1] for h in r["headings"] if h[0] == 'h2']
                if text in file_h2s:
                    print(f"    -> {r['file']}")
    else:
        print("  No duplicate H2s found across files.")

    print("\n=== Recommendations ===")
    print("1. Ensure every page has exactly one H1")
    print("2. Ensure every page with H1 also has at least one H2")
    print("3. Fix sequence violations (h3 before h2, etc.)")
    print("4. Make duplicate H2s unique per page")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    main(target)
