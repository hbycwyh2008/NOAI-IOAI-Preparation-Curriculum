from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import sys
import requests

URLS = {
    "CS50P": "https://cs50.harvard.edu/python/",
    "AI for Everyone": "https://www.deeplearning.ai/courses/ai-for-everyone/",
    "Machine Learning Specialization": "https://www.deeplearning.ai/specializations/machine-learning",
    "Google ML Crash Course": "https://developers.google.com/machine-learning/crash-course",
    "StatQuest video index": "https://statquest.org/video-index/",
    "3Blue1Brown neural networks": "https://www.3blue1brown.com/topics/neural-networks",
    "Deep Learning Specialization": "https://www.deeplearning.ai/courses/deep-learning-specialization/",
    "scikit-learn User Guide": "https://scikit-learn.org/stable/user_guide.html",
    "PyTorch Learn the Basics": "https://docs.pytorch.org/tutorials/beginner/basics/intro.html",
    "PyTorch tutorials": "https://docs.pytorch.org/tutorials/",
    "OpenCV University free courses": "https://opencv.org/university/free-courses/",
    "Hugging Face LLM Course": "https://huggingface.co/learn/llm-course/en/chapter1/1",
    "Hugging Face Audio Course": "https://huggingface.co/learn/audio-course/en/chapter0/introduction",
    "Qwen documentation": "https://qwen.readthedocs.io/",
    "IOAI 2026 syllabus": "https://ioai-official.org/republic-of-kazakhstan/syllabus-2026/",
    "IOAI 2026 contest rules": "https://ioai-official.org/republic-of-kazakhstan/2026-contest-rules/",
    "IOAI Education Hub": "https://ioai-official.org/resources/",
    "IOAI 2025 task repository": "https://github.com/IOAI-official/IOAI-2025",
    "NOAI 2025 task repository": "https://github.com/IOAIChina/NOAI-2025",
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
        response.close()
        if 200 <= code < 400:
            return "PASS", code, response.url
        if code in {401, 403, 429}:
            return "RESTRICTED/REACHABLE", code, response.url
        return "FAIL", code, response.url
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
        "`RESTRICTED/REACHABLE` means the host answered but blocked automated access or rate-limited the request; verify manually before class.",
        "",
        "| Resource | URL | Status | HTTP | Final URL / detail |",
        "|---|---|---|---:|---|",
    ]
    for name, url, status, code, detail in rows:
        safe_detail = detail.replace("|", "\\|")
        lines.append(f"| {name} | {url} | {status} | {code or ''} | {safe_detail} |")
    lines += [
        "",
        "## Local-only item",
        "",
        "The current NOAI China handbook/syllabus supplied by the organiser or teacher must be archived locally with its version and date. It is not replaced by an inferred public URL.",
    ]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(output)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
