# INTERCEPT — Cost-Effectiveness Analysis
### Karim Brohi Portfolio | Open Philanthropy Evaluation | March 2026

This folder contains the full evidence base and quantitative cost-effectiveness analysis for **INTERCEPT** — a program developing prehospital A2A receptor agonist therapy (regadenoson) for trauma/haemorrhagic shock and ischemia-reperfusion injury (IRI), anchored by an organ-on-chip (OoC) and digital twin validation platform.

---

## Bottom Line

> **Verdict: Marginal case. Plausible but requires favourable assumptions on multiple parameters.**

| Metric | Value |
|--------|-------|
| Median ROI | **1,871×** |
| Mean ROI | 3,382× |
| P(ROI > 2,100×) | **46%** ← Open Philanthropy threshold |
| P(ROI > 1,000×) | 69% |
| P(ROI > 5,000×) | 20% |
| E[P(overall success)] | ~11% |

The Moderate scenario (synthesis midpoint assumptions) clears the 2,100× bar; the Conservative scenario does not. Median ROI sits below the threshold, making this a coin-flip investment at current evidence quality.

---

## Simulation Overview

The analysis uses a **100,000-run Monte Carlo simulation** ([`intercept_monte_carlo.py`](intercept_monte_carlo.py)) implementing a staged, multiplicative probability model. Six corrections were applied relative to the v1 baseline:

### v2 Corrections

| # | Correction | Net Effect on ROI |
|---|-----------|------------------|
| 1 | **Attribution fraction** β(3,4): mode 40%, mean 43% — ReWiRe trial already registered before INTERCEPT, so full credit is inappropriate | ↓ large |
| 2 | **Staged drug funding**: P(Phase3 funded) × P(Phase3 success) × P(adoption) replaces a single-block estimate | clarifies structure |
| 3 | **Portfolio effect**: P(≥1 of n leads succeeds) = 1−(1−p)^n — E[n_leads] ≈ 1.8, boosts P(drug) by ~50% | ↑ partial offset |
| 4 | **HIC/LMIC split**: separate lognormal distributions for high-income and low-income country addressable DALYs, reflecting different deployment feasibility | clarifies structure |
| 5 | **Time discounting**: discount factor = (1+r)^−T; E[factor] ≈ 0.65 | ↓ moderate |
| 6 | **VOI guidance**: expert interview priorities derived from sensitivity analysis | qualitative |

Net effect: P(>2,100×) moves from 74% (v1, no attribution or discounting) to **46% (v2)**.

---

## Model Architecture

### Workflow Diagram

![Workflow diagram showing all variable dependencies](intercept_workflow.png)

All 13 sampled inputs flow left-to-right through first-level intermediates (annual addressable DALYs, per-lead drug probability, discount factor), second-level intermediates (portfolio probability, overall success probability), the DALY chain, and the final ROI node.

### ROI Formula

```
ROI = (discounted_DALYs × DALY_value × attribution) / rd_cost

where:
  annual_addressable  = HIC_arm + LMIC_arm
  p_drug_per_lead     = P(Phase3_funded) × P(Phase3_success) × P(adoption)
  p_drug_portfolio    = 1 − (1 − p_drug_per_lead) ^ n_leads
  p_success           = P(platform) × p_drug_portfolio
  expected_DALYs      = annual_addressable × acceleration_years × p_success
  discount_factor     = (1 + r) ^ (−T)
  discounted_DALYs    = expected_DALYs × discount_factor
```

### Input Distributions

| Parameter | Distribution | Mode / Mean | Rationale |
|-----------|-------------|-------------|-----------|
| HIC addressable DALYs | LogNormal(ln 5M, σ=0.45) | ~5M/yr | Bimodal trauma mortality; >30 min treatable window |
| LMIC addressable DALYs | LogNormal(ln 3.5M, σ=0.60) | ~3.5M/yr | IRI burden minus practical deployment constraints |
| P(OoC platform validates A2A) | Beta(7,4) | mean 64% | Kidney chip adenosine result; proven DILI OoC precedent |
| P(Phase 3 funded \| Phase 2a+) | Beta(7,3) | mean 70% | ARIA/CDMRP appetite; niche uncrowded vs BAU |
| P(Phase 3 success \| funded) | Beta(2,6) | mean 25% | IRI failure base rate (CIRCUS, CONDI2, AMISTAD-II) |
| P(adoption \| approval) | Beta(6,4) | mean 60% | TXA precedent; NAEMSP/ACEP/ACS-COT 2024 uptake |
| N viable leads | Discrete [1–5] | mode 1, mean 1.8 | Regadenoson primary + pipeline candidates |
| Attribution fraction | Beta(3,4) | mode 40%, mean 43% | ReWiRe pre-registered; BAU counterfactual |
| Acceleration vs BAU (years) | Triangular(2, 7, 15) | mode 7 yr | INTERCEPT platform speed-up estimate |
| Discount rate | Triangular(1%, 3%, 5%) | mode 3% | Standard philanthropic rate range |
| Time to impact | Triangular(8, 14, 22 yr) | mode 14 yr | Phase 2a → 3 → approval → deployment |
| R&D cost | Triangular($40M, $60M, $120M) | mode $60M | DARPA Biostasis ($23M) benchmark + Phase 3 budget |
| DALY value | Triangular($50k, $100k, $150k) | mode $100k | OpenPhil benchmark |

### Probability Decomposition

```
E[P(platform validates A2A)]:      63.6%
E[P(Phase 3 funded | 2a+)]:        69.9%
E[P(Phase 3 success | funded)]:    25.0%
E[P(adoption | approval)]:         60.0%
─────────────────────────────────────────
E[P(drug success per lead)]:        10.5%
E[n viable leads]:                  1.79
E[P(portfolio ≥1 lead succeeds)]:   17.0%
E[P(overall success)]:              10.8%
```

> ⚠ **Calibration flag:** The stage-product E[P(drug/lead)] ≈ 10% sits below the holistic synthesis estimate of 25–35%. The decomposition reveals that the synthesis estimate requires above-average performance on *all* stages simultaneously. The staged model is more conservative and transparent.

---

## Results

### Distribution of Outcomes

![Monte Carlo results 3×3 panel](intercept_monte_carlo.png)

The 3×3 panel shows: ROI distribution (log scale), P(success) decomposition, sensitivity tornado chart, scenario comparison, Pareto frontier, and correction-factor contributions (attribution and discounting).

### Scenario Analysis

| Scenario | Ann. DALYs | P(success) | Accel | Attribution | Disc. Factor | ROI | Pass |
|----------|-----------|-----------|-------|------------|-------------|-----|------|
| Platform fails / BAU | 6.0M | 4% | 2 yr | 15% | 0.59 | 65× | ✗ |
| Conservative | 7.5M | 9% | 5 yr | 30% | 0.64 | 1,000× | ✗ |
| **Moderate** | **8.5M** | **17%** | **7 yr** | **43%** | **0.66** | **4,108×** | **✓** |
| Optimistic | 11.0M | 22% | 8 yr | 58% | 0.70 | 12,116× | ✓ |
| Transformative | 15.0M | 33% | 10 yr | 70% | 0.74 | 36,833× | ✓ |

**Key finding:** With attribution and discounting applied, the Conservative scenario fails the 2,100× threshold. Clearing the bar requires at least Moderate assumptions on every dimension simultaneously.

### Pareto Frontier

![Pareto frontier: P(success) vs annual DALYs](intercept_pareto_frontier.png)

Shows which combinations of P(success) and annual addressable DALYs reach the 2,100× threshold under realistic attribution (~43%) and discounting (~0.65 factor). Reference scenario points are plotted.

---

## Sensitivity Analysis

Top drivers of ROI variance (Pearson r with final ROI, 100k simulations):

| Rank | Parameter | Direction | \|r\| |
|------|-----------|-----------|------|
| 1 | **P(Phase 3 RCT success \| funded + OoC)** | ↑ | 0.390 |
| 2 | N viable leads (portfolio effect) | ↑ | 0.331 |
| 3 | Counterfactual attribution fraction | ↑ | 0.296 |
| 4 | Acceleration vs BAU (years) | ↑ | 0.245 |
| 5 | LMIC addressable DALYs | ↑ | 0.200 |
| 6 | HIC addressable DALYs | ↑ | 0.198 |
| 7 | R&D cost | ↓ | 0.167 |
| 8 | P(guideline adoption \| approval) | ↑ | 0.165 |
| 9 | P(OoC/DT platform validates A2A) | ↑ | 0.162 |
| 10 | DALY value | ↑ | 0.152 |

Phase 3 success probability is the dominant uncertainty by a clear margin.

---

## Expert Interview Priorities (Value of Information)

### 1. IRI pharmacologist / independent ReWiRe trialist
_Targets: P(Phase 3 success) — highest sensitivity driver (r = +0.39)_
- Is regadenoson safe in hypotensive patients? (primary vasodilatory risk in shock)
- What is the realistic Phase 2a success criterion and current enrolment status?
- Does OoC comorbidity modelling change Phase 3 design confidence?

### 2. ARIA / CDMRP / funding landscape expert
_Targets: attribution fraction (r = +0.30) and acceleration years (r = +0.25) — same expert conversation_
- Would CDMRP JWMRP fund a Phase 3 if ReWiRe Phase 2a is positive, without INTERCEPT?
- What is the realistic counterfactual — would another funder act within 5 years?
- What is ARIA's appetite for this niche without the OoC platform?

---

## Critical Risk Factors

1. **Regadenoson vasodilatory safety in hypotension** — primary Phase 2a risk. ReWiRe (REC 19/LO/0329) results are the single highest-value upcoming data event.
2. **IRI Phase 3 failure base rate** — CIRCUS, CONDI2, AMISTAD-II all failed. A2A agonists are untested at Phase 3 and are not immune to translational failure.
3. **Attribution** — ReWiRe is already registered without INTERCEPT. If ARIA/CDMRP would fund Phase 3 independently, INTERCEPT's marginal SROI is sharply reduced.
4. **LMIC deployment bottleneck** — cold chain, IV administration, and EMS access constrain the large LMIC DALY burden from being practically addressable at scale.
5. **OoC-to-IRI validation gap** — DILI prediction from OoC is proven; IRI drug efficacy prediction is not yet clinically validated. Kidney chip adenosine result is promising but early-stage.
6. **Brain IRI caveat** — Mohamed 2016 shows A2A receptor *antagonism* (not agonism) is neuroprotective in cerebral IRI, limiting the programme's applicability to non-cerebral IRI.

---

## Evidence Files

| File | Priority | Topic |
|------|----------|-------|
| [priority-1-a2a-receptor-trauma.md](priority-1-a2a-receptor-trauma.md) | 1 (Highest VOI) | Lead asset: A2A agonists in trauma/IRI |
| [priority-2-iri-drug-failure.md](priority-2-iri-drug-failure.md) | 2 | IRI drug development track record |
| [priority-3-organ-on-chip.md](priority-3-organ-on-chip.md) | 3 | Organ-on-chip translation validity |
| [priority-4-trauma-timing.md](priority-4-trauma-timing.md) | 4 | Timing window and addressable mortality |
| [priority-5-mechanism-transfer.md](priority-5-mechanism-transfer.md) | 5 | IRI mechanism transfer across conditions |
| [priority-6-digital-twin.md](priority-6-digital-twin.md) | 6 | Digital twin validation evidence |
| [priority-7-prehospital-drugs.md](priority-7-prehospital-drugs.md) | 7 | Prehospital drug feasibility (TXA precedent) |
| [priority-8-funding-landscape.md](priority-8-funding-landscape.md) | 8 | Counterfactual research landscape |
| [synthesis.md](synthesis.md) | — | Overall synthesis and SROI implications |

---

## Output Files

| File | Description |
|------|-------------|
| [`intercept_monte_carlo.py`](intercept_monte_carlo.py) | Full simulation script (v2, 13-parameter, 100k runs) |
| [`intercept_monte_carlo.png`](intercept_monte_carlo.png) | 3×3 results panel |
| [`intercept_pareto_frontier.png`](intercept_pareto_frontier.png) | Threshold analysis: P(success) vs annual DALYs |
| [`intercept_workflow.png`](intercept_workflow.png) | Variable dependency DAG |
| [`intercept_analysis_report.txt`](intercept_analysis_report.txt) | Full text report (regenerated on each run) |

---

## Running the Simulation

```bash
pip install numpy matplotlib scipy -q
python intercept_monte_carlo.py
```

Outputs are written to the same directory. Runtime ~10–15 seconds for 100,000 iterations.

---

## Scite.ai MCP Connector Setup

The scite.ai MCP connector is configured in `.mcp.json` at the project root. To activate:

```bash
export SCITE_API_KEY="your-scite-api-key"
```

Once activated, use the `search_literature` tool to run citation searches directly against the scite.ai API.

---

*Analysis: March 2026 | Model: v2 (6-correction) | Simulations: 100,000*
