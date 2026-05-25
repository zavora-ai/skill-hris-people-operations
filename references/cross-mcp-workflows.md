# HRIS Cross-MCP Workflows

## HRIS + Identity: Employee Onboarding

```
HRIS: create_employee(name: "Alex Johnson", dept: "Engineering", start: "2025-02-01") → {id: "emp_456"}
IDENTITY: lifecycle_task(type: "onboard", user_id: "emp_456", role: "engineer")
  → Provisions: email, Slack, GitHub, Jira, VPN access
IDENTITY: check_mfa(user_id: "emp_456") → verify MFA enrolled
SLACK: send_message(channel: "#engineering", text: "👋 Welcome Alex Johnson! Starting Feb 1 as Software Engineer.")
CALENDAR: create_event(title: "Alex Johnson — Onboarding Kickoff", attendees: [alex, manager, hr])
```

## HRIS + Identity: Employee Offboarding

```
HRIS: update_employee(id: "emp_789", status: "terminated", last_day: "2025-01-31")
IDENTITY: lifecycle_task(type: "offboard", user_id: "emp_789")
  → Revokes: all access, disables accounts, transfers ownership
IDENTITY: emergency_revoke(user_id: "emp_789", reason: "Employment terminated")
EMAIL: send_email(to: "emp_789@company.com", subject: "Account deactivation notice")
```

## HRIS + Slack: Leave Notifications

```
HRIS: approve_time_off(request_id: "pto_456") → {employee: "Sarah", dates: "Feb 10-14"}
SLACK: send_message(channel: "#engineering", text: "📅 Sarah Mitchell OOO Feb 10-14. Coverage: @backup_engineer")
CALENDAR: create_event(title: "Sarah Mitchell — OOO", start: "Feb 10", end: "Feb 14", show_as: "away")
```

## HRIS + Finance: Payroll Integration

```
HRIS: run_payroll(period: "2025-01") → {total_gross: 450000, total_net: 320000, employees: 45}
FINANCE: create_journal_entry(
  debit: {account: "salary_expense", amount: 450000},
  credit: {account: "payroll_payable", amount: 450000}
)
BANKING: get_balances(account: "payroll") → verify sufficient funds
NOTIFICATIONS: send_notification(recipient: "finance_manager", title: "Payroll ready: $3,200 net for 45 employees")
```

## HRIS + Calendar: Team Coverage

```
HRIS: list_time_off(department: "Engineering", period: "next_week")
  → [{employee: "Sarah", dates: "Feb 10-14"}, {employee: "Tom", dates: "Feb 12-13"}]
SLACK: send_message(channel: "#engineering", text: "📅 *Next Week Coverage*\n• Sarah: OOO Mon-Fri\n• Tom: OOO Wed-Thu\n• Min coverage: 3 engineers available ✅")
```
