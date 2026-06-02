import unittest
from pathlib import Path
import tempfile

from proof_gradient.sovereign_enterprise_proof_economy import build_archive, write_site


class SovereignEnterpriseProofEconomyTest(unittest.TestCase):
    def setUp(self):
        self.archive = build_archive()
        self.proof = next(p for p in self.archive["proofs"] if p["slug"] == "007-sovereign-enterprise-proof-economy")

    def test_four_systems_are_present(self):
        promises = {system["name"]: system["promise"] for system in self.archive["systems"]}
        self.assertEqual(promises["Artifact Vault"], "stores reusable intelligence")
        self.assertEqual(promises["Run Fabric"], "executes agents at scale")
        self.assertEqual(promises["Proof Ledger"], "records what happened")
        self.assertEqual(promises["Selection Gate"], "promotes only what proved itself")

    def test_archive_has_seven_separate_proofs(self):
        self.assertEqual(self.archive["proof_count"], 7)
        slugs = {proof["slug"] for proof in self.archive["proofs"]}
        self.assertIn("001-sovereign-swarm", slugs)
        self.assertIn("002-evolution-tournament", slugs)
        self.assertIn("003-recursive-evolution-ladder", slugs)
        self.assertIn("004-corporate-rsi-dominion", slugs)
        self.assertIn("005-enterprise-rsi-superorganism", slugs)
        self.assertIn("006-sovereign-enterprise-constellation", slugs)
        self.assertIn("007-sovereign-enterprise-proof-economy", slugs)

    def test_sovereign_proof_economy_scale(self):
        summary = self.proof["summary"]
        self.assertGreaterEqual(summary["agents"], 65536)
        self.assertGreaterEqual(summary["sovereign_enterprises"], 256)
        self.assertGreaterEqual(summary["sovereign_domains"], 64)
        self.assertGreaterEqual(summary["rsi_cycles"], 32)
        self.assertGreaterEqual(summary["eval_cases"], 2097152)

    def test_proof_market_rsi_is_recursive_and_economic(self):
        economy = self.proof["evidence"]["recursive_self_improvement"]
        self.assertGreaterEqual(economy["meta_rsi_upgrade_count"], 8)
        self.assertGreater(economy["synthetic_market_index_final"], economy["synthetic_market_index_start"])
        self.assertGreater(economy["selected_patch_count"], 7000)
        self.assertGreaterEqual(economy["rollback_count"], 1)
        self.assertGreaterEqual(economy["proof_market_trade_count"], 1)
        self.assertGreaterEqual(economy["federated_adoption_count"], 1)
        self.assertGreaterEqual(economy["pricing_event_count"], 1)
        self.assertGreaterEqual(economy["reputation_event_count"], 1)
        self.assertGreaterEqual(economy["capital_allocation_event_count"], 32)

    def test_sovereignty_boundaries_are_safe(self):
        evidence = self.proof["evidence"]
        guarantees = evidence["sovereignty_guarantees"]
        self.assertFalse(guarantees["private_data_shared"])
        self.assertFalse(guarantees["private_customer_records_shared"])
        self.assertFalse(guarantees["private_financials_shared"])
        self.assertTrue(guarantees["local_eval_required_before_adoption"])
        self.assertTrue(guarantees["rollback_required_before_release"])
        self.assertIn("guaranteed ROI", evidence["not_claiming"])

    def test_each_proof_has_own_page_and_main_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site = root / "site"
            data = root / "data"
            write_site(site, data)

            main = (site / "index.html").read_text(encoding="utf-8")
            self.assertIn("proofs/007-sovereign-enterprise-proof-economy.html", main)

            for slug in [
                "001-sovereign-swarm",
                "002-evolution-tournament",
                "003-recursive-evolution-ladder",
                "004-corporate-rsi-dominion",
                "005-enterprise-rsi-superorganism",
                "006-sovereign-enterprise-constellation",
                "007-sovereign-enterprise-proof-economy",
            ]:
                self.assertTrue((site / "proofs" / f"{slug}.html").exists())
                self.assertTrue((site / "assets" / "proofs" / f"{slug}.json").exists())

            proof7 = (site / "proofs" / "007-sovereign-enterprise-proof-economy.html").read_text(encoding="utf-8")
            self.assertIn("../", proof7)
            self.assertIn("Proof Archive", proof7)


if __name__ == "__main__":
    unittest.main()
