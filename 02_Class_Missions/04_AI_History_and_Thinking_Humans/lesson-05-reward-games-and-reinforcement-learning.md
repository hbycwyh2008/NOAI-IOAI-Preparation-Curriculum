# Session 37 — Reward, Games, and Reinforcement Learning

**Class duration:** 70 minutes  
**Required reading before class:** Chapters 8–10  
**Essential question:** Does winning a game demonstrate intelligence that transfers to the real world?

## Required Mastery

Students must be able to:

1. Identify agent, environment, state, action, reward, and policy.
2. Distinguish supervised-learning labels from reinforcement-learning rewards.
3. Explain exploration versus exploitation.
4. Distinguish immediate reward from long-term return.
5. Explain how reward design shapes learned behaviour.
6. Explain reward hacking or specification gaming.
7. Explain why games provide clear rules, measurable outcomes, repeated simulation, and bounded action spaces.
8. Contrast game environments with incomplete, changing, socially consequential real environments.
9. Distinguish search, learning, and self-play.
10. Distinguish superhuman performance in one closed task from general intelligence.

## Misconceptions to Reject

- A task without human labels is free of human design choices.
- Maximising a written reward guarantees the intended human outcome.
- Game mastery automatically transfers to real-world decision making.
- A reinforcement-learning agent understands the meaning of its reward.

## Core Pattern

```text
state
→ action
→ environment response
→ reward
→ policy update
```

The class must also preserve this distinction:

```text
specified reward ≠ intended human goal
```

## 70-Minute Learning Cycle

| Time | Block | Required student action |
|---:|---|---|
| 0–7 | **Skill Warm-Up** | Label agent, state, action, reward, and policy in short scenarios. |
| 7–14 | **Talk Robin 1** | Compare one game success with one reason that real environments are harder. |
| 14–20 | **Entry Check** | Explain the difference between a label and a reward signal. |
| 20–32 | **Core Pattern** | Reconstruct the reinforcement-learning interaction loop and the reward–intention gap. |
| 32–48 | **Guided Practice** | Design a reward for a classroom-cleaning robot and identify behaviours that could maximise the score while violating the real goal. |
| 48–62 | **Independent Rebuild** | Specify a reinforcement-learning task with state, actions, reward, episode boundary, likely reward loophole, and at least one safety constraint. |
| 62–70 | **Talk Robin 2 + Evidence** | Defend the reward design and explain the most serious loophole. |

## Exit Evidence

Explain why achieving the specified reward does not prove that a machine understands the designer’s true intention.

## Gate

The student passes only when the task definition includes a plausible unintended strategy and a concrete method for detecting or limiting it.
