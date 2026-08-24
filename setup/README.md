# Setup — Codex CLI + Google Colab CLI

You need two command-line tools for the computer labs:

| Tool | What it is | What you use it for |
|------|-----------|---------------------|
| **Codex CLI** (`codex`) | OpenAI's coding agent, runs in your terminal | Talking to the **data-owner agent**, and running your own **data-analyst agent** |
| **Google Colab CLI** (`colab`) | Google's CLI for Colab runtimes | Running the heavy code on a **free T4 GPU** in the cloud instead of your laptop |

The idea: **your laptop holds the files and drives the agent; Google Colab does the computing.**
You never need a GPU of your own.

> **Windows users:** the Colab CLI only supports **macOS and Linux**. On Windows, install
> [WSL2](https://learn.microsoft.com/windows/wsl/install) (Ubuntu) and do everything inside
> the WSL terminal. Everything below works unchanged there.

Budget ~20 minutes. Do this **before** the first computer lab.

---

## Part 1 — Codex CLI

### 1.1 Install Node.js (if you don't have it)

```bash
node --version      # need v20 or newer
```

No output or an old version? Install from <https://nodejs.org> (LTS), or:

```bash
# macOS
brew install node
# Ubuntu / WSL
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt install -y nodejs
```

### 1.2 Install Codex

```bash
npm install -g @openai/codex
codex --version
```

If `npm install -g` fails with a permissions error, either use `sudo`, or set up a user-level
npm prefix (`npm config set prefix ~/.npm-global` and add `~/.npm-global/bin` to your `PATH`).

### 1.3 Log in with the course API key

You were given an API key for the course model **`gpt-5.6-luna`**. Do **not** use
"Sign in with ChatGPT" — we are using an API key.

```bash
export OPENAI_API_KEY="sk-proj-...the key you were given..."
printf '%s' "$OPENAI_API_KEY" | codex login --with-api-key
```

Check it:

```bash
codex login status
# → Logged in using an API key - sk-proj-***XXXXX
```

**Keep the key private.** Don't paste it into a notebook, a chat, a screenshot, or a git
commit. If you clone the course repo, put it in a local `.env` file (already gitignored):

```bash
cp .env.example .env      # then edit .env and paste the key
```

### 1.4 Make `gpt-5.6-luna` the default model

Create `~/.codex/config.toml`:

```bash
mkdir -p ~/.codex
cat > ~/.codex/config.toml <<'TOML'
model = "gpt-5.6-luna"
TOML
```

Now every `codex` run uses the course model. (You can always override per run with
`codex -m gpt-5.6-luna`.)

### 1.5 Test it

```bash
mkdir -p ~/ddls/test && cd ~/ddls/test && git init -q
codex exec -m gpt-5.6-luna "Reply with exactly: LUNA_OK"
```

Expected: a short session header, then `LUNA_OK`. If you see an auth error, redo step 1.3.

> **`Not inside a trusted directory`?** Codex refuses to run in a folder that isn't a git
> repository, so it can always undo its own edits. Either `git init` the folder (recommended —
> you get an undo button for free) or add `--skip-git-repo-check` to the command.

### 1.6 The two ways you'll run Codex

```bash
codex                      # interactive session — this is what you'll use in the lab
codex exec "do X"          # one-shot, non-interactive — good for scripting
```

Inside an interactive session, `/help` lists the slash commands, and `Ctrl-C` twice exits.

### 1.7 How Codex reads your instructions

Codex picks up an **`AGENTS.md`** file from the directory you start it in (and from
`~/.codex/AGENTS.md` globally). **This is where your system prompt goes.** When the lab asks
you to "write the system prompt for your data-analyst agent", you are writing an `AGENTS.md`:

```bash
mkdir -p ~/ddls/lab-1 && cd ~/ddls/lab-1 && git init -q
$EDITOR AGENTS.md          # your analyst's instructions: role, data, goal, constraints
codex                      # starts here, reads AGENTS.md, and follows it
```

Run one directory per lab. What's in the folder *is* your agent's context — put the dataset,
your interview notes, and `AGENTS.md` there.

---

## Part 2 — Google Colab CLI

This gives you a real Colab runtime — including a **free T4 GPU** — driven from your terminal.
Your agent can drive it too.

### 2.1 Install

```bash
# recommended: uv (fast, isolated)
curl -LsSf https://astral.sh/uv/install.sh | sh     # if you don't have uv
uv tool install google-colab-cli --with "jupyter-kernel-client==0.9.0"

# or plain pip
pip install google-colab-cli "jupyter-kernel-client==0.9.0"
```

> **Why the extra pin?** The current release (`google-colab-cli` 0.6.0) breaks against
> `jupyter-kernel-client` 1.0, which pip/uv would otherwise pick by default — every
> `colab exec` then dies with
> `AttributeError: module 'jupyter_kernel_client' has no attribute 'KernelClient'`.
> Pinning `0.9.0` avoids it. Once upstream fixes this, the pin can be dropped.

Make sure the install location is on your `PATH` (uv puts it in `~/.local/bin`):

```bash
export PATH="$HOME/.local/bin:$PATH"      # add this line to ~/.zshrc or ~/.bashrc
colab help
```

### 2.2 Log in with your Google account

Any command that touches the server triggers a browser login the first time:

```bash
colab sessions
```

A Google consent page opens (or a URL is printed — open it manually). Approve with the
**Google account you want the Colab quota from**. Google then shows an authorization code —
paste it back into the terminal. The token is cached in `~/.config/colab-cli/token.json`, so
this is a one-time step.

When it works, `colab sessions` prints your (initially empty) list of sessions instead of an
error. `colab whoami` shows which account and scopes you ended up with.

### 2.3 Rent a T4 GPU and run something

```bash
colab new -s ddls --gpu T4          # allocate a T4 runtime named "ddls"
colab status -s ddls                # check hardware + IDLE/BUSY
```

Run code on it — from a string, or from a local file:

```bash
echo "import torch; print(torch.cuda.get_device_name(0))" | colab exec -s ddls
colab exec -s ddls -f analysis.py   # runs your LOCAL file on the REMOTE machine
```

Two things worth knowing:

- **The kernel keeps its state between `colab exec` calls.** Variables and imports survive,
  like cells in a notebook. Build up your analysis step by step.
- **`colab exec -f` does not need an upload** — the CLI reads your local file and sends it.
  For data files you *do* need `colab upload` / `colab download`.

Move files and packages:

```bash
colab upload   -s ddls ./data.csv /content/data.csv
colab install  -s ddls scanpy umap-learn
colab download -s ddls /content/results.png ./results.png
colab ls       -s ddls /content
```

### 2.4 Always stop the runtime when you're done

```bash
colab stop -s ddls
```

An idle session keeps burning your Colab quota until a 24 h cap kicks in. **Stop it.**

### 2.5 One-shot jobs

If you just want to run a script on a fresh GPU and get the output back, skip `new`/`stop`:

```bash
colab run --gpu T4 train.py --epochs 5
```

This provisions a VM, runs the script (with your arguments), streams stdout back, and
**tears the VM down automatically** — even if the script crashes. This is the safest habit.

### 2.6 Export your session as a notebook

Handy for the Friday seminar and your report:

```bash
colab log -s ddls -o lab1.ipynb     # also works with .md, .txt, .jsonl
```

---

## Part 3 — Putting them together

The workflow for a computer lab:

**You will use two separate folders, and this matters.** Codex reads `AGENTS.md` from
the directory you start it in, so the data owner's prompt and your analyst's prompt have
to live apart — otherwise the second one overwrites the first and you end up interviewing
your own analyst.

| Folder | Holds | Whose `AGENTS.md` |
|---|---|---|
| `<course-repo>/week-N/data-owner/` | the collaborator | **ours** — do not edit it |
| `~/ddls/lab-N/` (you create this) | your notes, your analysis | **yours** — you write it |

```bash
# ---- 0. Get the data first (the data owner expects it to be there) ----
cd <course-repo>/week-N/data && python fetch_data.py

# ---- 1. Interview the data owner ----
cd ../data-owner        # AGENTS.md here IS the collaborator
codex
#    → ask about the biology, the samples, what decision they need to make,
#      what happens to your answer, and what they have already tried.
#    → when you are done, ask them to summarise the brief, and paste it into
#      ~/ddls/lab-N/notes.md

# ---- 2. Write your analyst's system prompt, in your OWN folder ----
mkdir -p ~/ddls/lab-N && cd ~/ddls/lab-N && git init -q
$EDITOR AGENTS.md       # role, the data, the goal from your brief, constraints

# ---- 3. Work with your analyst agent, GPU work deferred to Colab ----
colab new -s labN --gpu T4
codex                   # tell it: "run heavy code with `colab exec -s labN -f <file>`"
colab stop -s labN      # when you're done
```

The data stays in the course repo — point your analyst at it with an absolute path, or
copy the CSVs into your lab folder.

Tell your analyst agent, in `AGENTS.md`, that it has the Colab CLI available and how to use
it. Running `colab skill` prints Google's own agent-facing cheat sheet — pasting the relevant
parts into your `AGENTS.md` is a legitimate (and encouraged) move.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `codex: command not found` | npm's global bin isn't on `PATH`. Run `npm prefix -g` and add `<that path>/bin` to your `PATH`. |
| `401` / auth error from Codex | Re-run `printf '%s' "$OPENAI_API_KEY" \| codex login --with-api-key`. Check `codex login status`. |
| `model not found` | Check the spelling: `gpt-5.6-luna`. |
| `colab: command not found` | `export PATH="$HOME/.local/bin:$PATH"` and add it to your shell rc file. |
| `403` from `colab.pa.googleapis.com` | Missing OAuth scope. Delete `~/.config/colab-cli/token.json` and log in again. |
| `AttributeError: ... no attribute 'KernelClient'` | Wrong `jupyter-kernel-client` version. Re-install with the `==0.9.0` pin from step 2.1 (add `--force` for uv). |
| `400` on `colab new --gpu ...` | No quota/entitlement for that accelerator on your account. Use `--gpu T4`, or drop the flag for CPU. |
| Colab "session not found" | The backend reclaimed the VM. `colab sessions`, then `colab new` again. |
| `Not inside a trusted directory` | Run `git init` in your lab folder, or pass `--skip-git-repo-check`. |
| Colab CLI on Windows | Not supported — use WSL2. |
| Everything hangs in `colab repl` / `colab console` | Those need a real terminal. Use `colab exec` instead. |

Still stuck? Bring it to the start of the computer lab, or mail <ddls-course@scilifelab.se>.
