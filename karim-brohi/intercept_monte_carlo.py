#!/usr/bin/env python3
"""
Monte Carlo simulation for INTERCEPT cost-effectiveness (v3)
Estimating probability of meeting Open Philanthropy's 2100x threshold

v3 corrections align analysis to the Concept Note v2 (Karim Brohi, Dec 2025):
  - Reframes from A2A-specific to survival therapeutics discovery engine
  - Expands DALY scope to trauma + MI + stroke + PPH (concept note indications)
  - Fixes n_leads to peak at 5 (Year 5 milestone: "5+ qualified leads")
  - Fixes programme cost to ~£40M (~$51M) as stated in concept note
  - Adds platform-independent value pathway (diagnostics, spinouts, playbooks)
  - Retains v2 corrections: attribution, staged drug, portfolio, HIC/LMIC, discounting

v2 corrections retained:
  1. Counterfactual attribution fraction  (was: 100% credit assumed)
  2. Follow-on funding as a distinct node (was: collapsed into one P(drug))
  3. Portfolio effect of platform         (was: single binary drug outcome)
  4. HIC vs LMIC deployment split         (was: single blended addressable fraction)
  5. Time discounting of future DALYs     (was: undiscounted)
  6. VOI expert interview guidance        (was: absent from report)

Evidence base: karim-brohi/ 8-priority literature review (March 2026)
Concept note: "005 Karim Brohi Concept Note v2.pdf"

Key concept note claims calibrating this model:
  - "5-year programme budgeted at ~£40 million"
  - "5+ qualified leads across mechanism families" by Year 5
  - "3 priority mechanism families with cross-organ evidence"
  - Trauma as "proving ground" with extension to MI, stroke, PPH
  - "over 100,000 deaths/yr across UK and US; 120,000 disability cases"
  - Regadenoson is "proof-of-possible", not the sole asset
  - Platform outputs: atlas, OoC, digital twin, companion diagnostics,
    AI decision support, 2+ spinouts, repurposing playbook

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
# ADDRESSABLE DALY ARMS — now covers trauma + MI + stroke + PPH
# (concept note: "trauma, post-partum bleeding, heart attack and stroke")
# =============================================================================

def sample_annual_addressable_hic(n):
    """
    Annual DALYs addressable by INTERCEPT survival therapeutics in HIGH-INCOME COUNTRIES.

    Concept note scope: trauma/HS + myocardial infarction + ischaemic stroke + PPH.
    Concept note claim: "over 100,000 deaths/yr across UK and US; 120,000 disability cases"

    TRAUMA/HS component (proving ground — most advanced):
      ~60,000 US hemorrhagic shock deaths/yr (Priority 4)
      14% potentially preventable × organ-specificity filters
      ≈ 40k HIC trauma DALYs/yr (conservative)
      + ECPR contribution (Wisniewski 2024): ~500k-1M DALYs/yr

    MI component (extension via shared IRI mechanisms):
      ~800k MI events/yr in HIC; ~15% result in significant IRI damage
      despite timely reperfusion. DALY multiplier ~5-8 per preventable case
      If INTERCEPT therapies reduce IRI damage in even 20% of these:
      ~24k prevented × DALY ~6 ≈ 144k DALYs, scaling to HIC → ~500k-1.5M DALYs/yr

    STROKE component (concept note explicitly targets):
      ~1.5M ischaemic strokes/yr in HIC; IRI drives penumbra expansion
      Window extension of even 30 min could save ~5-15% of penumbra tissue
      Estimated: ~1-3M DALYs/yr addressable

    PPH component (smaller but included in concept note):
      ~50k severe PPH events/yr HIC → ~100-300k DALYs/yr

    Combined: median 8M DALYs/yr, log-normal σ=0.50
    90% CI: ~3M to ~21M DALYs/yr
    Higher than v2 (5M) because v2 modelled only trauma/HS + ECPR.
    """
    return np.random.lognormal(np.log(8e6), 0.50, n)


def sample_annual_addressable_lmic(n):
    """
    Annual DALYs addressable by INTERCEPT in LOW-AND-MIDDLE INCOME COUNTRIES.

    Concept note: "benefit is greater the farther the patient is from a hospital,
    thus massively improving equitable access to healthcare worldwide"

    LMIC carries ~80% of global trauma AND cardiovascular burden but faces
    severe deployment constraints (IV, cold chain, EMS access).

    Trauma: ~1.5M deaths/yr × filters → ~2-5% addressable = 1.5-3M DALYs/yr
    MI/stroke in LMIC: ~15M deaths/yr CVD in LMIC; even 0.5% addressable
    via hospital-administered INTERCEPT therapies = 3-5M DALYs/yr
    PPH: significant in LMIC (~300k deaths/yr), some overlap

    Net: median 6M DALYs/yr with high uncertainty
    Log-normal σ=0.65 (deployment gap is primary uncertainty)
    90% CI: ~1.8M to ~20M DALYs/yr
    """
    return np.random.lognormal(np.log(6e6), 0.65, n)


# =============================================================================
# COUNTERFACTUAL ATTRIBUTION FRACTION
# =============================================================================

def sample_attribution_fraction(n):
    """
    Fraction of eventual clinical impact attributable to INTERCEPT's investment
    vs. what would have happened in the counterfactual without INTERCEPT.

    Evidence for LOWER attribution (INTERCEPT partially redundant):
      - ReWiRe Phase 2a ALREADY REGISTERED at Queen Mary WITHOUT INTERCEPT
      - CDMRP JWMRP explicitly funds "drugs that extend the resuscitation window"
      - ARIA could fund Karim independently

    Evidence for HIGHER attribution (INTERCEPT is the marginal enabler):
      - No other OoC/DT survival therapeutics discovery engine identified
      - The platform itself (atlas + OoC + DT + EWiC) is unique infrastructure
      - Concept note: INTERCEPT creates a new category — "survival therapeutics"
      - Cross-indication playbook enables MI/stroke extension that individual
        condition-specific programmes would not achieve
      - INTERCEPT's value = platform + multiple leads, not just one drug trial

    v3 adjustment: attribution slightly higher than v2 because INTERCEPT's
    platform value (not just the drug) is harder to replicate counterfactually.
    Beta(4, 4) → mode = 50%, mean = 50%
    (v2 was Beta(3,4) → mode 40%, mean 43%)
    """
    return np.random.beta(4, 4, n)


# =============================================================================
# STAGED DRUG SUCCESS
# =============================================================================

def sample_p_platform(n):
    """
    P(OoC/digital-twin platform delivers validated discovery engine).

    Concept note TA1-TA3: pathway atlas + OoC + digital twin.
    Go/No-Go: "by Year 3, OoC/digital twins must predict human biomarkers
    within predefined thresholds"

    Supporting evidence:
      - Emulate Liver-Chip: 87%/100% DILI prediction (Ewart 2022)
      - First IND approved on OoC data alone (Qureator, 2025)
      - Kidney-on-chip adenosine protects renal IRI (Vormann 2022)
      - HS digital twin validated in porcine AND human data (Nat Comms Med, 2024)

    Tempering:
      - No OoC-to-IRI-drug-efficacy clinical validation precedent (DILI ≠ IRI)
      - Only 12% of "digital twin" studies meet NASEM criteria (Priority 6)
      - Concept note risk: "No conserved or druggable nodes emerge"

    Beta(7, 4) → mode ≈ 67%, mean ≈ 64%
    """
    return np.random.beta(7, 4, n)


def sample_p_phase3_funded(n):
    """
    P(Phase 3 RCT gets funded | Phase 2a positive + platform guidance).

    Concept note: "Enable a £100M+ Phase II to drive multiple therapeutic
    candidates through IND and first-in-human in trauma"

    This implies the concept note authors expect follow-on funding is likely,
    contingent on Phase 2a results.

    Beta(7, 3) → mode = 75%, mean = 70%
    """
    return np.random.beta(7, 3, n)


def sample_p_phase3_success(n):
    """
    P(Phase 3 RCT positive | funded + platform-guided trial design).

    BASE RATE — IRI field: catastrophically bad:
      CIRCUS (cyclosporine A): OR 1.04, NEJM 2015
      CONDI2 (remote conditioning): HR 1.10, Lancet 2019
      AMISTAD-II (non-selective adenosine): no benefit
      >1,000 stroke neuroprotectants: 0 human approvals

    INTERCEPT-specific adjustments:
      - Platform addresses comorbidity gap (#1 failure cause — Ferdinandy 2023)
      - OoC screens for human-relevant efficacy before Phase 3 commitment
      - Concept note: "Prioritise mechanistically justified with dominant OoC effect"
      - Concept note Go/No-Go: "by Year 4, trial demonstrates improvement;
        else shift emphasis to other leads"
      - Multiple mechanism families (not locked to A2A if it fails)

    v3 adjustment: slightly higher than v2 because the platform-guided approach
    directly mitigates the primary IRI failure causes, and multiple mechanism
    families provide pivot capability.
    Beta(2.5, 6) → mean ≈ 29%  (v2: Beta(2,6) → mean 25%)
    """
    return np.random.beta(2.5, 6, n)


def sample_p_adoption(n):
    """
    P(guideline adoption and field implementation | regulatory approval).

    Concept note: "Pre-build within INTERCEPT the buyer path transition lane
    to NHS/Defence/international buyers"

    The concept note explicitly designs for adoption from Year 1, including
    companion diagnostics and AI decision support for field deployment.

    Beta(6, 4) → mode = 62.5%, mean = 60%
    """
    return np.random.beta(6, 4, n)


# =============================================================================
# PORTFOLIO EFFECT — corrected to match concept note "5+ qualified leads"
# =============================================================================

def sample_n_viable_leads(n):
    """
    Number of viable therapeutic leads the platform identifies.

    Concept note Year 5 milestone: "5+ qualified leads across mechanism families"
    Concept note Year 1-3: "down-select to 3 priority mechanism families"
    Concept note: regadenoson is just "proof-of-possible" — one repurposed asset

    The programme is DESIGNED to produce 5+ leads. Probability reflects
    risk of platform underperformance, not just A2A analogues.

    v2 had: mode=1 (50%), reflecting A2A-only framing — WRONG per concept note.

    v3 distribution (aligned to concept note milestones):
      2 leads: 5%   (platform largely fails; only repurposed asset + 1 backup)
      3 leads: 15%  (one mechanism family delivers; others stall)
      4 leads: 25%  (two mechanism families deliver)
      5 leads: 35%  (target met — three families, ~2 leads each, some attrition)
      6 leads: 20%  (exceeds target)

    Expected n_leads ≈ 4.5
    """
    return np.random.choice([2, 3, 4, 5, 6], size=n, p=[0.05, 0.15, 0.25, 0.35, 0.20])


# =============================================================================
# TIME DISCOUNTING
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

    Concept note: 5-year programme + scale-up Phase II + regulatory + adoption
    Timeline for FIRST indication (trauma):
      Years 1-3: platform build
      Year 4: Phase IIa mechanistic study (within budget)
      Year 5: platform delivered, leads qualified
      Phase 3 RCT: ~3-5 yr
      Regulatory + adoption ramp: ~3-5 yr
      → Trauma midpoint: ~10-15 yr from programme start

    Extension indications (MI, stroke): +3-5 yr beyond trauma
    Weighted midpoint across indications: ~12-18 yr

    Triangular(8, 13, 20) → mode 13 yr, mean ≈ 13.7 yr
    Slightly shorter than v2 (mode 14) because concept note designs for speed.
    """
    return np.random.triangular(8, 13, 20, n)


# =============================================================================
# PROGRAMME COST — corrected to match concept note "~£40 million"
# =============================================================================

def sample_acceleration_years(n):
    """
    Years by which INTERCEPT accelerates treatment vs BAU.
    Concept note: discovery engine + EWiC clinical platform enables faster translation.
    TXA precedent: 14 yr without platform. INTERCEPT marginal speed-up: 5-10 yr.
    Triangular(2, 7, 15)
    """
    return np.random.triangular(2, 7, 15, n)


def sample_rd_cost(n):
    """
    Total INTERCEPT programme investment (the grant being evaluated).

    Concept note: "The five-year programme is budgeted at ~£40 million"
    At £1 = $1.27 → ~$51M

    This is the Phase 1 discovery engine cost ONLY.
    The £100M+ Phase II scale-up is a SEPARATE future investment.

    v2 had: Triangular($40M, $60M, $120M) — conflated Phase 1 + Phase 2.

    v3: Triangular($45M, $51M, $65M) — narrow range around £40M concept note figure.
    Upper tail ($65M) reflects modest cost overrun / currency risk only.
    """
    return np.random.triangular(45e6, 51e6, 65e6, n)


def sample_daly_value(n):
    """$/DALY averted. OpenPhil benchmark ~$100k. Triangular(50k, 100k, 150k)"""
    return np.random.triangular(50_000, 100_000, 150_000, n)


# =============================================================================
# PLATFORM-INDEPENDENT VALUE
# =============================================================================

def sample_platform_independent_value(n):
    """
    Value of INTERCEPT platform outputs EVEN IF no drug succeeds.

    Concept note describes substantial non-drug outputs:
      - Ischaemic Injury Pathway Atlas (shared public good)
      - Companion diagnostic dossiers with field-feasibility
      - AI decision support tools for emergency teams
      - 2+ spinouts
      - UK prehospital trial playbooks
      - Repurposing playbook for external performers (MI, stroke)
      - UK Survival Consortium with shared standards

    These outputs have value to the broader ecosystem even if the specific
    therapeutic leads fail in Phase 3. Estimated as a fraction of total
    programme cost that would be "returned" as ecosystem value.

    Conservative: $20-80M in ecosystem value (atlas, diagnostics, playbooks)
    This is modelled as a DALY-equivalent by dividing by DALY value.

    Triangular($20M, $40M, $80M) in direct ecosystem value.
    """
    return np.random.triangular(20e6, 40e6, 80e6, n)


# =============================================================================
# SIMULATION
# =============================================================================

def run_simulation(n_sims=N_SIMS):
    """
    Run Monte Carlo simulation aligned to Concept Note v2.

    Two ROI pathways:
      1. Drug pathway: platform → leads → Phase 3 → adoption → DALYs
      2. Platform pathway: non-drug ecosystem value (atlas, diagnostics, spinouts)

    ROI = drug_roi + platform_roi

    Drug ROI formula:
      p_drug_per_lead  = p_phase3_funded × p_phase3_success × p_adoption
      p_drug_portfolio = 1 − (1 − p_drug_per_lead)^n_leads
      p_success        = p_platform × p_drug_portfolio
      annual_addressable = hic_arm + lmic_arm
      expected_dalys     = annual_addressable × acceleration × p_success
      discount_factor    = (1 + discount_rate)^(−time_to_impact)
      discounted_dalys   = expected_dalys × discount_factor
      drug_roi           = (discounted_dalys × daly_value × attribution) / rd_cost

    Platform ROI:
      platform_roi = (platform_value × attribution × p_platform) / rd_cost
    """
    # HIC/LMIC arms (expanded to include MI + stroke + PPH)
    hic_arm            = sample_annual_addressable_hic(n_sims)
    lmic_arm           = sample_annual_addressable_lmic(n_sims)
    annual_addressable = hic_arm + lmic_arm

    # Attribution
    attribution        = sample_attribution_fraction(n_sims)

    # Platform
    p_platform         = sample_p_platform(n_sims)

    # Staged drug conditional
    p_phase3_funded    = sample_p_phase3_funded(n_sims)
    p_phase3_success   = sample_p_phase3_success(n_sims)
    p_adoption         = sample_p_adoption(n_sims)
    p_drug_per_lead    = p_phase3_funded * p_phase3_success * p_adoption

    # Portfolio (5+ leads target)
    n_leads            = sample_n_viable_leads(n_sims)
    p_drug_portfolio   = 1.0 - (1.0 - p_drug_per_lead) ** n_leads
    p_success          = p_platform * p_drug_portfolio

    # Acceleration + cost
    acceleration       = sample_acceleration_years(n_sims)
    rd_cost            = sample_rd_cost(n_sims)
    daly_value         = sample_daly_value(n_sims)

    # Discounting
    discount_rate      = sample_discount_rate(n_sims)
    time_to_impact     = sample_time_to_impact(n_sims)
    discount_factor    = (1.0 + discount_rate) ** (-time_to_impact)

    # Drug pathway ROI
    expected_dalys     = annual_addressable * acceleration * p_success
    discounted_dalys   = expected_dalys * discount_factor
    drug_roi           = (discounted_dalys * daly_value * attribution) / rd_cost

    # Platform-independent value pathway
    platform_value     = sample_platform_independent_value(n_sims)
    platform_roi       = (platform_value * attribution * p_platform) / rd_cost

    # Total ROI
    roi_multiple       = drug_roi + platform_roi

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
        'drug_roi':          drug_roi,
        'platform_value':    platform_value,
        'platform_roi':      platform_roi,
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
        # Correction factors
        'mean_attribution':      np.mean(r['attribution']),
        'mean_discount_factor':  np.mean(r['discount_factor']),
        'mean_time_to_impact':   np.mean(r['time_to_impact']),
        'mean_hic_arm_M':        np.mean(r['hic_arm']) / 1e6,
        'mean_lmic_arm_M':       np.mean(r['lmic_arm']) / 1e6,
        # New in v3
        'mean_drug_roi':         np.mean(r['drug_roi']),
        'median_drug_roi':       np.median(r['drug_roi']),
        'mean_platform_roi':     np.mean(r['platform_roi']),
        'median_platform_roi':   np.median(r['platform_roi']),
        'mean_platform_value_M': np.mean(r['platform_value']) / 1e6,
        'mean_rd_cost_M':        np.mean(r['rd_cost']) / 1e6,
    }


def sensitivity_analysis(results):
    """Pearson correlation of each parameter with ROI multiple."""
    params = [
        'hic_arm', 'lmic_arm',
        'p_platform', 'p_phase3_funded', 'p_phase3_success', 'p_adoption',
        'n_leads', 'attribution',
        'acceleration', 'discount_rate', 'time_to_impact',
        'rd_cost', 'daly_value', 'platform_value',
    ]
    return {p: np.corrcoef(results[p], results['roi_multiple'])[0, 1] for p in params}


# =============================================================================
# SCENARIO COMPARISON — updated for concept-note-aligned parameters
# =============================================================================

def scenario_comparison():
    """
    Fixed-parameter point estimates for 5 evidence-anchored scenarios.
    Updated for v3: broader DALY scope, more leads, concept-note cost.
    """
    r   = 0.03   # nominal discount rate
    rd_cost_base = 51e6  # £40M ≈ $51M

    scenarios = {
        'Platform fails / BAU': {
            'note':           'OoC fails; drug at IRI base rate; INTERCEPT adds minimal value',
            'annual_dalys':   10.0e6,
            'p_success':      0.04,
            'acceleration':   2,
            'attribution':    0.15,
            'time_to_impact': 18,
            'rd_cost':        rd_cost_base,
            'daly_value':     100_000,
            'platform_value': 15e6,
        },
        'Conservative': {
            'note':           'Platform works; Phase 2a signal; one mechanism family; trauma only',
            'annual_dalys':   12.0e6,
            'p_success':      0.12,
            'acceleration':   5,
            'attribution':    0.35,
            'time_to_impact': 15,
            'rd_cost':        rd_cost_base,
            'daly_value':     100_000,
            'platform_value': 30e6,
        },
        'Moderate': {
            'note':           'Concept note midpoint; trauma + early MI; 5 leads; attribution 50%',
            'annual_dalys':   14.0e6,
            'p_success':      0.25,
            'acceleration':   7,
            'attribution':    0.50,
            'time_to_impact': 13,
            'rd_cost':        rd_cost_base,
            'daly_value':     100_000,
            'platform_value': 40e6,
        },
        'Optimistic': {
            'note':           'Strong platform; Phase 3 success; trauma + MI + stroke; 6 leads',
            'annual_dalys':   18.0e6,
            'p_success':      0.35,
            'acceleration':   9,
            'attribution':    0.60,
            'time_to_impact': 11,
            'rd_cost':        rd_cost_base,
            'daly_value':     100_000,
            'platform_value': 60e6,
        },
        'Transformative': {
            'note':           'All indications; global adoption; multiple mechanism families succeed',
            'annual_dalys':   25.0e6,
            'p_success':      0.45,
            'acceleration':   12,
            'attribution':    0.70,
            'time_to_impact': 10,
            'rd_cost':        55e6,
            'daly_value':     100_000,
            'platform_value': 80e6,
        },
    }

    rows = []
    for name, p in scenarios.items():
        df             = (1 + r) ** (-p['time_to_impact'])
        expected_dalys = p['annual_dalys'] * p['acceleration'] * p['p_success']
        drug_roi       = (expected_dalys * df * p['daly_value'] * p['attribution']) / p['rd_cost']
        plat_roi       = (p['platform_value'] * p['attribution'] * 0.64) / p['rd_cost']  # E[p_platform]
        total_roi      = drug_roi + plat_roi
        rows.append({
            'Scenario':           name,
            'Note':               p['note'],
            'Annual DALYs (M)':   p['annual_dalys'] / 1e6,
            'P(success)':         p['p_success'],
            'Accel (yr)':         p['acceleration'],
            'Attribution':        p['attribution'],
            'Discount':           round(df, 3),
            'Drug ROI':           drug_roi,
            'Platform ROI':       plat_roi,
            'ROI Multiple':       total_roi,
            'Meets 2100x':        '✓' if total_roi > 2100 else '✗',
        })
    return rows


# =============================================================================
# VISUALIZATION  (3×3 grid, 9 panels)
# =============================================================================

def create_plots(results, stats_dict, correlations):
    """Generate 3×3 panel visualisation."""

    fig = plt.figure(figsize=(21, 19))
    fig.suptitle(
        'INTERCEPT Monte Carlo v3 — Concept-Note-Aligned SROI Analysis\n'
        'Survival Therapeutics Discovery Engine (Trauma + MI + Stroke + PPH)',
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

    # --- Panel 3: Drug vs Platform ROI decomposition ---
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.hist(np.log10(np.clip(results['drug_roi'], 1, None)), bins=60, density=True,
             alpha=0.6, color='steelblue', edgecolor='white', label='Drug pathway')
    ax3.hist(np.log10(np.clip(results['platform_roi'], 0.1, None)), bins=60, density=True,
             alpha=0.6, color='darkorange', edgecolor='white', label='Platform pathway')
    ax3.axvline(np.log10(2100), color='red', linestyle='--', lw=1.5, label='2100× threshold')
    ax3.set_xlabel('ROI component (log₁₀)')
    ax3.set_ylabel('Density')
    ax3.set_title(
        f'Drug vs Platform ROI Pathways\n'
        f'Drug median: {stats_dict["median_drug_roi"]:.0f}×  |  '
        f'Platform mean: {stats_dict["mean_platform_roi"]:.0f}×'
    )
    ax3.legend(fontsize=7)

    # --- Panel 4: HIC vs LMIC arms ---
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
        'Trauma + MI + Stroke + PPH (concept note scope)'
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
        f'TXA precedent: 14 yr | INTERCEPT platform speed-up'
    )
    ax5.legend(fontsize=8)

    # --- Panel 6: Discount factor ---
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.hist(results['discount_factor'], bins=50, density=True,
             alpha=0.7, color='slategray', edgecolor='white')
    ax6.axvline(stats_dict['mean_discount_factor'], color='black', linestyle='--', lw=1.5,
                label=f'Mean: {stats_dict["mean_discount_factor"]:.2f}')
    ax6.axvline(1.0, color='red', linestyle=':', lw=1.5, label='No discounting')
    ax6.set_xlabel('Discount factor  (1+r)^−T')
    ax6.set_ylabel('Density')
    ax6.set_title(
        f'Time Discount Factor\n'
        f'Mean T={stats_dict["mean_time_to_impact"]:.0f} yr at r=3% → '
        f'factor≈{stats_dict["mean_discount_factor"]:.2f}'
    )
    ax6.legend(fontsize=7)

    # --- Panel 7: Portfolio / n_leads ---
    ax7 = fig.add_subplot(gs[2, 0])
    lead_vals = [2, 3, 4, 5, 6]
    lead_probs = [0.05, 0.15, 0.25, 0.35, 0.20]
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
    ax7.set_xlabel('Number of viable leads (concept note target: 5+)')
    ax7.set_ylabel('Probability of N leads (%)', color='green')
    ax7.tick_params(axis='y', colors='green')
    ax7.set_title(
        'Portfolio Effect (Concept Note: "5+ qualified leads")\n'
        f'P(drug/lead)≈{p_per*100:.0f}% → '
        f'P(portfolio|n=5)≈{(1-(1-p_per)**5)*100:.0f}%'
    )
    lines1, lab1 = ax7.get_legend_handles_labels()
    lines2, lab2 = ax7b.get_legend_handles_labels()
    ax7.legend(lines1 + lines2, lab1 + lab2, fontsize=7)

    # --- Panel 8: Sensitivity tornado (14 parameters) ---
    ax8 = fig.add_subplot(gs[2, 1])
    labels_clean = {
        'hic_arm':           'HIC addressable DALYs',
        'lmic_arm':          'LMIC addressable DALYs',
        'p_platform':        'P(platform delivers engine)',
        'p_phase3_funded':   'P(Phase 3 funded | 2a+)',
        'p_phase3_success':  'P(Phase 3 success | funded)',
        'p_adoption':        'P(adoption | approval)',
        'n_leads':           'N viable leads (portfolio)',
        'attribution':       'Attribution fraction',
        'acceleration':      'Acceleration (years)',
        'discount_rate':     'Discount rate r',
        'time_to_impact':    'Time to impact T (years)',
        'rd_cost':           'Programme cost',
        'daly_value':        'DALY value ($)',
        'platform_value':    'Platform ecosystem value',
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
    ax8.set_title('Sensitivity Analysis\n(14 parameters — ranked by |r|)')
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
    Pareto frontier: P(success) vs annual DALYs needed to clear 2100×.
    Updated for v3 parameters.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    rd_cost      = 51e6     # £40M concept note
    daly_value   = 100_000
    threshold    = 2100
    attribution  = 0.50     # v3 moderate
    discount_f   = 0.681    # (1.03)^-13

    accelerations = [3, 5, 7, 10, 15]
    colors = ['#d73027', '#f46d43', '#4daf4a', '#377eb8', '#7b2d8b']
    p_range = np.linspace(0.005, 0.50, 300)

    for accel, color in zip(accelerations, colors):
        required = (threshold * rd_cost) / (daly_value * accel * discount_f * attribution * p_range)
        valid = required <= 30e6
        if valid.any():
            ax.plot(p_range[valid] * 100, required[valid] / 1e6,
                    color=color, linewidth=2.5, label=f'{accel}-yr acceleration')
            ax.fill_between(p_range[valid] * 100, required[valid] / 1e6, 30,
                            color=color, alpha=0.07)

    # Scenario reference points
    scenario_refs = [
        (10.0e6,  0.04,  '✗ Platform fails/BAU'),
        (12.0e6,  0.12,  '✗ Conservative'),
        (14.0e6,  0.25,  '✓ Moderate'),
        (18.0e6,  0.35,  '✓ Optimistic'),
        (25.0e6,  0.45,  '✓ Transformative'),
    ]
    marker_colors = ['firebrick', 'firebrick', 'forestgreen', 'forestgreen', 'forestgreen']
    for (dalys, ps, label), mc in zip(scenario_refs, marker_colors):
        ax.scatter(ps * 100, dalys / 1e6, s=80, color=mc, zorder=5)
        ax.annotate(label, (ps * 100, dalys / 1e6), fontsize=7,
                    xytext=(4, 4), textcoords='offset points', color=mc)

    ax.set_xlabel('P(success) = P(platform) × P(drug portfolio) — (%)', fontsize=11)
    ax.set_ylabel('Annual Addressable DALYs (millions)', fontsize=11)
    ax.set_title(
        'Pareto Frontier v3: Requirements to Clear 2,100× Threshold\n'
        f'(attribution={attribution}, discount factor={discount_f:.2f} [r=3%, T=13yr], '
        f'cost=${rd_cost/1e6:.0f}M, DALY=${daly_value/1e3:.0f}k)',
        fontsize=10
    )
    ax.legend(loc='upper right', fontsize=9, title='Acceleration')
    ax.set_xlim([0, 50])
    ax.set_ylim([0, 30])
    ax.grid(True, alpha=0.3)

    out_path = f'{OUTPUT_DIR}/intercept_pareto_frontier.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'  Saved: {out_path}')


# =============================================================================
# REPORT
# =============================================================================

def print_report(stats_dict, correlations, scenarios):
    """Print comprehensive v3 report."""

    labels_clean = {
        'hic_arm':           'HIC addressable DALYs (trauma+MI+stroke+PPH)',
        'lmic_arm':          'LMIC addressable DALYs (trauma+MI+stroke+PPH)',
        'p_platform':        'P(platform delivers discovery engine)',
        'p_phase3_funded':   'P(Phase 3 funded | Phase 2a positive)',
        'p_phase3_success':  'P(Phase 3 RCT success | funded + platform)',
        'p_adoption':        'P(guideline adoption | approval)',
        'n_leads':           'N viable leads (concept note target: 5+)',
        'attribution':       'Counterfactual attribution fraction',
        'acceleration':      'Acceleration vs BAU (years)',
        'discount_rate':     'Annual discount rate r',
        'time_to_impact':    'Time to impact midpoint T (years)',
        'rd_cost':           'Programme cost (~£40M)',
        'daly_value':        'DALY value ($)',
        'platform_value':    'Platform ecosystem value (non-drug)',
    }

    sorted_corrs = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)

    voi_text = {
        'p_phase3_success':  (
            'IRI pharmacologist / independent trialist (NOT Karim\'s group)\n'
            '    Questions: Can survival therapeutics (upstream cascade modulators) overcome\n'
            '    the IRI Phase 3 failure base rate? Does OoC comorbidity modelling\n'
            '    materially change Phase 3 design confidence? What is the realistic\n'
            '    probability across 3 mechanism families (not just A2A)?'
        ),
        'p_platform':        (
            'Independent OoC/organ-chip expert\n'
            '    Questions: Can the concept note\'s TA1-TA3 engine (atlas + OoC + DT)\n'
            '    be built to specification in 3 years? Is the Year 3 Go/No-Go\n'
            '    ("predict human biomarkers within predefined thresholds") realistic?'
        ),
        'hic_arm':           (
            'Trauma + cardiology + stroke implementation expert\n'
            '    Questions: What fraction of MI/stroke patients could benefit from\n'
            '    prehospital IRI intervention? Is cross-indication translation from\n'
            '    trauma "proving ground" to MI/stroke realistic or aspirational?'
        ),
        'lmic_arm':          (
            'Global health / LMIC emergency medicine expert\n'
            '    Questions: What fraction of LMIC trauma + CVD deaths occur where\n'
            '    prehospital therapeutics could be administered? Formulation needs?'
        ),
        'attribution':       (
            'ARIA / CDMRP / funding landscape expert\n'
            '    Questions: Would this discovery engine be built without INTERCEPT?\n'
            '    Is the cross-indication platform (not just ReWiRe) counterfactually\n'
            '    unique? Would CDMRP fund the trauma arm alone?'
        ),
        'p_phase3_funded':   (
            'Pharma BD / translational medicine expert\n'
            '    Questions: Given 5+ platform-validated leads, what pull-through\n'
            '    rate to Phase 3 is realistic? Is £100M+ follow-on credible?'
        ),
        'acceleration':      (
            'ARIA / funding landscape expert (see attribution above)\n'
            '    Drives both attribution and acceleration — same expert conversation.'
        ),
        'p_adoption':        (
            'EMS medical director / prehospital protocol expert\n'
            '    Questions: concept note pre-builds buyer pathway — does this\n'
            '    materially improve adoption speed vs TXA precedent?'
        ),
        'n_leads':           (
            'Platform / drug discovery expert\n'
            '    Questions: Is "5+ qualified leads across mechanism families"\n'
            '    by Year 5 realistic? What is the historical hit rate for\n'
            '    platform-based drug discovery in a 5-year timeframe?'
        ),
        'platform_value':    (
            'Health economics / ecosystem value expert\n'
            '    Questions: What is the independent value of the pathway atlas,\n'
            '    companion diagnostics, and repurposing playbook? Are 2+ spinouts\n'
            '    realistic from a 5-year academic programme?'
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
INTERCEPT MONTE CARLO v3 — CONCEPT-NOTE-ALIGNED SROI REPORT
Open Philanthropy Cost-Effectiveness Analysis | March 2026

V3 CHANGES (alignment to Concept Note v2, Karim Brohi Dec 2025)
  - Reframed from A2A-specific to survival therapeutics discovery engine
  - DALY scope expanded: trauma + MI + stroke + PPH (concept note indications)
  - n_leads: mode=5 (concept note: "5+ qualified leads") — was mode=1 in v2
  - Programme cost: ~£40M (~$51M) as stated — was $40-120M in v2
  - Platform-independent value pathway added (diagnostics, spinouts, playbooks)
  - Attribution: β(4,4) mode 50% — slightly higher than v2 (platform is unique)
  - P(Phase3 success): β(2.5,6) mean 29% — slightly higher (multiple mechanisms)

V2 CORRECTIONS RETAINED
  1. Attribution fraction:  β(4,4) → mode 50%, mean 50%
  2. Staged drug funding:   P(Phase3 funded) × P(Phase3 success) × P(adoption)
  3. Portfolio effect:      P(≥1 of n leads succeeds) = 1−(1−p_per_lead)^n_leads
                            E[n_leads]≈{stats_dict['mean_n_leads']:.1f}
  4. HIC/LMIC split:        HIC lognormal(8M, σ=0.50) + LMIC lognormal(6M, σ=0.65)
  5. Time discounting:      discount_factor = (1+r)^−T
                            E[factor]≈{stats_dict['mean_discount_factor']:.2f}
  6. VOI guidance:          Expert interview priorities (see below)

INVESTMENT PROFILE
  Programme cost:  ~£40M (~$51M) — concept note figure
  DALY value:      $50k-150k (OpenPhil benchmark ~$100k)
  Threshold:       2,100× ROI
  Simulations:     {N_SIMS:,}

TWO-PATHWAY ROI MODEL
  Drug pathway:     platform → leads → Phase 3 → adoption → DALYs → ROI
  Platform pathway: ecosystem value (atlas, diagnostics, spinouts) × attribution × P(platform) / cost
  Total ROI = drug_roi + platform_roi

  Mean drug ROI:      {stats_dict['mean_drug_roi']:>10,.0f}×
  Median drug ROI:    {stats_dict['median_drug_roi']:>10,.0f}×
  Mean platform ROI:  {stats_dict['mean_platform_roi']:>10,.1f}×
  Mean platform value: ${stats_dict['mean_platform_value_M']:.0f}M
  Mean programme cost: ${stats_dict['mean_rd_cost_M']:.0f}M

P(SUCCESS) DECOMPOSITION
  E[P(platform delivers engine)]:  {stats_dict['mean_p_platform']*100:>5.1f}%
  E[P(Phase 3 funded | 2a+)]:     {stats_dict['mean_p_phase3_funded']*100:>5.1f}%
  E[P(Phase 3 success | funded)]: {stats_dict['mean_p_phase3_success']*100:>5.1f}%
  E[P(adoption | approval)]:      {stats_dict['mean_p_adoption']*100:>5.1f}%
  ──────────────────────────────────────────────
  E[P(drug success per lead)]:      {stats_dict['mean_p_drug_per_lead']*100:>5.1f}%
  E[n viable leads]:                {stats_dict['mean_n_leads']:>5.2f}  (concept note target: 5+)
  E[P(portfolio ≥1 lead succeeds)]: {stats_dict['mean_p_drug_portfolio']*100:>5.1f}%
  E[P(success)] = E[platform×port]: {stats_dict['mean_p_success']*100:>5.1f}%

  Note: With E[n_leads]≈{stats_dict['mean_n_leads']:.1f} and multiple mechanism families,
  the portfolio effect is substantial. P(portfolio)≈{stats_dict['mean_p_drug_portfolio']*100:.0f}% is
  {(stats_dict['mean_p_drug_portfolio']/stats_dict['mean_p_drug_per_lead'] - 1)*100:.0f}% higher than single-lead P(drug/lead)≈{stats_dict['mean_p_drug_per_lead']*100:.0f}%.

CORRECTION FACTORS
  E[attribution]:             {stats_dict['mean_attribution']*100:>5.1f}%
  E[discount factor]:        {stats_dict['mean_discount_factor']:>5.3f}
  E[time to impact]:         {stats_dict['mean_time_to_impact']:>5.1f} yr
  E[HIC arm]:                {stats_dict['mean_hic_arm_M']:>5.1f}M DALYs/yr  (trauma+MI+stroke+PPH)
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
        report += f'  {labels_clean[param]:<52s} {direction}  r = {corr:+.3f}\n'

    report += f"""
{voi_section}
SCENARIO COMPARISON (fixed-parameter; r=3% discount rate; includes platform ROI)
{'─'*120}
{'Scenario':<28} {'Ann.DALYs':>9} {'P(succ)':>8} {'Accel':>6} {'Attr':>6} {'Disc.F':>7} {'Drug ROI':>10} {'Plat ROI':>9} {'Total':>10}  {'Pass':>4}
{'─'*120}
"""
    for s in scenarios:
        report += (
            f"{s['Scenario']:<28} "
            f"{s['Annual DALYs (M)']:>7.1f}M "
            f"{s['P(success)']:>8.0%} "
            f"{s['Accel (yr)']:>6.0f} "
            f"{s['Attribution']:>6.0%} "
            f"{s['Discount']:>7.3f} "
            f"{s['Drug ROI']:>10,.0f}× "
            f"{s['Platform ROI']:>8,.0f}× "
            f"{s['ROI Multiple']:>10,.0f}×  "
            f"{s['Meets 2100x']:>4}\n"
        )

    verdict = (
        'STRONG CASE: High probability of meeting threshold under most scenarios.'
        if stats_dict['prob_above_2100'] > 0.70 else
        'MODERATE CASE: More likely than not to meet threshold; significant downside risk.'
        if stats_dict['prob_above_2100'] > 0.50 else
        'MARGINAL CASE: Plausible but requires favorable assumptions on multiple parameters.'
        if stats_dict['prob_above_2100'] > 0.25 else
        'WEAK CASE: Unlikely to meet threshold without optimistic assumptions.'
    )

    report += f"""
CRITICAL RISK FACTORS
  1. IRI Phase 3 failure base rate remains catastrophic (CIRCUS, CONDI2, AMISTAD-II).
     Multiple mechanism families diversify but do not eliminate this risk.
  2. Platform delivery risk: building a validated cross-organ discovery engine in
     3 years is ambitious. Go/No-Go at Year 2-3 is the critical gate.
  3. Cross-indication translation: trauma is the "proving ground" but extension to
     MI and stroke requires separate clinical validation — not automatic.
  4. Attribution: the platform (not just ReWiRe) is unique, but ARIA/CDMRP could
     fund individual condition-specific programmes without the cross-indication engine.
  5. LMIC deployment bottleneck: cold chain, IV administration, EMS access all
     constrain the large LMIC DALY burden from being practically addressable.
  6. n_leads target: "5+ qualified leads by Year 5" is aspirational. Historical
     platform drug discovery hit rates suggest 3-4 may be more realistic.
  7. Concept note claims "100k deaths + 120k disability prevented in UK/US alone"
     — this requires successful deployment across ALL indications, not just trauma.

VERDICT: {verdict}

Median ROI {stats_dict['median_roi']:,.0f}× is {'ABOVE' if stats_dict['median_roi'] > 2100 else 'BELOW'} the 2,100× threshold.
v3 vs v2: broader DALY scope, more leads, and lower cost shift the analysis
significantly upward. The concept note describes a more ambitious programme
than the v2 A2A-only framing captured.

================================================================================
"""
    return report


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print('Running INTERCEPT Monte Carlo v3 (concept-note-aligned)...')

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
