# INTERCEPT Evidence Synthesis: SROI Assessment

*Compiled from scite.ai and academic database searches across 8 priority areas.*

**Search Date:** March 15, 2026
**Status:** All 8 priorities complete.

---

## Overall SROI Signal Summary

| Priority | Topic | Net SROI Direction | Confidence |
|----------|-------|-------------------|------------|
| 1 | A2A agonists in trauma/IRI (preclinical) | ↑↑ P(drug) | High ✅ |
| 2 | IRI drug clinical trial failure rates | ↓↓ P(drug) base rate | Very High |
| 3 | Organ-on-chip predictive validity | ↑↑ P(platform) | High |
| 4 | Trauma mortality timing / therapeutic window | ↑ Addressable DALYs | Very High |
| 5 | IRI mechanism transfer across conditions | ↑↑ P(mechanism validity) | High |
| 6 | Digital twin validation for acute physiology | ↑ P(platform) | Moderate-High |
| 7 | Prehospital drug feasibility | ↑ P(feasibility) | High |
| 8 | Counterfactual funding landscape | ↑ Speed-up estimate | Moderate |

---

## Key Evidence by SROI Component

### P(drug) — Probability of Drug Success

**Lowers P(drug):**
- No IRI cardioprotective drug has ever reached clinical guidelines — zero on market (Priority 2)
- >1,000 stroke neuroprotectants tested in animals; zero translated (Priority 2)
- Only 13% of preclinical cardioprotection datasets are neutral (publication bias) (Priority 2)
- Replication effect sizes ~85% smaller than originally reported (Priority 2)
- CIRCUS (cyclosporine A/mPTP): OR 1.04, p=0.77 in 970-patient NEJM trial (Priority 2)
- CONDI2/ERIC-PPCI (remote ischemic conditioning): HR 1.10, p=0.32 in 5,401 patients (Priority 2)
- Ischemia duration mismatch: animal models use 25–50 min no-flow; patients have 150–250 min low-flow (Priority 2)
- Comorbidity and comedication gap not captured in preclinical models (Priority 2)
- ALM (adenosine-lidocaine-magnesium combination) showed inferior survival vs. standard resuscitation in porcine model (Priority 7)

**Raises P(drug):**
- **Regadenoson: 100% vs. 40% survival at 24h in porcine ECPR model** (Wisniewski 2024, J Surg Res) (Priority 1)
- **ReWiRe Phase 2a trial registered and ethically approved** — regadenoson in human trauma/hemorrhagic shock, Queen Mary University London (Karim Brohi's institution) (Priority 1)
- CGS21680 improves survival in hemorrhagic shock rat model (Zhu 2013) (Priority 1)
- A2aR-KO mice show significantly worsened MOF after hemorrhagic shock — definitive causal proof (Kelestemur 2022) (Priority 1)
- ATL146e: 40% → 100% survival in mouse sepsis; ATL-146e: 65% → 13% lethality in liver injury (Priority 1)
- CGS21680 in DCD liver transplant porcine model: 100% vs. 40% 72h survival (p=0.04) (Priority 1)
- A2AR agonist CGS21680 protective in MI (~21% absolute infarct reduction in rabbit), cerebral ischemia (BDNF/MAPK), and spinal cord injury (Priority 5)
- A2A agonists operate primarily on leukocytes/lymphocytes — distinct from failed cardiomyocyte-intrinsic targets (Priority 5)
- Post-ischemic (reperfusion-phase) A2A activation is cardioprotective — clinically actionable timing (Priority 5)
- Kidney-on-chip: adenosine protects proximal tubule cells against renal IRI (Vormann et al. 2022) (Priority 3)
- **No selective A2A agonist has failed a Phase II/III IRI trial** — the failure prior applies to drugs that have been tried, not this class (Priority 2)
- Trauma/hemorrhagic shock context: shorter ischemic durations, younger patients, fewer comedications than STEMI — potentially more favorable translation (Priority 2)

**Critical caveat — brain IRI:**
- **A2AR ANTAGONISM (not agonism) is neuroprotective in cerebral IRI** (Mohamed 2016) (Priority 1)
- In the brain, adenosine activates A2AR to INDUCE neuronal damage — opposite of peripheral organs
- Patient selection must exclude severe isolated TBI; this is the primary contrasting finding for the A2A agonist program

**Net assessment on P(drug):** The base rate is poor (Priority 2), but Priority 1 evidence substantially updates this upward. Regadenoson is the only FDA-approved A2AR agonist; it has now demonstrated survival benefit in a large-animal shock model, and a Phase 2a human trial is registered at the lead investigator's institution. The leukocyte-mediated anti-inflammatory mechanism, reperfusion-phase timing, and trauma-context advantages distinguish it from all drugs that have failed. The brain-specific reversal of benefit is the single most important contrasting finding and must be addressed by patient selection criteria. Estimated P(drug) for trauma/hemorrhagic shock indication: **25–35%** — materially above the near-zero IRI base rate.

---

### P(platform) — Probability of OoC/Digital Twin Platform Success

**Raises P(platform):**
- Emulate Liver-Chip: 87% sensitivity / 100% specificity for DILI prediction vs. 0% for animals (Priority 3)
- First IND approved on OoC/organoid efficacy data alone (Qureator, 2025) (Priority 3)
- OoC data formally included in FDA IND for COVID-19 drug (Cantex Lung Chip, 2022) (Priority 3)
- FDA ISTAND accepted first OoC submission (Emulate Liver-Chip, September 2024) (Priority 3)
- FDA roadmap to phase out animal testing over 3–5 years (April 2025) (Priority 3)
- Quantitative human PK prediction from linked multi-organ chips confirmed (Herland et al. 2020) (Priority 3)
- Hemorrhagic shock digital twin (ODE model) validated in porcine AND human PROMMTT data; predicted time of death (Nature Comms Medicine, 2024) (Priority 6)
- INSIST stroke in silico trial: population-level predictions quantitatively matched MR CLEAN trial results (Priority 6)
- Hesperos: First digital twin of human disease derived from OoC platform (Priority 6)

**Raises concerns about P(platform):**
- No OoC-specific IRI drug has yet been confirmed to predict a successful human clinical trial outcome (Priority 3)
- Only 12% of studies claiming to be "digital twins" meet NASEM criteria for true DTs (Priority 6)
- Reproducibility and standardization remain barriers to OoC adoption (Priority 3)

**Net assessment on P(platform):** Strongly positive trajectory. The regulatory landscape has shifted dramatically in 5 years. The specific gap is IRI/OoC clinical validation, but mechanistic fidelity is demonstrated (cardiac organoids, kidney chip). The kidney IRI chip adenosine result is the most directly relevant data point.

---

### Addressable DALYs — Scale of the Problem

**Key statistics:**
- ~60,000 annual U.S. deaths from hemorrhagic shock; ~50% before hospital arrival (Priority 4)
- 14% of all trauma fatalities potentially preventable with advanced prehospital care (Priority 4)
- 90.9% of potentially survivable military combat deaths are hemorrhagic (Eastridge 2012) (Priority 4)
- 25–43% of prehospital trauma deaths are potentially preventable (Pfeifer et al. 2019) (Priority 4)
- Median survival time in hemorrhagic shock ~2 hours; 31% die within 2 hrs of ED arrival (Priority 4)
- Every minute delay in resuscitation = +2% odds of 30-day mortality (Priority 4)
- IRI mechanism is shared across trauma, cardiac (500,000+ US MI/year), and stroke (800,000+ US/year) — three-condition DALY pool is large (Priority 5)

**Net assessment on Addressable DALYs:** Very large. The 14% of trauma fatalities (~8,400 US deaths/year) potentially preventable by advanced prehospital care, combined with cardiac and stroke IRI populations, represents a substantial target. The therapeutic window is real (median ~2 hours) and consistent with prehospital pharmacological intervention.

---

### Speed-Up Estimate — Counterfactual Without INTERCEPT

**Key observations:**
- Pharmacological novel prehospital anti-shock drug space is **relatively uncrowded** — primary investment is in devices and blood products (Priority 8)
- No comparable active selective A2A agonist prehospital program identified (Priority 8)
- DARPA Biostasis ($23M): closest conceptual adjacent program; preclinical only, different mechanism (Priority 8)
- CDMRP JWMRP explicitly funds "drugs that extend the physiologic resuscitation window" (Priority 8)
- Civilian prehospital translation of military advances: explicitly identified as a gap (Priority 8)
- TXA precedent: 1g fixed-dose IV prehospital drug can achieve guideline endorsement through properly designed trials (Priority 7)

**Net assessment on Speed-Up:** Moderate positive. The specific A2A agonist prehospital program is not crowded, but the broader trauma/IRI field receives substantial military investment. INTERCEPT would meaningfully accelerate this specific mechanism in civilian prehospital applications. Estimated speed-up: 5–10 years.

---

## Critical Evidence Gaps Identified

1. **No Phase II/III human trial data for selective A2A agonist in IRI** — the most important missing evidence. Priority 1 results (pending) will help assess the preclinical depth.

2. **No OoC IRI drug-to-clinical-outcome prediction** — OoC is validated for toxicology (DILI) and PK, but not yet for IRI drug efficacy prediction. The kidney chip adenosine result is promising but not yet clinically validated.

3. **Trauma-specific A2A agonist human safety data absent** — regadenoson (FDA-approved A2A agonist for cardiac stress testing) provides some human safety context, but trauma/hemorrhagic shock specific PK/PD is unknown.

4. **Translation from trauma-focused animal models to the comorbid patient population** — the "comorbidity gap" (Priority 2) that has killed other IRI drugs must be explicitly addressed. The OoC platform is the primary tool for this.

---

## Evidence Interpretation Guide (Applied)

| Evidence Type | Finding | SROI Impact |
|--------------|---------|------------|
| A2A agonists show efficacy in trauma models (Priority 1 & 5) | **Confirmed** — regadenoson 100% vs. 40% survival (ECPR); CGS21680 improves survival in HS; A2aR-KO worsens MOF; Phase 2a trial registered | P(drug) ↑↑ |
| IRI drugs consistently fail in Phase 2/3 (Priority 2) | **Confirmed** — every IRI drug that reached Phase III has failed | P(drug) ↓ |
| OoC has predicted human outcomes (Priority 3) | **Confirmed** — DILI prediction; PK prediction; one IND approved on OoC data | P(platform) ↑ |
| No OoC-to-clinic translation precedent for IRI | **Confirmed gap** — mechanistic work exists but no clinical validation | P(platform) ↓ (partial) |
| Large fraction of trauma deaths occur >30 min post-injury | **Confirmed** — median survival ~2 hrs; 31% die within 2 hrs of ED | Addressable DALYs ↑ |
| Most deaths are immediate (<10min) | **Partially confirmed** — ~50% immediate but compression to bimodal means early window still large | Addressable DALYs ~ |
| Active DARPA/military programs in this space | **Confirmed** — but in devices/blood products, not novel pharmacology | Speed-up ↓ (partial) |
| Field neglected for novel prehospital drugs | **Partially confirmed** — specific A2A agonist niche is open | Speed-up ↑ |

---

## Recommended Next Research Steps

1. **ReWiRe trial results**: Identify the outcome of the Phase 2a dose-finding trial (Queen Mary University London, REC 19/LO/0329). If published, this is the single highest-value piece of evidence for updating P(drug).

2. **Regadenoson human safety data in hemorrhagic shock**: Review PK/PD and adverse event profile specifically in hypotensive/hemorrhaging patients — vasodilatory effects of regadenoson could be a concern in already-hypotensive trauma patients.

3. **Comorbidity-specific OoC experiment design**: Design the kidney and cardiac OoC experiments specifically with diabetic/hypertensive cell conditions to address the comorbidity gap.

4. **CDMRP JWMRP application**: The "drugs that extend the physiologic resuscitation window" focus area is a direct match. Explore FY2025 solicitation.

5. **Military partner identification**: The USAISR Blood & Shock Resuscitation division and THOR network (Remote Damage Control Resuscitation) are the most aligned DoD collaborators.
