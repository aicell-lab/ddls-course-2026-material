# Week 1 — Module 1 — Introduction to Data-Driven Life Sciences

## Before Wednesday

Work through [`../setup/`](../setup/). You need the Codex CLI and the Google Colab CLI
installed and working **before** the lab — we will not have time to debug installations
on Wednesday afternoon.

Then download the data and read the dictionary:

```bash
cd week-1/data && python fetch_data.py
```

That pulls three CSVs (~8 MB) from the course data store. No key or login needed.

## The dataset

An antifungal screening campaign: 24,000 compounds tested against *Candida auris*
across 150 assay plates, plus a dose–response follow-up on 1,800 of them.

It is **fully documented**. [`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md)
explains every column, its units, what is missing and why, and the problems the lab
already knows about in their own run. Read it before Wednesday. There are no hidden
columns and no tricks in the data itself.

## What happens in the lab

Understanding the *data* is the easy part. The hard part is that **nobody has told you
what question to answer.**

You will be introduced to the scientist who produced this dataset — played by an AI
agent in [`data-owner/`](data-owner/). They know the biology, the samples and the
instruments inside out, and they have a real decision they need to make. What they
cannot do is state it as an analysis task. They have never written a line of code, and
if you ask them a vague question you will get a vague answer.

To start the interview, run Codex **from inside that folder** — that is how it picks up
the collaborator's character:

```bash
cd week-1/data-owner
codex
```

Say hello and start asking. Your first message is the beginning of the interview, so
make it a good one. When you have what you need, ask them to summarise the brief in
their own words and save it — you will need it in step 3.

> Write your **own** agent's `AGENTS.md` in a **different folder** (e.g. `~/ddls/lab-1/`).
> Codex reads `AGENTS.md` from wherever you start it, so if you write yours here you will
> overwrite the collaborator and end up interviewing yourself. Leave `data-owner/` alone.

So the lab is:

1. **Interview the data owner.** Find out what they actually need, what they are going
   to do with the answer, and what constraints they are under. Push until you have
   something specific enough to be wrong.
2. **Write the brief.** Summarise what you learned, in your own words.
3. **Write the system prompt** for your own data-analyst agent, from that brief — that
   is an `AGENTS.md` in your own lab folder.
4. **Run the analysis**, sending anything heavy to Google Colab.

If you get stuck on the mechanics of any of this, [`../setup/README.md`](../setup/README.md)
Part 3 has the full command sequence.

Two things worth knowing before you start. The data owner **improvises a different
problem every time**, so your question will not be the same as the group next to you —
comparing prompts is useful, comparing answers is not. And they are holding something
back about their situation that changes what a good answer looks like. You will only get
it if you ask.

Tuesday's lecture covers system prompts, context and working with agents. Wednesday is
where you apply it.

## Friday

You present the analysis you did on Wednesday: what you were asked for, how you found
out, what you did, and what you would tell the collaborator. There is no paper to read.
