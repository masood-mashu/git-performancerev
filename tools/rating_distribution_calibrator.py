"""
rating_distribution_calibrator.py - Audits departmental performance rating curve to ensure top tier does not exceed 20.0%
"""
import sys
import json


def calibrate_ratings(ratings_json: str, max_top_tier_pct: float = 20.0):
    import json
    data = json.loads(ratings_json) if isinstance(ratings_json, str) else ratings_json
    top = data.get("top_tier_count", 5)
    total = max(data.get("total_employees", 30), 1)
    pct = (top / total) * 100.0
    calibrated = pct <= max_top_tier_pct
    return {
        "top_tier_count": top,
        "total_employees": total,
        "top_tier_pct": round(pct, 1),
        "calibrated": calibrated,
        "status": "DISTRIBUTION_CALIBRATED" if calibrated else "TOP_TIER_INFLATION_DETECTED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "rating-distribution-calibrator"}))
