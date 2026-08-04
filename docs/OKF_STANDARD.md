# Open Knowledge Format (OKF) Standard Guide

## 1. Specification Overview
The Open Knowledge Format (OKF) organizes knowledge into standardized Markdown files paired with structured YAML frontmatter metadata.

## 2. File Format Structure

```markdown
---
id: "okf:market:ai_micro_saas_2026"
type: "MarketOpportunity"
title: "AI Micro-SaaS API Opportunity"
created_at: "2026-08-03T19:15:00Z"
updated_at: "2026-08-03T19:15:00Z"
confidence_score: 0.92
status: "ACTIVE"
tags:
  - saas
  - api
  - automation
relations:
  - target_id: "okf:strategy:subscription_api"
    relationship_type: "COMPATIBLE_WITH"
  - target_id: "okf:product:content_gen_api"
    relationship_type: "SPAWNED_PRODUCT"
---

# AI Micro-SaaS API Opportunity

## Context & Narrative
Analysis of developer demands shows high interest in automated micro-APIs for structured text generation.

## Key Metrics
- Projected ROI: 340%
- Implementation Complexity: Medium
- Estimated Time to Revenue: 48 Hours
```

## 3. Benefits of OKF for Agentic Systems
- Direct compatibility with version control (Git).
- Human readability for auditing and debugging.
- Machine readability for LLM prompt context injection and automated graph building.
