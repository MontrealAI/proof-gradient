import unittest
from pathlib import Path
import tempfile

from proof_gradient.proof_archive import build_archive, write_site


class ProofArchiveTest(unittest.TestCase):
    def test_archive_has_three_connected_proofs(self):
        archive = build_archive()
        self.assertEqual(archive["proof_count"], 3)
        self.assertEqual(
            archive["proof_archive_verdict"],
            "each_proof_has_separate_webpage_and_all_pages_are_connected_to_main",
        )

        slugs = {proof["slug"] for proof in archive["proofs"]}
        self.assertIn("001-sovereign-swarm", slugs)
        self.assertIn("002-evolution-tournament", slugs)
        self.assertIn("003-recursive-evolution-ladder", slugs)

    def test_four_systems_are_present(self):
        archive = build_archive()
        promises = {system["name"]: system["promise"] for system in archive["systems"]}
        self.assertEqual(promises["Artifact Vault"], "stores reusable intelligence")
        self.assertEqual(promises["Run Fabric"], "executes agents at scale")
        self.assertEqual(promises["Proof Ledger"], "records what happened")
        self.assertEqual(promises["Selection Gate"], "promotes only what proved itself")

    def test_recursive_evolution_ladder(self):
        archive = build_archive()
        proof = next(p for p in archive["proofs"] if p["slug"] == "003-recursive-evolution-ladder")
        evidence = proof["evidence"]

        self.assertEqual(evidence["verdict"], "recursive_evolution_proven_with_selection_rejection_and_rollback")
        self.assertEqual(evidence["generation_count"], 5)
        self.assertGreaterEqual(evidence["total_eval_cases"], 300)
        self.assertEqual(evidence["rollback_count"], 1)
        self.assertEqual(evidence["rejected_generations"], 1)
        self.assertGreater(evidence["final_score"], evidence["starting_score"])

    def test_site_has_separate_pages_and_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            site = root / "site"
            data = root / "data"
            write_site(site, data)

            main = (site / "index.html").read_text(encoding="utf-8")
            proofs_index = (site / "proofs" / "index.html").read_text(encoding="utf-8")

            for slug in [
                "001-sovereign-swarm",
                "002-evolution-tournament",
                "003-recursive-evolution-ladder",
            ]:
                self.assertTrue((site / "proofs" / f"{slug}.html").exists())
                self.assertTrue((site / "assets" / "proofs" / f"{slug}.json").exists())
                self.assertIn(f"proofs/{slug}.html", main)
                self.assertIn(f"{slug}.html", proofs_index)

            proof3 = (site / "proofs" / "003-recursive-evolution-ladder.html").read_text(encoding="utf-8")
            self.assertIn("../", proof3)
            self.assertIn("Proof Archive", proof3)


if __name__ == "__main__":
    unittest.main()
