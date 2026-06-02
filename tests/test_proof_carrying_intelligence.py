import unittest
from pathlib import Path
import tempfile

from proof_gradient.proof_carrying_intelligence import build_archive, write_site


class ProofCarryingIntelligenceTest(unittest.TestCase):
    def setUp(self):
        self.archive = build_archive()
        self.proof = next(p for p in self.archive["proofs"] if p["slug"] == "010-proof-carrying-intelligence")

    def test_archive_has_ten_separate_proofs(self):
        self.assertEqual(self.archive["proof_count"], 10)
        slugs = {proof["slug"] for proof in self.archive["proofs"]}
        self.assertIn("010-proof-carrying-intelligence", slugs)

    def test_protocol_is_simple_and_canonical(self):
        evidence = self.proof["evidence"]
        self.assertEqual(evidence["protocol"], "Commit → Execute → Prove → Evolve")

        primitives = [primitive["name"] for primitive in evidence["protocol_primitives"]]
        self.assertEqual(primitives, ["Commit", "Execute", "Prove", "Evolve"])

    def test_four_systems_are_present(self):
        systems = {system["name"]: system["promise"] for system in self.proof["evidence"]["systems"]}
        self.assertEqual(systems["Artifact Vault"], "stores reusable intelligence")
        self.assertEqual(systems["Execution Fabric"], "executes agents at scale")
        self.assertEqual(systems["Proof Ledger"], "records what happened")
        self.assertEqual(systems["Evolution Gate"], "promotes only what proved itself")

    def test_scale_is_substantial(self):
        summary = self.proof["summary"]
        self.assertGreaterEqual(summary["agents"], 4194304)
        self.assertGreaterEqual(summary["sovereign_domains"], 2048)
        self.assertGreaterEqual(summary["rsi_cycles"], 256)
        self.assertGreaterEqual(summary["eval_cases"], 1073741824)
        self.assertGreaterEqual(summary["commits"], 524288)
        self.assertGreaterEqual(summary["proofs"], 524288)

    def test_goals_plans_skills_policies_evals_are_listed(self):
        summary = self.proof["summary"]
        self.assertGreaterEqual(summary["goals_used"], 4)
        self.assertGreaterEqual(summary["plans_used"], 4)
        self.assertGreaterEqual(summary["skills_used"], 8)
        self.assertGreaterEqual(summary["policies_used"], 3)
        self.assertGreaterEqual(summary["evals_used"], 4)

    def test_evolution_gate_and_rollbacks(self):
        evidence = self.proof["evidence"]
        self.assertEqual(evidence["evolution_gate"]["decision"], "approve_proof_carrying_intelligence_canary")
        self.assertGreater(evidence["evolution_gate"]["selected_upgrade_count"], 500000)
        self.assertGreater(evidence["evolution_gate"]["rollback_count"], 1)
        self.assertTrue(evidence["sovereignty_guarantees"]["rollback_required_before_release"])

    def test_claim_boundary_is_safe(self):
        evidence = self.proof["evidence"]
        self.assertEqual(evidence["vision_treatment"], "strategic scenario, not empirical claim")
        self.assertIn("guaranteed ROI", evidence["not_claiming"])
        self.assertFalse(evidence["sovereignty_guarantees"]["private_data_shared"])
        self.assertFalse(evidence["sovereignty_guarantees"]["real_world_energy_claim_made"])
        self.assertFalse(evidence["sovereignty_guarantees"]["real_world_kardashev_claim_made"])

    def test_each_proof_has_own_page_and_main_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site = root / "site"
            data = root / "data"
            write_site(site, data)

            main = (site / "index.html").read_text(encoding="utf-8")
            self.assertIn("proofs/010-proof-carrying-intelligence.html", main)

            for number in range(1, 11):
                matching = [p for p in self.archive["proofs"] if p["number"] == number]
                self.assertEqual(len(matching), 1)
                slug = matching[0]["slug"]
                self.assertTrue((site / "proofs" / f"{slug}.html").exists())
                self.assertTrue((site / "assets" / "proofs" / f"{slug}.json").exists())

            page = (site / "proofs" / "010-proof-carrying-intelligence.html").read_text(encoding="utf-8")
            self.assertIn("../", page)
            self.assertIn("Proof Archive", page)
            self.assertIn("Agent Evolution Protocol", page)
            self.assertIn("Commit → Execute → Prove → Evolve", page)
            self.assertIn("GoalOS / Aim Artifacts Used", page)
            self.assertIn("PlanOS / Strategy Artifacts Used", page)
            self.assertIn("SkillOS / Capability Artifacts Used", page)
            self.assertIn("Evolution Gate Funnel", page)
            self.assertIn("Claim-Boundary Ledger", page)


if __name__ == "__main__":
    unittest.main()
