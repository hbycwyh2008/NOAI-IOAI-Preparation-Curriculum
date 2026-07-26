# Required Resource Link Verification — 2026-07-19

The required public resources were opened and checked on 2026-07-19. Redirects were followed where applicable.

This file is a historical verification note. For current checks, run `python scripts/check_required_links.py`, which now uses the current edX CS50P learning-page link and Coursera links for Coursera-hosted Andrew / DeepLearning course resources.

| Resource | Status | Current destination / note |
|---|---|---|
| CS50P | PASS | `https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f` — teacher-selected edX learning page |
| AI for Everyone | PASS | `https://www.coursera.org/learn/ai-for-everyone` |
| Machine Learning Specialization | PASS | `https://www.coursera.org/specializations/machine-learning-introduction` |
| Google ML Crash Course | PASS | Current Google for Developers course page accessible |
| StatQuest video index | PASS WITH REDIRECT | The old video-index URL redirects; verify the final topic page before class |
| 3Blue1Brown Neural Networks | PASS WITH REDIRECT | Topic URL redirects to the neural-networks-filtered site page |
| Deep Learning Specialization | PASS WITH REDIRECT | `https://www.coursera.org/specializations/deep-learning` |
| scikit-learn User Guide | PASS | Stable User Guide accessible |
| PyTorch Learn the Basics | PASS | Current tutorial page accessible |
| OpenCV University free courses | PASS | Free-course index accessible |
| Hugging Face LLM Course | PASS | Chapter 1 introduction accessible |
| Hugging Face Audio Course | PASS | Course introduction accessible |
| Qwen documentation | PASS WITH REDIRECT | Redirects to the current `en/latest` documentation |
| IOAI 2026 syllabus | PASS | Official 2026 syllabus page accessible |
| IOAI 2026 contest rules | PASS | Official 2026 rules page accessible; later updates/clarifications may supersede it |
| IOAI Education Hub | PASS | Official resource hub accessible |
| IOAI 2025 task repository | PASS | Official GitHub task/data archive accessible |
| NOAI 2025 task repository | PASS | IOAIChina public GitHub archive accessible |

## Required maintenance

- Run `python scripts/check_required_links.py` before each cohort and immediately before the lesson that uses the link.
- A reachable page may still require enrolment, payment, login, cookies, or region-specific access; test from a student account/network.
- Use the named lesson/module rather than relying on fragile video timestamps, except where `05_Resources/CS50P_edX_Timestamp_Map.md` deliberately records exact CS50P timestamp ranges.
- Archive the current organiser-supplied NOAI China handbook locally with version/date; do not invent or redistribute an unlicensed download URL.
- Current annual rules override historical task repositories and this curriculum.
