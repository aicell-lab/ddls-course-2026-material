# The data owner

This folder holds the collaborator you are going to interview.

```bash
cd week-1/data-owner     # you must be IN this folder
codex
```

That is the whole setup. Codex takes its instructions from `AGENTS.md` in the folder it
starts in, and that file is what turns it into the scientist who ran this experiment.
Start it anywhere else — the repo root, `week-1/`, your own lab folder — and you get a
plain coding assistant instead, with no collaborator to interview.

**How to tell it worked:** your first message is answered by a named scientist describing
their experiment. A generic "How can I help you today?" means you are in the wrong folder.

## Rules of engagement

- **Fetch the data first** — `cd ../data && python3 fetch_data.py`. The collaborator looks
  at their own files before answering you, so the interview goes badly without them.
- **Do not edit `AGENTS.md` in this folder, and do not add one anywhere else in this
  repository.** Codex merges every `AGENTS.md` from the top of the repo down to the
  folder you start in, so a stray file higher up gets blended into the collaborator.
  Write your own agent's prompt in your own folder outside the repo — see
  [`../README.md`](../README.md).
- **You may read `AGENTS.md`.** It will not tell you the answer, because there isn't one
  written down: the collaborator invents their situation at the start of each
  conversation. Reading it tells you what kind of thing to ask about, which is fair game.
- They will not do the analysis for you, and they do not know any statistics. Asking them
  which method to use is a wasted question.
- Vague questions get vague answers. Specific questions get real ones.

## When you are done

Ask them to summarise the brief in their own words, and keep it — that summary is the
input to the system prompt you write next.
