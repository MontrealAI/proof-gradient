import unittest
from pathlib import Path
import tempfile

from proof_gradient.corporate_rsi_dominion import build_archive, write_site


class CorporateRSIDominionTest(unittest.TestCase):
    def setUp(self):
        self.archive = build_archive()
        self.proof = next(p for p in self.archive["proofs"] if p["slug"] == "004-corporate-rsi-dominion")

    def test_four_systems_are_present(self):
        promises = {system["name"]: system["promise"] for system in self.archive["systems"]}
        self.assertEqual(promises["Artifact Vault"], "stores reusable intelligence")
        self.assertEqual(promises["Run Fabric"], "executes agents at scale")
        self.assertEqual(promises["Proof Ledger"], "records what happened")
        self.assertEqual(promises["Selection Gate"], "promotes only what proved itself")

    def test_corporate_rsi_is_large_multi_agent(self):
        summary = self.proof["summary"]
        self.assertGreaterEqual(summary["agents"], 512)
        self.assertGreaterEqual(summary["corporate_domains"], 16)
        self.assertGreaterEqual(summary["rsi_cycles"], 8)
        self.assertGreaterEqual(summary["eval_cases"], 6144)

    def test_corporate_rsi_is_recursive(self):
        rsi = self.proof["evidence"]["recursive_self_improvement"]
        self.assertGreaterEqual(rsi["meta_rsi_upgrade_count"], 4)
        self.assertGreater(rsi["synthetic_enterprise_value_index_final"], rsi["synthetic_enterprise_value_index_start"])
        self.assertGreater(rsi["selected_patch_count"], 100)
        self.assertGreaterEqual(rsi["rollback_count"], 1)

    def test_claim_boundary_is_safe(self):
        evidence = self.proof["evidence"]
        self.assertIn("real revenue", evidence["not_claiming"])
        self.assertIn("guaranteed ROI", evidence["not_claiming"])
        self.assertIn("actual deployed superintelligence", evidence["not_claiming"])
        self.assertEqual(
            evidence["claim_boundary"],
            "All value numbers are deterministic synthetic enterprise value-index units, not dollars, not revenue, and not investment advice.",
        )

    def test_each_proof_has_own_page_and_main_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site = root / "site"
            data = root / "data"
            write_site(site, data)

            main = (site / "index.html").read_text(encoding="utf-8")
            self.assertIn("proofs/004-corporate-rsi-dominion.html", main)

            for slug in [
                "001-sovereign-swarm",
                "002-evolution-tournament",
                "003-recursive-evolution-ladder",
                "004-corporate-rsi-dominion",
            ]:
                self.assertTrue((site / "proofs" / f"{slug}.html").exists())
                self.assertTrue((site / "assets" / "proofs" / f"{slug}.json").exists())

            proof4 = (site / "proofs" / "004-corporate-rsi-dominion.html").read_text(encoding="utf-8")
            self.assertIn("../", proof4)
            self.assertIn("Proof Archive", proof4)


if __name__ == "__main__":
    unittest.main()
