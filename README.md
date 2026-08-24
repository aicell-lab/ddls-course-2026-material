# DDLS 2026 — Course Material

Shared course material for the **Data-Driven Life Sciences (DDLS) 2026** course at
KTH Royal Institute of Technology (SK2538 / FSK3538), run by AICell Lab (SciLifeLab / KTH).

- **Course website:** https://ddls.aicell.io/course/ddls-2026/
- **Schedule:** https://ddls.aicell.io/course/ddls-2026/schedule/

This repository holds the hands-on material students need each week — computer-lab
lab briefs, agent prompts, datasets and helper code. The
lectures, overview, and registration details live on the course website.

## Get the material

```bash
git clone https://github.com/aicell-lab/ddls-course-2026-material.git
cd ddls-course-2026-material
```

Run `git pull` before each lab — each week's material appears at the start of that week.

## Before the first lab — set up your tools

The computer labs are run from your terminal with two CLIs: **Codex** (your AI agent) and the
**Google Colab CLI** (free T4 GPUs in the cloud). Follow
**[`setup/README.md`](setup/README.md)** — about 20 minutes, do it before Week 1.

## How the computer labs work (new in 2026)

In each lab you play the role of a **data analyst**. A collaborator has handed you a
biological dataset — and that collaborator is simulated by an AI agent who is a wet-lab
scientist with no data-science background. Your job:

1. **Interview the data-owner agent** to work out what the biological question actually is.
2. **Summarise** what you learned into a brief.
3. **Write the system prompt** for your own data-analyst agent from that brief.
4. **Do the analysis** with your agent, deferring heavy compute to Google Colab.

You present that analysis at Friday's seminar — the seminar is your work, not a paper. Prompting, context building and how to instruct
an agent are covered in the Tuesday lecture.

## Structure

| Folder | Topic |
|--------|-------|
| [`week-1/`](week-1/) | Introduction to Data-Driven Life Sciences |
| [`week-2/`](week-2/) | Image Analysis and Microscopy |
| [`week-3/`](week-3/) | Precision Medicine and Systems Biology |
| [`week-4/`](week-4/) | Protein Structure and Molecular Biology |
| [`week-5/`](week-5/) | Single-cell Transcriptomics and Genomics |
| [`week-6/`](week-6/) | Automated Scientific Discovery and AI Agents |
| [`final-project/`](final-project/) | Final project materials and instructions |
| [`setup/`](setup/) | Tool setup guides (Codex CLI, Google Colab CLI) |

Material for each week is released at the start of the module week.

## Contact

Questions: <ddls-course@scilifelab.se> · course responsible <wei.ouyang@scilifelab.se>
