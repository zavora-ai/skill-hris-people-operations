# HRIS Tool Sequences Reference

## Tool Inventory (mcp-hris, 14 tools)

| Tool | Risk | Purpose |
|------|------|---------|
| `list_employees` | read | List with filters (dept, status, location) |
| `get_employee` | read | Full employee record |
| `create_employee` | write | Onboard new hire |
| `update_employee` | write | Update employee details |
| `list_departments` | read | All departments |
| `get_department` | read | Department details + headcount |
| `request_time_off` | write | Submit leave request |
| `list_time_off` | read | Leave balance and history |
| `approve_time_off` | write | Manager approves leave |
| `list_payroll` | read | Payroll runs (aggregate only) |
| `run_payroll` | financial | Execute payroll (requires approval) |
| `get_org_chart` | read | Reporting hierarchy |
| `get_headcount` | read | Team sizes by department |
| `get_directory` | read | Employee directory search |

## Sequence: Employee Lookup (1-2 calls)

```
1. get_directory(search: "Sarah Mitchell")
   → [{id: "emp_123", name: "Sarah Mitchell", title: "VP Engineering", dept: "Engineering", email: "sarah@company.com"}]

2. get_employee(id: "emp_123")
   → {name, title, department, manager: "CTO", location: "Nairobi", start_date: "2022-03-15", status: "active"}
   ⚠️ NEVER return: salary, SSN, bank_account
```

## Sequence: Leave Request (3 calls)

```
1. list_time_off(employee_id: "emp_123", year: 2025)
   → {vacation: {balance: 15, used: 5, pending: 2}, sick: {balance: 10, used: 1}}

2. request_time_off(
     employee_id: "emp_123",
     type: "vacation",
     start: "2025-02-10",
     end: "2025-02-14",
     reason: "Family holiday"
   )
   → {id: "pto_456", status: "pending_approval", approver: "manager_789"}

3. [Manager action] approve_time_off(request_id: "pto_456")
   → {status: "approved"}
```

## Sequence: Org Navigation (2 calls)

```
1. get_org_chart(department: "Engineering")
   → {head: "CTO", reports: [{name: "VP Eng", reports: [{name: "Team Lead 1", reports: [...]}, ...]}]}

2. get_headcount(department: "Engineering")
   → {total: 45, by_level: {senior: 12, mid: 20, junior: 13}, open_positions: 3}
```

## Sequence: New Hire Onboarding (3 calls)

```
1. get_directory(search: "new.hire@company.com")
   → [] (verify no duplicate)

2. create_employee(
     first_name: "Alex",
     last_name: "Johnson",
     email: "alex.johnson@company.com",
     title: "Software Engineer",
     department: "Engineering",
     manager_id: "emp_lead_1",
     start_date: "2025-02-01",
     location: "Remote"
   )
   → {id: "emp_new_456"}

3. [Cross-MCP] identity: lifecycle_task(type: "onboard", user_id: "emp_new_456")
   → Provisions accounts, assigns base groups, enables MFA
```

## PII Classification

| Field | Sensitivity | Who Can Access |
|-------|-------------|---------------|
| Name, title, department | Low | All employees |
| Email, phone, location | Medium | Team + HR |
| Manager, start date | Medium | Team + HR |
| **Salary, compensation** | **Critical** | **HR + Finance only** |
| **SSN, tax ID** | **Critical** | **HR + Payroll only** |
| **Bank account** | **Critical** | **Payroll only** |
