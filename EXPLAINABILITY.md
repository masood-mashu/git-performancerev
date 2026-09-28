# GitPerformanceRev Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitPerformanceRev** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitPerformanceRev consumes quarterly employee self-appraisals, peer feedback narratives, manager performance ratings, and documented OKR metric records. These data sources include goal completion percentages, key result milestone logs, narrative review feedback paragraphs, and calibration rating tiers. The agent ingests these inputs in raw JSON, text, and HRIS export format and parses them into standardized talent performance objects for downstream calibration analysis. Departmental rating historical archives and language bias dictionaries are also monitored as sensitive data sources to ensure fair evaluation is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When an employee performance cycle is evaluated, the agent first calculates goal achievement using the okr-attainment-scorer tool to verify that ratings align with empirical objective progress. Next, the reasoning engine invokes the feedback-bias-detector tool to scan review text for gendered or subjective language patterns. Furthermore, department rating distributions are audited using the rating-distribution-calibrator tool to prevent grade inflation. Finally, the agent correlates all evaluation metrics against predefined people standards to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated calibration memo.

---

## 3. Constraints, Limitations, and Known Issues

GitPerformanceRev operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitPerformanceRev operates under strict operational constraints to prevent unfair evaluations and subjective bias across corporate talent reviews. The agent is deliberately limited to statistical distribution calibration and linguistic bias scanning and cannot evaluate intangible leadership presence or in-person team dynamics. Another known issue and limitation is that highly technical individual contributor roles with bespoke experimental projects may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
