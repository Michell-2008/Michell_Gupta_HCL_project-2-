# Student Academic Performance Dataset Cleaning

## Project purpose
This project performs data inspection and cleaning on the supplied
`02_student_performance.csv` dataset. It is intentionally limited to
data cleaning: it does not perform statistical analysis or create charts.

## Dataset
The supplied file is stored at `data/02_student_performance.csv`.
The source dataset has 500 rows and 11 columns.

## Tools
- Python
- PyCharm
- Pandas

## Setup
Open this folder in PyCharm. In the PyCharm terminal, run:

```bash
python -m pip install -r requirements.txt
```

## Run
Run `src/data_cleaning.py` from PyCharm, or from the project root:

```bash
python src/data_cleaning.py
```

## Cleaning steps
1. Load and inspect the CSV file.
2. Display column names, dimensions, first records and data types.
3. Count missing values in each column.
4. Identify duplicate `Student_ID` values. Records are not automatically deleted.
5. Fill missing `Attendance_Percent` values with the median attendance.
6. Check `Python_Marks`, `Maths_Marks` and `Physics_Marks` for values outside 0–100.
7. Save a cleaned copy and separate cleaning reports in `output/`.

## Dataset inspection findings
- 500 rows and 11 columns.
- 10 missing values, all in `Attendance_Percent`.
- No duplicate `Student_ID` values.
- No subject marks outside the 0–100 range.

## Cleaning decision
The median is used to fill missing attendance because it is less affected by
extreme values than the mean. The original CSV is preserved. Duplicate IDs
and invalid marks are reported rather than silently deleting or changing data.

## Output files
- `output/cleaned_student_performance.csv`
- `output/missing_values_report.csv`
- `output/duplicate_student_ids.csv`
- `output/invalid_score_report.csv`
