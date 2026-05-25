# HRIS Skill Examples

## Example 1: "Who is Sarah Mitchell?"

**User says:** "Look up Sarah Mitchell"

**Tool calls:**
```
1. get_directory(search: "Sarah Mitchell")
   → [{id: "emp_123", name: "Sarah Mitchell", title: "VP Engineering", dept: "Engineering"}]

2. get_employee(id: "emp_123")
   → {title: "VP Engineering", department: "Engineering", manager: "James K (CTO)", location: "Nairobi", start_date: "2022-03-15", email: "sarah@company.com"}
```

**Response:**
```
## Sarah Mitchell

| Field | Value |
|-------|-------|
| Title | VP Engineering |
| Department | Engineering |
| Manager | James K (CTO) |
| Location | Nairobi |
| Tenure | 2 years, 10 months |
| Email | sarah@company.com |
```

## Example 2: "I want to take Feb 10-14 off"

**User says:** "Request vacation for February 10-14"

**Tool calls:**
```
1. list_time_off(employee_id: "current_user", year: 2025)
   → {vacation: {balance: 15, used: 5, pending: 0}}

2. request_time_off(employee_id: "current_user", type: "vacation", start: "2025-02-10", end: "2025-02-14", reason: "Personal")
   → {id: "pto_456", status: "pending_approval"}
```

**Response:**
```
✅ Leave request submitted

**Type:** Vacation
**Dates:** Feb 10-14, 2025 (5 days)
**Balance:** 15 days available (5 used this year)
**After this request:** 10 days remaining
**Status:** ⏳ Pending manager approval

Your manager will be notified to approve.
```

## Example 3: "How big is the engineering team?"

**User says:** "What's the headcount in engineering?"

**Tool calls:**
```
1. get_headcount(department: "Engineering")
   → {total: 45, by_level: {senior: 12, mid: 20, junior: 13}, open_positions: 3}

2. list_departments(parent: "Engineering")
   → [{name: "Backend", count: 18}, {name: "Frontend", count: 15}, {name: "Platform", count: 12}]
```

**Response:**
```
## Engineering Headcount

**Total:** 45 engineers + 3 open positions

| Team | Headcount |
|------|-----------|
| Backend | 18 |
| Frontend | 15 |
| Platform | 12 |

| Level | Count |
|-------|-------|
| Senior | 12 (27%) |
| Mid | 20 (44%) |
| Junior | 13 (29%) |

**Open positions:** 3 (hiring in progress)
```
