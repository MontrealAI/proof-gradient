import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from goalos_public_site_rules import (
    is_app_page,
    is_blocked_paid_or_private_artifact,
    is_public_aep_package,
    is_standalone_proof_page,
    requires_canonical_shell,
)


def test_public_aep_package_allowed():
    assert is_public_aep_package("standards/AEP-001/complete-package.zip")
    assert not is_blocked_paid_or_private_artifact(
        "standards/AEP-001/complete-package.zip"
    )


def test_public_aep_package_style_paths_allowed_case_insensitive():
    assert not is_blocked_paid_or_private_artifact(
        "standards/AEP-002/complete-package.zip"
    )
    assert not is_blocked_paid_or_private_artifact(
        "standards/aep-123/COMPLETE-PACKAGE.zip"
    )


def test_paid_workshop_zip_blocked():
    assert is_blocked_paid_or_private_artifact(
        "site/GoalOS_RSI_Sprint_Workshop_v6_0_COMPLETE_BUNDLE.zip"
    )


def test_blocked_delivery_kit_names():
    blocked = [
        "site/GoalOS_RSI_Sprint_Workshop_v6_0_BUYER_FACILITATOR_DELIVERY_KIT.zip",
        "site/GoalOS_Enterprise_RSI_Pilot_v2_0_BUYER_DELIVERY_KIT.zip",
        "site/GoalOS_Commercialization_Ready_Master_Pack.zip",
        "site/private-anything.zip",
    ]
    for rel in blocked:
        assert is_blocked_paid_or_private_artifact(rel)


def test_rsi_blockchain_proof_page_can_be_standalone():
    text = "<!-- GOALOS-STANDALONE-PROOF --><html><head><title>x</title></head></html>"
    assert is_standalone_proof_page(
        "rsi-ai-first-blockchain-capital-machine-proof.html",
        text,
    )
    assert not requires_canonical_shell(
        "rsi-ai-first-blockchain-capital-machine-proof.html",
        text,
    )


def test_rsi_governance_proof_page_can_be_standalone():
    text = '<meta name="goalos-page-type" content="standalone-proof"><title>x</title>'
    assert is_standalone_proof_page(
        "rsi-ai-first-governance-capital-engine-proof.html",
        text,
    )
    assert not requires_canonical_shell(
        "rsi-ai-first-governance-capital-engine-proof.html",
        text,
    )


def test_normal_public_page_requires_shell():
    assert requires_canonical_shell("pricing/index.html", "<html></html>")


def test_public_app_pages_do_not_require_marketing_shell():
    assert is_app_page("app/goalos-cloud-mvp/index.html")
    assert is_app_page("app/goalos-cloud-mvp/dashboard/index.html")
    assert not requires_canonical_shell("app/goalos-cloud-mvp/index.html", "<title>App</title>")


def test_safe_image_assets_are_not_blocked():
    assert not is_blocked_paid_or_private_artifact("assets/private-diagram.png")
    assert not is_blocked_paid_or_private_artifact("assets/buyer-flow.svg")
