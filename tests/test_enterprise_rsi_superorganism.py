import unittest
from pathlib import Path
import tempfile

from proof_gradient.enterprise_rsi_superorganism import build_archive, write_site


class EnterpriseRSISuperorganismTest(unittest.TestCase):
    def setUp(self):
        self.archive = build_archive()
        self.proof = next(p for p in self.archive["proofs"] if p["slug"] == "005-enterprise-rsi-superorganism")

    def test_four_systems_are_present(self):
        promises = {system["name"]: system["promise"] for system in self.archive["systems"]}
        self.assertEqual(promises["Artifact Vault"], "stores reusable intelligence")
        self.assertEqual(promises["Run Fabric"], "executes agents at scale")
        self.assertEqual(promises["Proof Ledger"], "records what happened")
        self.assertEqual(promises["Selection Gate"], "promotes only what proved itself")

    def test_archive_has_five_separate_proofs(self):
        self.assertEqual(self.archive["proof_count"], 5)
        slugs = {proof["slug"] for proof in self.archive["proofs"]}
        self.assertIn("001-sovereign-swarm", slugs)
        self.assertIn("002-evolution-tournament", slugs)
        self.assertIn("003-recursive-evolution-ladder", slugs)
        self.assertIn("004-corporate-rsi-dominion", slugs)
        self.assertIn("005-enterprise-rsi-superorganism", slugs)

    def test_enterprise_rsi_scale(self):
        summary = self.proof["summary"]
        self.assertGreaterEqual(summary["agents"], 2048)
        self.assertGreaterEqual(summary["guilds"], 32)
        self.assertGreaterEqual(summary["corporate_domains"], 32)
        self.assertGreaterEqual(summary["rsi_cycles"], 12)
        self.assertGreaterEqual(summary["eval_cases"], 49152)

    def test_enterprise_rsi_is_recursive_and_meta_recursive(self):
        rsi = self.proof["evidence"]["recursive_self_improvement"]
        self.assertGreaterEqual(rsi["meta_rsi_upgrade_count"], 6)
        self.assertGreater(rsi["synthetic_enterprise_index_final"], rsi["synthetic_enterprise_index_start"])
        self.assertGreater(rsi["selected_patch_count"], 300)
        self.assertGreaterEqual(rsi["rollback_count"], 1)
        self.assertGreaterEqual(rsi["cross_domain_transfer_count"], 1)
        self.assertGreaterEqual(rsi["capital_allocation_event_count"], 12)

    def test_claim_boundary_is_safe(self):
        evidence = self.proof["evidence"]
        self.assertIn("real revenue", evidence["not_claiming"])
        self.assertIn("real profit", evidence["not_claiming"])
        self.assertIn("guaranteed ROI", evidence["not_claiming"])
        self.assertIn("actual deployed superintelligence", evidence["not_claiming"])
        self.assertEqual(
            evidence["claim_boundary"],
            "All value numbers are deterministic synthetic enterprise-index units, not dollars, not revenue, not profit, and not investment advice.",
        )

    def test_each_proof_has_own_page_and_main_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site = root / "site"
            data = root / "data"
            write_site(site, data)

            main = (site / "index.html").read_text(encoding="utf-8")
            self.assertIn("proofs/005-enterprise-rsi-superorganism.html", main)

            for slug in [
                "001-sovereign-swarm",
                "002-evolution-tournament",
                "003-recursive-evolution-ladder",
                "004-corporate-rsi-dominion",
                "005-enterprise-rsi-superorganism",
            ]:
                self.assertTrue((site / "proofs" / f"{slug}.html").exists())
                self.assertTrue((site / "assets" / "proofs" / f"{slug}.json").exists())

            proof5 = (site / "proofs" / "005-enterprise-rsi-superorganism.html").read_text(encoding="utf-8")
            self.assertIn("../", proof5)
            self.assertIn("Proof Archive", proof5)


if __name__ == "__main__":
    unittest.main()
