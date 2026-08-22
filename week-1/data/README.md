# Week 1 — data

Run this to download the dataset:

```bash
python fetch_data.py
```

You should end up with three files here:

| File | Size |
|---|---|
| `screen_plates.csv` | 4.2 MB |
| `compound_index.csv` | 1.3 MB |
| `hits_confirmed.csv` | 24 KB |

The files are not stored in this repository — `fetch_data.py` pulls them from the course
data store. Nothing is required to download them: no login, no key.

## About the data

There is no data dictionary, and that is on purpose. The columns are not explained anywhere,
and some of them are not what they look like. You are not expected to understand this file
before the lab — working out what it means is the lab.
