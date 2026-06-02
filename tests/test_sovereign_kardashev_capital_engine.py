import unittest
from pathlib import Path
import tempfile

from proof_gradient.sovereign_kardashev_capital_engine import build_archive, write_site


class SovereignKardashevCapitalEngineTest(unittest.TestCase):
    def setUp(self):
        self.archive = build_archive()
        self.proof = next(p for p in self.archive["proofs"] if p["slug"] == "009-sovereign-kardashev-capital-engine")

    def test_four_systems_are_present(self):
        promises = {system["name"]: system["promise"] for system in self.archive["systems"]}
        self.assertEqual(promises["Artifact Vault"], "stores reusable intelligence")
        self.assertEqual(promises["Run Fabric"], "executes agents at scale")
        self.assertEqual(promises["Proof Ledger"], "records what happened")
        self.assertEqual(promises["Selection Gate"], "promotes only what proved itself")

    def test_archive_has_nine_separate_proofs(self):
        self.assertEqual(self.archive["proof_count"], 9)
        slugs = {proof["slug"] for proof in self.archive["proofs"]}
        self.assertIn("001-sovereign-swarm", slugs)
        self.assertIn("002-evolution-tournament", slugs)
        self.assertIn("003-recursive-evolution-ladder", slugs)
        self.assertIn("004-corporate-rsi-dominion", slugs)
        self.assertIn("005-enterprise-rsi-superorganism", slugs)
        self.assertIn("006-sovereign-enterprise-constellation", slugs)
        self.assertIn("007-sovereign-enterprise-proof-economy", slugs)
        self.assertIn("008-sovereign-domain-atlas", slugs)
        self.assertIn("009-sovereign-kardashev-capital-engine", slugs)

    def test_kardashev_engine_scale(self):
        summary = self.proof["summary"]
        self.assertGreaterEqual(summary["agents"], 1048576)
        self.assertGreaterEqual(summary["sovereign_domains"], 1024)
        self.assertGreaterEqual(summary["guilds"], 256)
        self.assertGreaterEqual(summary["rsi_cycles"], 128)
        self.assertGreaterEqual(summary["eval_cases"], 134217728)

    def test_goals_plans_skills_are_listed(self):
        evidence = self.proof["evidence"]
        self.assertGreaterEqual(len(evidence["goals_used"]), 5)
        self.assertGreaterEqual(len(evidence["plans_used"]), 4)
        self.assertGreaterEqual(len(evidence["skills_used"]), 8)

        for item in evidence["goals_used"] + evidence["plans_used"] + evidence["skills_used"]:
            self.assertIn("id", item)
            self.assertIn("name", item)
            self.assertIn("explains", item)

    def test_kardashev_rsi_is_recursive_and_bounded(self):
        rsi = self.proof["evidence"]["recursive_self_improvement"]
        self.assertGreaterEqual(rsi["meta_rsi_upgrade_count"], 32)
        self.assertGreater(rsi["synthetic_atlas_index_final"], rsi["synthetic_atlas_index_start"])
        self.assertGreater(rsi["synthetic_kardashev_scenario_index_final"], rsi["synthetic_kardashev_scenario_index_start"])
        self.assertGreater(rsi["selected_patch_count"], 100000)
        self.assertGreaterEqual(rsi["rollback_count"], 1)
        self.assertGreaterEqual(rsi["capital_allocation_event_count"], 128)
        self.assertGreaterEqual(rsi["compute_allocation_event_count"], 128)
        self.assertGreaterEqual(rsi["energy_allocation_event_count"], 128)
        self.assertGreaterEqual(rsi["trust_allocation_event_count"], 128)

    def test_claim_boundary_is_safe(self):
        evidence = self.proof["evidence"]
        guarantees = evidence["sovereignty_guarantees"]
        self.assertFalse(guarantees["private_data_shared"])
        self.assertFalse(guarantees["private_customer_records_shared"])
        self.assertFalse(guarantees["private_financials_shared"])
        self.assertFalse(guarantees["real_world_energy_claim_made"])
        self.assertFalse(guarantees["real_world_kardashev_claim_made"])
        self.assertTrue(guarantees["local_eval_required_before_adoption"])
        self.assertTrue(guarantees["rollback_required_before_release"])
        self.assertIn("guaranteed ROI", evidence["not_claiming"])
        self.assertEqual(evidence["vision_treatment"], "strategic scenario, not empirical claim")

    def test_institutional_graphs_exist(self):
        graphs = self.proof["evidence"]["institutional_graphs"]
        self.assertGreaterEqual(len(graphs["cycle_series"]), 128)
        self.assertGreaterEqual(len(graphs["kardashev_series"]), 128)
        self.assertGreaterEqual(len(graphs["leaderboard"]), 12)
        self.assertGreaterEqual(len(graphs["theater_summary"]), 16)
        self.assertIn("capital", graphs["allocation_tables"])
        self.assertIn("compute", graphs["allocation_tables"])
        self.assertIn("energy", graphs["allocation_tables"])
        self.assertIn("trust", graphs["allocation_tables"])

    def test_each_proof_has_own_page_and_main_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site = root / "site"
            data = root / "data"
            write_site(site, data)

            main = (site / "index.html").read_text(encoding="utf-8")
            self.assertIn("proofs/009-sovereign-kardashev-capital-engine.html", main)

            for slug in [
                "001-sovereign-swarm",
                "002-evolution-tournament",
                "003-recursive-evolution-ladder",
                "004-corporate-rsi-dominion",
                "005-enterprise-rsi-superorganism",
                "006-sovereign-enterprise-constellation",
                "007-sovereign-enterprise-proof-economy",
                "008-sovereign-domain-atlas",
                "009-sovereign-kardashev-capital-engine",
            ]:
                self.assertTrue((site / "proofs" / f"{slug}.html").exists())
                self.assertTrue((site / "assets" / "proofs" / f"{slug}.json").exists())

            proof9 = (site / "proofs" / "009-sovereign-kardashev-capital-engine.html").read_text(encoding="utf-8")
            self.assertIn("../", proof9)
            self.assertIn("Proof Archive", proof9)
            self.assertIn("Capital–Compute–Energy–Trust Flywheel", proof9)
            self.assertIn("Synthetic Kardashev Scenario Index", proof9)
            self.assertIn("GoalOS Artifacts Used", proof9)
            self.assertIn("PlanOS Artifacts Used", proof9)
            self.assertIn("SkillOS Artifacts Used", proof9)


if __name__ == "__main__":
    unittest.main()
