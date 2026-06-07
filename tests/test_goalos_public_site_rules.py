from scripts.goalos_public_site_rules import (
    is_blocked_paid_or_private_artifact,
    is_standalone_proof_page,
    requires_canonical_shell,
    is_app_page,
)


def test_public_aep_package_allowed():
    assert not is_blocked_paid_or_private_artifact("standards/AEP-001/complete-package.zip")
    assert not is_blocked_paid_or_private_artifact("site/standards/AEP-008/complete-package.zip")


def test_wrong_zip_blocked():
    assert is_blocked_paid_or_private_artifact("GoalOS_RSI_Sprint_Workshop_v6_0_COMPLETE_BUNDLE.zip")
    assert is_blocked_paid_or_private_artifact("site/GoalOS_Enterprise_RSI_Pilot_v2_0_BUYER_DELIVERY_KIT.zip")
    assert is_blocked_paid_or_private_artifact("public/private-anything.zip")


def test_rsi_proof_page_can_be_standalone_by_marker():
    text = "<!-- GOALOS-STANDALONE-PROOF --><html><head><title>x</title></head></html>"
    assert is_standalone_proof_page("rsi-ai-first-blockchain-capital-machine-proof.html", text)
    assert not requires_canonical_shell("rsi-ai-first-blockchain-capital-machine-proof.html", text)


def test_rsi_proof_page_can_be_standalone_by_filename():
    assert is_standalone_proof_page("rsi-ai-first-governance-capital-engine-proof.html", "")
    assert not requires_canonical_shell("rsi-ai-first-governance-capital-engine-proof.html", "")


def test_normal_public_page_requires_shell():
    assert requires_canonical_shell("pricing/index.html", "<html></html>")


def test_app_page_does_not_require_marketing_shell():
    assert is_app_page("app/goalos-cloud-mvp/index.html")
    assert not requires_canonical_shell("app/goalos-cloud-mvp/index.html", "<html></html>")


def test_safe_public_image_not_blocked():
    assert not is_blocked_paid_or_private_artifact("assets/brand/quebecaisealv5.png")


def test_aep_number_pattern_allows_future_public_standards_packages():
    assert not is_blocked_paid_or_private_artifact("standards/AEP-002/complete-package.zip")


def test_all_other_zips_remain_blocked():
    assert is_blocked_paid_or_private_artifact("GoalOS_Commercialization_Ready_Master_Pack.zip")
    assert is_blocked_paid_or_private_artifact("random-public.zip")
