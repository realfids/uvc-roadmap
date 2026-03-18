# Priority 2: IRI Drug Development Track Record

*Base rate for P(success) — how often do IRI drugs fail in translation?*

**Search Date:** March 15, 2026
**Queries:** IRI clinical trial failure/negative results, IRI translational failure preclinical, cardioprotection clinical trial no benefit

---

## SROI Signal

| Finding | Impact |
|---------|--------|
| Every IRI drug reaching Phase III cardiac trials has failed — zero on market | P(drug) ↓↓ |
| >1,000 stroke neuroprotectants tested in animals; 0 translated to humans | P(drug) ↓↓ |
| Only 13% of preclinical cardioprotection datasets are neutral (publication bias) | P(drug) ↓ (prior estimates inflated) |
| Replication effect sizes are ~85% smaller than original reported effects | P(drug) ↓ |
| Preclinical ischemia duration (25–50 min) ≠ clinical (150–250 min) — mechanistic mismatch | P(drug) ↓ |
| No comorbidities/comedications in animal models vs. real patients | P(drug) ↓ |
| CIRCUS (cyclosporine A, mPTP target): OR 1.04, p=0.77 in 970 patients (NEJM 2015) | P(drug) ↓ |
| CONDI2/ERIC-PPCI (remote ischemic conditioning): HR 1.10, p=0.32 in 5,401 patients | P(drug) ↓ |
| A2A agonists have NOT been tested in a Phase II/III IRI trial — novel mechanism | P(drug) ~ (unproven, but no failed trial either) |

---

## Section 1: The Scale of the Problem

IRI cardioprotection represents **one of the most thoroughly documented translational failures in modern medicine.** The core finding is stark:

> **No drug or mechanical cardioprotective strategy targeting IRI has successfully reached clinical guidelines** — despite decades of promising preclinical data.

### Aggregate Statistics

| Metric | Value |
|--------|-------|
| Overall drug pipeline failure rate (Phase I → approval) | ~90% |
| Stroke neuroprotectants tested in animals | >1,000 |
| Stroke drugs across ~150 clinical trials | >200 |
| Successful stroke neuroprotection translations | **0** (rtPA is thrombolysis, not neuroprotection) |
| Cardioprotective IRI drugs on market | **0** |
| Preclinical cardioprotection datasets that are neutral | **13%** (Basic Research in Cardiology, 2024) |
| Replication effect size vs. original reported | **85% smaller** on average |

---

## Section 2: Landmark Review Articles

### Paper 1: "Cardioprotection and Myocardial Reperfusion: Pitfalls to Clinical Application"
- **Authors:** Vander Heide RS & Steenbergen C
- **Journal:** Circulation Research, 2013 | **PMID:** 23908333
- **[PMC3824252](https://pmc.ncbi.nlm.nih.gov/articles/PMC3824252/)**
- Key quote: "Most has been conducted in rodent models which may not be directly applicable to human disease and even promising agents have been disappointing in large-scale clinical trials."
- Five primary barriers: patient heterogeneity, prolonged clinical ischemia duration, pre-existing medications and comorbidities, genetic polymorphisms, limited salvageable myocardium
- **Adenosine case study:** AMISTAD (236 patients) showed 33% relative infarct size reduction (p=0.03) → AMISTAD-II (2,118 patients) showed no significant clinical outcomes improvement
- **NHE inhibitor case study:** ESCAMI (959 patients) — no infarct size reduction; EXPEDITION (5,761 patients) — reduced MI incidence but increased cerebrovascular accidents, negating mortality benefit

---

### Paper 2: "Critical Issues for the Translation of Cardioprotection" ⭐ Landmark
- **Author:** Heusch G
- **Journal:** Circulation Research, 2017 | **PMID:** [28450365](https://pubmed.ncbi.nlm.nih.gov/28450365/)
- Key quote: "The translation from numerous successful animal experiments on cardioprotection beyond that by reperfusion to clinical practice has to date been disappointing."
- Three domains of failure: (1) experimental model limitations, (2) conceptual gaps, (3) grave faults in clinical trial design
- Critical flaw: animal experiments use "young and healthy animals which lack the risk factors, comorbidities, and comedications which are characteristics of patients suffering AMI"
- Criticizes "lack of adequate phase II dosing and timing studies when rushing from promising proof-of-concept trials to larger clinical outcome trials"

---

### Paper 3: "Cardioprotection — New Paradigms or New Pragmatism?" (Heusch, 2023)
- **PMID:** [37259502](https://pubmed.ncbi.nlm.nih.gov/37259502/)
- Key quote: "None of the successful initial preclinical attempts of infarct size reduction translated into clinical practice, except for timely reperfusion."
- Critical barrier: current STEMI trial mortality is so low (<3% at 1 year in CONDI2/ERIC-PPCI) that further reduction by any adjunct cardioprotective intervention may be **statistically impossible**
- Identifies coronary microcirculation (not just cardiomyocytes) as an underexplored target

---

### Paper 4: "Comorbidities and Comedications With IRI and Cardioprotection" ⭐ Comprehensive
- **Authors:** Ferdinandy P, Andreadou I, Baxter GF, Bøtker HE, Davidson SM, Dobrev D, Gersh BJ, Heusch G, et al. (13 co-authors)
- **Journal:** Pharmacological Reviews, 2023 (January) — 57-page flagship article
- **PMID:** [36753049](https://pubmed.ncbi.nlm.nih.gov/36753049/)
- Key quote: "While many signaling pathways leading to endogenous cardioprotection have been elucidated in experimental studies over the past 30 years, **no cardioprotective drug is on the market yet for that indication.**"
- **"Comorbidity gap":** Most preclinical studies use animals without comorbidities; real patients have hypertension, hyperlipidemia, diabetes, atherosclerosis — all of which **abrogate** cardioprotective signaling
- Comedications that abrogate cardioprotection: statins, beta-blockers, metformin, GLP-1 agonists, SGLT2 inhibitors, heparin, aspirin, P2Y12 inhibitors, nitroglycerine, opioids, benzodiazepines, propofol

---

### Paper 5: Meta-Analysis of Anti-Inflammatory Compounds in Large Animal Models (Van Hout et al., 2016)
- **Journal:** Cardiovascular Research | **PMID:** [26487693](https://pubmed.ncbi.nlm.nih.gov/26487693/)
- **183 large animal studies, 3,331 animals**
- Anti-inflammatory drugs: infarct size reduction **12.7%** (95% CI: 11.1–14.4%) as area-at-risk ratio
- Despite consistent large animal positive results: translation to clinical practice "has proved to be difficult"
- Key finding: investigator blinding correlated with **higher mortality in treated groups** — unblinded studies overestimate benefit
- Moderating variables explaining translational failure: timing of outcome assessment, sex (male-only studies exaggerated effect sizes), study quality

---

### Paper 6: "The Search for a Clinically Effective Cardioprotective Therapy" (Wang et al., Cells 2023)
- **[PMC10217104](https://pmc.ncbi.nlm.nih.gov/articles/PMC10217104/)**
- Fundamental mechanistic mismatch: preclinical models use **no-flow ischemia (25–50 min)** vs. clinical **low-flow ischemia (150–250 min)** — mechanistically different injuries
- Specific failures: volatile anesthetics (no clinical evidence despite "very convincing" experimental findings); xenon (only small troponin differences in 492-patient trial); colchicine NLRP3 inhibition (no cardioprotection despite inflammatory marker improvements)
- Improved preclinical screening could potentially identify ~**70% of cardiac toxicities** observed in clinical trials

---

### Paper 7: Stroke IRI — "Everything Works in Animals, But Nothing Works in People"
- **PMID:** [23353570](https://pubmed.ncbi.nlm.nih.gov/23353570/) | **[PMC3638705](https://pmc.ncbi.nlm.nih.gov/articles/PMC3638705/)**
- >1,000 candidate neuroprotective drugs tested in animals; **not one found to benefit humans with stroke**
- >200 drugs across ~150 clinical trials — all failed
- NXY-059 case study: positive in rats AND primates; SAINT-I showed reduced disability; SAINT-II failed → withdrawn
- The one success: rtPA approved 1996 (thrombolysis, not neuroprotection per se)

---

## Section 3: Landmark Failed Clinical Trials

### Trial 1: CIRCUS — Cyclosporine A (NEJM 2015) ⭐ Most Prominent Recent Failure
- **Citation:** Cung TT et al., NEJM 2015;373:1021
- **Design:** International, double-blinded, placebo-controlled RCT; 42 hospitals; n=970
- **Mechanism targeted:** mPTP inhibition (the same "common end-effector" of IRI across all organ systems)
- **Prior signal:** Piot et al. pilot study appeared positive
- **Results:** Primary outcome 59.0% (cyclosporine) vs. 58.1% (control); OR 1.04; **p=0.77** — no benefit
- **No adverse LV remodeling prevention at 1 year**
- Proposed failure reasons: formulation change (Sandimmune → CicloMulsion), longer ischemic time in larger trial, increased use of newer antiplatelet agents

---

### Trial 2: CONDI-2/ERIC-PPCI — Remote Ischemic Conditioning (Lancet 2019)
- **Citation:** Hausenloy DJ et al., Lancet 2019;394:1415–1424 | **PMID:** [31500849](https://pubmed.ncbi.nlm.nih.gov/31500849/)
- **Design:** International single-blind RCT; 33 centers; **n=5,401**
- **Mechanism:** Four cycles of arm cuff inflation/deflation before PPCI (systemic neurohormonal preconditioning)
- **Results:** Cardiac death or HF hospitalization at 12 months: 9.4% vs. 8.6%; HR 1.10 (95% CI 0.91–1.32); **p=0.32** — no benefit
- **Lancet editorial title:** "The broken promise of remote ischaemic conditioning"
- Despite multiple earlier smaller trials showing infarct size reduction — no clinical outcome benefit in adequately powered trial

---

### Trial 3: AMISTAD-II — Adenosine in STEMI
- **Design:** 2,118-patient RCT (vs. positive pilot AMISTAD: 236 patients, 33% relative infarct size reduction, p=0.03)
- **Results:** No significant improvement in clinical outcomes (CHF, rehospitalization, or death at 6 months)
- Classic example: positive small trial, negative large definitive trial
- **Note:** Adenosine (non-selective) is distinct from selective A2A receptor agonists — mechanism comparison required

---

### Trial 4: EXPEDITION — Cariporide (NHE Inhibitor), n=5,761
- Reduced MI incidence (p=0.000005) but **increased cerebrovascular accidents** — net harm → abandoned

### Trial 5: ESCAMI — Eniporide (NHE Inhibitor), n=959
- No significant infarct size reduction

---

## Section 4: The "Valley of Death" — Root Causes

### Paper: "Lost in translation: the valley of death" (Springer Nature, 2019)
- **[Link](https://link.springer.com/article/10.1186/s41231-019-0050-7)**
- 90% failure rate for drugs entering Phase I to final approval
- Replication effect sizes **85% smaller** than original reported effect sizes
- Key culprits: poor hypotheses, irreproducible data, ambiguous preclinical models, statistical errors, publication bias, lack of transparency

### Publication Bias (Basic Research in Cardiology, 2024)
- 269 cardioprotection papers analyzed (2013–2023) from top three journals
- Only 26/269 papers applied prospective power analysis
- **Only 13% of all analyzed data sets were neutral** — strongly indicating systematic underreporting of null results

---

## Section 5: Complete Drug Failure Table

| Drug/Intervention | Mechanism | Key Trial | Outcome |
|-------------------|-----------|-----------|---------|
| Cyclosporine A | mPTP inhibitor | CIRCUS (NEJM 2015) | No benefit (OR 1.04, p=0.77) |
| Remote ischemic conditioning | Neurohormonal preconditioning | CONDI2/ERIC-PPCI (Lancet 2019) | No benefit (HR 1.10, p=0.32) |
| Local postconditioning | Mechanical IPC at reperfusion | POST trial | No benefit |
| Adenosine (non-selective) | Purinergic signaling | AMISTAD-II (2,118 pts) | No clinical benefit |
| Cariporide | NHE-1 inhibitor | EXPEDITION (5,761 pts) | Excess stroke, net harm |
| Eniporide | NHE-1 inhibitor | ESCAMI (959 pts) | No benefit |
| TRO40303 | Mitochondrial target | Phase II | No benefit |
| MTP-131 (Elamipretide) | Mitochondrial oxidative stress | Phase II/III | Failed |
| Volatile anesthetics | Metabolic preconditioning | Multiple large RCTs | No clinical evidence |
| Xenon | Noble gas preconditioning | 492-patient trial | Only small troponin difference |
| Colchicine | NLRP3 inflammasome inhibitor | RCTs | No cardioprotection |
| IV sodium nitrite | NO donor | RCTs | No sufficient evidence |
| Nicorandil | K-ATP opener | RCTs | No sufficient evidence |
| Delcasertib | PKC-δ inhibitor | Phase II | No benefit |
| NXY-059 (stroke) | Free radical scavenger | SAINT-I/II | SAINT-I positive, SAINT-II failed |
| **Selective A2A agonists** | **A2A receptor agonist** | **No Phase II/III trial completed** | **Untested at scale — novel** |

---

## Section 6: Why Preclinical Models Fail — Synthesized Root Causes

1. **Animal model mismatch:** Rodent hearts have higher heart rates, different electrophysiology, and coronary anatomy vs. humans; genetic homogeneity vs. human diversity
2. **Comorbidity gap:** Young, healthy animals vs. patients with diabetes, hypertension, dyslipidemia, atherosclerosis — all of which abrogate cardioprotective signaling
3. **Comedication confounding:** Statins, beta-blockers, metformin, P2Y12 inhibitors, opioids all independently alter IRI mechanisms — not modeled preclinically
4. **Ischemia duration mismatch:** No-flow ischemia 25–50 min (animal) vs. low-flow ischemia 150–250 min (clinical) — mechanistically different injuries
5. **Publication bias:** 13% neutral datasets reported; 85% effect size shrinkage on replication
6. **Trial design failures:** Insufficient Phase II dosing/timing; inadequate patient selection; surrogate endpoints (infarct size by CMR) vs. clinical outcomes
7. **Low baseline event rates:** Modern STEMI mortality <3% at 1 year makes demonstrating additional benefit statistically near-impossible
8. **Pathway redundancy:** Blocking one cell death pathway insufficient; alternative mechanisms continue

---

## Implications for INTERCEPT / A2A Agonist Program

The base rate for IRI drug translation is **extremely poor**. This is the single most important prior probability adjustment for the INTERCEPT SROI. However, several features distinguish a selective A2A agonist program:

1. **Untested mechanism:** No selective A2A agonist has failed a Phase II/III IRI trial — the failure prior applies to drugs that have been tried, not to this class specifically
2. **Leukocyte-mediated mechanism:** A2AR protection operates primarily on leukocytes/lymphocytes (Circulation 2005, A2AAR-KO study) — not cardiomyocyte-intrinsic survival signaling, which is where most failures have occurred
3. **Post-ischemic timing:** A2A agonists work at reperfusion (the clinically deliverable window), addressing the timing mismatch critique
4. **Trauma context differs:** The trauma/hemorrhagic shock setting has shorter ischemic durations, younger healthier patients, and fewer comedications than STEMI — potentially a more favorable translation context
5. **OoC platform advantage:** The organ-on-chip platform addresses the comorbidity gap and comedication confounding by enabling human-cell-based testing with patient-specific conditions

**SROI implication:** The IRI drug failure base rate significantly **lowers P(drug)**, but the A2A mechanism has specific features that partially mitigate the worst aspects of the translational failure pattern. The OoC platform is specifically valuable as a tool to de-risk translation before large clinical trials.

---

## Sources

- [Vander Heide & Steenbergen, Circ Res 2013 (PMC3824252)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3824252/)
- [Heusch, Circ Res 2017 (PMID 28450365)](https://pubmed.ncbi.nlm.nih.gov/28450365/)
- [Heusch, J Cardiovasc Pharmacol Ther 2023 (PMID 37259502)](https://pubmed.ncbi.nlm.nih.gov/37259502/)
- [Ferdinandy et al., Pharmacol Rev 2023 (PMID 36753049)](https://pubmed.ncbi.nlm.nih.gov/36753049/)
- [Van Hout et al., Cardiovasc Res 2016 (PMID 26487693)](https://pubmed.ncbi.nlm.nih.gov/26487693/)
- [Wang et al., Cells 2023 (PMC10217104)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10217104/)
- [Altamirano et al., J Physiol 2015 (PMC4575567)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4575567/)
- [Stroke neuroprotection failure (PMC3638705, 2013)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3638705/)
- [CIRCUS Trial, Cung et al., NEJM 2015](https://pubmed.ncbi.nlm.nih.gov/26321103/)
- [CONDI-2/ERIC-PPCI, Hausenloy et al., Lancet 2019 (PMID 31500849)](https://pubmed.ncbi.nlm.nih.gov/31500849/)
- [Valley of death review (Springer Nature, 2019)](https://link.springer.com/article/10.1186/s41231-019-0050-7)
- [Publication bias in cardioprotection (Basic Research in Cardiology, 2024)](https://link.springer.com/article/10.1007/s00395-024-01050-4)
- [Multitarget Strategies for Myocardial IRI (JACC Review, 2019)](https://www.jacc.org/doi/10.1016/j.jacc.2018.09.086)
