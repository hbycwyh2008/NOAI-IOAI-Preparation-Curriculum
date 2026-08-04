# Student Setup and Evidence Index

Complete these files in order before or during the opening Sessions:

1. [How This Course Works](00_How_This_Course_Works.md)
2. [Set Up the Student GitHub Repository](01_Set_Up_Student_GitHub_Repo.md)
3. [Set Up Python and Jupyter](02_Set_Up_Python_Jupyter.md)
4. [Set Up Bohrium](03_Set_Up_Bohrium.md)
5. [How to Submit Evidence](04_How_To_Submit_Evidence.md)
6. [AI Use Policy](05_AI_Use_Policy.md)
7. [Competition Notebook Rules](06_Competition_Notebook_Rules.md)
8. [Student Mastery Dashboard](07_Mastery_Dashboard.md)
9. [Student Progress Example](../03_Templates/Student_Progress.example.json)
10. [Model Recognition Daily Drills](../04_Assessment/Model_Recognition_Drills/README.md)
11. [Model Recognition Answer Record](../04_Assessment/Model_Recognition_Drills/Answer_Record.md)

Copy the mastery dashboard and model-recognition answer record into your own course repository. The teacher creates a separate private schema-v2 progress ledger with a pseudonymous student ID. Do not reuse the public example as a real record and do not store a name, email address, protected answer, credential, or hidden label.

The ledger records route state, Red debt, pathway qualifications, one drill assignment per date, task-family accuracy, baseline/metric accuracy, total score, and private-confirmation status. Earlier schema-v1 ledgers must be migrated with:

```bash
python scripts/manage_student_progress.py migrate \
  --path student-progress/student-001.json
```

Generate the assigned worksheet with the private ledger:

```bash
python scripts/generate_daily_model_drill.py \
  --date YYYY-MM-DD \
  --level mixed \
  --progress student-progress/student-001.json \
  --record-progress \
  --output daily-drills/YYYY-MM-DD.md
```

Rerunning the same recorded date restores the same Set ID. Recent assigned scenarios are avoided when possible, and a different second assignment on that date is rejected.

The teacher may generate a progress report showing route completion, Red debt, pending reviews, the dual-threshold five-set streak, secured confirmation, and maintenance due. That report uses ledger metadata only and does not replace the detailed evidence in the dashboard, worksheet, notebook, code, or correction record.

The canonical class entry point remains [Class Missions](../02_Class_Missions/README.md). Use the [Workflow Competency Crosswalk](../00_Course_Overview/Workflow_Competency_Crosswalk.md) to understand the recurring evidence gates, and use only the executable pathway assigned by your teacher.
