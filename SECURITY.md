# Security Policy

Agent SkillOS is a reference implementation. It is designed to demonstrate safe skill learning patterns, not to replace enterprise security controls.

## Core safety expectations

- Do not let agents silently publish global skill changes.
- Do not let private data become a shared network skill.
- Do not grant tool access through skill text alone.
- Require approval for high-impact actions.
- Keep release history and rollback paths.

## Reporting issues

For a real deployment, route security reports through your organization's vulnerability disclosure process.

## GoalOS public proof and AI workflow safety

- Report vulnerabilities and accidental exposure risks through responsible disclosure before public discussion.
- GoalOS improves workflows around AI; it does not modify base AI models.
- Do not place private buyer data, private evidence, secrets, credentials, or regulated personal data in public proof cards.
- Do not upload paid artifacts, buyer ZIPs, workshop bundles, implementation bundles, enterprise pilot bundles, or private delivery kits to the public site.
- Keep API keys and model-provider credentials out of commits, logs, public proofs, screenshots, and static site assets.
- Treat model-provider data handling as a deployment risk: review provider retention, training, privacy, and enterprise controls before using buyer data.
