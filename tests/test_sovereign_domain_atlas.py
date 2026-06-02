import unittest
from pathlib import Path
import tempfile

from proof_gradient.sovereign_domain_atlas import build_archive, write_site


class SovereignDomainAtlasTest(unittest.TestCase):
    def setUp(self):
        self.archive = build_archive()
        self.proof = next(p for p in self.archive["proofs"] if p["slug"] == "008-sovereign-domain-atlas")

    def test_four_systems_are_present(self):
        promises = {system["name"]: system["promise"] for system in self.archive["systems"]}
        self.assertEqual(promises["Artifact Vault"], "stores reusable intelligence")
        self.assertEqual(promises["Run Fabric"], "executes agents at scale")
        self.assertEqual(promises["Proof Ledger"], "records what happened")
        self.assertEqual(promises["Selection Gate"], "promotes only what proved itself")

    def test_archive_has_eight_separate_proofs(self):
        self.assertEqual(self.archive["proof_count"], 8)
        slugs = {proof["slug"] for proof in self.archive["proofs"]}
        self.assertIn("001-sovereign-swarm", slugs)
        self.assertIn("002-evolution-tournament", slugs)
        self.assertIn("003-recursive-evolution-ladder", slugs)
        self.assertIn("004-corporate-rsi-dominion", slugs)
        self.assertIn("005-enterprise-rsi-superorganism", slugs)
        self.assertIn("006-sovereign-enterprise-constellation", slugs)
        self.assertIn("007-sovereign-enterprise-proof-economy", slugs)
        self.assertIn("008-sovereign-domain-atlas", slugs)

    def test_sovereign_domain_atlas_scale(self):
        summary = self.proof["summary"]
        self.assertGreaterEqual(summary["agents"], 262144)
        self.assertGreaterEqual(summary["sovereign_domains"], 512)
        self.assertGreaterEqual(summary["guilds"], 128)
        self.assertGreaterEqual(summary["rsi_cycles"], 64)
        self.assertGreaterEqual(summary["eval_cases"], 16777216)

    def test_sovereign_domain_atlas_rsi(self):
        rsi = self.proof["evidence"]["recursive_self_improvement"]
        self.assertGreaterEqual(rsi["meta_rsi_upgrade_count"], 16)
        self.assertGreater(rsi["synthetic_domain_atlas_index_final"], rsi["synthetic_domain_atlas_index_start"])
        self.assertGreater(rsi["selected_patch_count"], 30000)
        self.assertGreaterEqual(rsi["rollback_count"], 1)
        self.assertGreaterEqual(rsi["domain_transfer_count"], 1)
        self.assertGreaterEqual(rsi["proof_market_trade_count"], 1)
        self.assertGreaterEqual(rsi["capital_allocation_event_count"], 64)
        self.assertGreaterEqual(rsi["compute_allocation_event_count"], 64)
        self.assertGreaterEqual(rsi["trust_allocation_event_count"], 64)

    def test_institutional_graphs_exist(self):
        graphs = self.proof["evidence"]["institutional_graphs"]
        self.assertGreaterEqual(len(graphs["cycle_series"]), 64)
        self.assertGreaterEqual(len(graphs["leaderboard"]), 12)
        self.assertGreaterEqual(len(graphs["theater_summary"]), 16)
        self.assertIn("capital", graphs["allocation_tables"])
        self.assertIn("compute", graphs["allocation_tables"])
        self.assertIn("trust", graphs["allocation_tables"])

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
            self.assertIn("proofs/008-sovereign-domain-atlas.html", main)

            for slug in [
                "001-sovereign-swarm",
                "002-evolution-tournament",
                "003-recursive-evolution-ladder",
                "004-corporate-rsi-dominion",
                "005-enterprise-rsi-superorganism",
                "006-sovereign-enterprise-constellation",
                "007-sovereign-enterprise-proof-economy",
                "008-sovereign-domain-atlas",
            ]:
                self.assertTrue((site / "proofs" / f"{slug}.html").exists())
                self.assertTrue((site / "assets" / "proofs" / f"{slug}.json").exists())

            proof8 = (site / "proofs" / "008-sovereign-domain-atlas.html").read_text(encoding="utf-8")
            self.assertIn("../", proof8)
            self.assertIn("Proof Archive", proof8)
            self.assertIn("Sovereign Domain Index by RSI Cycle", proof8)
            self.assertIn("Sovereign Domain Leaderboard", proof8)
            self.assertIn("Institutional RSI Flow", proof8)


if __name__ == "__main__":
    unittest.main()
