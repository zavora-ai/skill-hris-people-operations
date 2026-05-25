# HRIS & People Operations Skill

> HR operations for AI agents — employee lookup, leave management, org navigation, headcount reporting, and payroll coordination with strict PII governance.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--hris-green)](https://github.com/zavora-ai/mcp-hris)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates 14 HRIS tools into governed people operations workflows — with strict PII controls ensuring salary and personal data never leak.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Employee Lookup | 1-2 | Find people with safe data exposure |
| Leave Management | 2-3 | Request, validate, approve with coverage check |
| Org Navigation | 1-2 | Hierarchy and headcount visibility |
| Onboarding | 3+ | New hire setup with cross-MCP provisioning |
| Payroll | 1-2 | Aggregate reporting (never individual) |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-hris-people-operations.git \
  ~/.skills/skills/hris-people-operations
```

## Requirements

**Required:** `mcp-hris` (14 tools)

**Cross-MCP:**
- `mcp-identity` — account provisioning on onboard/offboard
- `mcp-slack` — leave notifications, welcome messages
- `mcp-calendar` — OOO events, onboarding meetings
- `mcp-finance` — payroll journal entries

## Folder Structure

```
hris-people-operations/
├── SKILL.md                       # Main skill (decision tree + 5 workflows)
├── scripts/
│   └── validate_leave.py          # Balance, coverage, blackout validation
├── assets/
│   └── headcount-report.md        # Headcount output template
├── references/
│   ├── tool-sequences.md          # 14 tools + PII classification
│   ├── cross-mcp-workflows.md     # HRIS + Identity + Slack + Calendar + Finance
│   └── examples.md                # 3 real scenarios with traces
├── README.md
└── LICENSE
```

## PII Governance

| Data | Access Level |
|------|-------------|
| Name, title, department | All employees |
| Email, phone, location | Team + HR |
| **Salary, compensation** | **HR + Finance only** |
| **SSN, bank account** | **Payroll only** |

The skill NEVER exposes salary or financial data in responses.

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on HR queries |
| Privacy compliance | 0 salary/PII leaks |
| Leave validation | Balance + coverage checked before approval |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
