# Codex Prompt — Implement AEP-005

You are Codex acting as a world-class senior software engineer.

Repository: MontrealAI/proof-gradient

Task:
Add AEP-005 — Tool Permission Standard v1.1 as an additive protocol standard.

Rules:
- Do not delete AEP-001.
- Do not delete AEP-002.
- Do not delete AEP-003.
- Do not delete AEP-004.
- Do not remove existing proof pages.
- Use `docs/standards/AEP-005/` as canonical source location.
- Use `site/standards/AEP-005/` as public website output.
- Add workflows only if safe.
- Do not commit paid product ZIPs.
- Run validators.

Files to add:
- AEP-005 markdown, PDF, DOCX, LaTeX
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
- AEP-005 site page exists.
- sample tool permission decisions validate.
- sample lease validates.
- gateway audit passes.
- no files deleted.
- AEP-001, AEP-002, AEP-003, and AEP-004 links remain intact.
