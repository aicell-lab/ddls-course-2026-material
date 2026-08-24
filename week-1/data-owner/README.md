# The data owner

This folder holds the collaborator you are going to interview.

```bash
cd week-1/data-owner
codex
```

That is the whole setup. Codex reads `AGENTS.md` from the folder it starts in, which is
what turns it into the scientist who ran this experiment. Say hello and start asking.

## Rules of engagement

- **Fetch the data first** — `cd ../data && python fetch_data.py`. The collaborator looks
  at their own files before answering you, so the interview goes badly without them.
- **Do not edit `AGENTS.md` in this folder.** It is the character. Your own agent's
  system prompt goes in a *different* folder — see [`../README.md`](../README.md).
- **You may read `AGENTS.md`.** It will not tell you the answer, because there isn't one
  written down: the collaborator invents their situation at the start of each
  conversation. Reading it tells you what kind of thing to ask about, which is fair game.
- They will not do the analysis for you, and they do not know any statistics. Asking them
  which method to use is a wasted question.
- Vague questions get vague answers. Specific questions get real ones.

## When you are done

Ask them to summarise the brief in their own words, and keep it — that summary is the
input to the system prompt you write next.
