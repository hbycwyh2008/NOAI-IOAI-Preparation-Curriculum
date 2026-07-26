# BML15 70-Minute Lesson Split

This plan converts 北京市十一学校《中学机器学习十五讲》 into a practical after-school club sequence.

The purpose is not to make students passively finish videos. Each lesson uses the full assigned video as the **Skill Warm-Up**, then moves through the classroom flow:

**Skill Warm-Up → Talk Robin 1 → Entry Check → Core Pattern → Guided Practice → Independent Rebuild → Talk Robin 2 + Evidence**

## Planning Assumptions

- Standard duration for this BML15 sequence: **70 minutes per club session**.
- Students watch the assigned video in full when possible.
- If the assigned video is too long for meaningful practice and rebuild, reduce practice size rather than removing **Independent Rebuild**.
- If a future Bohrium update changes video titles or duration, teachers must update this file before the next cohort.
- This sequence is mainly for **NOAI Round 1 A/B**: Python-related reasoning, AI foundations, machine-learning concepts, and paper-test explanations.

## Sequence Overview

| Lesson | Video content | Video time | Remaining class time | Main classroom focus |
|---:|---|---:|---:|---|
| 1 | 第零讲：目录视频 | 28:17 | 41:43 | Build the NOAI/AI learning map and evidence expectations. |
| 2 | 第一讲：人工智能的定义 | 40:09 | 29:51 | Define AI, distinguish AI from non-AI, connect to official A/B concepts. |
| 3 | 第二讲：人工智能发展史 | 45:43 | 24:17 | Symbolism, connectionism, behaviourism, Turing Test. |
| 4 | 第三讲：连接主义与机器学习 | 48:48 | 21:12 | Data-driven learning, model, training, inference. |
| 5 | 第四讲：面向对象编程与机器学习标准库 | 36:23 | 33:37 | Python objects, libraries, sklearn/documentation awareness. |
| 6 | 第五讲：机器学习训练模型的范式 | 44:02 | 25:58 | Data → Model → Training → Prediction → Evaluation. |
| 7 | 第六讲：分类问题与逻辑斯蒂回归 | 41:12 | 28:48 | Classification, probability, decision boundary, confusion matrix. |
| 8 | 第七讲：求解机器学习问题——优化理论 | 40:54 | 29:06 | Loss function, gradient descent, optimisation reasoning. |
| 9 | 第八讲：神经网络与反向传播算法 | 38:29 | 31:31 | Forward pass, loss, backward pass, optimiser step. |
| 10 | 第九讲：距离与K近邻算法 + 第十一讲：贝叶斯理论 | 39:45 | 30:15 | Distance-based reasoning and probability-based reasoning. |
| 11 | 第十讲：支持向量机与拉格朗日乘子法 | 41:52 | 28:08 | Margin, boundary, SVM intuition. |
| 12 | 第十二讲：信息熵与决策树 + 第十三讲：多分类问题与集成学习 | 49:37 | 20:23 | Entropy, decision tree, random forest, ensemble learning. |
| 13 | 第十四讲：无监督学习和强化学习简介 | 28:03 | 41:57 | Clustering, unsupervised learning, reinforcement-learning scenario recognition. |
| 14 | 第十五讲：深度神经网络 | 52:23 | 17:37 | Deep-network synthesis and bridge to Round 2 / PyTorch. |

## Timing Templates

### Template A — video is about 28–37 minutes

Use for Lessons 1, 5, and 13.

| Time | Block | Student output |
|---|---|---|
| 0–video end | Skill Warm-Up | Watch full video and complete guided notes. |
| next 5 min | Talk Robin 1 | Explain main idea and confusion to a partner. |
| next 7 min | Entry Check | Answer short concept/code/scenario questions. |
| next 8–10 min | Core Pattern | Teacher extracts one reusable pattern. |
| next 10–15 min | Guided Practice | Apply pattern with support. |
| next 6–8 min | Independent Rebuild | Rebuild pattern on a new example. |
| final 3 min | Talk Robin 2 + Evidence | Explain and submit evidence. |

### Template B — video is about 38–45 minutes

Use for Lessons 2, 6, 7, 8, 9, and 11.

| Time | Block | Student output |
|---|---|---|
| 0–video end | Skill Warm-Up | Watch full video and complete guided notes. |
| next 5 min | Talk Robin 1 | Partner explanation. |
| next 5 min | Entry Check | Core check. |
| next 7 min | Core Pattern | Teacher extracts one pattern. |
| next 8–10 min | Guided Practice | Small supported task. |
| next 4–6 min | Independent Rebuild | Minimal independent rebuild. |
| final 2–3 min | Talk Robin 2 + Evidence | Submit notes, check, and rebuild. |

### Template C — video is about 46–53 minutes

Use for Lessons 3, 4, 12, and 14.

| Time | Block | Student output |
|---|---|---|
| 0–video end | Skill Warm-Up | Watch full video and complete guided notes. |
| next 4 min | Talk Robin 1 | Identify the teacher's main explanation and one confusion. |
| next 4 min | Entry Check | Answer the highest-priority check questions. |
| next 5 min | Core Pattern | Teacher compresses the video into one testable pattern. |
| next 5 min | Guided Practice | One micro-task only. |
| next 3 min | Independent Rebuild | One new example or one short explanation. |
| final 2 min | Talk Robin 2 + Evidence | Submit evidence. |

## Lesson-by-Lesson Evidence Requirements

| Lesson | Required evidence |
|---:|---|
| 1 | Learning map; three key terms; one personal goal; one confusion. |
| 2 | AI definition; one AI/non-AI contrast; one ethical or capability boundary. |
| 3 | Table comparing symbolism, connectionism, behaviourism, and Turing Test. |
| 4 | Data → model → training → inference explanation. |
| 5 | Library/documentation usage note; one simple sklearn-style workflow sketch. |
| 6 | Complete ML workflow diagram with evaluation evidence. |
| 7 | Classification scenario; decision boundary explanation; confusion-matrix mini-check. |
| 8 | Loss/gradient/descent explanation and one optimisation misconception. |
| 9 | Forward/loss/backward/optimiser trace in words or a simple table. |
| 10 | KNN vs Bayes comparison: distance reasoning vs probability reasoning. |
| 11 | SVM margin/boundary explanation with one visual or verbal example. |
| 12 | Entropy/tree/ensemble comparison table. |
| 13 | Supervised vs unsupervised vs reinforcement-learning scenario sort. |
| 14 | Deep neural network synthesis and bridge to PyTorch Round 2 practice. |

## Placement in the Curriculum

Use this split in two places:

1. `02_Class_Missions/05-learning-paradigms/lesson-03-bml15-full-video.md` — concept-building use.
2. `02_Class_Missions/15-round-1-exam-training/lesson-05-bml15-round1-review.md` — Round 1 A/B review use.

The same video sequence can be taught once as the main concept-building path, or selectively reused before Round 1 paper-test mocks.

## Non-Negotiable Teaching Rule

Watching the video is never the final product. Every lesson must end with at least:

1. completed guided notes;
2. one Entry Check response;
3. one Core Pattern statement;
4. one Guided Practice or Independent Rebuild artifact;
5. one short explanation submitted orally or in writing.
