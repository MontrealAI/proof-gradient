# AEP-002 v1.1 Institutional QA Report

Generated: 2026-06-05

## Render QA

- DOCX was rendered with LibreOffice through the DOCX render workflow.
- Final PDF was generated from the rendered DOCX.
- Rendered PNGs were visually inspected through contact sheets.
- One-page brief was rendered and visually inspected.
- No obvious clipping, table overflow, missing page content, or unreadable layout was observed.

## Schema / tool QA

- `tools/validate_evidence_docket.py` validates the institutional example.
- `tools/score_conformance.py` scores the example dockets and returns Level 4 for included complete examples.

## Package QA

This package includes:

- PDF
- DOCX
- Markdown
- LaTeX
- one-page PDF
- one-page DOCX
- JSON schemas
- example dockets
- templates
- conformance checklist
- validator and scoring tools
- GitHub Actions for website, release, and conformance CI
- figures
- installation guide
- checksums

## Claim boundary

AEP-002 is a proof package standard. It does not claim achieved AGI, achieved ASI, perfect safety, legal compliance certification, financial or legal advice, guaranteed ROI, production readiness, government endorsement, or national-security readiness.
