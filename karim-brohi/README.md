# INTERCEPT Evidence Search: Karim Brohi Portfolio

## Overview

This folder contains the results of a systematic evidence search using scite.ai and related academic databases, conducted to evaluate the scientific basis for INTERCEPT — a program developing prehospital therapeutic interventions for trauma and ischemia-reperfusion injury.

**Search Date:** March 15, 2026
**Researcher:** Karim Brohi (portfolio context)
**Tool:** scite.ai Smart Citation search + PubMed/academic databases

## Scite.ai MCP Connector Setup

The scite.ai MCP connector is configured in `.mcp.json` at the project root. To activate:

```bash
# Set your scite.ai API key
export SCITE_API_KEY="your-scite-api-key"

# The connector is pre-configured in .mcp.json:
# {
#   "mcpServers": {
#     "scite": {
#       "type": "sse",
#       "url": "https://api.scite.ai/mcp",
#       "headers": { "Authorization": "Bearer ${SCITE_API_KEY}" }
#     }
#   }
# }
```

Once activated, you can query scite.ai directly with the `search_literature` tool.

## Evidence Files

| File | Priority | Topic |
|------|----------|-------|
| [priority-1-a2a-receptor-trauma.md](priority-1-a2a-receptor-trauma.md) | 1 (Highest VOI) | Lead Asset: A2A agonists in trauma/IRI |
| [priority-2-iri-drug-failure.md](priority-2-iri-drug-failure.md) | 2 | IRI Drug Development Track Record |
| [priority-3-organ-on-chip.md](priority-3-organ-on-chip.md) | 3 | Organ-on-Chip Translation Validity |
| [priority-4-trauma-timing.md](priority-4-trauma-timing.md) | 4 | Timing Window Evidence |
| [priority-5-mechanism-transfer.md](priority-5-mechanism-transfer.md) | 5 | IRI Mechanism Transfer Across Conditions |
| [priority-6-digital-twin.md](priority-6-digital-twin.md) | 6 | Digital Twin Validation |
| [priority-7-prehospital-drugs.md](priority-7-prehospital-drugs.md) | 7 | Prehospital Drug Feasibility |
| [priority-8-funding-landscape.md](priority-8-funding-landscape.md) | 8 | Counterfactual Research Landscape |
| [synthesis.md](synthesis.md) | - | Overall synthesis and SROI implications |

## Evidence Interpretation Key

| Finding | Impact on SROI |
|---------|---------------|
| A2A agonists show efficacy in trauma models (supporting citations) | P(drug) ↑ |
| IRI drugs consistently fail in Phase 2/3 (contrasting citations) | P(drug) ↓ |
| OoC has predicted human outcomes (supporting) | P(platform) ↑ |
| No OoC-to-clinic translation precedent | P(platform) ↓ |
| Large fraction of trauma deaths occur >30min post-injury | Addressable DALYs ↑ |
| Most deaths are immediate (<10min) or late (hospital) | Addressable DALYs ↓ |
| Active DARPA/military programs in this space | Speed-up ↓ |
| Field is neglected, no comparable programs | Speed-up ↑ |

## Citation Tally Interpretation

- **High supporting/contrasting ratio** → Accepted science, strong consensus
- **High contrasting/supporting ratio** → Controversial or failed field
- **Many contrasting citations** → Claims have been challenged, replications failed
