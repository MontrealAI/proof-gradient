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
    CANONICAL_SHELL_MARKER,
    LINK_RE,
    REQUIRED_ICON_PATHS,
    classify_html_page,
    contains_blocked_claim_language,
    has_goalos_or_proof_gradient_escape,
    has_meta_description,
    has_old_shell_marker,
    has_quebec_ai_visible_brand,
    has_standalone_marker,
    has_title,
    is_blocked_paid_or_private_artifact,
    normalize_rel,
    page_class,
    requires_canonical_shell,
)

ROOT = Path(__file__).resolve().parents[1]


def public_root() -> Path:
    """Detect the public deploy root, preferring site/ and falling back to public/."""
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


def validate_blocked_references(root: Path, rel: str, text: str, errors: list[str]) -> None:
    for raw in LINK_RE.findall(text):
        parsed = urlparse(raw)
        link_path = parsed.path
        if link_path.startswith("/proof-gradient/") and not site_target_exists(root, link_path):
            add_error(errors, rel, f"broken internal link {raw}", "update the link or add the target file under the public root")
        if link_path and is_blocked_paid_or_private_artifact(link_path):
            add_error(errors, rel, f"links to paid/private artifact {raw}", "remove the link or move the file outside the public deploy root")
        if is_blocked_paid_or_private_artifact(raw):
            add_error(errors, rel, f"references paid/private artifact {raw}", "remove public references to buyer/private artifacts")


def validate_html(root: Path, path: Path, errors: list[str]) -> None:
    rel = normalize_rel(path.relative_to(root))
    text = path.read_text(encoding="utf-8", errors="ignore")
    cls = classify_html_page(rel, text)

    if requires_canonical_shell(rel, text):
        shell_count = text.count(CANONICAL_SHELL_MARKER)
        footer_count = text.count(CANONICAL_FOOTER_MARKER)
        if shell_count != 1:
            add_error(
                errors,
                rel,
                f"is classified as canonical_page but has {shell_count} canonical shells",
                "inject exactly one canonical shell, or mark it as GOALOS-STANDALONE-PROOF if intentionally standalone",
            )
        if footer_count != 1:
            add_error(
                errors,
                rel,
                f"is classified as canonical_page but has {footer_count} canonical footers",
                "inject exactly one canonical footer, or mark it as GOALOS-STANDALONE-PROOF if intentionally standalone",
            )

    if cls == "standalone_proof_page":
        explicit_standalone = has_standalone_marker(text)
        if not explicit_standalone:
            # v14 microsite compatibility: legacy root proof/readiness pages are
            # classified by path and do not need the marketing shell. New
            # standalone pages should still add explicit metadata.
            pass
        if not has_title(text):
            add_error(errors, rel, "is classified as standalone_proof_page but lacks a useful <title>", "add a concise proof title")
        if explicit_standalone and not has_meta_description(text):
            add_error(errors, rel, "is classified as standalone_proof_page but lacks meta description", "add <meta name=\"description\" content=\"...\">")
        if explicit_standalone and not has_goalos_or_proof_gradient_escape(text):
            add_error(errors, rel, "is classified as standalone_proof_page but lacks a GoalOS / Proof Gradient link back", "add <a href="/proof-gradient/">QUEBEC.AI ⚜️✨ · GoalOS · Proof Gradient</a>")
        if explicit_standalone and not has_quebec_ai_visible_brand(text):
            add_error(errors, rel, "is classified as standalone_proof_page but lacks QUEBEC.AI identity", "include QUEBEC.AI, ⚜️✨, or quebecaisealv5 in the page")
        if contains_blocked_claim_language(text):
            add_error(errors, rel, "contains blocked claim language", "remove unsupported investment or model self-modification claims")

    if cls == "app_page" and not has_title(text):
        add_error(errors, rel, "is classified as app_page but lacks a useful <title>", "add an app-shell title")

    if has_old_shell_marker(text):
        add_error(errors, rel, "contains an old GoalOS shell marker", "remove legacy shell markers and keep only current canonical/app/standalone markers")

    validate_blocked_references(root, rel, text, errors)


def validate_public_assets(root: Path, errors: list[str]) -> None:
    for required in REQUIRED_ICON_PATHS:
        if not (root / required).exists():
            add_error(errors, required, "required public identity asset is missing", "restore the QUEBEC.AI seal/icon asset before deploy")

    if not (root / BRAND_MANIFEST_PATH).exists():
        add_error(errors, BRAND_MANIFEST_PATH, "required site.webmanifest is missing", "add the public web app manifest")

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
            add_error(errors, rel, f"is classified as {page_class(rel)} and is blocked from public deploy", "remove from public root or add a narrow reviewed public allowlist rule in goalos_public_site_rules.py")


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
