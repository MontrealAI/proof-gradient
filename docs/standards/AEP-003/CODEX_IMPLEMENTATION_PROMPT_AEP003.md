# Codex Prompt — Implement AEP-003

You are Codex acting as a world-class senior software engineer.

Repository: MontrealAI/proof-gradient

Task:
Add AEP-003 — ProofPacket Schema v1.1 as an additive protocol standard.

Rules:
- Do not delete AEP-001.
- Do not delete AEP-002.
- Do not remove existing proof pages.
- Use `docs/standards/AEP-003/` as canonical source location.
- Use `site/standards/AEP-003/` as public website output.
- Add workflows only if safe.
- Do not commit paid product ZIPs.
- Run validators.

Files to add:
- AEP-003 markdown, PDF, DOCX, LaTeX
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
- AEP-003 site page exists.
- sample packets validate.
- packet chain validates.
- no files deleted.
- AEP-001 and AEP-002 links remain intact.
