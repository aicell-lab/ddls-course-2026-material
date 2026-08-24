# Week 1 — data

Download the dataset:

```bash
python fetch_data.py
```

You should end up with three files here:

| File | Rows | Size |
|---|---|---|
| `compounds.csv` | 24,000 | 2.5 MB |
| `screen_wells.csv` | 57,600 | 6.0 MB |
| `followup_assays.csv` | 1,800 | 96 KB |

The files are not stored in this repository — `fetch_data.py` pulls them from the course
data store. Nothing is required to download them: no login, no key.

## About the data

Read **[`DATA_DICTIONARY.md`](DATA_DICTIONARY.md)** first. It describes the experiment,
every column in every file, how the files join, what is missing and why, and the
problems the lab already knows about in their own run.

The data is documented honestly and completely. It is also real-shaped: there are
missing values, flagged wells, an instrument setting that changed partway through, and
readings that are not measuring what they appear to measure. All of that is described in
the dictionary. Handling it is your job.

What the dictionary does *not* tell you is **what question to answer**. That comes from
the scientist who produced the data — see [`../data-owner/`](../data-owner/).
