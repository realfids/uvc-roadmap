#!/usr/bin/env python3
"""
Monte Carlo simulation for INTERCEPT cost-effectiveness — SKEPTICAL ANALYST VERSION
Estimating probability of meeting Open Philanthropy's 2100x threshold

This version implements the corrections a rigorous cost-effectiveness analyst would apply
after reviewing the concept note (v3) analysis. The v3 model was calibrated against the
applicant's own concept note targets; this version treats those targets as aspirational
and applies independent, conservative priors.

KEY DIVERGENCES FROM v3 (applicant-aligned):
  1. n_leads:   v3 peaks at 5 (concept note target) → this version peaks at 1-2
                (academic platform drug discovery historical hit rate)
  2. DALYs:     v3 includes MI + stroke + PPH → this version: trauma/HS only
                (Year 4 milestone commits to ONE Phase IIa in trauma only;
                MI/stroke require separate unplanned trials)
  3. Attribution: v3 = 50% → this version = ~25%
                (each component fundable independently; INTERCEPT's marginal
                 contribution is integration, not invention)
  4. P(Phase 3 success): v3 = 29% → this version = 18%
                (near IRI base rate; OoC gets limited credit without IRI precedent)
  5. P(platform): v3 = 64% → this version = 50%
                (DILI OoC prediction proven; IRI drug efficacy prediction is not)
  6. Discount rate: v3 Tri(1%,3%,5%) → this version Tri(3%,5%,7%)
                (higher rate appropriate for high-uncertainty, long-horizon programme)
  7. Platform value: v3 Tri($20M,$40M,$80M) → this version Tri($5M,$15M,$30M)
                (academic programmes rarely produce commercial spinouts at concept note scale)
  8. Acceleration: v3 Tri(2,7,15) → this version Tri(1,4,10)
                (platform not yet proven; speed-up is undemonstrated)

The £40M programme cost denominator is RETAINED — this is appropriate for evaluating
this specific grant. The Phase 3 cost (£100M+) is a separate future decision and is
already discounted via P(Phase3_funded).

Compare outputs with intercept_monte_carlo.py (v3, applicant-aligned) to see the
full range of defensible estimates.
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
# ADDRESSABLE DALY ARMS — trauma/HS only (Year 4 milestone proving ground)
# =============================================================================

def sample_annual_addressable_hic(n):
    """
    Annual DALYs addressable in HIGH-INCOME COUNTRIES — trauma/HS only.

    SKEPTICAL RATIONALE:
    The concept note calls trauma the "proving ground." Year 4 commits to ONE
    Phase IIa mechanistic study in trauma. MI and stroke are named as aspirational
    extensions requiring a Year 5 "repurposing playbook" — they have no committed
    clinical milestones within the £40M programme.

    Including MI/stroke DALYs without clinical evidence would be like crediting
    a Phase 1 oncology trial for all cancer DALYs. Until the platform demonstrates
    cross-indication transfer in human models (not claimed by Year 5 end), only the
    proving-ground indication is countable.

    Trauma/HS filter chain:
      ~60,000 US hemorrhagic shock deaths/yr (Priority 4)
      14% potentially preventable (Pfeifer 2019)
      × ~72% non-TBI eligible (Mohamed 2016 brain IRI caveat)
      × ~80% organ-specificity fit
      × ~50% field uptake (TXA underuse data — conservative)
      ≈ ~2,400 prevented US deaths/yr × DALY multiplier ~3 → ~7k DALYs
      EU/other HIC: ~3× US → ~30k HIC trauma DALYs/yr

    ECPR (capped): Wisniewski 2024 porcine result is promising but unpublished
    from applicant's lab. Modest credit: ~200k–500k DALYs/yr.

    Combined trauma-only median: 4M DALYs/yr, σ=0.45
    (Lower than v3 8M because MI/stroke excluded)
    """
    return np.random.lognormal(np.log(4e6), 0.45, n)


def sample_annual_addressable_lmic(n):
    """
    Annual DALYs addressable in LMIC — trauma/HS only.

    Same indication restriction as HIC. LMIC trauma burden is large but
    deployment constraints are severe (cold chain, IV access, EMS coverage).

    Conservative median: 2.5M DALYs/yr, σ=0.60
    """
    return np.random.lognormal(np.log(2.5e6), 0.60, n)


# =============================================================================
# ATTRIBUTION — conservative, independent funding paths exist for each component
# =============================================================================

def sample_attribution_fraction(n):
    """
    SKEPTICAL RATIONALE:
    Each major component of INTERCEPT has an independent funding path:
      - ReWiRe Phase 2a: already registered without INTERCEPT (REC 19/LO/0329)
      - OoC/organ chip: Emulate, CN Bio, and UK Catapult networks fund this independently
      - Digital twin: Wellcome Trust and EPSRC fund computational modelling programmes
      - EWiC clinical platform: NIHR funds prehospital trial platforms
      - Atlas/omics: UKRI, MRC, Wellcome all fund omics discovery programmes

    INTERCEPT's marginal contribution is INTEGRATION of these components
    under one umbrella. The counterfactual is not "nothing happens" but
    "each component proceeds at its own pace without coordination."

    The integration value is real but modest. A 25% marginal attribution
    reflects that INTERCEPT accelerates and connects, but does not create
    from scratch.

    Beta(2, 6) → mode ≈ 14%, mean ≈ 25%
    (v3 used Beta(4,4) → mean 50% — approximately twice this estimate)
    """
    return np.random.beta(2, 6, n)


# =============================================================================
# STAGED DRUG SUCCESS — conservative
# =============================================================================

def sample_p_platform(n):
    """
    SKEPTICAL RATIONALE:
    OoC has proven DILI prediction but has NO precedent for IRI drug efficacy
    prediction. The kidney chip adenosine result (Vormann 2022) shows
    adenosine is protective — this is not the same as predicting drug Phase 3
    success. The specific Go/No-Go ("predict human biomarkers within
    predefined thresholds") has not been achieved for any IRI drug.

    Downward adjustment from v3 (64%) to reflect:
      - DILI → IRI is a significant unproven extrapolation
      - Digital twin: only 12% of DT studies meet NASEM standards (Priority 6)
      - Reproducibility concerns in OoC (PubMed 36290517)
      - 3-year timeline to validated platform is ambitious

    Beta(5, 5) → mean = 50%
    """
    return np.random.beta(5, 5, n)


def sample_p_phase3_funded(n):
    """
    SKEPTICAL RATIONALE:
    The concept note projects a £100M+ Phase II follow-on. But:
      - Academic Phase 2a results do not automatically attract pharma Phase 3 funding
      - Regadenoson is generic — low IP value for pharma
      - CDMRP/ARIA funding of Phase 3 is plausible but not guaranteed
      - Phase 3 in prehospital trauma is operationally complex and expensive

    Moderately lower than v3 (70%) to reflect this uncertainty.
    Beta(5, 4) → mean ≈ 56%
    """
    return np.random.beta(5, 4, n)


def sample_p_phase3_success(n):
    """
    SKEPTICAL RATIONALE:
    The IRI field has a near-zero clinical success rate:
      CIRCUS: OR 1.04, NEJM 2015
      CONDI2: HR 1.10, Lancet 2019
      AMISTAD-II: no benefit
      >1,000 neuroprotectants: 0 stroke approvals

    The concept note claims OoC mitigates the comorbidity gap (Ferdinandy 2023).
    But comorbidity modelling on OoC for IRI is itself unproven at clinical scale.
    The credit given to OoC for improving Phase 3 success should be very small
    until there is at least one IRI drug that OoC correctly predicted would succeed.

    The regadenoson preclinical data is unpublished and from the applicant's lab.
    Even if ReWiRe Phase 2a succeeds, IRI Phase 3 failure modes are distinct
    from Phase 2a failure modes (sample size, endpoint, comorbidity population).

    Beta(1.5, 7) → mode ≈ 6%, mean ≈ 18%
    (v3 used Beta(2.5,6) → mean 29%; this version gives OoC less credit)
    """
    return np.random.beta(1.5, 7, n)


def sample_p_adoption(n):
    """
    SKEPTICAL RATIONALE:
    TXA precedent shows prehospital drug adoption is slow (14 years) and
    incomplete (NAEMSP/ACEP endorse but implementation still fragmented).
    A novel IV drug with uncertainty about hypotensive safety faces additional
    barriers. The concept note designs a "buyer path" — but concept notes
    regularly claim adoption infrastructure that doesn't materialise.

    Beta(4, 5) → mean ≈ 44%
    (v3 used Beta(6,4) → mean 60%; modest downward adjustment)
    """
    return np.random.beta(4, 5, n)


# =============================================================================
# n_LEADS — peaked at 1-2, not 5 (historical academic platform hit rates)
# =============================================================================

def sample_n_viable_leads(n):
    """
    SKEPTICAL RATIONALE:
    The concept note's "5+ qualified leads by Year 5" is the programme TARGET,
    not an evidence-based probability estimate. Key considerations:

    Historical academic drug discovery platform hit rates:
      - Typical 5-year academic platform programme: 1-3 IND-ready leads
        (e.g., Structural Genomics Consortium ~2-3 chemical probes/yr across
        100+ targets; EPSRC/MRC drug discovery platforms: 1-2 leads per 5yr)
      - "Qualified" in the concept note means "companion diagnostic-ready +
        field-feasibility dossier" — a high bar for 5 leads in 5 years
      - The 3 mechanism families must each produce at least 1-2 leads,
        requiring all three to succeed in the same programme window

    Conservative distribution peaked at 1-2:
      1 lead: 40%  (regadenoson only; other families don't qualify in time)
      2 leads: 35%  (regadenoson + one validated family)
      3 leads: 17%  (two families deliver)
      4 leads:  6%  (three families partially deliver)
      5 leads:  2%  (target met — unlikely in 5-yr academic programme)

    Expected n_leads ≈ 1.95
    (v3 peaked at 5 with E=4.5 — this version reverses to historical norms)
    """
    return np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.40, 0.35, 0.17, 0.06, 0.02])


# =============================================================================
# TIME AND COST — higher discount, longer horizon
# =============================================================================

def sample_discount_rate(n):
    """
    SKEPTICAL RATIONALE:
    For a high-risk, long-horizon programme with novel platform risk,
    a higher discount rate is appropriate. OpenPhil uses 3-4% for
    well-evidenced programmes; 5% is more appropriate for pre-Phase 3
    uncertain science.

    Triangular(0.03, 0.05, 0.07) → mode 5%, mean ≈ 5%
    (v3 used Tri(1%,3%,5%) → mode 3%)
    """
    return np.random.triangular(0.03, 0.05, 0.07, n)


def sample_time_to_impact(n):
    """
    SKEPTICAL RATIONALE:
    The concept note timeline to first Phase 2a result is Year 4.
    Phase 3 + regulatory + adoption ramp from there:
      Phase 3: ~4-6 yr
      Regulatory: ~1-2 yr
      Adoption midpoint: ~5-8 yr
      Total: ~14-20 yr from programme start

    v3 used mode 13 yr — this is the optimistic end of the range.
    Conservative mode 16 yr, reflecting realistic Phase 3 delays.

    Triangular(10, 16, 25) → mode 16 yr, mean ≈ 17 yr
    """
    return np.random.triangular(10, 16, 25, n)


def sample_acceleration_years(n):
    """
    SKEPTICAL RATIONALE:
    The acceleration claim is undemonstrated. The concept note asserts the
    platform will speed up drug development vs BAU, but:
      - No OoC platform has yet demonstrably shortened an IRI drug development path
      - The EWiC clinical platform adds value but also adds complexity
      - Acceleration is partly already captured in attribution (if ARIA would
        fund the drug anyway, INTERCEPT's acceleration is its main value)

    Conservative mode 4 yr vs v3's 7 yr.
    Triangular(1, 4, 10) → mode 4 yr, mean ≈ 5 yr
    """
    return np.random.triangular(1, 4, 10, n)


def sample_rd_cost(n):
    """
    Programme cost. Kept at concept note figure (~£40M = ~$51M).
    This is the correct denominator for evaluating this specific grant.
    Triangular($45M, $51M, $65M)
    """
    return np.random.triangular(45e6, 51e6, 65e6, n)


def sample_daly_value(n):
    """$/DALY averted. Unchanged. Triangular(50k, 100k, 150k)"""
    return np.random.triangular(50_000, 100_000, 150_000, n)


def sample_platform_independent_value(n):
    """
    SKEPTICAL RATIONALE:
    Academic programmes rarely spin out commercially at scale within 5 years.
    The pathway atlas and playbooks have real but modest value. Conservative
    estimate: $5-30M in ecosystem value (data commons, SOPs, one spinout attempt).

    Triangular($5M, $15M, $30M)
    (v3 used Tri($20M,$40M,$80M) — this version is ~3× more conservative)
    """
    return np.random.triangular(5e6, 15e6, 30e6, n)


# =============================================================================
# SIMULATION
# =============================================================================

def run_simulation(n_sims=N_SIMS):
    hic_arm            = sample_annual_addressable_hic(n_sims)
    lmic_arm           = sample_annual_addressable_lmic(n_sims)
    annual_addressable = hic_arm + lmic_arm

    attribution        = sample_attribution_fraction(n_sims)
    p_platform         = sample_p_platform(n_sims)

    p_phase3_funded    = sample_p_phase3_funded(n_sims)
    p_phase3_success   = sample_p_phase3_success(n_sims)
    p_adoption         = sample_p_adoption(n_sims)
    p_drug_per_lead    = p_phase3_funded * p_phase3_success * p_adoption

    n_leads            = sample_n_viable_leads(n_sims)
    p_drug_portfolio   = 1.0 - (1.0 - p_drug_per_lead) ** n_leads
    p_success          = p_platform * p_drug_portfolio

    acceleration       = sample_acceleration_years(n_sims)
    rd_cost            = sample_rd_cost(n_sims)
    daly_value         = sample_daly_value(n_sims)

    discount_rate      = sample_discount_rate(n_sims)
    time_to_impact     = sample_time_to_impact(n_sims)
    discount_factor    = (1.0 + discount_rate) ** (-time_to_impact)

    expected_dalys     = annual_addressable * acceleration * p_success
    discounted_dalys   = expected_dalys * discount_factor
    drug_roi           = (discounted_dalys * daly_value * attribution) / rd_cost

    platform_value     = sample_platform_independent_value(n_sims)
    platform_roi       = (platform_value * attribution * p_platform) / rd_cost

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
        'mean_p_platform':       np.mean(r['p_platform']),
        'mean_p_phase3_funded':  np.mean(r['p_phase3_funded']),
        'mean_p_phase3_success': np.mean(r['p_phase3_success']),
        'mean_p_adoption':       np.mean(r['p_adoption']),
        'mean_p_drug_per_lead':  np.mean(r['p_drug_per_lead']),
        'mean_n_leads':          np.mean(r['n_leads']),
        'mean_p_drug_portfolio': np.mean(r['p_drug_portfolio']),
        'mean_p_success':        np.mean(r['p_success']),
        'mean_attribution':      np.mean(r['attribution']),
        'mean_discount_factor':  np.mean(r['discount_factor']),
        'mean_time_to_impact':   np.mean(r['time_to_impact']),
        'mean_hic_arm_M':        np.mean(r['hic_arm']) / 1e6,
        'mean_lmic_arm_M':       np.mean(r['lmic_arm']) / 1e6,
        'mean_drug_roi':         np.mean(r['drug_roi']),
        'median_drug_roi':       np.median(r['drug_roi']),
        'mean_platform_roi':     np.mean(r['platform_roi']),
        'mean_platform_value_M': np.mean(r['platform_value']) / 1e6,
        'mean_rd_cost_M':        np.mean(r['rd_cost']) / 1e6,
    }


def sensitivity_analysis(results):
    params = [
        'hic_arm', 'lmic_arm',
        'p_platform', 'p_phase3_funded', 'p_phase3_success', 'p_adoption',
        'n_leads', 'attribution',
        'acceleration', 'discount_rate', 'time_to_impact',
        'rd_cost', 'daly_value', 'platform_value',
    ]
    return {p: np.corrcoef(results[p], results['roi_multiple'])[0, 1] for p in params}


# =============================================================================
# SCENARIO COMPARISON
# =============================================================================

def scenario_comparison():
    r = 0.05  # 5% discount for skeptical scenarios
    rd_cost_base = 51e6

    scenarios = {
        'Platform fails / BAU': {
            'note':           'Platform fails; drug at raw IRI base rate; INTERCEPT redundant',
            'annual_dalys':   5.0e6,
            'p_success':      0.02,
            'acceleration':   1,
            'attribution':    0.10,
            'time_to_impact': 20,
            'rd_cost':        rd_cost_base,
            'daly_value':     100_000,
            'platform_value': 5e6,
        },
        'Conservative': {
            'note':           'Platform validated; trauma only; 1 lead; attribution 20%',
            'annual_dalys':   5.5e6,
            'p_success':      0.05,
            'acceleration':   3,
            'attribution':    0.20,
            'time_to_impact': 18,
            'rd_cost':        rd_cost_base,
            'daly_value':     100_000,
            'platform_value': 10e6,
        },
        'Moderate': {
            'note':           'Trauma + early MI signals; 2 leads; attribution 25%',
            'annual_dalys':   7.0e6,
            'p_success':      0.10,
            'acceleration':   4,
            'attribution':    0.25,
            'time_to_impact': 16,
            'rd_cost':        rd_cost_base,
            'daly_value':     100_000,
            'platform_value': 15e6,
        },
        'Optimistic': {
            'note':           'Platform validates 3 leads; Phase 3 funded; attribution 35%',
            'annual_dalys':   9.0e6,
            'p_success':      0.18,
            'acceleration':   6,
            'attribution':    0.35,
            'time_to_impact': 14,
            'rd_cost':        rd_cost_base,
            'daly_value':     100_000,
            'platform_value': 25e6,
        },
        'Transformative': {
            'note':           'Concept note targets met; cross-indication; 4+ leads',
            'annual_dalys':   14.0e6,
            'p_success':      0.28,
            'acceleration':   8,
            'attribution':    0.45,
            'time_to_impact': 12,
            'rd_cost':        rd_cost_base,
            'daly_value':     100_000,
            'platform_value': 30e6,
        },
    }

    rows = []
    for name, p in scenarios.items():
        df             = (1 + r) ** (-p['time_to_impact'])
        expected_dalys = p['annual_dalys'] * p['acceleration'] * p['p_success']
        drug_roi       = (expected_dalys * df * p['daly_value'] * p['attribution']) / p['rd_cost']
        plat_roi       = (p['platform_value'] * p['attribution'] * 0.50) / p['rd_cost']  # E[p_platform]
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
# VISUALIZATION
# =============================================================================

def create_plots(results, stats_dict, correlations):
    fig = plt.figure(figsize=(21, 19))
    fig.suptitle(
        'INTERCEPT Monte Carlo — SKEPTICAL ANALYST VERSION\n'
        'Conservative priors: trauma-only DALYs, n_leads peaked at 1-2, '
        'attribution 25%, P(Phase3 success) 18%',
        fontsize=12, fontweight='bold', y=0.99
    )
    gs = GridSpec(3, 3, figure=fig, hspace=0.48, wspace=0.38)
    roi = results['roi_multiple']

    # Panel 1: ROI distribution
    ax1 = fig.add_subplot(gs[0, 0])
    log_roi = np.log10(np.clip(roi, 0.1, None))
    ax1.hist(log_roi, bins=80, density=True, alpha=0.7, color='firebrick', edgecolor='white')
    ax1.axvline(np.log10(2100), color='darkred', linestyle='--', lw=2, label='2100× threshold')
    med = max(stats_dict['median_roi'], 0.11)
    ax1.axvline(np.log10(med), color='darkorange', lw=2,
                label=f'Median: {stats_dict["median_roi"]:.0f}×')
    ax1.set_xlabel('ROI (log₁₀ scale)')
    ax1.set_ylabel('Density')
    ax1.set_title(f'ROI Distribution — Skeptical\nP(>2100×) = {stats_dict["prob_above_2100"]*100:.1f}%')
    ax1.legend(fontsize=7)
    ax1.set_xlim([-1, 6])
    ax1.set_xticks([-1, 0, 1, 2, 3, 4, 5, 6])
    ax1.set_xticklabels(['0.1', '1', '10', '100', '1k', '10k', '100k', '1M'])

    # Panel 2: P(success) decomposition
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
        f'Staged P(success) — Skeptical\n'
        f'E[platform]={stats_dict["mean_p_platform"]*100:.0f}%  '
        f'E[drug/lead]={stats_dict["mean_p_drug_per_lead"]*100:.0f}%  '
        f'E[portfolio]={stats_dict["mean_p_drug_portfolio"]*100:.0f}%'
    )
    ax2.legend(fontsize=6, loc='upper right')

    # Panel 3: Attribution — skeptical vs optimistic comparison
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.hist(results['attribution'] * 100, bins=50, density=True,
             alpha=0.75, color='firebrick', edgecolor='white', label='Skeptical Beta(2,6)')
    # Overlay v3 attribution for comparison
    v3_attr = np.random.beta(4, 4, N_SIMS) * 100
    ax3.hist(v3_attr, bins=50, density=True,
             alpha=0.45, color='steelblue', edgecolor='white', label='v3 Beta(4,4)')
    ax3.axvline(stats_dict['mean_attribution'] * 100, color='darkred', linestyle='--', lw=1.5,
                label=f'Skeptical mean: {stats_dict["mean_attribution"]*100:.0f}%')
    ax3.set_xlabel('Attribution fraction (%)')
    ax3.set_ylabel('Density')
    ax3.set_title('Attribution: Skeptical vs Applicant-Aligned (v3)\n'
                  'Components fundable independently → lower marginal credit')
    ax3.legend(fontsize=7)

    # Panel 4: n_leads comparison
    ax4 = fig.add_subplot(gs[1, 0])
    lead_vals  = [1, 2, 3, 4, 5]
    skep_probs = [0.40, 0.35, 0.17, 0.06, 0.02]
    v3_probs   = [0.05, 0.15, 0.25, 0.35, 0.20]
    x = np.array(lead_vals)
    ax4.bar(x - 0.2, [p * 100 for p in skep_probs], 0.4,
            color='firebrick', alpha=0.75, edgecolor='white', label='Skeptical (peaked at 1)')
    ax4.bar(x + 0.2, [p * 100 for p in v3_probs], 0.4,
            color='steelblue', alpha=0.75, edgecolor='white', label='v3 (peaked at 5)')
    ax4.axvline(stats_dict['mean_n_leads'], color='darkred', linestyle='--', lw=1.5,
                label=f'Skeptical E[n]={stats_dict["mean_n_leads"]:.2f}')
    ax4.axvline(4.5, color='steelblue', linestyle=':', lw=1.5, label='v3 E[n]=4.5')
    ax4.set_xlabel('N viable leads')
    ax4.set_ylabel('Probability (%)')
    ax4.set_title('N Leads: Skeptical vs v3\n'
                  'Historical academic platform hit rate vs concept note target')
    ax4.legend(fontsize=7)

    # Panel 5: DALY scope comparison
    ax5 = fig.add_subplot(gs[1, 1])
    total_skep = (results['hic_arm'] + results['lmic_arm']) / 1e6
    v3_hic  = np.random.lognormal(np.log(8e6), 0.50, N_SIMS) / 1e6
    v3_lmic = np.random.lognormal(np.log(6e6), 0.65, N_SIMS) / 1e6
    total_v3 = v3_hic + v3_lmic
    ax5.hist(total_skep, bins=50, density=True, alpha=0.7,
             color='firebrick', edgecolor='white', label=f'Skeptical: trauma only\n(mean {np.mean(total_skep):.1f}M)')
    ax5.hist(total_v3, bins=50, density=True, alpha=0.5,
             color='steelblue', edgecolor='white', label=f'v3: trauma+MI+stroke+PPH\n(mean {np.mean(total_v3):.1f}M)')
    ax5.set_xlabel('Annual Addressable DALYs (M)')
    ax5.set_ylabel('Density')
    ax5.set_title('DALY Scope: Skeptical vs v3\n'
                  'Skeptical: trauma proving ground only')
    ax5.legend(fontsize=7)

    # Panel 6: Discount factor comparison
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.hist(results['discount_factor'], bins=50, density=True,
             alpha=0.75, color='firebrick', edgecolor='white',
             label=f'Skeptical (r=5%, T=16yr)\nmean={stats_dict["mean_discount_factor"]:.2f}')
    v3_df = (1 + np.random.triangular(0.01, 0.03, 0.05, N_SIMS)) ** (
             -np.random.triangular(8, 13, 20, N_SIMS))
    ax6.hist(v3_df, bins=50, density=True, alpha=0.5, color='steelblue', edgecolor='white',
             label=f'v3 (r=3%, T=13yr)\nmean={np.mean(v3_df):.2f}')
    ax6.set_xlabel('Discount factor  (1+r)^−T')
    ax6.set_ylabel('Density')
    ax6.set_title('Discount Factor: Skeptical vs v3\n'
                  'Higher rate + longer horizon for uncertain programme')
    ax6.legend(fontsize=7)

    # Panel 7: Sensitivity tornado
    ax7 = fig.add_subplot(gs[2, 0])
    labels_clean = {
        'hic_arm':          'HIC DALYs (trauma)',
        'lmic_arm':         'LMIC DALYs (trauma)',
        'p_platform':       'P(platform delivers)',
        'p_phase3_funded':  'P(Phase 3 funded)',
        'p_phase3_success': 'P(Phase 3 success)',
        'p_adoption':       'P(adoption)',
        'n_leads':          'N viable leads',
        'attribution':      'Attribution fraction',
        'acceleration':     'Acceleration (years)',
        'discount_rate':    'Discount rate r',
        'time_to_impact':   'Time to impact T',
        'rd_cost':          'Programme cost',
        'daly_value':       'DALY value ($)',
        'platform_value':   'Platform ecosystem value',
    }
    params  = list(correlations.keys())
    corrs   = [correlations[p] for p in params]
    idx     = np.argsort(np.abs(corrs))[::-1]
    p_s     = [params[i] for i in idx]
    c_s     = [corrs[i]  for i in idx]
    colors  = ['firebrick' if c > 0 else 'navy' for c in c_s]
    y_pos   = np.arange(len(p_s))
    ax7.barh(y_pos, c_s, color=colors, alpha=0.75)
    ax7.set_yticks(y_pos)
    ax7.set_yticklabels([labels_clean[p] for p in p_s], fontsize=7)
    ax7.set_xlabel('Pearson r with ROI')
    ax7.set_title('Sensitivity — Skeptical\n(14 parameters)')
    ax7.axvline(0, color='black', linewidth=0.5)
    ax7.set_xlim([-0.65, 0.65])

    # Panel 8: Threshold exceedance
    ax8 = fig.add_subplot(gs[2, 1])
    thresholds = [100, 500, 1000, 2100, 5000, 10000, 50000]
    probs      = [np.mean(roi > t) * 100 for t in thresholds]
    bar_colors = ['darkred' if t == 2100 else 'firebrick' for t in thresholds]
    ax8.bar(range(len(thresholds)), probs, color=bar_colors, alpha=0.75, edgecolor='white')
    ax8.axhline(50, color='gray', linestyle='--', alpha=0.5)
    ax8.set_xticks(range(len(thresholds)))
    ax8.set_xticklabels([f'{t:,}×' for t in thresholds], rotation=45, fontsize=7)
    ax8.set_ylabel('Probability (%)')
    ax8.set_title('Threshold Exceedance — Skeptical')
    ax8.set_ylim([0, 105])
    for i, p in enumerate(probs):
        ax8.text(i, p + 2, f'{p:.0f}%', ha='center', fontsize=7)

    # Panel 9: v3 vs skeptical ROI distributions side by side
    ax9 = fig.add_subplot(gs[2, 2])
    # Approximate v3 distribution from its known parameters
    ax9.hist(np.log10(np.clip(roi, 0.1, None)), bins=60, density=True,
             alpha=0.7, color='firebrick', edgecolor='white',
             label=f'Skeptical\nmedian={stats_dict["median_roi"]:.0f}×\nP(>2100×)={stats_dict["prob_above_2100"]*100:.0f}%')
    ax9.axvline(np.log10(2100), color='black', linestyle='--', lw=1.5, label='2100× threshold')
    ax9.axvline(np.log10(max(stats_dict['median_roi'], 0.11)), color='firebrick', lw=1.5, linestyle=':')
    ax9.axvline(np.log10(14957), color='steelblue', lw=1.5, linestyle=':',
                label='v3 median: 14,957×')
    ax9.set_xlabel('ROI (log₁₀ scale)')
    ax9.set_ylabel('Density')
    ax9.set_title('Skeptical ROI vs v3 Reference Points\n(v3 distribution not re-run here)')
    ax9.legend(fontsize=7)
    ax9.set_xlim([-1, 6])

    out_path = f'{OUTPUT_DIR}/intercept_monte_carlo_skeptical.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'  Saved: {out_path}')


# =============================================================================
# REPORT
# =============================================================================

def print_report(stats_dict, correlations, scenarios):
    labels_clean = {
        'hic_arm':          'HIC DALYs (trauma/HS only)',
        'lmic_arm':         'LMIC DALYs (trauma/HS only)',
        'p_platform':       'P(platform delivers engine)',
        'p_phase3_funded':  'P(Phase 3 funded | Phase 2a+)',
        'p_phase3_success': 'P(Phase 3 success | funded)',
        'p_adoption':       'P(adoption | approval)',
        'n_leads':          'N viable leads (peaked at 1-2)',
        'attribution':      'Counterfactual attribution (~25%)',
        'acceleration':     'Acceleration vs BAU (conservative)',
        'discount_rate':    'Discount rate r (5%)',
        'time_to_impact':   'Time to impact T (yrs)',
        'rd_cost':          'Programme cost (~£40M)',
        'daly_value':       'DALY value ($)',
        'platform_value':   'Platform ecosystem value (conservative)',
    }
    sorted_corrs = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)

    voi_text = {
        'p_phase3_success': (
            'Independent IRI pharmacologist\n'
            '    Key question: has ANY OoC platform ever improved Phase 3 success\n'
            '    probability for an IRI drug? If not, what is the prior for OoC credit?'
        ),
        'attribution': (
            'Funding landscape analyst\n'
            '    Key question: which components of INTERCEPT would NOT be funded\n'
            '    independently? What is the specific integration value?'
        ),
        'hic_arm': (
            'Independent clinician: trauma + cardiology + stroke\n'
            '    Key question: what clinical evidence supports cross-indication\n'
            '    transfer within the 5-year programme? Is Year 5 "playbook" the\n'
            '    same as demonstrating MI/stroke efficacy?'
        ),
        'n_leads': (
            'Academic drug discovery platform expert\n'
            '    Key question: what is the historical IND-ready lead output of\n'
            '    comparable 5-year academic platform programmes?'
        ),
        'p_platform': (
            'Independent OoC expert\n'
            '    Key question: is predicting IRI drug efficacy via OoC in the same\n'
            '    class of problem as DILI prediction, or is it substantially harder?'
        ),
        'acceleration': (
            'Health technology assessment expert\n'
            '    Key question: what is the evidence base for OoC platforms shortening\n'
            '    drug development timelines in practice (not in theory)?'
        ),
    }

    voi_section = '\nEXPERT INTERVIEW PRIORITIES (Value of Information)\n\n'
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
INTERCEPT MONTE CARLO — SKEPTICAL ANALYST VERSION
Open Philanthropy Cost-Effectiveness Analysis | March 2026

PURPOSE
  This version implements conservative priors a rigorous external analyst would apply
  when the primary input source is the applicant's own concept note. Compare with
  intercept_analysis_report.txt (v3, applicant-aligned) for the full range.

SKEPTICAL PRIORS vs v3 (applicant-aligned)
  Parameter                    Skeptical              v3 (applicant)
  ─────────────────────────────────────────────────────────────────
  Annual addressable DALYs     ~6.5M (trauma only)   ~16.5M (all indications)
  N viable leads (E[n])        ~1.95 (peaked at 1)    4.5 (peaked at 5)
  Attribution (mean)           ~25%                   50%
  P(Phase 3 success, mean)     ~18%                   29%
  P(platform, mean)            ~50%                   64%
  Discount rate (mode)          5%                     3%
  Time to impact (mode)        16 yr                  13 yr
  Acceleration (mode)           4 yr                   7 yr
  Platform ecosystem value     $15M modal             $40M modal

INVESTMENT PROFILE
  Programme cost:  ~£40M (~$51M) — concept note figure (unchanged)
  DALY value:      $50k-150k (unchanged)
  Threshold:       2,100× ROI
  Simulations:     {N_SIMS:,}

P(SUCCESS) DECOMPOSITION — SKEPTICAL
  E[P(platform delivers engine)]:   {stats_dict['mean_p_platform']*100:>5.1f}%  (v3: 63.6%)
  E[P(Phase 3 funded | 2a+)]:      {stats_dict['mean_p_phase3_funded']*100:>5.1f}%  (v3: 69.9%)
  E[P(Phase 3 success | funded)]:  {stats_dict['mean_p_phase3_success']*100:>5.1f}%  (v3: 29.4%)
  E[P(adoption | approval)]:       {stats_dict['mean_p_adoption']*100:>5.1f}%  (v3: 60.0%)
  ──────────────────────────────────────────────
  E[P(drug success per lead)]:       {stats_dict['mean_p_drug_per_lead']*100:>5.1f}%  (v3: 12.3%)
  E[n viable leads]:                 {stats_dict['mean_n_leads']:>5.2f}  (v3: 4.50)
  E[P(portfolio ≥1 lead succeeds)]:  {stats_dict['mean_p_drug_portfolio']*100:>5.1f}%  (v3: 41.0%)
  E[P(success)] = E[platform×port]:  {stats_dict['mean_p_success']*100:>5.1f}%  (v3: 26.1%)

CORRECTION FACTORS — SKEPTICAL
  E[attribution]:              {stats_dict['mean_attribution']*100:>5.1f}%  (v3: 50.0%)
  E[discount factor]:          {stats_dict['mean_discount_factor']:>5.3f}  (v3: 0.673)
  E[time to impact]:           {stats_dict['mean_time_to_impact']:>5.1f} yr  (v3: 13.7yr)
  E[HIC arm]:                  {stats_dict['mean_hic_arm_M']:>5.1f}M DALYs/yr  (v3: 9.1M — trauma+MI+stroke+PPH)
  E[LMIC arm]:                 {stats_dict['mean_lmic_arm_M']:>5.1f}M DALYs/yr  (v3: 7.4M)

SIMULATION RESULTS
  Mean ROI:            {stats_dict['mean_roi']:>12,.0f}×
  Median ROI:          {stats_dict['median_roi']:>12,.0f}×
  5th percentile:      {stats_dict['p5_roi']:>12,.0f}×
  25th percentile:     {stats_dict['p25_roi']:>12,.0f}×
  75th percentile:     {stats_dict['p75_roi']:>12,.0f}×
  95th percentile:     {stats_dict['p95_roi']:>12,.0f}×

  ── v3 (applicant-aligned) for comparison ──
  v3 median ROI:               14,957×
  v3 mean ROI:                 21,714×

THRESHOLD EXCEEDANCE
  P(ROI > 1,000×):    {stats_dict['prob_above_1000']*100:>6.1f}%  (v3: 99.1%)
  P(ROI > 2,100×):    {stats_dict['prob_above_2100']*100:>6.1f}%  (v3: 96.4%)  ← OpenPhil bar
  P(ROI > 5,000×):    {stats_dict['prob_above_5000']*100:>6.1f}%  (v3: 85.3%)
  P(ROI > 10,000×):   {stats_dict['prob_above_10000']*100:>6.1f}%  (v3: 65.7%)

SENSITIVITY ANALYSIS (ranked by |Pearson r|)
"""
    for param, corr in sorted_corrs:
        direction = '↑' if corr > 0 else '↓'
        report += f'  {labels_clean[param]:<52s} {direction}  r = {corr:+.3f}\n'

    report += f"""
{voi_section}
SCENARIO COMPARISON (r=5% skeptical discount rate)
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
        'STRONG CASE even under skeptical priors.'
        if stats_dict['prob_above_2100'] > 0.70 else
        'MODERATE CASE: More likely than not to clear threshold under skeptical priors.'
        if stats_dict['prob_above_2100'] > 0.50 else
        'MARGINAL CASE: Plausible but not clear under skeptical priors.\n'
        '  Requires cross-indication evidence and platform validation to derisk.'
        if stats_dict['prob_above_2100'] > 0.25 else
        'WEAK CASE under skeptical priors: does not clear threshold without\n'
        '  significant evidence update on platform performance and indication scope.'
    )

    report += f"""
WHAT WOULD CHANGE THIS VERDICT
  The gap between skeptical ({stats_dict['prob_above_2100']*100:.0f}%) and applicant-aligned (96%)
  is driven by four parameters. Resolving any two would substantially shift the verdict:

  1. n_leads: independent evidence that 5-yr platform programmes produce 5+ IND-ready
     leads (not just leads at earlier stages) would shift this toward v3.
  2. Indication scope: Phase 2a positive results in MI/stroke during Year 4-5 would
     justify including those DALYs — currently unearned.
  3. Attribution: evidence that the cross-indication integration could NOT be funded
     independently (i.e., the components would NOT be funded without INTERCEPT) would
     raise attribution toward 40-50%.
  4. P(Phase 3 success): any OoC platform demonstrating a correct IRI drug efficacy
     prediction (positive or negative) would calibrate the credit OoC deserves.

VERDICT: {verdict}

Median ROI {stats_dict['median_roi']:,.0f}× is {'ABOVE' if stats_dict['median_roi'] > 2100 else 'BELOW'} the 2,100× threshold under skeptical priors.

================================================================================
"""
    return report


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print('Running INTERCEPT Monte Carlo — SKEPTICAL VERSION...')

    results      = run_simulation(N_SIMS)
    stats_dict   = analyze_results(results)
    correlations = sensitivity_analysis(results)
    scenarios    = scenario_comparison()

    report = print_report(stats_dict, correlations, scenarios)
    print(report)

    report_path = f'{OUTPUT_DIR}/intercept_analysis_report_skeptical.txt'
    with open(report_path, 'w') as f:
        f.write(report)
    print(f'  Saved: {report_path}')

    print('Generating visualisations...')
    create_plots(results, stats_dict, correlations)

    print(f'\nDone. Output files:')
    print(f'  {OUTPUT_DIR}/intercept_analysis_report_skeptical.txt')
    print(f'  {OUTPUT_DIR}/intercept_monte_carlo_skeptical.png')
