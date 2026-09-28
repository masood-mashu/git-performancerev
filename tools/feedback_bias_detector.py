"""
feedback_bias_detector.py - Detects subjective gendered or biased adjectives in performance review text
"""
import sys
import json


def detect_feedback_bias(feedback_text: str):
    BIASED_WORDS = ["abrasive", "bossy", "emotional", "aggressive", "irrational", "hysterical"]
    text_lower = feedback_text.lower()
    found = [w for w in BIASED_WORDS if w in text_lower]
    has_bias = len(found) > 0
    return {
        "flagged_adjectives": found,
        "bias_detected": has_bias,
        "action": "REVISE_FEEDBACK_LANGUAGE" if has_bias else "LANGUAGE_CLEARED",
        "status": "BIAS_FLAGGED" if has_bias else "NEUTRAL_FEEDBACK"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "feedback-bias-detector"}))
