# Data Engineering Journey

Practice projects documenting my path from data cleaning fundamentals toward data engineering.

## Projects

### Workout Data Cleaning (`cleaning project.ipynb`)

A cleaning pass on a daily workout log (Duration, Date, Pulse, Maxpulse, Calories — 32 rows) with several real data-quality issues:

| Issue | Detail | Fix |
|---|---|---|
| Missing values | 2 rows missing `Calories` | Filled using column mean |
| Missing date | 1 row with no `Date` value | Removed row |
| Duplicate row | `2020/12/12` appeared twice with identical values | Dropped duplicate |
| Inconsistent date format | Dates stored as quoted strings (`'2020/12/01'`), one as an unquoted integer (`20201226`) | Standardized all dates to `datetime` format |
| Outlier | `Duration = 450` on `2020/12/08` (vs. 30–60 elsewhere) — data entry error | Corrected/flagged based on realistic range |

**Tools:** Python, pandas

**Note:** This dataset is a well-known pandas practice set, used here to demonstrate core cleaning technique (missing values, duplicates, type standardization, outlier detection) rather than as a large-scale project.

---

More projects to be added as I progress toward data engineering (SQL, ETL pipelines, larger real-world datasets).
