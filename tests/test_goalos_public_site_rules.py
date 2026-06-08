from scripts.goalos_public_site_rules import (
    classify_html_page,
    is_blocked_paid_or_private_artifact,
    is_public_aep_package,
    is_standalone_proof_page,
    requires_canonical_shell,
    is_app_page,
)


def test_public_aep_package_allowed():
    assert is_public_aep_package("standards/AEP-001/complete-package.zip")
    assert is_public_aep_package("site/standards/AEP-008/complete-package.zip")
    assert is_public_aep_package("public/standards/AEP-002/complete-package.zip")
    assert not is_blocked_paid_or_private_artifact("standards/AEP-001/complete-package.zip")
    assert not is_blocked_paid_or_private_artifact("site/standards/AEP-008/complete-package.zip")


def test_wrong_zip_blocked():
    assert is_blocked_paid_or_private_artifact("GoalOS_RSI_Sprint_Workshop_v6_0_COMPLETE_BUNDLE.zip")
    assert is_blocked_paid_or_private_artifact("site/GoalOS_Enterprise_RSI_Pilot_v2_0_BUYER_DELIVERY_KIT.zip")
    assert is_blocked_paid_or_private_artifact("public/private-anything.zip")
    assert is_blocked_paid_or_private_artifact("GoalOS_RSI_Sprint_Workshop_v6_0_BUYER_FACILITATOR_DELIVERY_KIT.zip")
    assert is_blocked_paid_or_private_artifact("GoalOS_Commercialization_Ready_Master_Pack.zip")


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
    assert classify_html_page("app/goalos-cloud-mvp/index.html", "<html></html>") == "app_page"
    assert not requires_canonical_shell("app/goalos-cloud-mvp/index.html", "<html></html>")


def test_safe_public_image_not_blocked():
    assert not is_blocked_paid_or_private_artifact("assets/brand/quebecaisealv5.png")


def test_aep_number_pattern_allows_future_public_standards_packages():
    assert not is_blocked_paid_or_private_artifact("standards/AEP-002/complete-package.zip")


def test_all_other_zips_remain_blocked():
    assert is_blocked_paid_or_private_artifact("GoalOS_Commercialization_Ready_Master_Pack.zip")
    assert is_blocked_paid_or_private_artifact("random-public.zip")


def test_page_classification_is_not_shell_silencing():
    assert classify_html_page("pricing/index.html", "<html></html>") == "canonical_page"
    assert classify_html_page("rsi-ai-first-blockchain-capital-machine-proof.html", "") == "standalone_proof_page"
    assert classify_html_page("README.md", "") == "other"


def test_near_miss_aep_zip_paths_are_blocked():
    assert not is_public_aep_package("standards/AEP-01/complete-package.zip")
    assert not is_public_aep_package("standards/AEP-001/buyer-package.zip")
    assert is_blocked_paid_or_private_artifact("standards/AEP-001/buyer-package.zip")
    assert is_blocked_paid_or_private_artifact("standards/AEP-001/complete-package-v2.zip")


def test_path_normalization_and_public_root_stripping():
    from scripts.goalos_public_site_rules import normalize_rel, strip_public_root

    assert normalize_rel(r".\\site\\standards\\AEP-001\\complete-package.zip") == "site/standards/AEP-001/complete-package.zip"
    assert strip_public_root("public/standards/AEP-002/complete-package.zip") == "standards/AEP-002/complete-package.zip"
    assert strip_public_root("/site/pricing/index.html") == "pricing/index.html"


def test_site_prefixed_rsi_and_app_pages_keep_classification():
    assert is_standalone_proof_page("site/rsi-ai-first-blockchain-capital-machine-proof.html", "")
    assert not requires_canonical_shell("public/rsi-ai-first-governance-capital-engine-proof.html", "")
    assert is_app_page("site/app/goalos-cloud-mvp/index.html")
    assert not requires_canonical_shell("site/app/goalos-cloud-mvp/index.html", "<html></html>")


def test_current_paid_buyer_artifact_examples_are_blocked():
    blocked = [
        "GoalOS_AI_Efficiency_Sprint_Kit_v1_4_BUYER_EXCELLENCE_EDITION.zip",
        "GoalOS_RSI_Lite_Recursive_Self_Improving_Workflow_Kit_v1_6_CLEAN_BUYER_OFFICIAL.zip",
        "GoalOS_Proof_Room_Lite_Department_Pack_v2_0_WORLD_CLASS_BILINGUAL_BUYER_OFFICIAL.zip",
        "GoalOS_RSI_Sprint_Workshop_v7_0_PRIME_TIME_PROOF_CARD_EDITION_COMPLETE_BUNDLE.zip",
        "GoalOS_Enterprise_RSI_Pilot_v2_0_INSTITUTIONAL_BOARDROOM_FINAL_COMPLETE_BUNDLE.zip",
    ]
    assert not is_blocked_paid_or_private_artifact("standards/AEP-001/complete-package.zip")
    for filename in blocked:
        assert is_blocked_paid_or_private_artifact(filename)
