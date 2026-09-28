# Segregation of Duties (SOD) Policy: GitPerformanceRev

This document establishes the role boundaries and segregation of duties for the GitPerformanceRev agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring performance calibration rubrics, configuring linguistic bias dictionaries, and preparing automated appraisal diffs.
This role cannot approve or merge its own changes into protected talent management branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming performance ratings, OKR attainments, and narrative bias flags.
This role operates as an impartial auditor to verify compliance with enterprise HR benchmarks and equal employment guidelines.

### 3. Approver
The Approver role is strictly reserved for human Chief People Officers and Performance Calibration Committee members.
Human approval is required for all final promotion approvals, rating certifications, and calibration exception overrides.
