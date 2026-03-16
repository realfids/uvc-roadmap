#!/usr/bin/env python3
"""
Monte Carlo simulation for INTERCEPT intervention cost-effectiveness (v2)
Estimating probability of meeting Open Philanthropy's 2100x threshold

v2 adds 6 corrections identified from the OpenPhil analyst conversation:
  1. Counterfactual attribution fraction  (was: 100% credit assumed)
  2. Follow-on funding as a distinct node (was: collapsed into one P(drug))
  3. Portfolio effect of OoC platform     (was: single binary drug outcome)
  4. HIC vs LMIC deployment split         (was: single blended addressable fraction)
  5. Time discounting of future DALYs     (was: undiscounted)
  6. VOI expert interview guidance        (was: absent from report)

Evidence base: karim-brohi/ 8-priority literature review (March 2026)
Key calibration sources:
  - Wisniewski 2024 (PMID 39029264): regadenoson 100% vs 40% survival, porcine ECPR
  - Kelestemur 2022 (PMID 36018304): A2aR-KO mice → worsened MOF (causal proof)
  - Mohamed 2016 (PMID 26642806): A2AR antagonism neuroprotective in cerebral IRI
  - Heusch 2017 (PMID 28450365): IRI translational failure root causes
  - Ferdinandy 2023 (PMID 36753049): comorbidity gap as #1 IRI trial failure driver
  - Ewart 2022 (PMC9727064): Emulate Liver-Chip 87%/100% DILI prediction
  - Vormann 2022: kidney chip adenosine protects renal IRI
  - ReWiRe Phase 2a trial: Queen Mary Univ London, REC 19/LO/0329
  - Priority 7: TXA HR 0.72; NAEMSP/ACEP/ACS-COT 2024 endorsement
  - Priority 8: selective A2A agonist prehospital niche is uncrowded
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)
N_SIMS = 100_000
OUTPUT_DIR = '/home/user/uvc-roadmap/karim-brohi'


# =============================================================================
# GAP 4: HIC / LMIC ADDRESSABLE DALY ARMS  (replaces sample_global_dalys +
#         sample_addressable_fraction — those are no longer separate functions)
# =============================================================================

def sample_annual_addressable_hic(n):
    """
    Annual DALYs addressable by A2A agonist in HIGH-INCOME COUNTRIES.

    Scope: trauma/HS + ECPR + DCD transplant in US, EU, Australia, Japan.

    Trauma/HS filter chain:
      ~60,000 US hemorrhagic shock deaths/yr (Priority 4)
      14% potentially preventable with advanced prehospital care (Pfeifer 2019)
      × ~72% TBI-eligible (Mohamed 2016 brain IRI caveat; ~28% of trauma is TBI-dominant)
      × ~80% organ-specificity fit (lung/liver/kidney/heart protected; gut NOT — Haskó 2006)
      × ~65% field uptake (TXA underuse data — BMJ Open 2024, PMC11287560)
      ≈ 3,200 prevented US deaths/yr × DALY multiplier ~3 ≈ 9,600 DALY_US
      EU/other HIC: ~3× US volume → ~40k HIC trauma DALYs/yr

    ECPR contribution (Wisniewski 2024 porcine: 100% vs 40%, p=0.01):
      ~5,000-10,000 ECPR cases/yr in HIC and growing
      60% absolute survival improvement × ~7,500 cases × DALY multiplier ~15 ≈ 675k DALY/yr
      (optimistic; actual ECPR scale and applicability uncertain)

    Combined: median 5M DALYs/yr, log-normal σ=0.45
    90% CI: ~2.3M to ~11M DALYs/year
    """
    return np.random.lognormal(np.log(5e6), 0.45, n)


def sample_annual_addressable_lmic(n):
    """
    Annual DALYs addressable by A2A agonist in LOW-AND-MIDDLE INCOME COUNTRIES.

    LMIC carries ~80% of global trauma burden but faces severe deployment constraints:

    LMIC trauma/HS burden: ~1.5M deaths/yr × DALY multiplier → ~40-60M DALY/yr total.
    But deployment feasibility is the binding constraint:

      EMS prehospital access: ~20-35% (trimodal distribution persists — LMIC data,
        PubMed 36939860 — unlike HIC, the late peak still exists, reflecting care gaps)
      IV administration in field: often infeasible without trained paramedic workforce
      Cold chain for regadenoson: likely requires refrigeration — major LMIC barrier
        (regadenoson currently approved only for cardiac stress labs in HIC settings)
      Prehospital drug operationalisation: very low without explicit LMIC programme

    Net addressable: ~2-5% of LMIC burden after deployment filters
    Median 3.5M DALYs/yr, log-normal σ=0.60 (high uncertainty reflects deployment gap)
    90% CI: ~1.2M to ~10M DALYs/year

    UPSIDE NOT MODELLED: an oral/intranasal/autoinjector formulation of regadenoson
    could increase LMIC addressable 3-5×. Not in current INTERCEPT scope.
    """
    return np.random.lognormal(np.log(3.5e6), 0.60, n)


# =============================================================================
# GAP 1: COUNTERFACTUAL ATTRIBUTION FRACTION
# =============================================================================

def sample_attribution_fraction(n):
    """
    Fraction of eventual clinical impact attributable to INTERCEPT's investment
    vs. what would have happened in the counterfactual without INTERCEPT.

    Evidence for LOWER attribution (INTERCEPT partially redundant):
      - ReWiRe Phase 2a ALREADY REGISTERED at Queen Mary WITHOUT INTERCEPT (REC 19/LO/0329)
        → INTERCEPT is not starting from zero; it accelerates an existing programme
      - CDMRP JWMRP explicitly funds "drugs that extend the physiologic resuscitation
        window" — a direct match (Priority 8)
      - ARIA could fund Karim independently (home-institution context)
      - Military/DoD funding of adjacent trauma programmes (DARPA: $70M+ in portfolio)

    Evidence for HIGHER attribution (INTERCEPT is the marginal enabler):
      - No other OoC/DT A2A-agonist-in-trauma programme identified (Priority 8)
      - The OoC platform de-risking of Phase 3 design is INTERCEPT-specific value
      - Civilian prehospital translation of military advances: explicitly identified gap
      - INTERCEPT's marginal contribution = better Phase 3 design + faster adoption,
        not the drug trial itself (ReWiRe proceeds either way)

    Modal estimate: ~40%.  Range: ~12-76%.
    Beta(3, 4) → mode = 2/5 = 40%, mean = 3/7 ≈ 43%
    """
    return np.random.beta(3, 4, n)


# =============================================================================
# GAP 2: STAGED DRUG SUCCESS (replaces single sample_p_drug_conditional)
# =============================================================================

def sample_p_platform(n):
    """
    P(OoC/digital-twin platform validates A2A agonism and guides Phase 3 design).

    Supporting evidence (Priority 3 & 6):
      - Emulate Liver-Chip: 87% sensitivity / 100% specificity for DILI (Ewart 2022)
      - First IND approved on OoC/organoid efficacy data alone (Qureator, 2025)
      - OoC data in FDA IND for COVID-19 drug (Cantex Lung Chip, 2022)
      - FDA ISTAND accepted first OoC submission (Sept 2024)
      - Kidney-on-chip: adenosine protects proximal tubule cells vs renal IRI (Vormann 2022)
      - HS digital twin validated in porcine AND human PROMMTT data (Nat Comms Med, 2024)

    Tempering:
      - No OoC-to-IRI-drug-efficacy clinical validation precedent yet (DILI ≠ IRI)
      - Only 12% of "digital twin" studies meet NASEM criteria (Priority 6)
      - OoC reproducibility/standardisation barriers (PubMed 36290517)

    Beta(7, 4) → mode ≈ 67%, mean ≈ 64%
    """
    return np.random.beta(7, 4, n)


def sample_p_phase3_funded(n):
    """
    P(Phase 3 RCT gets funded | Phase 2a positive + platform guidance).

    Positive:
      - A2A agonist niche is uncrowded in pharma → high IP and competitive value
      - Phase 2a safety signal + OoC mechanistic validation = strong pull-through
      - CDMRP JWMRP is a direct funding match (Priority 8)
      - Wellcome Trust / NIHR / NHS trauma funding routes exist
      - TXA precedent: prehospital drugs do get funded to Phase 3 (CRASH-2 → PATCH)
      - Regadenoson generic status may actually help: lowers pharma cost basis

    Risk:
      - Phase 3 in prehospital trauma = $100-200M — large for an unproven mechanism
      - Pharma may demand larger Phase 2b before committing; regadenoson low IP value
      - ReWiRe being academic-led may reduce pharma pull-through vs industry-sponsored

    Beta(7, 3) → mode = 75%, mean = 70%
    """
    return np.random.beta(7, 3, n)


def sample_p_phase3_success(n):
    """
    P(Phase 3 RCT positive | funded + OoC-guided trial design).

    BASE RATE — IRI field: catastrophically bad:
      CIRCUS (cyclosporine A / mPTP): OR 1.04, p=0.77, NEJM 2015, n=970
      CONDI2/ERIC-PPCI (remote ischaemic conditioning): HR 1.10, p=0.32, Lancet 2019, n=5,401
      AMISTAD-II (non-selective adenosine): no benefit, n=2,118
      >1,000 stroke neuroprotectants in animals → 0 human approvals (Priority 2)
      Root causes (Heusch 2017, Ferdinandy 2023):
        - Animal models: 25-50 min no-flow; patients: 150-250 min low-flow
        - Comorbidity/comedication gap not captured in preclinical models
        - Publication bias: only 13% of preclinical datasets are neutral

    SPECIFIC UPWARD ADJUSTMENTS for A2A agonist in trauma:
      - Selective A2A agonists UNTESTED at Phase 3 → no negative prior for this mechanism
      - Leukocyte-mediated anti-inflammatory: distinct from all failed cardiomyocyte targets
      - Trauma context vs STEMI: shorter ischaemia, younger patients, fewer comedications
        (all three are the primary IRI translational failure drivers per Heusch 2017)
      - OoC platform directly addresses the comorbidity gap (#1 structural failure cause)
        (Ferdinandy 2023, PMID 36753049)
      - Regadenoson FDA-approved → safety profile partially de-risked

    DOWNWARD:
      - Vasodilatory effects in hypotensive trauma patients (primary Phase 2a safety concern)
      - Gut non-protection: splanchnic ischaemia patients may not benefit (Haskó 2006)
      - TBI exclusion adds trial complexity; reduces enrolled N

    CALIBRATION NOTE (important):
      E[p_phase3_funded × p_phase3_success × p_adoption] ≈ 0.70 × 0.25 × 0.60 = 10.5%
      This is below the v1 synthesis holistic estimate of 25-35%.
      The gap shows that the synthesis estimate requires above-average performance at
      every stage simultaneously. The staged model is the more conservative and
      transparent representation. See CALIBRATION FLAG in report.

    Beta(2, 6) → mode ≈ 17%, mean = 25%
    """
    return np.random.beta(2, 6, n)


def sample_p_adoption(n):
    """
    P(guideline adoption and field implementation | regulatory approval).

    Positive:
      - TXA precedent: CRASH-2 (2010) → NAEMSP/ACEP/ACS-COT endorsement (2024) (Priority 7)
      - Ketamine and prehospital blood transfusion: expanding prehospital pharmacology
      - Regadenoson already in EMS physician awareness via cardiac stress testing

    Dampeners:
      - TXA underuse study: guideline ≠ automatic adoption — lower in women/elderly
        (BMJ Open 2024, PMC11287560)
      - Prehospital blood transfusion rollout remains fragmented in US civilian EMS
      - IV administration in field adds complexity vs simple drug

    Beta(6, 4) → mode = 62.5%, mean = 60%
    """
    return np.random.beta(6, 4, n)


# =============================================================================
# GAP 3: PORTFOLIO EFFECT (number of viable drug leads from OoC platform)
# =============================================================================

def sample_n_viable_leads(n):
    """
    Number of viable drug candidates the OoC platform identifies for A2A/IRI.

    Known and potential candidates:
      - Regadenoson (FDA-approved A2AR agonist; primary focus)       → 1 certain lead
      - Selective A2AR analogues with improved haemodynamic safety profile
        (motivated by regadenoson vasodilation risk in hypotensive patients)
      - ATL1223 / ATL146e: different A2AR scaffolds (Mehaffey 2019, PMID 31082918)
      - A2B agonist (BAY 60-6583): parallel purinergic protection (Koscsó 2013)
      - Combination regimens (regadenoson + TXA dosing optimisation)

    Probability of N leads emerging from OoC screen:
      1 lead: 50%  (regadenoson only, no superior analogue found)
      2 leads: 30%  (regadenoson + one strong analogue or A2B compound)
      3 leads: 13%  (multiple scaffolds validated)
      4 leads:  5%
      5 leads:  2%
    Expected n_leads ≈ 1.69
    """
    return np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.50, 0.30, 0.13, 0.05, 0.02])


# =============================================================================
# GAP 5: TIME DISCOUNTING
# =============================================================================

def sample_discount_rate(n):
    """
    Annual discount rate applied to future DALYs.
    OpenPhil/GiveWell use ~3-4% empirically.
    Triangular(0.01, 0.03, 0.05) → mode 3%, mean 3%
    """
    return np.random.triangular(0.01, 0.03, 0.05, n)


def sample_time_to_impact(n):
    """
    Years from now until midpoint of cumulative impact accrual.

    Timeline:
      Phase 2a (ReWiRe, ongoing): ~1-2 yr to results
      Phase 2b (dose confirmation): ~2-3 yr
      Phase 3 RCT (trauma endpoint): ~4-6 yr
      Regulatory review: ~1-2 yr
      Adoption ramp-up (midpoint): ~4-8 yr from approval
      Total to midpoint: 12-21 yr from now

    TXA calibration: CRASH-2 (2010) → NAEMSP guideline (2024) = 14 yr.
    INTERCEPT OoC de-risking should shorten this somewhat.

    Triangular(8, 14, 22) → mode 14 yr, mean ≈ 14.7 yr
    """
    return np.random.triangular(8, 14, 22, n)


# =============================================================================
# UNCHANGED PARAMETERS
# =============================================================================

def sample_acceleration_years(n):
    """
    Years by which INTERCEPT accelerates treatment adoption vs BAU.
    TXA precedent: 14 yr without platform. INTERCEPT marginal speed-up: 5-10 yr.
    Triangular(2, 7, 15)
    """
    return np.random.triangular(2, 7, 15, n)


def sample_rd_cost(n):
    """
    Total INTERCEPT programme investment.
    OoC platform ($15-25M) + DT ($10-15M) + trial co-funding ($25-70M) + regulatory.
    Triangular(40M, 60M, 120M)
    """
    return np.random.triangular(40e6, 60e6, 120e6, n)


def sample_daly_value(n):
    """$/DALY averted. OpenPhil benchmark ~$100k. Triangular(50k, 100k, 150k)"""
    return np.random.triangular(50_000, 100_000, 150_000, n)


# =============================================================================
# SIMULATION
# =============================================================================

def run_simulation(n_sims=N_SIMS):
    """
    Run Monte Carlo simulation with all 6 corrections applied.

    Updated ROI formula:
      p_drug_per_lead  = p_phase3_funded × p_phase3_success × p_adoption
      p_drug_portfolio = 1 − (1 − p_drug_per_lead)^n_leads   [Gap 3]
      p_success        = p_platform × p_drug_portfolio

      annual_addressable = hic_arm + lmic_arm                 [Gap 4]
      expected_dalys     = annual_addressable × acceleration × p_success
      discount_factor    = (1 + discount_rate)^(−time_to_impact)  [Gap 5]
      discounted_dalys   = expected_dalys × discount_factor

      ROI = (discounted_dalys × daly_value × attribution) / rd_cost  [Gap 1]
    """
    # Gap 4: HIC/LMIC arms
    hic_arm            = sample_annual_addressable_hic(n_sims)
    lmic_arm           = sample_annual_addressable_lmic(n_sims)
    annual_addressable = hic_arm + lmic_arm

    # Gap 1: attribution
    attribution        = sample_attribution_fraction(n_sims)

    # Platform
    p_platform         = sample_p_platform(n_sims)

    # Gap 2: staged drug conditional
    p_phase3_funded    = sample_p_phase3_funded(n_sims)
    p_phase3_success   = sample_p_phase3_success(n_sims)
    p_adoption         = sample_p_adoption(n_sims)
    p_drug_per_lead    = p_phase3_funded * p_phase3_success * p_adoption

    # Gap 3: portfolio
    n_leads            = sample_n_viable_leads(n_sims)
    p_drug_portfolio   = 1.0 - (1.0 - p_drug_per_lead) ** n_leads
    p_success          = p_platform * p_drug_portfolio

    # Acceleration + cost
    acceleration       = sample_acceleration_years(n_sims)
    rd_cost            = sample_rd_cost(n_sims)
    daly_value         = sample_daly_value(n_sims)

    # Gap 5: discounting
    discount_rate      = sample_discount_rate(n_sims)
    time_to_impact     = sample_time_to_impact(n_sims)
    discount_factor    = (1.0 + discount_rate) ** (-time_to_impact)

    # ROI
    expected_dalys     = annual_addressable * acceleration * p_success
    discounted_dalys   = expected_dalys * discount_factor
    roi_multiple       = (discounted_dalys * daly_value * attribution) / rd_cost

    return {
        'hic_arm':           hic_arm,
        'lmic_arm':          lmic_arm,
        'annual_addressable':annual_addressable,
        'attribution':       attribution,
        'p_platform':        p_platform,
        'p_phase3_funded':   p_phase3_funded,
        'p_phase3_success':  p_phase3_success,
        'p_adoption':        p_adoption,
        'p_drug_per_lead':   p_drug_per_lead,
        'n_leads':           n_leads.astype(float),
        'p_drug_portfolio':  p_drug_portfolio,
        'p_success':         p_success,
        'acceleration':      acceleration,
        'rd_cost':           rd_cost,
        'daly_value':        daly_value,
        'discount_rate':     discount_rate,
        'time_to_impact':    time_to_impact,
        'discount_factor':   discount_factor,
        'expected_dalys':    expected_dalys,
        'discounted_dalys':  discounted_dalys,
        'roi_multiple':      roi_multiple,
    }


def analyze_results(results):
    """Compute summary statistics."""
    roi = results['roi_multiple']
    r   = results
    return {
        'mean_roi':              np.mean(roi),
        'median_roi':            np.median(roi),
        'p5_roi':                np.percentile(roi, 5),
        'p25_roi':               np.percentile(roi, 25),
        'p75_roi':               np.percentile(roi, 75),
        'p95_roi':               np.percentile(roi, 95),
        'prob_above_2100':       np.mean(roi > 2100),
        'prob_above_1000':       np.mean(roi > 1000),
        'prob_above_5000':       np.mean(roi > 5000),
        'prob_above_10000':      np.mean(roi > 10000),
        # P(success) decomposition
        'mean_p_platform':       np.mean(r['p_platform']),
        'mean_p_phase3_funded':  np.mean(r['p_phase3_funded']),
        'mean_p_phase3_success': np.mean(r['p_phase3_success']),
        'mean_p_adoption':       np.mean(r['p_adoption']),
        'mean_p_drug_per_lead':  np.mean(r['p_drug_per_lead']),
        'mean_n_leads':          np.mean(r['n_leads']),
        'mean_p_drug_portfolio': np.mean(r['p_drug_portfolio']),
        'mean_p_success':        np.mean(r['p_success']),
        # New correction factors
        'mean_attribution':      np.mean(r['attribution']),
        'mean_discount_factor':  np.mean(r['discount_factor']),
        'mean_time_to_impact':   np.mean(r['time_to_impact']),
        'mean_hic_arm_M':        np.mean(r['hic_arm']) / 1e6,
        'mean_lmic_arm_M':       np.mean(r['lmic_arm']) / 1e6,
    }


def sensitivity_analysis(results):
    """Pearson correlation of each parameter with ROI multiple."""
    params = [
        'hic_arm', 'lmic_arm',
        'p_platform', 'p_phase3_funded', 'p_phase3_success', 'p_adoption',
        'n_leads', 'attribution',
        'acceleration', 'discount_rate', 'time_to_impact',
        'rd_cost', 'daly_value',
    ]
    return {p: np.corrcoef(results[p], results['roi_multiple'])[0, 1] for p in params}


# =============================================================================
# SCENARIO COMPARISON
# =============================================================================

def scenario_comparison():
    """
    Fixed-parameter point estimates for 5 evidence-anchored scenarios.

    All scenarios now include:
      - attribution fraction (Gap 1)
      - time_to_impact → discount_factor (Gap 5)

    KEY FINDING: With attribution and discounting applied, even the Conservative
    scenario fails to clear 2,100×. Clearing the threshold requires at least
    Moderate assumptions on all dimensions simultaneously.
    """
    r   = 0.03   # nominal discount rate for scenario calculations
    scenarios = {
        'Platform fails / BAU': {
            'note':           'OoC fails; drug at IRI base rate; ReWiRe proceeds but INTERCEPT '
                              'adds minimal marginal value',
            'annual_dalys':   6.0e6,
            'p_success':      0.04,    # IRI base rate without platform de-risking
            'acceleration':   2,       # minimal acceleration
            'attribution':    0.15,    # INTERCEPT largely redundant (ReWiRe already running)
            'time_to_impact': 18,
            'rd_cost':        65e6,
            'daly_value':     100_000,
        },
        'Conservative': {
            'note':           'Platform works; Phase 2a signal present; Phase 3 lower bound; '
                              'HIC only',
            'annual_dalys':   7.5e6,
            'p_success':      0.09,    # p_platform~0.60 × p_drug~0.065 × portfolio~1 lead
            'acceleration':   5,
            'attribution':    0.30,
            'time_to_impact': 15,
            'rd_cost':        65e6,
            'daly_value':     100_000,
        },
        'Moderate': {
            'note':           'Synthesis midpoint; trauma/HS + ECPR; n_leads=1.7; attribution 43%',
            'annual_dalys':   8.5e6,
            'p_success':      0.17,    # p_platform~0.64 × p_drug_portfolio~0.167 (n=1.7)
            'acceleration':   7,
            'attribution':    0.43,
            'time_to_impact': 14,
            'rd_cost':        70e6,
            'daly_value':     100_000,
        },
        'Optimistic': {
            'note':           'Strong platform; Phase 3 funded/successful; LMIC emerging; '
                              'n_leads=2',
            'annual_dalys':   11.0e6,
            'p_success':      0.22,    # p_platform~0.72 × p_drug_portfolio~0.29 (n=2)
            'acceleration':   8,
            'attribution':    0.58,
            'time_to_impact': 12,
            'rd_cost':        65e6,
            'daly_value':     100_000,
        },
        'Transformative': {
            'note':           'TXA-equivalent global adoption; 3 indications; LMIC accessible; '
                              'n_leads=3',
            'annual_dalys':   15.0e6,
            'p_success':      0.33,    # p_platform~0.80 × p_drug_portfolio~0.41 (n=3)
            'acceleration':   10,
            'attribution':    0.70,
            'time_to_impact': 10,
            'rd_cost':        70e6,
            'daly_value':     100_000,
        },
    }

    rows = []
    for name, p in scenarios.items():
        df             = (1 + r) ** (-p['time_to_impact'])
        expected_dalys = p['annual_dalys'] * p['acceleration'] * p['p_success']
        roi            = (expected_dalys * df * p['daly_value'] * p['attribution']) / p['rd_cost']
        rows.append({
            'Scenario':           name,
            'Note':               p['note'],
            'Annual DALYs (M)':   p['annual_dalys'] / 1e6,
            'P(success)':         p['p_success'],
            'Accel (yr)':         p['acceleration'],
            'Attribution':        p['attribution'],
            'Discount':           round(df, 3),
            'ROI Multiple':       roi,
            'Meets 2100x':        '✓' if roi > 2100 else '✗',
        })
    return rows


# =============================================================================
# VISUALIZATION  (3×3 grid, 9 panels)
# =============================================================================

def create_plots(results, stats_dict, correlations):
    """Generate 3×3 panel visualisation incorporating all 6 corrections."""

    fig = plt.figure(figsize=(21, 19))
    fig.suptitle(
        'INTERCEPT Monte Carlo v2 — 6-Correction SROI Analysis\n'
        'Regadenoson / A2A Agonist in Trauma & Hemorrhagic Shock',
        fontsize=13, fontweight='bold', y=0.99
    )
    gs = GridSpec(3, 3, figure=fig, hspace=0.48, wspace=0.38)

    roi = results['roi_multiple']

    # --- Panel 1: ROI distribution ---
    ax1 = fig.add_subplot(gs[0, 0])
    log_roi = np.log10(np.clip(roi, 1, None))
    ax1.hist(log_roi, bins=80, density=True, alpha=0.7, color='steelblue', edgecolor='white')
    ax1.axvline(np.log10(2100), color='red', linestyle='--', lw=2, label='2100× threshold')
    ax1.axvline(np.log10(max(stats_dict['median_roi'], 1.1)), color='green', lw=2,
                label=f'Median: {stats_dict["median_roi"]:.0f}×')
    ax1.set_xlabel('ROI (log₁₀ scale)')
    ax1.set_ylabel('Density')
    ax1.set_title(f'ROI Distribution\nP(>2100×) = {stats_dict["prob_above_2100"]*100:.1f}%')
    ax1.legend(fontsize=7)
    ax1.set_xlim([0, 6])
    ax1.set_xticks([0, 1, 2, 3, 4, 5, 6])
    ax1.set_xticklabels(['1', '10', '100', '1k', '10k', '100k', '1M'])

    # --- Panel 2: P(success) staged decomposition ---
    ax2 = fig.add_subplot(gs[0, 1])
    stages = [
        (results['p_platform'],       'P(platform)',         'cornflowerblue'),
        (results['p_phase3_funded'],   'P(Phase 3 funded)',   'mediumseagreen'),
        (results['p_phase3_success'],  'P(Phase 3 success)',  'orange'),
        (results['p_adoption'],        'P(adoption)',         'mediumpurple'),
        (results['p_success'],         'P(success) — product','firebrick'),
    ]
    for arr, label, color in stages:
        ax2.hist(arr * 100, bins=60, density=True, alpha=0.55, color=color,
                 edgecolor='white', label=label)
    ax2.axvline(stats_dict['mean_p_success'] * 100, color='black', linestyle='--', lw=1.5,
                label=f'E[P(success)]={stats_dict["mean_p_success"]*100:.0f}%')
    ax2.set_xlabel('Probability (%)')
    ax2.set_ylabel('Density')
    ax2.set_title(
        f'Staged P(success)\n'
        f'E[platform]={stats_dict["mean_p_platform"]*100:.0f}%  '
        f'E[drug/lead]={stats_dict["mean_p_drug_per_lead"]*100:.0f}%  '
        f'E[portfolio]={stats_dict["mean_p_drug_portfolio"]*100:.0f}%'
    )
    ax2.legend(fontsize=6, loc='upper right')

    # --- Panel 3: Attribution fraction (Gap 1) ---
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.hist(results['attribution'] * 100, bins=50, density=True,
             alpha=0.7, color='darkorange', edgecolor='white')
    ax3.axvline(stats_dict['mean_attribution'] * 100, color='black', linestyle='--', lw=1.5,
                label=f'Mean: {stats_dict["mean_attribution"]*100:.0f}%')
    ax3.axvline(100, color='red', linestyle=':', lw=1.5, label='v1 assumption (100%)')
    ax3.set_xlabel('Attribution fraction (%)')
    ax3.set_ylabel('Density')
    ax3.set_title(
        f'Counterfactual Attribution\n'
        f'Mean {stats_dict["mean_attribution"]*100:.0f}%  '
        f'[v1 assumed 100% — ReWiRe already registered]'
    )
    ax3.legend(fontsize=7)

    # --- Panel 4: HIC vs LMIC arms (Gap 4) ---
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.hist(results['hic_arm'] / 1e6, bins=50, density=True,
             alpha=0.7, color='royalblue', edgecolor='white',
             label=f'HIC  (mean {stats_dict["mean_hic_arm_M"]:.1f}M)')
    ax4.hist(results['lmic_arm'] / 1e6, bins=50, density=True,
             alpha=0.7, color='coral', edgecolor='white',
             label=f'LMIC (mean {stats_dict["mean_lmic_arm_M"]:.1f}M)')
    ax4.set_xlabel('Annual Addressable DALYs (M)')
    ax4.set_ylabel('Density')
    ax4.set_title(
        'HIC vs LMIC Addressable Arms\n'
        'HIC: high access, smaller burden  |  LMIC: large burden, low EMS access'
    )
    ax4.legend(fontsize=8)

    # --- Panel 5: Acceleration ---
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.hist(results['acceleration'], bins=50, density=True,
             alpha=0.7, color='mediumpurple', edgecolor='white')
    ax5.axvline(np.mean(results['acceleration']), color='black', linestyle='--', lw=1.5,
                label=f'Mean: {np.mean(results["acceleration"]):.1f} yr')
    ax5.set_xlabel('Acceleration (years)')
    ax5.set_ylabel('Density')
    ax5.set_title(
        f'Acceleration vs BAU\n'
        f'TXA precedent: 14 yr without INTERCEPT | synthesis: 5-10 yr speed-up'
    )
    ax5.legend(fontsize=8)

    # --- Panel 6: Discount factor (Gap 5) ---
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.hist(results['discount_factor'], bins=50, density=True,
             alpha=0.7, color='slategray', edgecolor='white')
    ax6.axvline(stats_dict['mean_discount_factor'], color='black', linestyle='--', lw=1.5,
                label=f'Mean: {stats_dict["mean_discount_factor"]:.2f}')
    ax6.axvline(1.0, color='red', linestyle=':', lw=1.5, label='v1 (no discounting)')
    ax6.set_xlabel('Discount factor  (1+r)^−T')
    ax6.set_ylabel('Density')
    ax6.set_title(
        f'Time Discount Factor\n'
        f'Mean T={stats_dict["mean_time_to_impact"]:.0f} yr at r=3% → '
        f'factor≈{stats_dict["mean_discount_factor"]:.2f}'
    )
    ax6.legend(fontsize=7)

    # --- Panel 7: Portfolio / n_leads (Gap 3) ---
    ax7 = fig.add_subplot(gs[2, 0])
    lead_vals = [1, 2, 3, 4, 5]
    lead_probs = [0.50, 0.30, 0.13, 0.05, 0.02]
    ax7.bar(lead_vals, [p * 100 for p in lead_probs],
            color='mediumseagreen', alpha=0.75, edgecolor='white')
    ax7.axvline(stats_dict['mean_n_leads'], color='black', linestyle='--', lw=1.5,
                label=f'E[n]={stats_dict["mean_n_leads"]:.2f}')
    ax7b = ax7.twinx()
    p_per = stats_dict['mean_p_drug_per_lead']
    port_probs = [(1 - (1 - p_per) ** k) * 100 for k in lead_vals]
    ax7b.plot(lead_vals, port_probs, 'rs--', linewidth=1.5, markersize=5,
              label='P(≥1 lead succeeds)')
    ax7b.set_ylabel('P(portfolio success) %', color='red', fontsize=8)
    ax7b.tick_params(axis='y', colors='red')
    ax7.set_xlabel('Number of viable leads identified by platform')
    ax7.set_ylabel('Probability of N leads (%)', color='green')
    ax7.tick_params(axis='y', colors='green')
    ax7.set_title(
        'Portfolio Effect\n'
        f'P(drug/lead)≈{p_per*100:.0f}% → '
        f'P(portfolio|n=2)≈{(1-(1-p_per)**2)*100:.0f}%'
    )
    lines1, lab1 = ax7.get_legend_handles_labels()
    lines2, lab2 = ax7b.get_legend_handles_labels()
    ax7.legend(lines1 + lines2, lab1 + lab2, fontsize=7)

    # --- Panel 8: Sensitivity tornado (13 parameters) ---
    ax8 = fig.add_subplot(gs[2, 1])
    labels_clean = {
        'hic_arm':           'HIC addressable DALYs',
        'lmic_arm':          'LMIC addressable DALYs',
        'p_platform':        'P(OoC/DT platform validates)',
        'p_phase3_funded':   'P(Phase 3 funded | 2a+)',
        'p_phase3_success':  'P(Phase 3 success | funded)',
        'p_adoption':        'P(adoption | approval)',
        'n_leads':           'N viable leads (portfolio)',
        'attribution':       'Attribution fraction',
        'acceleration':      'Acceleration (years)',
        'discount_rate':     'Discount rate r',
        'time_to_impact':    'Time to impact T (years)',
        'rd_cost':           'R&D cost',
        'daly_value':        'DALY value ($)',
    }
    params   = list(correlations.keys())
    corrs    = [correlations[p] for p in params]
    idx      = np.argsort(np.abs(corrs))[::-1]
    p_sorted = [params[i] for i in idx]
    c_sorted = [corrs[i]  for i in idx]
    colors   = ['steelblue' if c > 0 else 'firebrick' for c in c_sorted]
    y_pos    = np.arange(len(p_sorted))
    ax8.barh(y_pos, c_sorted, color=colors, alpha=0.75)
    ax8.set_yticks(y_pos)
    ax8.set_yticklabels([labels_clean[p] for p in p_sorted], fontsize=7)
    ax8.set_xlabel('Pearson r with ROI')
    ax8.set_title('Sensitivity Analysis\n(13 parameters — ranked by |r|)')
    ax8.axvline(0, color='black', linewidth=0.5)
    ax8.set_xlim([-0.65, 0.65])

    # --- Panel 9: Threshold exceedance ---
    ax9 = fig.add_subplot(gs[2, 2])
    thresholds = [100, 500, 1000, 2100, 5000, 10000, 50000]
    probs      = [np.mean(roi > t) * 100 for t in thresholds]
    bar_colors = ['firebrick' if t == 2100 else 'steelblue' for t in thresholds]
    ax9.bar(range(len(thresholds)), probs, color=bar_colors, alpha=0.75, edgecolor='white')
    ax9.axhline(50, color='gray', linestyle='--', alpha=0.5)
    ax9.set_xticks(range(len(thresholds)))
    ax9.set_xticklabels([f'{t:,}×' for t in thresholds], rotation=45, fontsize=7)
    ax9.set_ylabel('Probability (%)')
    ax9.set_title('Threshold Exceedance Probabilities')
    ax9.set_ylim([0, 105])
    for i, p in enumerate(probs):
        ax9.text(i, p + 2, f'{p:.0f}%', ha='center', fontsize=7)

    out_path = f'{OUTPUT_DIR}/intercept_monte_carlo.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'  Saved: {out_path}')


def create_pareto_frontier_plot():
    """
    Pareto frontier updated for v2: axes now show P(success) and attribution-weighted
    annual addressable DALYs, with discount factor baked into threshold lines.
    Three acceleration curves; reference lines from the five scenarios.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    rd_cost      = 65e6
    daly_value   = 100_000
    threshold    = 2100
    attribution  = 0.43    # Moderate scenario value
    discount_f   = 0.661   # (1.03)^-14

    # Effective threshold accounting for attribution and discounting
    # ROI = annual_dalys × accel × p_success × df × daly_value × attr / rd_cost > threshold
    # → annual_dalys × p_success > threshold × rd_cost / (accel × df × daly_value × attr)
    accelerations = [3, 5, 7, 10, 15]
    colors = ['#d73027', '#f46d43', '#4daf4a', '#377eb8', '#7b2d8b']
    p_range = np.linspace(0.005, 0.40, 300)

    for accel, color in zip(accelerations, colors):
        required = (threshold * rd_cost) / (daly_value * accel * discount_f * attribution * p_range)
        valid = required <= 20e6
        if valid.any():
            ax.plot(p_range[valid] * 100, required[valid] / 1e6,
                    color=color, linewidth=2.5, label=f'{accel}-yr acceleration')
            ax.fill_between(p_range[valid] * 100, required[valid] / 1e6, 20,
                            color=color, alpha=0.07)

    # Scenario reference points
    scenario_refs = [
        (6.0e6,  0.04,  '✗ Platform fails/BAU\n(6M DALYs, p=4%)'),
        (7.5e6,  0.09,  '✗ Conservative\n(7.5M DALYs, p=9%)'),
        (8.5e6,  0.17,  '✓ Moderate\n(8.5M DALYs, p=17%)'),
        (11.0e6, 0.22,  '✓ Optimistic\n(11M DALYs, p=22%)'),
        (15.0e6, 0.33,  '✓ Transformative\n(15M DALYs, p=33%)'),
    ]
    marker_colors = ['firebrick', 'firebrick', 'forestgreen', 'forestgreen', 'forestgreen']
    for (dalys, ps, label), mc in zip(scenario_refs, marker_colors):
        ax.scatter(ps * 100, dalys / 1e6, s=80, color=mc, zorder=5)
        ax.annotate(label, (ps * 100, dalys / 1e6), fontsize=7,
                    xytext=(4, 4), textcoords='offset points', color=mc)

    ax.set_xlabel('P(success) = P(platform) × P(drug portfolio) — (%)', fontsize=11)
    ax.set_ylabel('Annual Addressable DALYs (millions)', fontsize=11)
    ax.set_title(
        'Pareto Frontier v2: Requirements to Clear 2,100× Threshold\n'
        f'(attribution={attribution}, discount factor={discount_f:.2f} [r=3%, T=14yr], '
        f'rd_cost=${rd_cost/1e6:.0f}M, DALY=${daly_value/1e3:.0f}k)',
        fontsize=10
    )
    ax.legend(loc='upper right', fontsize=9, title='Acceleration')
    ax.set_xlim([0, 40])
    ax.set_ylim([0, 18])
    ax.grid(True, alpha=0.3)

    out_path = f'{OUTPUT_DIR}/intercept_pareto_frontier.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'  Saved: {out_path}')


# =============================================================================
# REPORT
# =============================================================================

def print_report(stats_dict, correlations, scenarios):
    """Print comprehensive v2 report including calibration flag and VOI guidance."""

    labels_clean = {
        'hic_arm':           'HIC addressable DALYs',
        'lmic_arm':          'LMIC addressable DALYs',
        'p_platform':        'P(OoC/DT platform validates A2A)',
        'p_phase3_funded':   'P(Phase 3 funded | Phase 2a positive)',
        'p_phase3_success':  'P(Phase 3 RCT success | funded + OoC)',
        'p_adoption':        'P(guideline adoption | approval)',
        'n_leads':           'N viable leads (portfolio effect)',
        'attribution':       'Counterfactual attribution fraction',
        'acceleration':      'Acceleration vs BAU (years)',
        'discount_rate':     'Annual discount rate r',
        'time_to_impact':    'Time to impact midpoint T (years)',
        'rd_cost':           'R&D cost',
        'daly_value':        'DALY value ($)',
    }

    sorted_corrs = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)
    top3 = [k for k, v in sorted_corrs[:3]]

    voi_text = {
        'p_phase3_success':  (
            'IRI pharmacologist / independent ReWiRe trialist (NOT Karim\'s group)\n'
            '    Questions: Is regadenoson safe in hypotensive patients? (vasodilatory risk)\n'
            '    What is the realistic Phase 2a success criterion and enrolment status?\n'
            '    Does OoC comorbidity modelling change Phase 3 design confidence at all?'
        ),
        'p_platform':        (
            'Independent OoC/organ-chip expert\n'
            '    Questions: Is kidney-chip-to-IRI-drug-efficacy-prediction a validated milestone\n'
            '    or still basic research? What is the gap between DILI prediction (proven) and\n'
            '    IRI efficacy prediction? What timeline to pharma-grade OoC IRI validation?'
        ),
        'hic_arm':           (
            'Trauma EMS/prehospital implementation expert\n'
            '    Questions: What fraction of HIC hemorrhagic shock patients are TBI-free and\n'
            '    reach a hospital with IV drug capacity within the 2h window? What is the\n'
            '    realistic prehospital IV drug uptake rate (cf. TXA underuse data)?'
        ),
        'lmic_arm':          (
            'Global health / LMIC emergency medicine expert\n'
            '    Questions: What fraction of LMIC trauma deaths occur in a setting where a\n'
            '    prehospital IV drug could realistically be administered? Cold chain feasibility\n'
            '    for regadenoson in LMIC EMS? What formulation would change this?'
        ),
        'attribution':       (
            'ARIA / CDMRP / funding landscape expert\n'
            '    Questions: Would CDMRP JWMRP fund a Phase 3 if ReWiRe Phase 2a is positive?\n'
            '    What is ARIA\'s appetite for this niche without INTERCEPT\'s OoC platform?\n'
            '    What is the realistic counterfactual — would another funder do this in 5 yr?'
        ),
        'p_phase3_funded':   (
            'Pharma business development / translational medicine expert\n'
            '    Questions: Would a Phase 2a safety+signal result attract pharma Phase 3 funding\n'
            '    for regadenoson (generic) in trauma? What Phase 2b data would pharma require?\n'
            '    Is a BARDA/Biomedical Advanced Research partnership feasible for this niche?'
        ),
        'acceleration':      (
            'ARIA / CDMRP / funding landscape expert (see attribution above)\n'
            '    Drives both attribution and acceleration estimates — same expert conversation.'
        ),
        'p_adoption':        (
            'EMS medical director / prehospital protocol expert\n'
            '    Questions: Given TXA underuse, what would drive adoption of a second IV trauma\n'
            '    drug? What implementation infrastructure would be needed? Autoinjector feasible?'
        ),
    }

    # Build VOI section from top 3 sensitivity drivers
    voi_section = '\nEXPERT INTERVIEW PRIORITIES (Value of Information — top 3 sensitivity drivers)\n'
    voi_section += '  Based on sensitivity analysis, these conversations have highest expected VOI:\n\n'
    rank = 1
    seen = set()
    for param, corr in sorted_corrs:
        if param in voi_text and param not in seen:
            voi_section += f'  {rank}. [{labels_clean[param]}  r={corr:+.3f}]\n'
            voi_section += f'     {voi_text[param]}\n\n'
            seen.add(param)
            rank += 1
            if rank > 3:
                break

    report = f"""
================================================================================
INTERCEPT MONTE CARLO v2 — 6-CORRECTION SROI REPORT
Open Philanthropy Cost-Effectiveness Analysis | March 2026

V2 CORRECTIONS APPLIED
  1. Attribution fraction:  β(3,4) → mode 40%, mean 43%  [was 100% — ReWiRe already registered]
  2. Staged drug funding:   P(Phase3 funded) × P(Phase3 success) × P(adoption)
                            replaces single Beta(4,9) block
  3. Portfolio effect:      P(≥1 of n leads succeeds) = 1−(1−p_per_lead)^n_leads
                            E[n_leads]≈1.7; boosts P(drug) by ~50% vs single-lead
  4. HIC/LMIC split:        HIC lognormal(5M, σ=0.45) + LMIC lognormal(3.5M, σ=0.60)
                            replaces single global_dalys × addressable_fraction
  5. Time discounting:      discount_factor = (1+r)^−T; Tri(1%,3%,5%) × Tri(8,14,22yr)
                            E[factor]≈{stats_dict['mean_discount_factor']:.2f}  [was 1.0 — no discounting]
  6. VOI guidance:          Expert interview priorities added to report (see below)

INVESTMENT PROFILE
  Program cost:  $40-120M (modal $60M)
  DALY value:    $50k-150k (OpenPhil benchmark ~$100k)
  Threshold:     2,100× ROI
  Simulations:   {N_SIMS:,}

P(SUCCESS) DECOMPOSITION
  E[P(platform validates A2A)]:     {stats_dict['mean_p_platform']*100:>5.1f}%
  E[P(Phase 3 funded | 2a+)]:       {stats_dict['mean_p_phase3_funded']*100:>5.1f}%
  E[P(Phase 3 success | funded)]:   {stats_dict['mean_p_phase3_success']*100:>5.1f}%
  E[P(adoption | approval)]:        {stats_dict['mean_p_adoption']*100:>5.1f}%
  ──────────────────────────────────────────────
  E[P(drug success per lead)]:       {stats_dict['mean_p_drug_per_lead']*100:>5.1f}%
  E[n viable leads]:                 {stats_dict['mean_n_leads']:>5.2f}
  E[P(portfolio ≥1 lead succeeds)]:  {stats_dict['mean_p_drug_portfolio']*100:>5.1f}%
  E[P(success)] = E[platform×port]:  {stats_dict['mean_p_success']*100:>5.1f}%

  ⚠ CALIBRATION FLAG: stage-product E[P(drug/lead)] ≈ {stats_dict['mean_p_drug_per_lead']*100:.0f}% is below
  the v1 synthesis holistic estimate (25-35%). The decomposition reveals that the
  synthesis estimate requires above-average performance on ALL stages simultaneously.
  The staged model is more conservative and transparent. Priority expert interview:
  the Phase 3 success probability (see VOI section).

NEW CORRECTION FACTORS
  E[attribution]:            {stats_dict['mean_attribution']*100:>5.1f}%  (v1: 100%)
  E[discount factor]:        {stats_dict['mean_discount_factor']:>5.3f}  (v1: 1.000 — no discounting)
  E[time to impact]:         {stats_dict['mean_time_to_impact']:>5.1f} yr
  E[HIC arm]:                {stats_dict['mean_hic_arm_M']:>5.1f}M DALYs/yr
  E[LMIC arm]:               {stats_dict['mean_lmic_arm_M']:>5.1f}M DALYs/yr

SIMULATION RESULTS
  Mean ROI:            {stats_dict['mean_roi']:>12,.0f}×
  Median ROI:          {stats_dict['median_roi']:>12,.0f}×
  5th percentile:      {stats_dict['p5_roi']:>12,.0f}×
  25th percentile:     {stats_dict['p25_roi']:>12,.0f}×
  75th percentile:     {stats_dict['p75_roi']:>12,.0f}×
  95th percentile:     {stats_dict['p95_roi']:>12,.0f}×

THRESHOLD EXCEEDANCE
  P(ROI > 1,000×):    {stats_dict['prob_above_1000']*100:>6.1f}%
  P(ROI > 2,100×):    {stats_dict['prob_above_2100']*100:>6.1f}%  ← Open Philanthropy bar
  P(ROI > 5,000×):    {stats_dict['prob_above_5000']*100:>6.1f}%
  P(ROI > 10,000×):   {stats_dict['prob_above_10000']*100:>6.1f}%

SENSITIVITY ANALYSIS (ranked by |Pearson r| with ROI)
"""
    for param, corr in sorted_corrs:
        direction = '↑' if corr > 0 else '↓'
        report += f'  {labels_clean[param]:<48s} {direction}  r = {corr:+.3f}\n'

    report += f"""
{voi_section}
SCENARIO COMPARISON (fixed-parameter; r=3% discount rate applied)
  ⚠ Key finding: with attribution + discounting, Conservative FAILS the threshold.
    Clearing 2,100× requires at least Moderate assumptions on every dimension.
{'─'*110}
{'Scenario':<28} {'Ann.DALYs':>9} {'P(succ)':>8} {'Accel':>6} {'Attr':>6} {'Disc.F':>7} {'ROI':>10}  {'Pass':>4}
{'─'*110}
"""
    for s in scenarios:
        report += (
            f"{s['Scenario']:<28} "
            f"{s['Annual DALYs (M)']:>7.1f}M "
            f"{s['P(success)']:>8.0%} "
            f"{s['Accel (yr)']:>6.0f} "
            f"{s['Attribution']:>6.0%} "
            f"{s['Discount']:>7.3f} "
            f"{s['ROI Multiple']:>10,.0f}×  "
            f"{s['Meets 2100x']:>4}\n"
        )

    verdict = (
        'STRONG CASE: High probability of meeting threshold under most scenarios.'
        if stats_dict['prob_above_2100'] > 0.70 else
        'MODERATE CASE: More likely than not to meet threshold; significant downside risk.'
        if stats_dict['prob_above_2100'] > 0.50 else
        'MARGINAL CASE: Plausible but requires favorable assumptions on multiple parameters.\n'
        '  The Moderate scenario (synthesis midpoint) just clears the threshold.'
        if stats_dict['prob_above_2100'] > 0.25 else
        'WEAK CASE: Unlikely to meet threshold without optimistic assumptions.'
    )

    report += f"""
CRITICAL RISK FACTORS
  1. Regadenoson vasodilatory safety in hypotensive trauma patients — primary Phase 2a risk.
     ReWiRe results are the single highest-value upcoming data event.
  2. IRI Phase 3 failure base rate is catastrophic (CIRCUS, CONDI2, AMISTAD-II all failed).
     A2A agonists are untested at Phase 3 — not immune to translational failure.
  3. Attribution: ReWiRe is already registered without INTERCEPT. If ARIA/CDMRP would
     fund Phase 3 anyway, INTERCEPT's marginal SROI is sharply reduced.
  4. LMIC deployment bottleneck: cold chain, IV administration, EMS access all constrain
     the large LMIC DALY burden from being practically addressable.
  5. OoC-to-IRI validation gap: DILI prediction is proven; IRI drug efficacy prediction
     is not yet clinically validated. Kidney chip adenosine result is promising but early.

VERDICT: {verdict}

Median ROI {stats_dict['median_roi']:,.0f}× is {'ABOVE' if stats_dict['median_roi'] > 2100 else 'BELOW'} the 2,100× threshold.
The v2 corrections reduce P(>2100×) from 74% (v1) to {stats_dict['prob_above_2100']*100:.0f}% (v2), primarily
driven by the attribution fraction (~43%) and time discounting (~{stats_dict['mean_discount_factor']:.2f} factor).
The portfolio effect (~+50% on P(drug)) partially offsets these corrections.

================================================================================
"""
    return report


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print('Running INTERCEPT Monte Carlo v2 (6-correction update)...')

    results      = run_simulation(N_SIMS)
    stats_dict   = analyze_results(results)
    correlations = sensitivity_analysis(results)
    scenarios    = scenario_comparison()

    report = print_report(stats_dict, correlations, scenarios)
    print(report)

    report_path = f'{OUTPUT_DIR}/intercept_analysis_report.txt'
    with open(report_path, 'w') as f:
        f.write(report)
    print(f'  Saved: {report_path}')

    print('Generating visualisations...')
    create_plots(results, stats_dict, correlations)
    create_pareto_frontier_plot()

    print(f'\nDone. Output files:')
    print(f'  {OUTPUT_DIR}/intercept_analysis_report.txt')
    print(f'  {OUTPUT_DIR}/intercept_monte_carlo.png')
    print(f'  {OUTPUT_DIR}/intercept_pareto_frontier.png')
