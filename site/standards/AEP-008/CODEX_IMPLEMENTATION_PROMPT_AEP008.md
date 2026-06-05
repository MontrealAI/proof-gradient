# Codex Prompt — Implement AEP-008

You are Codex acting as a world-class senior software engineer.

Repository: MontrealAI/proof-gradient

Task:
Add AEP-008 — Proof Room Standard v1.1 as an additive protocol standard.

Rules:
- Do not delete AEP-001 through AEP-007.
- Do not remove existing proof pages.
- Use `docs/standards/AEP-008/` as canonical source location.
- Use `site/standards/AEP-008/` as public website output.
- Add workflows only if safe.
- Do not commit paid product ZIPs.
- Run validators.

Files to add:
- AEP-008 markdown, PDF, DOCX, LaTeX
- schemas/
- examples/
- templates/
- tools/
- conformance/
- implementation/
- website workflow
- conformance CI workflow
- release workflow

Acceptance:
- AEP-008 site page exists.
- sample Proof Room manifest validates.
- Proof Room audit passes.
- no files deleted.
- AEP-001 through AEP-007 links remain intact.
