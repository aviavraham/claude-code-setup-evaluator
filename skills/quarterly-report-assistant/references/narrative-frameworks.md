# Narrative Refinement Frameworks

For each top achievement, write THREE narrative versions using different frameworks, then choose the best fit.

## Framework 1: Business Impact Style

Transform technical description to emphasize:
- WHAT problem this solves for customers/users
- HOW this enables business objectives
- WHO benefits (team, customers, enterprise)
- WHY this matters strategically

Example:
```
Raw: "Add Windows BYOH provisioning support to step-registry"
Context: "37 files, +666 lines, 17 days, Phase 1 BYOH support"

Refined:
"I delivered Phase 1 BYOH (Bring Your Own Host) provisioning support to Prow CI,
establishing foundational infrastructure that enables all future BYOH testing for
the Windows QE team. This was strategic infrastructure investment spanning 37 files
(+666 lines) over 17 days. I used a phased rollout strategy, starting with Azure
IPI and vSphere to de-risk deployment before expanding to other platforms. This
work is now running in production and directly enables Q2 Phase 2 work (WINC-1837)."
```

## Framework 2: Technical Depth Style

Transform to emphasize:
- WHAT technical challenges were solved
- HOW you approached the problem (architecture, design decisions)
- Technical complexity and scope (lines changed, files affected)
- Engineering rigor (testing, validation, production deployment)

Example:
```
Raw: "Create Go templates and resource generators"
Context: "22 files changed, +1280/-1257 lines, 7 days, consolidates 23 YAMLs → 3 templates"

Refined:
"I architected consolidation of 23 static YAML test files into 3 parameterized Go
templates (+1,280/-1,257 lines), building 11 resource code generators for
programmatic generation. The net +23 lines (after deleting 1,257) demonstrates
massive complexity reduction. Created single source of truth eliminating copy-paste
errors and enabling future OTE migration. This is technical debt reduction done right -
investing in architectural improvements that pay long-term dividends."
```

## Framework 3: Leadership Style

Transform to emphasize:
- HOW you influenced outcomes beyond individual contribution
- WHAT decisions you made and why
- WHO you helped or unblocked
- Strategic thinking and judgment calls

Example:
```
Raw: "Add vSphere proxy test"
Context: "9 files, +187 lines, 6 days, strategic pivot from AWS to vSphere"

Refined:
"I investigated AWS proxy configuration, discovered a bootstrap limitation where
Windows nodes can't reach external resources through proxy during initial setup
(before WMCO configures them), and made a strategic pivot to vSphere platform where
proxy works correctly. Rather than forcing a broken approach, I documented the
decision-making process in the PR description and leveraged proven patterns from
existing vsphere-proxy-e2e-operator job. Filled coverage gap in 6 days with working
solution, demonstrating engineering judgment and knowledge sharing."
```

## Choosing the Best Style

Not all achievements fit the same narrative style:
- Infrastructure/foundational work → business_impact or technical_depth
- Problem-solving with pivots → leadership
- Large refactors → technical_depth
- Customer-facing features → business_impact

## Key Principles

1. Answer WHAT, HOW, and WHY
2. Weave technical details into impact narrative
3. Use first person ("I delivered", "I architected")
4. Focus on decision-making and strategic thinking
5. Quantify where possible (X files, Y days, Z releases)

## Report Structure

### Section 1: Top Accomplishments - WHAT and HOW

For each of the top 5 achievements:
- Write 2-4 paragraphs per achievement
- Lead with the refined narrative
- Include technical details (files changed, cycle time)
- Explain HOW you accomplished it (phased rollout, architecture decisions)
- Show WHY it matters (enables Q2 work, fills coverage gap, team impact)

Example structure for one achievement:

```markdown
### 1. Built Foundational BYOH Infrastructure (PR #73920)

**WHAT I Accomplished:**
- Delivered Phase 1 BYOH provisioning support to Prow CI
- Scope: 37 files changed, +666 lines
- Duration: 17 days (2026-01-24 → 2026-02-10)
- Related Jira: WINC-1473

**HOW I Accomplished It:**
- Phased rollout strategy - Started with Azure IPI and vSphere to de-risk
- Step-registry integration - Integrated terraform-windows-provisioner
- Reusable components - Built provision/deprovision chains
- Production deployment - Successfully deployed and running

**Impact:**
- Foundation for Q2 work - Enables WINC-1837 (Phase 2)
- Team capability expansion - Windows QE can now test BYOH scenarios
- Risk-managed rollout - Phased approach prevented disruptions

**Why This Matters:**
This is strategic infrastructure investment - not fixing a bug, but building
foundational capability that multiplies team testing capacity.
```

### Section 2: By The Numbers

Include a summary table:

```markdown
| Metric | Q1 2026 Achievement |
|--------|---------------------|
| GitHub PRs Merged | 93 |
| Jira Issues Filed | 58 |
| Jira Issues Closed | 41 (70.7% closure rate) |
| Release Branches Supported | 5 (4.18-4.22) |
| Average Cycle Time (Jira) | 24 days |
| Average Cycle Time (GitHub) | 15 days |
```

### Section 3: How I Work - Key Themes

Analyze patterns across the top achievements:
- Strategic decision-making (pivots, phased rollouts)
- Fast iteration (cycle times, delivery speed)
- Multi-release thinking (backports, broad impact)
- Production mindset (deployed and running)
- Infrastructure over features (foundational capability building)

## Writing Style

**Conversational, not structured:**
- Write in first person ("I delivered", "I architected")
- Answer WHAT, HOW, WHY naturally in narrative flow
- Focus on decision-making and strategic thinking, not just activity

**Impact over activity:**
- "Enabled comprehensive Windows testing for enterprise customers" > "Merged 25 PRs"
- "Filled vSphere proxy coverage gap with strategic pivot" > "Added test job"
- "60% reduction in manual triage time" > "Built dashboard"

**Quantify where possible:**
- Cycle times (17 days, 8 days)
- Scope (37 files, +666 lines)
- Impact (5 releases, 60% time savings, 93 PRs)
- Team benefit ("Windows QE can now test BYOH scenarios")
