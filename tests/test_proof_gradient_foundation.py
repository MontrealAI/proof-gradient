import unittest

from proof_gradient.models import run_customer_response_demo


class ProofGradientFoundationTest(unittest.TestCase):
    def setUp(self):
        self.demo = run_customer_response_demo()

    def test_four_system_artifacts_exist(self):
        artifact_types = {artifact["artifact_type"] for artifact in self.demo["artifacts"]}
        self.assertIn("goal", artifact_types)
        self.assertIn("plan", artifact_types)
        self.assertIn("skill", artifact_types)
        self.assertIn("tool", artifact_types)
        self.assertIn("policy", artifact_types)
        self.assertIn("eval", artifact_types)

    def test_run_contract_resolves_versions(self):
        contract = self.demo["run_contract"]
        self.assertEqual(contract["direction"], "customer_response_goal@1.2.0")
        self.assertEqual(contract["strategy"], "customer_response_plan@1.4.0")
        self.assertIn("claim_verification_skill@1.8.0", contract["capabilities"])

    def test_proof_contains_trace_events(self):
        proof = self.demo["proof"]
        event_types = [event["event_type"] for event in proof["trace_events"]]
        self.assertIn("job_received", event_types)
        self.assertIn("eval_failed", event_types)
        self.assertIn("selection_canary_approved", event_types)

    def test_score_assigns_credit(self):
        score = self.demo["score"]
        self.assertTrue(score["passed"])
        self.assertEqual(score["credit_assignment"]["primary_failure"], "plan")
        self.assertIn("plan_patch:add_policy_grounding_before_draft", score["credit_assignment"]["recommended_patches"])

    def test_patch_has_rollback_target(self):
        patch = self.demo["patch"]
        self.assertEqual(patch["patch_type"], "plan_patch")
        self.assertEqual(patch["rollback_target"], "customer_response_plan@1.4.0")

    def test_selection_gate_canary(self):
        selection = self.demo["selection"]
        self.assertEqual(selection["decision"], "approve_canary")
        self.assertEqual(selection["rollout_percentage"], 10)
        self.assertEqual(selection["rollback_target"], "customer_response_plan@1.4.0")


if __name__ == "__main__":
    unittest.main()
