#!/usr/bin/env python3
"""
Leave Request Validator
Checks balance, team coverage, and blackout dates before approving.
Usage: python validate_leave.py '{"employee_id": "emp_123", "type": "vacation", "start": "2025-02-10", "end": "2025-02-14", "balance": 15, "team_size": 5, "team_on_leave": 1}'
"""
import json
import sys
from datetime import datetime, timedelta

BLACKOUT_DATES = []  # Add company-wide blackout dates here
MIN_COVERAGE_RATIO = 0.5  # At least 50% of team must be available

def validate_leave(data: dict) -> dict:
    result = {"valid": True, "errors": [], "warnings": []}

    start = datetime.strptime(data["start"], "%Y-%m-%d")
    end = datetime.strptime(data["end"], "%Y-%m-%d")
    days_requested = (end - start).days + 1
    balance = data.get("balance", 0)
    team_size = data.get("team_size", 1)
    team_on_leave = data.get("team_on_leave", 0)

    # Balance check
    if days_requested > balance:
        result["valid"] = False
        result["errors"].append(f"Insufficient balance: requesting {days_requested} days, only {balance} available")

    # Coverage check
    available_after = team_size - team_on_leave - 1  # -1 for this person
    if available_after / team_size < MIN_COVERAGE_RATIO:
        result["warnings"].append(f"Team coverage below 50%: only {available_after}/{team_size} available")

    # Blackout check
    for blackout in BLACKOUT_DATES:
        bd = datetime.strptime(blackout, "%Y-%m-%d")
        if start <= bd <= end:
            result["valid"] = False
            result["errors"].append(f"Overlaps blackout date: {blackout}")

    # Notice period
    days_notice = (start - datetime.now()).days
    if days_notice < 3:
        result["warnings"].append(f"Short notice: only {days_notice} days ahead (recommend 7+)")

    result["computed"] = {
        "days_requested": days_requested,
        "balance_after": balance - days_requested,
        "team_coverage": f"{available_after}/{team_size}",
        "notice_days": days_notice,
    }
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python validate_leave.py \'{"start": "2025-02-10", "end": "2025-02-14", "balance": 15, "team_size": 5, "team_on_leave": 1}\'')
        sys.exit(1)
    print(json.dumps(validate_leave(json.loads(sys.argv[1])), indent=2))
