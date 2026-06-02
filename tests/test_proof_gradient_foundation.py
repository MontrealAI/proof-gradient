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

    def test_artifact_vault_contains_reusable_intelligence(self):
        artifact_types = {artifact["artifact_type"] for artifact in self.demo["artifacts"]}
        self.assertIn("goal", artifact_types)
        self.assertIn("plan", artifact_types)
        self.assertIn("skill", artifact_types)
        self.assertIn("tool", artifact_types)
        self.assertIn("policy", artifact_types)
        self.assertIn("eval", artifact_types)

    def test_run_fabric_resolves_artifacts(self):
        contract = self.demo["run_contract"]
        self.assertEqual(contract["direction"], "customer_response_goal@1.2.0")
        self.assertEqual(contract["strategy"], "customer_response_plan@1.4.0")
        self.assertIn("claim_verification_skill@1.8.0", contract["capabilities"])

    def test_proof_ledger_records_what_happened(self):
        event_types = [event["event_type"] for event in self.demo["proof"]["trace_events"]]
        self.assertIn("job_received", event_types)
        self.assertIn("artifacts_resolved", event_types)
        self.assertIn("eval_failed", event_types)
        self.assertIn("credit_assigned", event_types)
        self.assertIn("patch_proposed", event_types)

    def test_selection_gate_promotes_only_what_proved_itself(self):
        score = self.demo["score"]
        selection = self.demo["selection"]
        self.assertTrue(score["passed"])
        self.assertEqual(selection["decision"], "approve_canary")
        self.assertEqual(selection["rollout_percentage"], 10)
        self.assertEqual(selection["rollback_target"], "customer_response_plan@1.4.0")

    def test_patch_is_proof_backed_and_rollbackable(self):
        patch = self.demo["patch"]
        self.assertEqual(patch["patch_type"], "plan_patch")
        self.assertEqual(patch["source_proof"], "proof_customer_refund_001")
        self.assertEqual(patch["rollback_target"], "customer_response_plan@1.4.0")


if __name__ == "__main__":
    unittest.main()
