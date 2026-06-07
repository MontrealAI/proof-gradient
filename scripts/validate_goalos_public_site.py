#!/usr/bin/env python3
"""Validate the classified GoalOS public website deploy root."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

from goalos_public_site_rules import (
    BRAND_ASSET_MANIFEST_PATH,
    BRAND_MANIFEST_PATH,
    CANONICAL_FOOTER_MARKER,
    CANONICAL_NAV_MARKER,
    LINK_RE,
    OLD_SHELL_MARKER_RE,
    REQUIRED_ICON_PATHS,
    contains_blocked_claim_language,
    has_goalos_or_proof_gradient_escape,
    has_meta_description,
    has_quebec_ai_visible_brand,
    has_standalone_marker,
    has_title,
    is_app_page,
    is_blocked_paid_or_private_artifact,
    is_standalone_proof_page,
    normalize_rel,
    page_class,
    requires_canonical_shell,
)

ROOT = Path(__file__).resolve().parents[1]


def public_root() -> Path:
    if (ROOT / "site").is_dir():
        return ROOT / "site"
    if (ROOT / "public").is_dir():
        return ROOT / "public"
    raise FileNotFoundError("No public deploy root found. Expected site/ or public/.")


def site_target_exists(root: Path, url_path: str) -> bool:
    if not url_path.startswith("/proof-gradient/"):
        return True
    rel = url_path.removeprefix("/proof-gradient/").split("#", 1)[0].split("?", 1)[0]
    if rel == "":
        return (root / "index.html").exists()
    candidate = root / rel
    return (
        candidate.is_file()
        or (candidate.is_dir() and (candidate / "index.html").exists())
        or (rel.endswith("/") and (root / rel / "index.html").exists())
        or (root / f"{rel}.html").exists()
    )


def add_error(errors: list[str], rel: str, reason: str, fix: str) -> None:
    errors.append(f"{rel}: {reason}. Suggested fix: {fix}")


def validate_html(root: Path, path: Path, errors: list[str]) -> None:
    rel = normalize_rel(path.relative_to(root))
    text = path.read_text(encoding="utf-8", errors="ignore")
    cls = page_class(rel, text)

    if requires_canonical_shell(rel, text):
        nav_count = text.count(CANONICAL_NAV_MARKER)
        footer_count = text.count(CANONICAL_FOOTER_MARKER)
        if nav_count != 1:
            add_error(
                errors,
                rel,
                f"classified as canonical_page but has {nav_count} canonical shells",
                "inject exactly one canonical GoalOS shell or mark as GOALOS-STANDALONE-PROOF if intentionally standalone",
            )
        if footer_count != 1:
            add_error(
                errors,
                rel,
                f"classified as canonical_page but has {footer_count} canonical footers",
                "inject exactly one canonical GoalOS footer or mark as GOALOS-STANDALONE-PROOF if intentionally standalone",
            )
    elif is_standalone_proof_page(rel, text) and text.count(CANONICAL_NAV_MARKER) == 0 and text.count(CANONICAL_FOOTER_MARKER) == 0:
        if not has_standalone_marker(text):
            add_error(
                errors,
                rel,
                "matches standalone proof path but lacks explicit standalone metadata",
                "add <!-- GOALOS-STANDALONE-PROOF --> and <meta name=\"goalos-page-type\" content=\"standalone-proof\">",
            )
        if not has_title(text):
            add_error(errors, rel, "standalone_proof_page lacks a non-empty <title>", "add a concise proof title")
        if not has_meta_description(text):
            add_error(errors, rel, "standalone_proof_page lacks meta description", "add <meta name=\"description\" content=\"...\">")
        if not has_goalos_or_proof_gradient_escape(text):
            add_error(errors, rel, "standalone_proof_page lacks visible GoalOS / Proof Gradient escape link", "add <a href=\"/proof-gradient/\">GoalOS · Proof Gradient</a>")
        if not has_quebec_ai_visible_brand(text):
            add_error(errors, rel, "standalone_proof_page lacks visible QUEBEC.AI ⚜️✨ brand boundary", "include QUEBEC.AI ⚜️✨ in visible page copy")
        if contains_blocked_claim_language(text):
            add_error(errors, rel, "contains blocked claim language", "remove unsupported superintelligence, investment, token, or model self-modification claims")
    elif is_app_page(rel):
        if not has_title(text):
            add_error(errors, rel, "app_page lacks a non-empty <title>", "add an app-shell title")

    if OLD_SHELL_MARKER_RE.search(text):
        add_error(errors, rel, "old GoalOS shell marker remains", "remove legacy shell markers and keep only current canonical/app/standalone markers")

    for raw in LINK_RE.findall(text):
        parsed = urlparse(raw)
        link_path = parsed.path
        if link_path.startswith("/proof-gradient/") and not site_target_exists(root, link_path):
            add_error(errors, rel, f"broken internal link {raw}", "update the link or add the target file under the public root")
        if link_path and is_blocked_paid_or_private_artifact(link_path):
            add_error(errors, rel, f"links to paid/private artifact {raw}", "remove the link or move the file outside the public deploy root")

    for raw in LINK_RE.findall(text):
        if is_blocked_paid_or_private_artifact(raw):
            add_error(errors, rel, f"references paid/private artifact {raw}", "remove public references to buyer/private artifacts")


def validate_public_assets(root: Path, errors: list[str]) -> None:
    for required in REQUIRED_ICON_PATHS:
        if not (root / required).exists():
            add_error(errors, required, "required QUEBEC.AI seal/icon file is missing", "generate/copy the public brand asset before deploy")

    if (root / "assets" / "brand").exists() and not (root / BRAND_MANIFEST_PATH).exists():
        add_error(errors, BRAND_MANIFEST_PATH, "brand assets exist but site.webmanifest is missing", "add the public brand manifest")
    if (root / "assets" / "brand").exists() and not (root / BRAND_ASSET_MANIFEST_PATH).exists():
        add_error(errors, BRAND_ASSET_MANIFEST_PATH, "brand assets exist but brand asset manifest is missing", "add assets/brand-assets-v8.json")
    elif (root / BRAND_ASSET_MANIFEST_PATH).exists():
        try:
            manifest = json.loads((root / BRAND_ASSET_MANIFEST_PATH).read_text(encoding="utf-8"))
            if not isinstance(manifest.get("assets"), list):
                add_error(errors, BRAND_ASSET_MANIFEST_PATH, "brand asset manifest lacks an assets list", "include an assets array")
        except Exception as exc:  # noqa: BLE001 - validator reports parse exception
            add_error(errors, BRAND_ASSET_MANIFEST_PATH, f"brand asset manifest could not be parsed: {exc}", "write valid JSON")

    for path in sorted(p for p in root.rglob("*") if p.is_file() and "_archive" not in p.parts):
        rel = normalize_rel(path.relative_to(root))
        if is_blocked_paid_or_private_artifact(rel):
            add_error(errors, rel, f"classified as {page_class(rel)} and is blocked from public deploy", "remove from public root or add a narrow reviewed public allowlist rule in goalos_public_site_rules.py")


def main() -> int:
    try:
        root = public_root()
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    errors: list[str] = []
    validate_public_assets(root, errors)

    html_files = sorted(p for p in root.rglob("*.html") if "_archive" not in p.parts)
    for path in html_files:
        validate_html(root, path, errors)

    if errors:
        print("GoalOS public site validation failed:", file=sys.stderr)
        for error in errors[:250]:
            print(f"- {error}", file=sys.stderr)
        if len(errors) > 250:
            print(f"... {len(errors) - 250} more failures", file=sys.stderr)
        return 1

    print(f"GoalOS public site validation passed for {root.relative_to(ROOT)}/ ({len(html_files)} HTML pages).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
