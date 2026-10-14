# Sample audit report: warehouse process audits, July to October 2026

> **All data in this report is fictional** and was generated for this learning project. It does not describe any real site, employer or person.

## 1. Purpose
To show how routine and confirmation audit results can be analysed and reported to operational managers: what was found, where the risk sits, and what should happen next.

## 2. Scope and method
- 59 routine audits and 12 confirmation audits across five areas: Goods In, Picking, Despatch, Returns and Hazardous Storage.
- Each audit used a checklist of 10 to 20 checks. An audit **passes at 90% or higher**.
- Results are held in [`data/audit-tracker.xlsx`](../data/audit-tracker.xlsx) and summarised with [`scripts/audit_trends.py`](../scripts/audit_trends.py).

## 3. Headline results
- **25% of routine audits failed** (15 of 59).
- **Returns is the main concern:** 8 of 12 audits failed (67%), with an average pass rate of 87%.
- Despatch failed 3 of 12 (25%). Picking and Hazardous Storage each failed 2 of 13 (15%). Goods In failed none of 9.

| Area | Audits | Failed | Fail rate | Average pass rate |
|---|---|---|---|---|
| Returns | 12 | 8 | 67% | 87% |
| Despatch | 12 | 3 | 25% | 93% |
| Picking | 13 | 2 | 15% | 93% |
| Hazardous Storage | 13 | 2 | 15% | 96% |
| Goods In | 9 | 0 | 0% | 96% |

## 4. Trend over time

| Month | Audits | Failed | Fail rate |
|---|---|---|---|
| July | 18 | 3 | 17% |
| August | 17 | 6 | 35% |
| September | 18 | 5 | 28% |
| October (to date) | 6 | 1 | 17% |

Failures peaked in August and have eased since. October covers only part of the month, so it is too early to call it an improvement.

## 5. Most common findings
1. Reason code missing: 5
2. Late processing: 3
3. Item not quarantined: 3
4. Load not secured: 3
5. Wrong location pick: 2

Three of the top findings sit in Returns processing. Two (reason codes and quarantine) are paperwork and control points rather than speed issues.

## 6. Confirmation audits
Of the 15 failed routine audits:
- **8 closed**: the confirmation audit passed.
- **4 re-failed**: the issue was not fixed. These need escalating to the area supervisor.
- **3 awaiting** a confirmation audit.

## 7. Recommendations
1. **Returns:** brief the team on the reason code and quarantine steps, and have the supervisor check these two points daily for two weeks.
2. **Re-failed items:** agree actions and owners for the four re-failed audits with the area supervisor this week.
3. **Confirmation backlog:** complete the three outstanding confirmation audits within seven days.
4. **Next review:** re-run the analysis at the end of November. If Returns is still above a 25% fail rate, move it to weekly audits.

## 8. Confidentiality
Audit results identify individuals and shifts in real use. In practice this report would go only to the managers who need it.
