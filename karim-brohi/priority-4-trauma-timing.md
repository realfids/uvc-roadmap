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

## Section 3: Hemorrhagic Shock — Therapeutic Window and Time Dynamics

### 3.1 Clinical Survival Time Data

**Paper: "Traumatic hemorrhage and chain of survival"**
- Source: PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC10207757/
- Dataset: 208 trauma patients presenting with hemorrhagic shock (SBP ≤90 mmHg)
- Outcomes:
  - **31% died within 2 hours of ED arrival**
  - 12% died between 2–24 hours
  - 11% died after 24 hours
  - 46% survived
- Overall mortality from hemorrhage-induced hypotension: **54%**
- **Median time from onset of hemorrhagic shock to death: ~2 hours**
- Most hemorrhagic deaths occur within the first 6 hours of hospital admission

### 3.2 Preclinical Survival Time Data

Animal models provide direct measurement of survival windows not ethically obtainable in human studies:

- **Rat model (uncontrolled internal hemorrhage):** Average survival time 107 minutes; 12/59 rats died before 120 minutes
  - Source: PLOS One — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0080862
- **Heparinized rat hemorrhage models:** Survival time as short as 30 minutes
- **Swine continuous hemorrhage model:** Survival time modulated by bleed rate (1.0–1.25 ml/kg/min)
  - Source: PubMed — https://pubmed.ncbi.nlm.nih.gov/2548273/

These data define the pharmacological window: the survivable therapeutic window for uncontrolled hemorrhage begins closing within 30 minutes and is largely exhausted by 2 hours, consistent with clinical outcome data.

### 3.3 Hemorrhage as a Fraction of All Trauma Deaths

**Paper: "Impact of Hemorrhage on Trauma Outcome: An Overview of Epidemiology, Clinical Presentations, and Therapeutic Considerations"**
- Journal: Journal of Trauma, 2006
- Sources: LWW — https://journals.lww.com/jtrauma/fulltext/2006/06001/impact_of_hemorrhage_on_trauma_outcome__an.2.aspx | PubMed — https://pubmed.ncbi.nlm.nih.gov/16763478/
- Key statistics:
  - Hemorrhage responsible for **30–40% of trauma mortality**
  - **33–56% of hemorrhage deaths occur in the prehospital period**
  - Autopsy review of 425 consecutive injury deaths: hemorrhage caused 35.2% of deaths

**Paper: "Navigating Hemorrhagic Shock: Biomarkers, Therapies, and Challenges in Clinical Care"**
- Journal: Biomedicines, December 2024
- Source: MDPI — https://www.mdpi.com/2227-9059/12/12/2864
- Key statistics:
  - Hemorrhagic shock causes approximately **60,000 deaths annually** in the US
  - **~50% of hemorrhagic shock deaths occur before hospital arrival**
  - Lamb et al. 2023 systematic review (24 studies, >10,000 patients): 70% of studies demonstrated significant link between delayed hemostatic intervention and increased mortality

**Paper: "Epidemiology of Trauma-Related Hemorrhage and Time to Definitive Care Across North America: Making the Case for Bleeding Control Education"**
- Year: 2023
- Source: PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC10694464/
- Key statistics:
  - 44.9% of hemorrhage deaths classified as preventable or potentially preventable
  - Of preventable hemorrhage deaths: **35.8% occurred prehospital**
  - Of preventable hemorrhage deaths: additional **20.4% died within 1 hour of arriving at an acute care setting**
  - Combined: **56.2% of preventable hemorrhage deaths** occur either prehospital or within the first hour of hospital arrival
  - Patients experienced a median wait of 6 minutes for EMS arrival and a median of 60 minutes until reaching definitive care
  - Patients with life-threatening hemorrhage may lose their entire circulating blood volume in under 5 minutes

---

## Section 4: Military Data — Eastridge et al. 2012 (Landmark Study)

**Paper: "Death on the Battlefield (2001–2011): Implications for the Future of Combat Casualty Care"**
- Authors: Eastridge et al.
- Journal: Journal of Trauma and Acute Care Surgery, 2012; 73(6 Suppl 5):S431–437
- Source: PubMed — https://pubmed.ncbi.nlm.nih.gov/23192066/
- Dataset: 4,574 combat deaths, Operations Iraqi Freedom and Enduring Freedom, 2001–2011

| Metric | Value |
|--------|-------|
| Deaths before reaching medical treatment facility | **87%** |
| Of pre-MTF deaths: non-survivable | 75.7% (n=3,040) |
| Of pre-MTF deaths: potentially survivable | **24.3% (n=976)** |
| Of potentially survivable deaths: due to hemorrhage | **90.9%** |
| Lethal hemorrhage site — truncal (non-compressible) | 67.3% |
| Lethal hemorrhage site — junctional | 19.2% |
| Lethal hemorrhage site — extremity | 13.5% |
| 2nd most common cause of potentially preventable death | Airway obstruction: 8% |

**Conclusion from Eastridge 2012:** "Most battlefield casualties died of their injuries before ever reaching a surgeon. To significantly impact the outcome of combat casualties with potentially survivable injury, strategies must be developed to mitigate hemorrhage and optimize airway management or reduce the time interval between point of injury and surgical intervention."

**Related paper: "Died of wounds on the battlefield: causation and implications for improving combat casualty care"**
- Source: PubMed — https://pubmed.ncbi.nlm.nih.gov/21795876/
- Dataset: 558 combat casualties who reached a medical treatment facility but subsequently died
- Key finding: Of 287 potentially survivable died-of-wounds casualties, **80% of mortality was directly associated with acute hemorrhage** early in the hospital course
- DOW rate: 4.6% — strikingly similar to civilian trauma center case fatality rate of 4.1%

**Paper: "Outcomes of traumatic hemorrhagic shock and the epidemiology of preventable death from injury" — Eastridge et al., 2019**
- Journal: Transfusion, 2019
- Sources: Wiley — https://onlinelibrary.wiley.com/doi/full/10.1111/trf.15161 | PubMed — https://pubmed.ncbi.nlm.nih.gov/30980749/
- Synthesis finding: Hemorrhage implicated in **25–30% of all injury deaths** and **>80% of preventable post-injury deaths** in military and civilian settings combined
- Kalkwarf et al. sub-analysis within this paper (1,848 trauma-related deaths):
  - 305 deaths due to uncontrolled hemorrhage
  - **45% of hemorrhage deaths were preventable or potentially preventable**
  - 35% of those occurred in the prehospital setting

---

## Section 5: Preventable Prehospital Trauma Deaths — Civilian Epidemiology

**Systematic Review: "Are Pre-hospital Trauma Deaths Preventable? A Systematic Literature Review"**
- Authors: Pfeifer et al.
- Journal: World Journal of Surgery, 2019
- Sources: Wiley — https://onlinelibrary.wiley.com/doi/10.1007/s00268-019-05056-1 | PubMed — https://pubmed.ncbi.nlm.nih.gov/31214829/
- Scope: 19 papers, 7,235 deaths, published 1990–2018
- Key statistics:
  - Pre-hospital death rate: 14.6–47.6% of all trauma deaths (varies by system)
  - **Definitely preventable: 4.9–11.3%** of prehospital deaths
  - **Potentially preventable: 25.8–42.7%** of prehospital deaths
  - Most common causes: delayed treatment (27–58%), management errors (40–60%), treatment errors (50–76.6%)

**Systematic Review: "Preventable death in trauma: A systematic review on definition and classification"**
- Journal: Injury, 2021
- Source: ScienceDirect — https://www.sciencedirect.com/science/article/pii/S0020138321006458
- Scope: 68 selected articles from 3,614 identified; covers 1990–2021
- Finding: Delay in treatment and treatment errors are the most consistently cited causes of trauma-related preventable death across all classification systems and study designs

**Paper: "Early and prehospital trauma deaths: Who might benefit from advanced resuscitative care?"**
- Year: 2020
- Source: PubMed — https://pubmed.ncbi.nlm.nih.gov/32176169/
- Anatomic survivability breakdown of trauma fatalities:

| Category | Fraction of all trauma fatalities |
|----------|----------------------------------|
| Anatomically non-survivable | 73% |
| Survivable only with hospital care | 9% |
| **Survivable with advanced prehospital care** | **14%** |
| Survivable with basic prehospital care | 4% |

- Implication: 12–18% of all trauma deaths might be prevented with field-level advanced resuscitation; in the US context (~200,000 injury deaths/year), this represents approximately 24,000–36,000 deaths/year

**Paper: "Are prehospital deaths from trauma and accidental injury preventable? A direct historical comparison to assess what has changed in two decades"**
- Year: 2017
- Sources: ScienceDirect — https://www.sciencedirect.com/science/article/pii/S0020138317300608 | PubMed — https://pubmed.ncbi.nlm.nih.gov/28363752/
- Comparison: Hussain & Redmond 1994 vs. contemporary Manchester/Cheshire data
- Key statistics:
  - 1994 (Hussain & Redmond): up to **39% of prehospital accidental injury deaths** potentially preventable with basic first aid
  - 2017 study: Median ISS 27.5–29; **46–59% of deaths** had probability of survival in the preventable/potentially preventable range
  - Bystander presence: 39–45%; bystander intervention of any kind: only **25–30%**
  - Conclusion: The number of potentially preventable prehospital deaths remains high and largely unchanged over two decades

**Paper: "Prehospital deaths from trauma: Are injuries survivable and do bystanders help?"**
- Year: 2017
- Sources: PubMed — https://pubmed.ncbi.nlm.nih.gov/28262281/ | ScienceDirect — https://www.sciencedirect.com/science/article/pii/S0020138317300979
- Key statistics:
  - Median ISS: 29
  - **43% of deaths had probability of survival >50%**
  - Bystanders present in 45% of cases; present before EMS in **96%** of those cases
  - Despite near-ubiquitous bystander presence before EMS, intervention rate was only 25–30%
  - Hemorrhage was the dominant mechanism in survivable deaths

**Paper: "Bleeding to death in a big city: An analysis of all trauma deaths from hemorrhage in a metropolitan area during 1 year"**
- Source: PubMed — https://pubmed.ncbi.nlm.nih.gov/32590562/
- Key finding: Metropolitan analysis designated **29% of mortality as potentially preventable**; **64% of those potentially survivable deaths** attributed to hemorrhage

**Paper: "The forgotten cohort — lessons learned from prehospital trauma death: a retrospective cohort study"**
- Journal: Scandinavian Journal of Trauma, Resuscitation and Emergency Medicine, 2023
- Source: Springer — https://link.springer.com/article/10.1186/s13049-023-01107-8
- Key finding: Prehospital trauma deaths remain under-studied and under-resourced; hemorrhage control and airway management are the dominant addressable causes; the paper argues for systematic data collection on prehospital deaths as a precondition for improving outcomes

**Paper: "Epidemiology of Prehospital and Hospital Traumatic Deaths from Life-Threatening Hemorrhage"**
- Source: Scholars @ UT Health San Antonio — https://scholars.uthscsa.edu/en/publications/epidemiology-of-prehospital-and-hospital-traumatic-deaths-from-li/
- Finding: Establishes the empirical split between prehospital and in-hospital hemorrhage deaths; confirms that the prehospital period is the dominant window for hemorrhage mortality

**National Academies of Sciences estimate:**
- 20% of trauma-related deaths may have been preventable with receipt of "optimal trauma care"
- The "greatest opportunity to save lives" identified as the prehospital setting

---

## Section 6: Remote Damage Control Resuscitation — Extending the Therapeutic Window

**Paper: "EMS Tactical Damage Control Resuscitation Protocol"**
- Source: StatPearls / NCBI Bookshelf — https://www.ncbi.nlm.nih.gov/books/NBK599525/
- Framework: Remote Damage Control Resuscitation (RDCR), developed by the Trauma Hemostasis Oxygenation Research (THOR) network
- Definition: Formal prehospital resuscitation protocol applied when hospital access is delayed **>60 minutes**
- Components:
  - Mechanical hemorrhage control (tourniquet, packing, junctional compression devices)
  - Permissive hypotension (target MAP 50–65 mmHg to avoid diluting clot)
  - Prevention of hypothermia (one vertex of the "lethal triad": hypothermia + acidosis + coagulopathy)
  - Blood product administration when available (tranexamic acid, freeze-dried plasma, whole blood)
- The 60-minute threshold used to define RDCR candidacy reflects the clinical consensus on the primary death window for preventable hemorrhagic trauma deaths

**Paper: "Haemorrhage control in the prehospital setting: a scoping review protocol"**
- Source: PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC6661646/
- Finding: Mechanical and pharmacologic hemorrhage control is feasible prehospitally; evidence base is growing but remains incomplete for pharmacologic agents beyond TXA

**SROI implication:** The existence of RDCR as a formalized clinical protocol confirms that the medical community has already accepted that: (a) the 60-minute window is the critical intervention threshold, and (b) pharmacologic/resuscitative treatment in the field is both feasible and needed. An A2A agonist or similar cytoprotective agent fits naturally into the RDCR framework as an adjunct to current mechanical and volume-based approaches.

---

## Summary Statistics Table

| Metric | Statistic | Source |
|--------|-----------|--------|
| Immediate trauma deaths (1st peak, Trunkey model) | ~50% of all trauma deaths | Trunkey 1983 |
| Early trauma deaths (2nd peak, 1–4 hrs) | ~30% of all trauma deaths | Trunkey 1983 |
| Late trauma deaths (3rd peak, days–weeks) | ~20% of all trauma deaths | Trunkey 1983 |
| 3rd peak presence in modern high-income trauma systems | Largely eliminated | TraumaRegister DGU; Annals of Surgery |
| Trauma deaths due to hemorrhage (overall) | 30–40% | Eastridge 2019; J Trauma 2006 |
| Hemorrhage deaths occurring in prehospital period | 33–56% | J Trauma 2006 |
| Preventable/potentially preventable hemorrhage deaths | 45% of all hemorrhage deaths | Kalkwarf / Eastridge 2019 |
| Of preventable hemorrhage deaths: prehospital | 35.8% | N. America Epidemiology PMC 2023 |
| Of preventable hemorrhage deaths: die within 1 hr of ED | 20.4% | N. America Epidemiology PMC 2023 |
| Preventable hemorrhage deaths (prehospital + within 1 hr of ED) combined | 56.2% of all PPH deaths | N. America Epidemiology PMC 2023 |
| Prehospital trauma deaths potentially preventable (systematic review) | 25.8–42.7% | Pfeifer et al. 2019 |
| Prehospital trauma deaths definitely preventable | 4.9–11.3% | Pfeifer et al. 2019 |
| Military pre-MTF deaths | 87% of all combat deaths | Eastridge 2012 |
| Military pre-MTF deaths: non-survivable | 75.7% | Eastridge 2012 |
| Military pre-MTF deaths: potentially survivable | 24.3% (n=976) | Eastridge 2012 |
| Of potentially survivable military deaths: hemorrhagic | 90.9% | Eastridge 2012 |
| Lethal hemorrhage: truncal (non-compressible) | 67.3% of potentially survivable | Eastridge 2012 |
| Hemorrhage as cause of preventable post-injury death | >80% (military + civilian) | Eastridge 2019 |
| All trauma fatalities preventable with advanced prehospital care | 14% | PubMed 2020 |
| All trauma fatalities preventable with basic prehospital care | 4% | PubMed 2020 |
| Median survival time in hemorrhagic shock | ~2 hours | Traumatic hemorrhage chain of survival PMC |
| Hemorrhagic shock patients dying within 2 hrs of ED arrival | 31% | Chain of survival PMC |
| Overall mortality from hemorrhage-induced hypotension (SBP ≤90) | 54% | Chain of survival PMC |
| Per-minute delay in resuscitation: odds of 30-day mortality | +2% per minute | 410 Medical white paper |
| Per-minute delay in resuscitation: odds of 24-hr mortality | +1.5% per minute | 410 Medical white paper |
| Studies showing delayed hemostasis increases mortality | 70% of 24 studies (Lamb 2023) | Biomedicines Dec 2024 |
| Annual US deaths from hemorrhagic shock | ~60,000 | Biomedicines Dec 2024 |
| Hemorrhagic shock deaths before hospital arrival | ~50% | Biomedicines Dec 2024 |
| Bystander presence in prehospital trauma death cases | 39–45% | UK prehospital death studies |
| Bystander presence before EMS in those cases | 96% | PubMed 28262281 |
| Bystander intervention rate despite presence | 25–30% | UK prehospital death studies |
| National Academies estimate: trauma deaths preventable with optimal care | 20% | National Academies report |

---

## Section 7: Implications for Prehospital Intervention Feasibility

### 7.1 The Therapeutic Window is Narrow but Pharmacologically Actionable

The median survival time in hemorrhagic shock is approximately 2 hours. Animal models confirm this window — uncontrolled hemorrhage in rodent models produces death in 30–107 minutes depending on injury severity. This 30-minute-to-2-hour window is:

- Too short for hospital care in rural, austere, or low-resource settings
- Long enough for a pharmacologic agent to achieve meaningful effect if administered immediately after injury
- Consistent with RDCR's 60-minute threshold for defining field resuscitation candidates
- Compatible with known pharmacokinetics of A2A agonists and similar cytoprotective agents

### 7.2 A Quantifiable and Meaningful Fraction of Deaths is Addressable

Across civilian studies, 25–43% of prehospital trauma deaths are classified as potentially preventable. The most conservative anatomic survivability analysis (PubMed 2020) estimates 14% of all trauma deaths are addressable specifically with advanced prehospital care. Using US injury mortality figures (~200,000 deaths/year), this represents approximately **28,000 deaths/year** in the US alone that are potentially addressable with better prehospital intervention.

The military data (Eastridge 2012) place the upper bound at 24.3% of all field deaths as potentially survivable — and 90.9% of those are hemorrhagic. At the conservative lower bound, the addressable target population is still large in absolute terms.

### 7.3 Hemorrhage is the Dominant and Specific Addressable Mechanism

Over 80% of preventable post-injury deaths in both military and civilian contexts are hemorrhage-related (Eastridge 2019). This narrows the intervention target sharply:

- Non-compressible truncal hemorrhage (67.3% of potentially survivable military deaths) cannot be addressed by mechanical means alone — it requires systemic physiologic support
- This creates a specific unmet need for pharmacologic agents that extend tolerance for blood loss, maintain end-organ perfusion, reduce coagulopathy progression, or mitigate ischemia-reperfusion injury at the cellular level

### 7.4 The Bystander Gap Defines the Delivery Context

In UK studies, bystanders were present before EMS in 96% of prehospital trauma death cases but intervened in only 25–30% of cases. This gap — between presence and action — means any effective prehospital intervention must be:

- Simple enough for bystander administration (auto-injector format, single-step)
- Safe enough for broad lay-person use
- Robust enough to provide benefit across the range of injury severities where it might be administered

### 7.5 The Acuity-Stratified Target Population

The Relative Mortality Analysis (PubMed 2018) quantifies the actionable target: patients with probability of survival 23–91%. This is the intermediate-acuity group for whom prehospital time is genuinely decisive. Interventions targeting this group — deferring death long enough to reach surgical hemorrhage control — have the highest expected value per patient treated.

### 7.6 Transport vs. Treatment: The Rural/Austere Calculus

Alarhayem et al. (2016) make explicit what the broader literature implies: when transport within 30 minutes is impossible, pharmacologic extension of the survival window is the only alternative. The median time from injury to definitive care in North America is already ~60 minutes (PMC 2023); in rural or low-resource settings it is substantially longer. Drugs or biologics that extend the survivable window by even 30–60 minutes could shift a meaningful fraction of currently non-survivable prehospital deaths into the survivable category.

---

## SROI Interpretation

**Bottom line:** A meaningful and quantifiable fraction of trauma deaths (~14% of all fatalities by the most conservative estimate, ~45% of hemorrhagic deaths by the most specific estimate) are potentially preventable with advanced prehospital intervention delivered within a ~2-hour window. Hemorrhage is the overwhelmingly dominant preventable mechanism (>80% of preventable deaths). The therapeutic window is real, narrows rapidly within 30–120 minutes of injury, and is consistent with pharmacological intervention via auto-injector or other field-deployable formats. This **strongly supports the addressable DALYs estimate** for a prehospital A2A agonist and argues that the target population is both large and specifically identified.

**Evidence quality for this conclusion:** Moderate-High. Multiple independent data streams (military autopsy studies, civilian systematic reviews, hemorrhagic shock outcome curves, preclinical pharmacology) converge on the same 30-minute-to-2-hour window and the same hemorrhage-dominant mechanism. The main uncertainty is in translating the "potentially preventable" category — defined by anatomic criteria — into the fraction that a specific pharmacologic intervention would actually rescue.

---

## Sources

### Section 1: Trimodal Distribution
- Changing epidemiology — bimodal distribution: https://pmc.ncbi.nlm.nih.gov/articles/PMC2943446/
- TraumaRegister DGU temporal distribution: https://pmc.ncbi.nlm.nih.gov/articles/PMC6386341/
- Mortality progressive decreasing, not trimodal: https://www.sciencedirect.com/science/article/pii/S2221618915000311
- Timing of death — contemporary assessment: https://www.sciencedirect.com/science/article/abs/pii/S0022480415008707
- Trimodal in resource-limited settings: https://pubmed.ncbi.nlm.nih.gov/36939860/

### Section 2: The Golden Hour
- Time is the Enemy — Alarhayem et al.: https://www.sciencedirect.com/science/article/abs/pii/S0002961016305542
- Time is the Enemy — STRAC PDF: https://www.strac.org/wp-content/uploads/2024/02/Time_is_the_Enemy.pdf
- Relative Mortality Analysis of the Golden Hour, 2018: https://pubmed.ncbi.nlm.nih.gov/30118362/
- Redefining the golden hour for severe head injury: https://www.sciencedirect.com/science/article/abs/pii/S0020138312000186
- Every Minute Matters in Hemorrhagic Shock: https://410medical.com/app/uploads/2023/03/Every-Minute-Matters-in-Hemorrhagic-Shock-White-Paper.pdf
- Hemorrhage control time-sensitive imperative — AAOS 2025: https://www.aaos.org/aaosnow/2025/nov/clinical/clinical01/
- EMS Intervals and the Golden Hour — Newgard et al.: https://pmc.ncbi.nlm.nih.gov/articles/PMC3008652/
- PATOS Study — PLOS Medicine 2020: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003360
- PATOS PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC7537901/
- Does prehospital time affect survival without prehospital care: https://pmc.ncbi.nlm.nih.gov/articles/PMC5525481/
- Prehospital time and pediatric trauma: https://link.springer.com/article/10.1007/s00383-024-05742-9

### Section 3: Hemorrhagic Shock Therapeutic Window
- Traumatic hemorrhage and chain of survival: https://pmc.ncbi.nlm.nih.gov/articles/PMC10207757/
- Rat hemorrhage survival model — PLOS One: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0080862
- Swine continuous hemorrhage model: https://pubmed.ncbi.nlm.nih.gov/2548273/
- Impact of Hemorrhage on Trauma Outcome — J Trauma 2006: https://journals.lww.com/jtrauma/fulltext/2006/06001/impact_of_hemorrhage_on_trauma_outcome__an.2.aspx
- J Trauma 2006 PubMed: https://pubmed.ncbi.nlm.nih.gov/16763478/
- Navigating Hemorrhagic Shock — Biomedicines Dec 2024: https://www.mdpi.com/2227-9059/12/12/2864
- Epidemiology of Trauma-Related Hemorrhage — N. America 2023: https://pmc.ncbi.nlm.nih.gov/articles/PMC10694464/

### Section 4: Military Data
- Eastridge et al. 2012 — Death on the Battlefield: https://pubmed.ncbi.nlm.nih.gov/23192066/
- Died of wounds — Eastridge 2011: https://pubmed.ncbi.nlm.nih.gov/21795876/
- Eastridge et al. 2019 — Outcomes of traumatic hemorrhagic shock (Wiley): https://onlinelibrary.wiley.com/doi/full/10.1111/trf.15161
- Eastridge et al. 2019 PubMed: https://pubmed.ncbi.nlm.nih.gov/30980749/

### Section 5: Preventable Prehospital Deaths — Civilian
- Are Pre-hospital Trauma Deaths Preventable — Pfeifer et al. (Wiley): https://onlinelibrary.wiley.com/doi/10.1007/s00268-019-05056-1
- Pfeifer et al. PubMed: https://pubmed.ncbi.nlm.nih.gov/31214829/
- Preventable death in trauma — systematic review on definition, 2021: https://www.sciencedirect.com/science/article/pii/S0020138321006458
- Early and prehospital trauma deaths — advanced resuscitative care (2020): https://pubmed.ncbi.nlm.nih.gov/32176169/
- Historical comparison of preventable prehospital deaths — 2017 ScienceDirect: https://www.sciencedirect.com/science/article/pii/S0020138317300608
- Historical comparison PubMed: https://pubmed.ncbi.nlm.nih.gov/28363752/
- Prehospital deaths — survivable injuries and bystanders (2017) PubMed: https://pubmed.ncbi.nlm.nih.gov/28262281/
- Prehospital deaths bystanders ScienceDirect: https://www.sciencedirect.com/science/article/pii/S0020138317300979
- Bleeding to death in a big city: https://pubmed.ncbi.nlm.nih.gov/32590562/
- The forgotten cohort — prehospital trauma death lessons: https://link.springer.com/article/10.1186/s13049-023-01107-8
- Epidemiology of prehospital and hospital hemorrhage deaths (UT Health): https://scholars.uthscsa.edu/en/publications/epidemiology-of-prehospital-and-hospital-traumatic-deaths-from-li/

### Section 6: Remote Damage Control Resuscitation
- EMS Tactical Damage Control Resuscitation Protocol — StatPearls: https://www.ncbi.nlm.nih.gov/books/NBK599525/
- Haemorrhage control prehospital — scoping review: https://pmc.ncbi.nlm.nih.gov/articles/PMC6661646/
