# Scout Report Template

Use this template to generate consistent scout reports.

---

```markdown
# MasterClass Scout Report — {{DATE}}

## Executive Summary

**Roster Status**: {{TOTAL_AGENTS}} agents ({{PERSPECTIVE_COUNT}} perspective + {{DOMAIN_COUNT}} domain + {{MEDIATOR_COUNT}} mediator + {{ARBITER_COUNT}} arbiter + {{CUSTOM_COUNT}} custom)

**Critical Gaps**: {{GAP_LIST}}

**Top Recommendation**: {{TOP_CANDIDATE}} — {{ONE_LINE_RATIONALE}}

---

## Current Coverage Analysis

### Coverage by Domain

| Domain | Agents | Status |
|--------|--------|--------|
| Finance & Investment | {{FINANCE_AGENTS}} | {{FINANCE_STATUS}} |
| Product & Design | {{PRODUCT_AGENTS}} | {{PRODUCT_STATUS}} |
| Writing & Communication | {{WRITING_AGENTS}} | {{WRITING_STATUS}} |
| Marketing & Growth | {{MARKETING_AGENTS}} | {{MARKETING_STATUS}} |
| Technology & AI | {{TECH_AGENTS}} | {{TECH_STATUS}} |
| Leadership & Operations | {{OPS_AGENTS}} | {{OPS_STATUS}} |
| Strategy & Disruption | {{STRATEGY_AGENTS}} | {{STRATEGY_STATUS}} |
| Defense & Security | {{DEFENSE_AGENTS}} | {{DEFENSE_STATUS}} |
| Entrepreneurship | {{ENTREP_AGENTS}} | {{ENTREP_STATUS}} |
| Physical & Performance | {{PHYSICAL_AGENTS}} | {{PHYSICAL_STATUS}} |
| Emotional Intelligence | {{EI_AGENTS}} | {{EI_STATUS}} |
| Culinary & Craft | {{CRAFT_AGENTS}} | {{CRAFT_STATUS}} |
| Creative Performance | {{CREATIVE_AGENTS}} | {{CREATIVE_STATUS}} |
| Health & Wellness | {{WELLNESS_AGENTS}} | {{WELLNESS_STATUS}} |

### Gaps Identified

#### 🔴 Critical (Zero Coverage)
{{#each CRITICAL_GAPS}}
- **{{NAME}}**: {{DESCRIPTION}}
{{/each}}

#### 🟡 Partial (Single Agent)
{{#each PARTIAL_GAPS}}
- **{{NAME}}**: Currently only {{CURRENT_AGENT}}. Gap in {{MISSING_ASPECT}}.
{{/each}}

#### 🟢 Well Covered
{{#each COVERED_DOMAINS}}
- **{{NAME}}**: {{AGENTS_LIST}}
{{/each}}

---

## Top 3 Candidates

### 🥇 Candidate 1: {{CANDIDATE_1_NAME}}

| Attribute | Value |
|-----------|-------|
| **MasterClass Course** | {{C1_COURSE}} |
| **Proposed Domain** | {{C1_DOMAIN}} |
| **Gap Filled** | {{C1_GAP}} |
| **Total Score** | **{{C1_SCORE}}/100** |

#### Scoring Breakdown

| Criterion | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| Domain Gap Fill | 40% | {{C1_GAP_SCORE}} | {{C1_GAP_WEIGHTED}} |
| Distinctiveness | 25% | {{C1_DISTINCT_SCORE}} | {{C1_DISTINCT_WEIGHTED}} |
| Profile Buildability | 20% | {{C1_BUILD_SCORE}} | {{C1_BUILD_WEIGHTED}} |
| User Relevance | 15% | {{C1_RELEVANCE_SCORE}} | {{C1_RELEVANCE_WEIGHTED}} |

#### Why This Candidate

{{C1_RATIONALE}}

#### Source Material Available

- [{{C1_BOOKS_CHECK}}] Published books
- [{{C1_INTERVIEWS_CHECK}}] Extended interviews/podcasts
- [{{C1_SPEECHES_CHECK}}] Speeches/keynotes
- [{{C1_DECISIONS_CHECK}}] Documented decisions
- [{{C1_MC_CHECK}}] MasterClass content

#### Preview: Core Principles

1. "{{C1_PRINCIPLE_1}}"
2. "{{C1_PRINCIPLE_2}}"
3. "{{C1_PRINCIPLE_3}}"

---

### 🥈 Candidate 2: {{CANDIDATE_2_NAME}}

[Same structure as Candidate 1]

---

### 🥉 Candidate 3: {{CANDIDATE_3_NAME}}

[Same structure as Candidate 1]

---

## Comparison Matrix

| Criterion | {{C1_NAME}} | {{C2_NAME}} | {{C3_NAME}} |
|-----------|-------------|-------------|-------------|
| Gap Fill | {{C1_GAP_SCORE}} | {{C2_GAP_SCORE}} | {{C3_GAP_SCORE}} |
| Distinctiveness | {{C1_DISTINCT_SCORE}} | {{C2_DISTINCT_SCORE}} | {{C3_DISTINCT_SCORE}} |
| Buildability | {{C1_BUILD_SCORE}} | {{C2_BUILD_SCORE}} | {{C3_BUILD_SCORE}} |
| Relevance | {{C1_RELEVANCE_SCORE}} | {{C2_RELEVANCE_SCORE}} | {{C3_RELEVANCE_SCORE}} |
| **Total** | **{{C1_SCORE}}** | **{{C2_SCORE}}** | **{{C3_SCORE}}** |

---

## Recommendation Priority

| Priority | Candidate | Rationale | Effort |
|----------|-----------|-----------|--------|
| 🥇 **Build First** | {{C1_NAME}} | {{C1_PRIORITY_RATIONALE}} | {{C1_EFFORT}} |
| 🥈 **Build Second** | {{C2_NAME}} | {{C2_PRIORITY_RATIONALE}} | {{C2_EFFORT}} |
| 🥉 **Consider** | {{C3_NAME}} | {{C3_PRIORITY_RATIONALE}} | {{C3_EFFORT}} |

---

## Rejected Candidates

| Instructor | Reason for Rejection |
|------------|---------------------|
{{#each REJECTED}}
| {{NAME}} | {{REASON}} |
{{/each}}

---

## Next Steps

### To Build a Candidate Profile

```
/add-agent {{RECOMMENDED_NAME}}: {{RECOMMENDED_DOMAIN}} expert known for {{RECOMMENDED_SPECIALTY}}
```

### To Request Full Research

```
"Build a complete agent profile for {{RECOMMENDED_NAME}} with deep research"
```

### To Defer Decision

```
"Save this scout report and remind me next week"
```

---

## Appendix: Scoring Methodology

### Domain Gap Fill (40%)
- 100: Fills domain with zero current agents
- 80: Fills domain with only one agent (enables debate)
- 50: Adds meaningful depth to partially covered domain
- 20: Adds redundant coverage to well-covered domain

### Distinctiveness (25%)
- 100: Completely novel perspective, frameworks, and voice
- 75: Different angle within similar domain
- 50: Moderate overlap with existing agent
- 25: High overlap, limited incremental value

### Profile Buildability (20%)
- 100: Extensive books, interviews, speeches, documented decisions
- 75: Good source material, some gaps
- 50: Moderate material, will require inference
- 25: Limited public material, difficult to build authentic voice

### User Relevance (15%)
Based on alignment with user's stated domains:
- Defense consulting
- AI advisory
- Strategy
- Entrepreneurship
- Business development

---

*Report Generated: {{TIMESTAMP}}*
*Scout Version: 1.0*
*Next Scheduled Scan: {{NEXT_SCAN_DATE}}*
```

---

## Usage Notes

1. Replace all `{{VARIABLE}}` placeholders with actual data
2. Use checkboxes `[x]` for available, `[ ]` for unavailable source material
3. Keep scoring consistent across candidates
4. Include at least 3 rejected candidates for context
5. Save completed report to: `scout-reports/{{DATE}}-scout-report.md`
