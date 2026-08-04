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

Copy the mastery dashboard and model-recognition answer record into your own course repository. The teacher creates a separate private progress ledger from the example using a pseudonymous student ID. Do not reuse the example file as a real record and do not store a name or email address in the ledger.

Update the dashboard after every assigned Session and the recognition record after every assigned daily set. Each claimed level must link to evidence that you can explain and reconstruct. The machine-readable ledger records only route state, Red debt, qualifications, assigned Set IDs, and reviewed scores.

Generate the assigned worksheet with your private ledger:

```bash
python scripts/generate_daily_model_drill.py \
  --date YYYY-MM-DD \
  --level mixed \
  --progress student-progress/student-001.json \
  --record-progress \
  --output daily-drills/YYYY-MM-DD.md
```

The same date, level, count, and history state produce the same Set ID. Recent assigned scenarios are avoided when possible. Do not search for a public answer key or delete assignments from the ledger; the correction process is part of the evidence.

The canonical class entry point remains [Class Missions](../02_Class_Missions/README.md). Use the [Workflow Competency Crosswalk](../00_Course_Overview/Workflow_Competency_Crosswalk.md) to understand the evidence gates that recur across the course, and use only the executable pathway assigned by your teacher.
