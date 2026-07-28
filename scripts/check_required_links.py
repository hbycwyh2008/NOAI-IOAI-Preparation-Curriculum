from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import requests

URLS = {
    "Harvard CS50’s Introduction to Programming with Python": "https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@5c4566382df54814ba604df6369ca2fc/block-v1:HarvardX+CS50P+Python+type@vertical+block@8cbabae6d04047638c12604d810d127f",
    "北京市十一学校《中学机器学习十五讲》": "https://www.bohrium.com/courses/5963419225/content?file=8496",
    "台湾大学李宏毅《机器学习》内容精选版": "https://www.bohrium.com/courses/7890895681/content?file=2496",
    "AI for Everyone": "https://www.coursera.org/learn/ai-for-everyone",
    "Machine Learning Specialization": "https://www.coursera.org/specializations/machine-learning-introduction",
    "Course 1 — Supervised Machine Learning: Regression and Classification": "https://www.coursera.org/learn/machine-learning",
    "Course 2 — Advanced Learning Algorithms": "https://www.coursera.org/learn/advanced-learning-algorithms",
    "Deep Learning Specialization": "https://www.coursera.org/specializations/deep-learning",
    "Course 2 — Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization": "https://www.coursera.org/learn/deep-neural-network",
    "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow": "https://github.com/ageron/handson-ml3",
    "DeepLearning.AI PyTorch for Deep Learning Professional Certificate": "https://www.coursera.org/professional-certificates/pytorch-for-deep-learning",
    "Course 1 — PyTorch: Fundamentals": "https://www.coursera.org/learn/pytorch-fundamentals",
    "Course 2 — PyTorch: Techniques and Ecosystem Tools": "https://www.coursera.org/learn/pytorch-techniques-and-ecosystem-tools",
    "Course 3 — PyTorch: Advanced Architectures and Deployment": "https://www.coursera.org/learn/pytorch-advanced-architectures-and-deployment",
    "Google Machine Learning Crash Course": "https://developers.google.com/machine-learning/crash-course",
    "StatQuest Video Index": "https://statquest.org/video-index/",
    "3Blue1Brown Neural Networks": "https://www.3blue1brown.com/topics/neural-networks",
    "NumPy Documentation": "https://numpy.org/doc/stable/",
    "Pandas — 10 Minutes to Pandas": "https://pandas.pydata.org/docs/user_guide/10min.html",
    "Pandas — Working with Missing Data": "https://pandas.pydata.org/docs/user_guide/missing_data.html",
    "Pandas — Group By": "https://pandas.pydata.org/docs/user_guide/groupby.html",
    "Matplotlib Pyplot Tutorial": "https://matplotlib.org/stable/tutorials/pyplot.html",
    "Scikit-Learn User Guide": "https://scikit-learn.org/stable/user_guide.html",
    "PyTorch Learn the Basics": "https://docs.pytorch.org/tutorials/beginner/basics/intro.html",
    "PyTorch Tutorials": "https://docs.pytorch.org/tutorials/",
    "Optuna Documentation": "https://optuna.readthedocs.io/",
    "OpenCV University Free Courses": "https://opencv.org/university/free-courses/",
    "Hugging Face LLM Course": "https://huggingface.co/learn/llm-course/en/chapter1/1",
    "Hugging Face Audio Course": "https://huggingface.co/learn/audio-course/en/chapter0/introduction",
    "Qwen Documentation": "https://qwen.readthedocs.io/",
    "IOAI 2026 Syllabus": "https://ioai-official.org/republic-of-kazakhstan/syllabus-2026/",
    "IOAI 2026 Contest Rules": "https://ioai-official.org/republic-of-kazakhstan/2026-contest-rules/",
    "IOAI Education Hub": "https://ioai-official.org/resources/",
    "IOAI 2025 Task Repository": "https://github.com/IOAI-official/IOAI-2025",
    "NOAI 2025 Task Repository": "https://github.com/IOAIChina/NOAI-2025",
}


def check(name: str, url: str) -> tuple[str, int | None, str]:
    try:
        response = requests.get(
            url,
            timeout=25,
            allow_redirects=True,
            stream=True,
            headers={"User-Agent": "NOAI-Curriculum-Link-Checker/1.0"},
        )
        code = response.status_code
        final_url = response.url
        response.close()
        if 200 <= code < 400:
            return "PASS", code, final_url
        if code in {401, 403, 429}:
            return "RESTRICTED/REACHABLE", code, final_url
        return "FAIL", code, final_url
    except requests.RequestException as exc:
        return "ERROR", None, f"{type(exc).__name__}: {exc}"


def main() -> int:
    rows = []
    failures = 0
    for name, url in URLS.items():
        status, code, detail = check(name, url)
        rows.append((name, url, status, code, detail))
        if status in {"FAIL", "ERROR"}:
            failures += 1

    output = Path("10_Ready_to_Teach_Pack/Link_Verification_Latest.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Required Resource Link Verification",
        "",
        f"Checked: {datetime.now(timezone.utc).isoformat()}",
        "",
        "`RESTRICTED/REACHABLE` means the host answered but blocked automated access, required authentication, or rate-limited the request; verify manually before class.",
        "",
        "| Resource | URL | Status | HTTP | Final URL / detail |",
        "|---|---|---|---:|---|",
    ]
    for name, url, status, code, detail in rows:
        safe_detail = detail.replace("|", "\\|")
        lines.append(f"| {name} | {url} | {status} | {code or ''} | {safe_detail} |")
    lines += [
        "",
        "## Manual checks still required",
        "",
        "- Authenticated edX, Coursera, and Bohrium pages must be opened from the actual teacher/student account.",
        "- Course week, module, video title, duration, and access terms must be checked before each cohort.",
        "- The current NOAI China handbook/syllabus supplied by the organiser or teacher must be archived locally with its version and date. It is not replaced by an inferred public URL.",
        "- Current competition rules override links, historical repositories, and curriculum assumptions.",
    ]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(output)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
