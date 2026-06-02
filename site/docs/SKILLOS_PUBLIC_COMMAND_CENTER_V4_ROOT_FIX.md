# Proof Gradient Public Command Center v4 Root Fix

Generated: `2026-06-01T16:50:00Z`

## What this fixes

The canonical v4 deployment prevents the older command-center generator from overwriting the public root URL.

Expected public checks:

```text
https://montrealai.github.io/proof-gradient/
https://montrealai.github.io/proof-gradient/index.html
https://montrealai.github.io/proof-gradient/data/command-center-manifest.json
```

The manifest should contain:

```text
schema: skillos.command_center.root_fix.v4
```

The homepage must not show:

```text
Autonomous Proof Command Center
SkillOS Proof Command Center
Proof Gradient Command Center v2
```

## Safe public claim

SkillOS makes the mechanism testable: completed work can become verified traces, verified traces can become reusable skills, and reusable skills can improve future routing under measured benchmark conditions.
