#!/usr/bin/env python3
"""Validate GoalOS public site files using shared classification rules."""
from __future__ import annotations

import sys
from pathlib import Path

from goalos_public_site_rules import (
    BLOCKED_CLAIM_RE,
    CANONICAL_FOOTER_MARKER,
    CANONICAL_NAV_MARKER,
    OLD_SHELL_MARKERS,
    ValidationError,
    classify_public_path,
    discover_public_root,
    has_goalos_backlink,
    has_meta_description,
    has_quebec_ai_identity,
    has_title,
    internal_proof_gradient_links,
    is_blocked_paid_or_private_artifact,
    is_public_html_path,
    normalize_rel,
    requires_canonical_shell,
    site_target_exists,
    validate_required_brand_assets,
)

ROOT = Path(__file__).resolve().parents[1]


def validate_html(public_root: Path, path: Path) -> list[ValidationError]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    rel = normalize_rel(path.relative_to(public_root))
    page_class = classify_public_path(rel, text)
    errors: list[ValidationError] = []

    if requires_canonical_shell(rel, text):
        nav_count = text.count(CANONICAL_NAV_MARKER)
        footer_count = text.count(CANONICAL_FOOTER_MARKER)
        if nav_count != 1:
            errors.append(ValidationError(
                rel,
                f"is classified as {page_class} but has {nav_count} canonical shells",
                "Inject exactly one canonical GoalOS shell, or mark it GOALOS-STANDALONE-PROOF if it is intentionally standalone.",
            ))
        if footer_count != 1:
            errors.append(ValidationError(
                rel,
                f"is classified as {page_class} but has {footer_count} canonical footers",
                "Inject exactly one canonical GoalOS footer, or mark it GOALOS-STANDALONE-PROOF if it is intentionally standalone.",
            ))

    if page_class in {"standalone_proof_page", "app_page"}:
        if not has_title(text):
            errors.append(ValidationError(rel, f"is classified as {page_class} but has no <title>", "Add a descriptive <title> element."))
        if page_class == "standalone_proof_page" and not has_meta_description(text):
            errors.append(ValidationError(rel, "is a standalone proof page but has no meta description", "Add <meta name=\"description\" content=\"...\">."))
        if page_class == "standalone_proof_page" and not has_goalos_backlink(text):
            errors.append(ValidationError(rel, "is a standalone proof page without a GoalOS / Proof Gradient backlink", "Add a visible link to /proof-gradient/."))
        if page_class == "standalone_proof_page" and not has_quebec_ai_identity(text):
            errors.append(ValidationError(rel, "is a standalone proof page without visible QUEBEC.AI identity", "Add visible QUEBEC.AI ⚜️✨ identity text."))

    if OLD_SHELL_MARKERS.search(text):
        errors.append(ValidationError(rel, "contains an obsolete GoalOS shell marker", "Remove old shell markers and use the canonical shell, app shell, or standalone proof marker."))

    blocked_claim = BLOCKED_CLAIM_RE.search(text)
    if blocked_claim:
        errors.append(ValidationError(rel, f"contains blocked claim language ({blocked_claim.group(0)!r})", "Describe workflow-level recursive improvement with human approval, proof records, versioning, monitoring, and rollback instead of model self-modification."))

    for raw in internal_proof_gradient_links(text):
        link_path = raw.split("#", 1)[0].split("?", 1)[0]
        if not site_target_exists(public_root, link_path):
            errors.append(ValidationError(rel, f"has broken internal link {raw}", "Update the href/src target or create the linked public page/asset."))

    for raw in internal_proof_gradient_links(text):
        rel_target = raw.split("#", 1)[0].split("?", 1)[0].removeprefix("/proof-gradient/")
        if rel_target and is_blocked_paid_or_private_artifact(rel_target):
            errors.append(ValidationError(rel, f"links to blocked paid/private artifact {raw}", "Remove the public link and keep buyer materials outside public deploy roots."))

    return errors


def validate_public_artifacts(public_root: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []
    for path in sorted(public_root.rglob("*")):
        if not path.is_file() or "_archive" in path.parts:
            continue
        rel = normalize_rel(path.relative_to(public_root))
        if is_blocked_paid_or_private_artifact(rel):
            errors.append(ValidationError(rel, "is a blocked paid/private artifact in the public deploy root", "Remove it from site/public, or add a narrow reviewed public allowlist rule in goalos_public_site_rules.py."))
    return errors


def main() -> int:
    try:
        public_root = discover_public_root(ROOT)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    errors: list[ValidationError] = []
    errors.extend(validate_required_brand_assets(public_root))
    errors.extend(validate_public_artifacts(public_root))
    html_files = sorted(p for p in public_root.rglob("*.html") if is_public_html_path(p))
    for path in html_files:
        errors.extend(validate_html(public_root, path))

    if errors:
        print("GoalOS public site validation failed:", file=sys.stderr)
        for error in errors[:250]:
            print(f"- {error.format()}", file=sys.stderr)
        if len(errors) > 250:
            print(f"... {len(errors) - 250} more failures", file=sys.stderr)
        return 1

    print(f"GoalOS public site validation passed for {len(html_files)} HTML pages under {public_root.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
