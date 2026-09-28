"""
okr_attainment_scorer.py - Calculates composite OKR attainment percentage across weighted key result milestones
"""
import sys
import json


def score_okr_attainment(okr_data_json: str):
    import json
    goals = json.loads(okr_data_json) if isinstance(okr_data_json, str) else okr_data_json
    weighted_sum = sum(g.get("weight", 1.0) * g.get("completion_pct", 100.0) for g in goals)
    total_weight = max(sum(g.get("weight", 1.0) for g in goals), 1.0)
    score = weighted_sum / total_weight
    tier = "EXCEEDS" if score >= 90 else ("MEETS" if score >= 70 else "NEEDS_IMPROVEMENT")
    return {
        "attainment_pct": round(score, 1),
        "performance_tier": tier,
        "status": f"OKR_{tier}"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "okr-attainment-scorer"}))
