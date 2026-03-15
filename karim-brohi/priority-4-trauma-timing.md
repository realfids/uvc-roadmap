# Priority 4: Trauma Mortality Timing and Therapeutic Windows

*What fraction of trauma deaths occur in a treatable window? Updates addressable DALYs.*

**Search Date:** March 15, 2026
**Queries executed:**
- Query 4.1: "prehospital mortality" AND trauma AND ("time to death" OR "survival time" OR "golden hour")
- Query 4.2: "hemorrhagic shock" AND ("therapeutic window" OR "time-sensitive" OR "intervention timing")
- Query 4.3: trauma AND mortality AND ("preventable death" OR "potentially survivable") AND prehospital
- Additional: "trimodal trauma death distribution"; "preventable trauma death percentage prehospital"

---

## SROI Signal

| Finding | Impact |
|---------|--------|
| Median survival in hemorrhagic shock ~2 hours | Addressable DALYs ↑ (window exists) |
| 31% of shock patients die within 2 hrs of ED arrival | Addressable DALYs ↑ |
| 25–43% of prehospital trauma deaths are potentially preventable | Addressable DALYs ↑ |
| 90.9% of preventable military deaths are hemorrhagic | P(drug target validity) ↑ |
| "Golden hour" effect only proven for intermediate-acuity patients | Addressable DALYs ~ (nuanced) |
| 73% of trauma fatalities are anatomically non-survivable | Addressable DALYs ↓ (limits target population) |

---

## Section 1: The Trimodal Distribution of Trauma Deaths

### Classic Model — Trunkey (1983)

Retrospective autopsy analysis of 425–437 fatalities from northern California counties proposed three temporal death peaks:

| Peak | Timing | Fraction | Causes | Preventable? |
|------|--------|----------|--------|--------------|
| Immediate (1st) | Seconds–minutes at scene | ~50% | Massive CNS trauma, aortic transection, catastrophic hemorrhage | No — unsurvivable |
| Early (2nd) | 1–4 hours (ED/OR) | ~30% | Subdural/epidural hematoma, hemopneumothorax, liver/spleen lacerations, pelvic fractures | **Yes — primary target** |
| Late (3rd) | Days–weeks | ~20% | Sepsis, multi-organ failure, post-traumatic immunosuppression | Partially |

### Modern Revision: Bimodal or Single-Peak Distribution

Multiple contemporary studies have found the 3rd peak has largely disappeared in high-income countries with advanced critical care. The relevant implication is that a larger share of mortality is now concentrated in the acute and early windows — which are the same windows targeted by prehospital intervention.

**Paper: "Changing epidemiology of trauma deaths leads to a bimodal distribution"**
- Journal: Annals of Surgery
- Source: PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC2943446/
- Finding: The late peak is no longer detectable in modern trauma systems; mortality concentrated in immediate and early windows

**Paper: "Changes in the temporal distribution of in-hospital mortality in severely injured patients — TraumaRegister DGU"**
- Source: PMC / PLOS One — https://pmc.ncbi.nlm.nih.gov/articles/PMC6386341/
- Finding: German registry data confirms the third peak has largely disappeared; mortality is now concentrated in the immediate and early windows

**Paper: "Mortality after acute trauma: Progressive decreasing rather than a trimodal distribution"**
- Year: 2015
- Source: ScienceDirect — https://www.sciencedirect.com/science/article/pii/S2221618915000311
- Finding: Confirms that modern trauma care has collapsed the classic trimodal pattern into a monotonically decreasing mortality curve

**Paper: "Timing of death after traumatic injury — a contemporary assessment"**
- Source: ScienceDirect — https://www.sciencedirect.com/science/article/abs/pii/S0022480415008707
- Finding: Contemporary data shows mortality after acute trauma follows a progressively decreasing rather than trimodal distribution

**Paper: "Tri-modal Distribution of Trauma Deaths in a Resource-Limited Setting: Perception Versus Reality"**
- Year: 2023
- Source: PubMed — https://pubmed.ncbi.nlm.nih.gov/36939860/
- Finding: The trimodal pattern is still observed in low/middle-income countries where critical care infrastructure is lacking; the 3rd peak remains a target in global health trauma contexts; directly relevant for estimating addressable DALYs in LMICs

**SROI implication:** The compression of mortality into the immediate-to-early window means the survivable fraction may be somewhat smaller than Trunkey's original ~30% estimate, but the window for intervention has also become more clearly defined and shorter. Pharmacologic extension of that window is therefore more, not less, relevant.

---

## Section 2: The Golden Hour — Evidence and Limitations

### 2.1 Papers Supporting Time-Sensitivity

**Paper: "Time is the Enemy: Mortality in Trauma Patients with Hemorrhage from Torso Injury"**
- Authors: Alarhayem et al.
- Journal: The American Journal of Surgery, 2016
- Sources: ScienceDirect — https://www.sciencedirect.com/science/article/abs/pii/S0002961016305542 | STRAC PDF — https://www.strac.org/wp-content/uploads/2024/02/Time_is_the_Enemy.pdf
- Dataset: National Trauma Data Bank 2012–2014; 2,523,394 injured patients; 42,135 adult patients with torso hemorrhage (thorax/abdomen AIS) and prehospital SBP ≤110 mmHg
- Key statistics:
  - Overall mortality in cohort: 7.9% (3,326/42,135)
  - Mortality risk was most pronounced within the first 30 minutes of prehospital time
  - Risk increased monotonically with torso Abbreviated Injury Scale score
  - Prehospital time and torso AIS were strong independent predictors of mortality (p <0.05) across all strata
- Direct quote: "Evacuation times ≤30 min may not be realistic in rural or austere environments, directing future efforts toward therapies to increase the survival window prehospitally"
- SROI implication: This paper directly motivates a prehospital pharmacologic approach — if transport cannot be accelerated, extending the survival window is the primary alternative

**Paper: "Relative Mortality Analysis of the 'Golden Hour': A Comprehensive Acuity Stratification Approach"**
- Year: 2018
- Source: PubMed — https://pubmed.ncbi.nlm.nih.gov/30118362/
- Key finding: Prior studies failed to detect the golden hour effect not because it does not exist, but because they failed to stratify by patient acuity
  - For lowest-acuity patients (PS >91%): prehospital time is irrelevant — likely to survive regardless
  - For highest-acuity patients (PS <23%): prehospital time is also irrelevant — likely to die regardless
  - **For intermediate-acuity patients (PS 23–91%): the golden hour IS significant**
- This intermediate group is large, clinically real, and represents the primary addressable target population

**Paper: "Redefining the Golden Hour for Severe Head Injury in an Urban Setting"**
- Journal: Injury, 2012
- Source: ScienceDirect — https://www.sciencedirect.com/science/article/abs/pii/S0020138312000186
- Key statistics:
  - Hazard ratio 1.002 per minute of prehospital time (95% CI 1.001–1.004, p=0.001)
  - No aggregate survival benefit observed for arrival within 60 minutes (vs. >60 min)
  - Survival benefit specifically observed for arrival within 2 hours
  - Rapid transport specifically beneficial for hypotensive patients and penetrating brain injury

**Paper: "Every Minute Matters in Hemorrhagic Shock" (410 Medical White Paper)**
- Source: https://410medical.com/app/uploads/2023/03/Every-Minute-Matters-in-Hemorrhagic-Shock-White-Paper.pdf
- Key findings:
  - Every 1-minute increase in time to early resuscitative intervention: **+2% increase in odds of 30-day mortality**
  - Every 1-minute increase: **+1.5% increase in odds of 24-hour mortality**

**Paper: "Hemorrhage control and physiologic resuscitation are time-sensitive imperatives in multisystem trauma"**
- Source: AAOS Now, 2025 — https://www.aaos.org/aaosnow/2025/nov/clinical/clinical01/
- Key finding: Combat casualties who received blood products or damage control resuscitation transfer within 1 hour of injury had significantly lower mortality than those receiving care later

**Lamb et al. 2023 systematic review (cited in Biomedicines 2024, Navigating Hemorrhagic Shock):**
- 24 studies, >10,000 patients
- **70% of studies** demonstrated a significant link between delayed hemostatic intervention and increased mortality
- Source: https://www.mdpi.com/2227-9059/12/12/2864

### 2.2 Papers Challenging Universal Application of the Golden Hour

**Paper: "Emergency Medical Services Intervals and Survival in Trauma: Assessment of the 'Golden Hour' in a North American Prospective Cohort"**
- Authors: Newgard et al.
- Source: PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC3008652/
- Dataset: 146 EMS agencies, 10 North American sites, high-risk trauma patients with field physiologic abnormality
- Finding: No statistically significant relationship between out-of-hospital time and mortality across diverse patient populations, trauma systems, regions, and confounders
- Limitation: Did not stratify by patient acuity — the failure to detect the effect is explained by the Relative Mortality Analysis (2018) above

**Paper: "Association between prehospital time and outcome of trauma patients in 4 Asian countries" (Pan-Asia Trauma Outcomes Study — PATOS)**
- Journal: PLOS Medicine, 2020
- Sources: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003360 | PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC7537901/
- Dataset: Multi-national retrospective cohort, January 2016–November 2018
- Key findings:
  - No association between prehospital time and 30-day mortality overall
  - Every 10-minute delay was associated with a **6% increase in odds of poor functional outcome** at discharge
  - Highlights that functional outcome may be a more sensitive endpoint than mortality alone

**Paper: "Does prehospital time affect survival of major trauma patients where there is no prehospital care?"**
- Source: PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC5525481/
- Finding: In-hospital mortality was associated with age, mechanism, shock, GCS <9, ISS ≥16, and need for ventilatory support — but not with prehospital time in this low-resource setting; confounding by absence of formal prehospital care limits interpretation

**Paper: "Prehospital time and mortality in pediatric trauma"**
- Journal: Pediatric Surgery International, 2024
- Source: Springer — https://link.springer.com/article/10.1007/s00383-024-05742-9
- Finding: Non-linear relationship — highest mortality in patients arriving in <30 minutes (reflecting appropriate triage of most critical patients), nadir at 30–45 minutes, then no further association; does not disprove time-sensitivity but shows selection bias in raw prehospital time analysis

### 2.3 Synthesis: What the Golden Hour Evidence Actually Shows

The conflicting literature is largely resolved by three observations:

1. **Acuity stratification is essential.** The golden hour effect disappears in pooled analyses that do not separate by injury severity. It is real and significant for the intermediate-acuity hemorrhagic trauma patient (PS 23–91%).
2. **The threshold is not exactly 60 minutes.** For some patients (severe penetrating torso trauma with hemodynamic instability) the window may close in 30 minutes; for others with slower hemorrhage it may extend beyond 2 hours.
3. **Non-detectability of transport time effects in aggregate studies does not mean time is unimportant.** It means the effect is concentrated in a specific subpopulation. That subpopulation is exactly the one a prehospital pharmacologic intervention would target.

---

## Section 3: Hemorrhagic Shock — Therapeutic Window

### Median Survival Data

**"Traumatic hemorrhage and chain of survival" (PMC10207757)**
- 208 trauma patients with hemorrhagic shock (SBP ≤90 mmHg):
  - 31% died within 2 hours of ED arrival
  - 12% died between 2–24 hours
  - 11% died after 24 hours
  - 46% survived
- Overall mortality from hemorrhage-induced hypotension: **54%**
- **Median time from onset to death: ~2 hours**

**Animal model data:**
- Rat (uncontrolled internal hemorrhage): Average survival time 107 minutes; 12/59 rats died before 120 minutes ([PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0080862))
- Swine continuous hemorrhage: survival modulated by bleed rate (1.0–1.25 ml/kg/min)

### Hemorrhage as a Fraction of All Trauma Deaths

**"Impact of Hemorrhage on Trauma Outcome" — Journal of Trauma 2006 (PubMed 16763478)**
- Hemorrhage responsible for **30–40% of trauma mortality**
- **33–56% of hemorrhage deaths occur in the prehospital period**
- Autopsy review (425 consecutive injury deaths): hemorrhage caused 35.2%

**"Navigating Hemorrhagic Shock" — Biomedicines, December 2024**
- Hemorrhagic shock causes ~**60,000 deaths annually** in the US
- **~50% of deaths happen before hospital arrival**
- [MDPI](https://www.mdpi.com/2227-9059/12/12/2864)

---

## Section 4: Military Data — Eastridge et al. 2012 (Landmark)

**"Death on the Battlefield (2001–2011): Implications for the Future of Combat Casualty Care"**
- Authors: Eastridge et al. | JTACS 2012 (73:S431–S437)
- Dataset: 4,574 combat deaths, 2001–2011
- [PubMed 23192066](https://pubmed.ncbi.nlm.nih.gov/23192066/)

| Metric | Value |
|--------|-------|
| Deaths before reaching medical treatment facility | **87%** |
| Of pre-MTF deaths: non-survivable | 75.7% |
| Of pre-MTF deaths: potentially survivable | **24.3% (n=976)** |
| Of potentially survivable: due to hemorrhage | **90.9%** |
| Lethal hemorrhage site — truncal | 67.3% |
| Lethal hemorrhage site — junctional | 19.2% |
| Lethal hemorrhage site — extremity | 13.5% |

**Eastridge 2019 synthesis:** Hemorrhage implicated in 25–30% of all injury deaths and **>80% of preventable post-injury deaths** in military and civilian settings.

---

## Section 5: Preventable Prehospital Trauma Deaths

**"Are Pre-hospital Trauma Deaths Preventable?" — Pfeifer et al. 2019 (systematic review)**
- 19 papers, 7,235 deaths, published 1990–2018
- Pre-hospital death rate: 14.6–47.6% of all trauma deaths
- **Definitely preventable: 4.9–11.3%**
- **Potentially preventable: 25.8–42.7%**
- Most common causes: delayed treatment (27–58%), management errors (40–60%), treatment errors (50–76.6%)
- [Wiley](https://onlinelibrary.wiley.com/doi/10.1007/s00268-019-05056-1)

**"Early and prehospital trauma deaths: Who might benefit from advanced resuscitative care?" (PubMed 32176169, 2020)**
| Category | Fraction of all trauma fatalities |
|----------|----------------------------------|
| Anatomically non-survivable | 73% |
| Survivable only with hospital care | 9% |
| **Survivable with advanced prehospital care** | **14%** |
| Survivable with basic prehospital care | 4% |

**North America hemorrhage epidemiology (PMC10694464, 2023):**
- 44.9% of hemorrhage deaths: preventable or potentially preventable
- Of those: **35.8% occurred prehospital**
- Additional 20.4% died within 1 hour of ED arrival

**Bystander gap (UK data, PubMed 28262281, 2017):**
- Bystanders present before EMS: 96% of cases
- Bystander intervention of any kind: only **25–30%**

---

## Section 6: Remote Damage Control Resuscitation — Extending the Window

**EMS Tactical Damage Control Resuscitation Protocol (StatPearls/NCBI NBK599525)**
- Remote Damage Control Resuscitation (RDCR), developed by THOR network
- Applied when hospital access is delayed **>60 minutes**
- Includes: hemorrhage control, permissive hypotension, hypothermia prevention, TXA, freeze-dried plasma
- The 60-minute threshold is the clinical consensus on the primary death window for preventable hemorrhagic trauma deaths

---

## Summary Statistics Table

| Metric | Value | Source |
|--------|-------|--------|
| Immediate trauma deaths | ~50% | Trunkey 1983 |
| Early deaths (1–4 hrs) | ~30% | Trunkey 1983 |
| Trauma deaths due to hemorrhage | 30–40% | Eastridge 2019 |
| Hemorrhage deaths occurring prehospital | 33–56% | J Trauma 2006 |
| Preventable/potentially preventable hemorrhage deaths | 45% | Kalkwarf/Eastridge 2019 |
| Of preventable hemorrhage deaths: prehospital | 35.8% | PMC 2023 |
| Die within 1 hr of ED arrival (preventable group) | 20.4% | PMC 2023 |
| Prehospital trauma deaths potentially preventable | 25.8–42.7% | Pfeifer et al. 2019 |
| Military pre-MTF deaths | 87% of all combat deaths | Eastridge 2012 |
| Potentially survivable military deaths from hemorrhage | 90.9% | Eastridge 2012 |
| Median survival time, hemorrhagic shock | ~2 hours | PMC10207757 |
| Shock patients dying within 2 hrs of ED arrival | 31% | PMC10207757 |
| Each minute delay in resuscitation | +2% odds 30-day mortality | 410 Medical WP |
| Studies showing delayed hemostasis increases mortality | 70% of 24 studies | Lamb 2023 |
| Trauma deaths preventable with advanced prehospital care | **14% of all fatalities** | PubMed 2020 |
| US annual hemorrhagic shock deaths | ~60,000 | Biomedicines 2024 |
| Hemorrhage deaths before hospital arrival | ~50% | Biomedicines 2024 |

---

## SROI Interpretation

**Bottom line:** A meaningful and quantifiable fraction of trauma deaths (~14% of all fatalities, ~45% of hemorrhagic deaths) are potentially preventable with advanced prehospital intervention delivered within a ~2-hour window. Hemorrhage is the overwhelmingly dominant preventable mechanism (>80% of preventable deaths). The therapeutic window is real, narrows rapidly, and is consistent with pharmacological intervention via autoinjector or other field-deployable formats. This **strongly supports the addressable DALYs estimate** for a prehospital A2A agonist.

---

## Sources

- [Time is the Enemy — Alarhayem et al., ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0002961016305542)
- [PATOS Study — PLOS Medicine 2020](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003360)
- [EMS Intervals and the Golden Hour — Newgard et al., PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3008652/)
- [Relative Mortality Analysis of the Golden Hour — PubMed 2018](https://pubmed.ncbi.nlm.nih.gov/30118362/)
- [Changing epidemiology: bimodal distribution — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2943446/)
- [TraumaRegister DGU temporal distribution — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6386341/)
- [Trimodal in Resource-Limited Settings — PubMed](https://pubmed.ncbi.nlm.nih.gov/36939860/)
- [Are Pre-hospital Trauma Deaths Preventable? — Pfeifer et al., Wiley](https://onlinelibrary.wiley.com/doi/10.1007/s00268-019-05056-1)
- [Preventable death systematic review — ScienceDirect 2021](https://www.sciencedirect.com/science/article/pii/S0020138321006458)
- [Historical comparison preventable prehospital deaths — ScienceDirect 2017](https://www.sciencedirect.com/science/article/pii/S0020138317300608)
- [Prehospital deaths: survivable injuries, bystanders — PubMed 2017](https://pubmed.ncbi.nlm.nih.gov/28262281/)
- [Early and prehospital trauma deaths: advanced resuscitative care — PubMed 2020](https://pubmed.ncbi.nlm.nih.gov/32176169/)
- [Eastridge et al. 2012: Death on the Battlefield — PubMed](https://pubmed.ncbi.nlm.nih.gov/23192066/)
- [Eastridge et al. 2019: Outcomes of traumatic hemorrhagic shock — Wiley](https://onlinelibrary.wiley.com/doi/full/10.1111/trf.15161)
- [Impact of Hemorrhage on Trauma Outcome — J Trauma 2006](https://journals.lww.com/jtrauma/fulltext/2006/06001/impact_of_hemorrhage_on_trauma_outcome__an.2.aspx)
- [Epidemiology of Trauma-Related Hemorrhage — PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10694464/)
- [Navigating Hemorrhagic Shock — Biomedicines Dec 2024](https://www.mdpi.com/2227-9059/12/12/2864)
- [Traumatic hemorrhage and chain of survival — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10207757/)
- [EMS Tactical Damage Control Resuscitation — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK599525/)
- [Every Minute Matters in Hemorrhagic Shock — 410 Medical](https://410medical.com/app/uploads/2023/03/Every-Minute-Matters-in-Hemorrhagic-Shock-White-Paper.pdf)
- [AAOS Now: Hemorrhage control time-sensitive, 2025](https://www.aaos.org/aaosnow/2025/nov/clinical/clinical01/)
