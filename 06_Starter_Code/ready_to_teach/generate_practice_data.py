"""Generate reproducible, non-scored practice datasets.

This script intentionally generates *practice* data whose mechanism is visible.
For scored mocks, the teacher must generate a separate hidden-label package.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def sigmoid(values: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-values))


def generate_tabular(output: Path, seed: int) -> None:
    rng = np.random.default_rng(seed)
    n = 900
    school = rng.choice([f"S{i:02d}" for i in range(15)], n)
    device = rng.choice(["desktop", "tablet", "phone"], n, p=[0.45, 0.2, 0.35])
    course = rng.choice(["python", "web", "ai"], n)
    age = np.clip(rng.normal(16, 1.4, n), 13, 20)
    weekly_hours = np.clip(rng.gamma(2.2, 2.4, n), 0, 20)
    assignments = rng.integers(0, 13, n)
    forum_posts = rng.poisson(2.4, n)
    late_ratio = np.clip(rng.beta(1.5, 5.0, n), 0, 1)
    school_effects = {name: effect for name, effect in zip(sorted(set(school)), rng.normal(0, 0.35, 15))}

    logit = (
        -1.2
        + 0.22 * (5 - weekly_hours)
        + 0.18 * (7 - assignments)
        + 1.9 * late_ratio
        - 0.09 * forum_posts
        + np.array([school_effects[value] for value in school])
        + (device == "phone") * 0.25
    )
    target = rng.binomial(1, sigmoid(logit))

    frame = pd.DataFrame(
        {
            "student_id": [f"P{i:05d}" for i in range(n)],
            "school_id": school,
            "device": device,
            "course": course,
            "age": age.round(1),
            "weekly_hours": weekly_hours.round(2),
            "assignments_completed": assignments,
            "forum_posts": forum_posts,
            "late_ratio": late_ratio.round(3),
            "target": target,
        }
    )
    for column, fraction in {"age": 0.04, "weekly_hours": 0.07, "device": 0.03}.items():
        indexes = rng.choice(frame.index, int(n * fraction), replace=False)
        frame.loc[indexes, column] = np.nan

    frame.to_csv(output / "tabular_practice.csv", index=False)


def generate_text(output: Path, seed: int) -> None:
    rng = np.random.default_rng(seed + 1)
    positive = ["clear", "helpful", "excellent", "understand", "works", "fast"]
    negative = ["confusing", "broken", "slow", "error", "unclear", "fails"]
    neutral = ["lesson", "model", "code", "data", "project", "video"]
    rows: list[dict[str, object]] = []

    for index in range(600):
        label = int(rng.random() > 0.5)
        sentiment = positive if label else negative
        words = list(rng.choice(neutral, size=rng.integers(2, 5), replace=True))
        words += list(rng.choice(sentiment, size=rng.integers(1, 3), replace=True))
        if rng.random() < 0.15:
            words.insert(0, "not")
            label = 1 - label
        rng.shuffle(words)
        rows.append(
            {
                "text_id": f"T{index:04d}",
                "source": rng.choice(["survey", "forum", "email"]),
                "text": " ".join(words),
                "label": label,
            }
        )

    pd.DataFrame(rows).to_csv(output / "text_practice.csv", index=False)


def generate_diagrams(output: Path, seed: int) -> None:
    rng = np.random.default_rng(seed + 2)
    image_dir = output / "diagram_images"
    image_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, object]] = []
    shapes = ["circle", "rectangle", "triangle"]

    for index in range(240):
        shape = str(rng.choice(shapes))
        size = str(rng.choice(["small", "large"]))
        stated_shape = shape if rng.random() > 0.5 else str(rng.choice([item for item in shapes if item != shape]))
        label = int(stated_shape == shape)
        sample_id = f"D{index:04d}"

        figure, axis = plt.subplots(figsize=(2, 2))
        axis.set_xlim(0, 1)
        axis.set_ylim(0, 1)
        axis.axis("off")
        radius = 0.18 if size == "small" else 0.32
        if shape == "circle":
            patch = plt.Circle((0.5, 0.5), radius, fill=False, linewidth=4)
        elif shape == "rectangle":
            side = radius * 2
            patch = plt.Rectangle((0.5 - side / 2, 0.5 - side / 2), side, side * 0.75, fill=False, linewidth=4)
        else:
            points = np.array([[0.5, 0.5 + radius], [0.5 - radius, 0.5 - radius], [0.5 + radius, 0.5 - radius]])
            patch = plt.Polygon(points, fill=False, linewidth=4)
        axis.add_patch(patch)
        figure.savefig(image_dir / f"{sample_id}.png", dpi=80, bbox_inches="tight", pad_inches=0.05)
        plt.close(figure)

        records.append(
            {
                "sample_id": sample_id,
                "caption": f"The diagram contains a {size} {stated_shape}.",
                "source": str(rng.choice(["generator_a", "generator_b"])),
                "label": label,
            }
        )

    pd.DataFrame(records).to_csv(output / "diagram_caption_practice.csv", index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("practice_data"))
    parser.add_argument("--seed", type=int, default=2026)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    generate_tabular(args.output, args.seed)
    generate_text(args.output, args.seed)
    generate_diagrams(args.output, args.seed)
    print(f"Practice data written to {args.output.resolve()}")


if __name__ == "__main__":
    main()
