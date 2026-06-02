import unittest

from proof_gradient.foundation import build_foundation


class ProofGradientFoundationTest(unittest.TestCase):
    def setUp(self):
        self.foundation = build_foundation()
        self.demo = self.foundation["demo"]

    def test_four_promises_are_explicit(self):
        promises = {system["name"]: system["promise"] for system in self.foundation["systems"]}
        self.assertEqual(promises["Artifact Vault"], "stores reusable intelligence")
        self.assertEqual(promises["Run Fabric"], "executes agents at scale")
        self.assertEqual(promises["Proof Ledger"], "records what happened")
        self.assertEqual(promises["Selection Gate"], "promotes only what proved itself")

    def test_artifact_vault_stores_reusable_intelligence(self):
        artifact_types = {artifact["artifact_type"] for artifact in self.demo["artifacts"]}
        self.assertIn("goal", artifact_types)
        self.assertIn("plan", artifact_types)
        self.assertIn("skill", artifact_types)
        self.assertIn("policy", artifact_types)
        self.assertIn("eval", artifact_types)
        self.assertIn("context_recipe", artifact_types)

    def test_run_fabric_executes_large_multi_agent_swarm(self):
        swarm = self.demo["swarm"]
        self.assertGreaterEqual(swarm["agent_count"], 64)
        self.assertGreaterEqual(swarm["division_count"], 8)
        self.assertGreaterEqual(swarm["handoff_count"], 63)
        self.assertEqual(swarm["coordination_verdict"], "large_multi_agent_coordination_proven_deterministically")

    def test_proof_ledger_records_what_happened(self):
        proof = self.demo["proof"]
        self.assertGreaterEqual(len(proof["trace_events"]), 64)
        self.assertEqual(proof["output"]["claim_status"], "strategic_scenario_not_empirical_claim")
        self.assertIn("large deterministic multi-agent coordination", proof["output"]["current_repository_proves"])

    def test_selection_gate_promotes_only_what_proved_itself(self):
        score = self.demo["score"]
        selection = self.demo["selection"]
        self.assertTrue(score["passed"])
        self.assertEqual(selection["decision"], "approve_canary")
        self.assertEqual(selection["rollout_percentage"], 10)
        self.assertEqual(selection["rollback_target"], "sovereign_swarm_plan@1.0.0")

    def test_kardashev_claim_is_scenario_not_false_fact(self):
        thesis = self.foundation["civilization_scale_thesis"]
        self.assertEqual(thesis["treatment"], "strategic scenario, not empirical claim")
        self.assertEqual(thesis["status"], "scenario_lab_active")


if __name__ == "__main__":
    unittest.main()
