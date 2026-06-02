from pathlib import Path
import re
import sys

FORBIDDEN_CLAIMS = [
    "guaranteed ROI",
    "guaranteed profit",
    "achieved Kardashev Type II",
    "real superintelligence achieved",
    "private data shared automatically",
]

SAFE_BOUNDARY_CONTEXTS = [
    "not claiming",
    "does not claim",
    "do not claim",
    "doesnt claim",
    "doesn't claim",
    "not claim",
    "not a claim",
    "not revenue",
    "not profit",
    "not investment advice",
    "not achieved",
    "not an achieved",
    "not real",
    "not empirical",
    "claim boundary",
    "claim-boundary",
    "forbidden claim",
    "not a guarantee",
    "strategic scenario",
    "synthetic",
    "archived",
    "deprecated",
    "unsupported claims",
    "does not represent",
    "not presented as",
]

SCAN_PATHS = [
    Path("README.md"),
    Path("docs/architecture.md"),
    Path("docs/final_acceptance_report.md"),
    Path("docs/security.md"),
    Path("docs/api.md"),
    Path("docs/cli.md"),
    Path("docs/deployment.md"),
    Path("docs/migration_from_skillos_v2.md"),
    Path("site/index.html"),
]


def normalize(text: str) -> str:
    text = text.lower()
    text = text.replace("**", " ")
    text = text.replace("__", " ")
    text = text.replace("`", " ")
    text = text.replace("*", " ")
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def line_is_safe(line: str) -> bool:
    normalized = normalize(line)
    return any(normalize(context) in normalized for context in SAFE_BOUNDARY_CONTEXTS)


failures = []
scanned = 0

for path in SCAN_PATHS:
    if not path.exists() or not path.is_file():
        continue

    scanned += 1
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()

    for number, line in enumerate(lines, start=1):
        normalized_line = normalize(line)

        for claim in FORBIDDEN_CLAIMS:
            normalized_claim = normalize(claim)

            if normalized_claim in normalized_line and not line_is_safe(line):
                failures.append((str(path), number, claim, line.strip()))

if failures:
    for path, number, claim, line in failures:
        print(f"FORBIDDEN CLAIM: {claim!r} in {path}:{number}")
        print(f"  {line}")
    sys.exit(1)

print(f"security review passed; scanned {scanned} generated public files")
