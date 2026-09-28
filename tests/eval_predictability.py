"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitPerformanceRev.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.okr_attainment_scorer import *
from tools.feedback_bias_detector import *
from tools.rating_distribution_calibrator import *

class TestGitPerformanceRevPredictability(unittest.TestCase):

    def test_okr_attainment_scorer(self):
        res = score_okr_attainment('[{"weight": 1.0, "completion_pct": 80}, {"weight": 1.0, "completion_pct": 85}]')
        self.assertEqual(res["performance_tier"], "MEETS")
        self.assertEqual(res["status"], "OKR_MEETS")

    def test_feedback_bias_detector(self):
        res = detect_feedback_bias("The employee delivers strong engineering results on schedule.")
        self.assertFalse(res["bias_detected"])
        self.assertEqual(res["status"], "NEUTRAL_FEEDBACK")

    def test_rating_distribution_calibrator(self):
        res = calibrate_ratings('{"top_tier_count": 4, "total_employees": 25}')
        self.assertTrue(res["calibrated"])
        self.assertEqual(res["status"], "DISTRIBUTION_CALIBRATED")


if __name__ == "__main__":
    unittest.main()
