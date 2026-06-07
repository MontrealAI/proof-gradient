# QA verification

This package was verified locally before delivery.

Commands run:

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/qa_check.py
python -m skillos.cli wealth-proof
node --check site/app.js
```

Expected result:

```text
✅ Repository file verification passed
Ran 6 tests ... OK
✅ Agent SkillOS verification passed
✅ Verified GitHub Pages output at dist
✅ Repository QA passed
```

What is checked:

- End-to-end SkillOS loop: Work → Trace → Learn → Skill → Test → Release.
- SQLite storage initialization.
- GitHub Pages demo snapshot generation.
- reference workflow proof generation at `data/wealth_proof.json` and `dist/data/wealth_proof.json`.
- Monotonic economic checks: every release decreases cost, decreases minutes, increases quality, and increases accepted rate.
- `dist/index.html`, `dist/styles.css`, `dist/app.js`, `dist/data/demo.json`, `dist/data/wealth_proof.json`, `.nojekyll`, and manifest creation.
- Repository targets `MontrealAI/proof-gradient` and `https://montrealai.github.io/proof-gradient/`.
- JavaScript syntax for the static website.
- Root-level fallback website mirror is included for branch-root GitHub Pages deployment.

GitHub Actions re-runs the same QA path during deployment.

## v3.0 reference workflow proof

This repository includes `scripts/prove_wealth_loop.py`, `skillos/wealth_proof.py`, `tests/test_wealth_proof.py`, and `data/wealth_proof.json`.

The proof uses the sales follow-up workflow to verify that each completed job creates a tested release and that the workflow gets cheaper, faster, and better after every release.

Current proof result:

```text
Workflow: Sales follow-up email from call notes
Final skill version: v6
Quality: 0.50 → 0.96
Minutes/job: 6.75 → 2.55
Cost/job: $8.48 → $3.23
projected annual savings under demo assumptions vs human baseline at 10,000 jobs: $117,700
```

The GitHub Pages deploy refuses to publish if the reference workflow proof fails.

## GoalOS documentation validation

This documentation-only refresh adds two local validators that do not edit files and do not inspect or modify website implementation files.

Recommended documentation commands:

```bash
python scripts/validate_docs_tables_figures.py
python scripts/validate_goalos_catalog.py
```

What is checked:

- required GoalOS docs exist;
- required CSV tables are parseable;
- required Mermaid figure sources exist;
- `docs/data/goalos_catalog.yml` is parseable;
- README and documentation-index local links resolve;
- product ladder prices and versions match the catalog;
- safe-boundary language appears in key docs;
- prohibited claims are controlled as claim-boundary language, not live promises;
- direct paid ZIP public links are flagged;
- documentation-only scope is respected by changed-file checks.

Skipped by design:

- Mermaid SVG export unless Mermaid CLI (`mmdc`) is installed;
- website-file edits or generated GitHub Pages changes;
- application-code fixes for failures outside documentation scope.
