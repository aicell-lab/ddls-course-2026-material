# Data dictionary — antifungal primary screen

Everything we know about these files is written down here. If a column is not
described below, it is not in the data. Read this before you start.

## What the experiment was

*Candida auris* is a drug-resistant fungal pathogen. Our lab screened a
**24,000-compound small-molecule library** against a clinical isolate to look
for growth inhibitors.

The primary screen ran in **150 × 384-well plates** over seven weeks
(2 March – 20 April 2026). Every compound was tested **twice: once at 2 µM and
once at 20 µM**, in two separate wells on the same plate.

Each well was read three ways:

| Read | What it measures |
|---|---|
| `growth_od600` | optical density at 600 nm — how much fungus is in the well |
| `resazurin_rfu` | resazurin fluorescence — metabolic activity of living cells |
| `background_rfu` | the **same plate layout with no cells**, fully reduced dye |

The third read exists because compounds can interfere with the *optics* rather
than with the *fungus*. It is the control for that.

A subset of compounds was then taken into a **dose–response follow-up assay**
between 11 May and 24 June 2026, which is where the MIC values come from.

**Breakpoint used by this lab:** a compound is called active if its
**MIC90 ≤ 32 µM**.

---

## Files and how they join

```
compounds.csv  ──< screen_wells.csv          (compound_id)
       └────────< followup_assays.csv        (compound_id)
```

| File | Rows | Grain |
|---|---|---|
| `compounds.csv` | 24,000 | one row per library compound |
| `screen_wells.csv` | 57,600 | one row per well of the primary screen |
| `followup_assays.csv` | 1,800 | one row per compound taken to follow-up |

---

## `compounds.csv`

The library inventory, with calculated physicochemical descriptors.

| Column | Type | Unit | Description |
|---|---|---|---|
| `compound_id` | string | — | Primary key, `CMPnnnnn`. Unique. |
| `compound_name` | string | — | Internal name. Unique. |
| `scaffold_class` | category | — | Chemical family assigned by our chemist. One of `azole`, `polyene`, `echinocandin_like`, `pyrimidine`, `quinoline`, `benzimidazole`, `sulfonamide`, `chalcone`, `terpenoid`, `uncategorised`. |
| `mol_weight_da` | float | daltons | Molecular weight. |
| `clogp` | float | — | Calculated octanol/water partition coefficient. Higher = more lipophilic. |
| `tpsa_a2` | float | Å² | Topological polar surface area. |
| `h_bond_donors` | int | count | Hydrogen-bond donors. |
| `h_bond_acceptors` | int | count | Hydrogen-bond acceptors. |
| `rotatable_bonds` | int | count | Rotatable bonds. |
| `aromatic_rings` | int | count | Aromatic rings. |
| `fraction_sp3` | float | 0–1 | Fraction of sp³-hybridised carbons. |
| `heavy_atom_count` | int | count | Non-hydrogen atoms. |
| `supplier` | category | — | `Chembridge`, `Enamine`, `Selleck`, `MolPort`, `in_house`. |
| `salt_form` | category | — | `free_base`, `hydrochloride`, `sodium`, `mesylate`, `tosylate`. |
| `purity_pct` | float | % | Supplier-reported purity. **Empty for ~11% of compounds** — those suppliers did not report it. Missing means unreported, not impure. |
| `stock_conc_mm` | float | mM | DMSO stock concentration: 5, 10 or 20 mM. |
| `library_plate` | string | — | Source plate the compound was picked from, `LIBnnn`. 75 plates, 320 compounds each. |

---

## `screen_wells.csv`

One row per physical well. 150 plates × 384 wells.

| Column | Type | Unit | Description |
|---|---|---|---|
| `well_id` | string | — | Primary key, `PLTnnnn_Rcc`. |
| `plate_id` | string | — | Assay plate, `PLT0001`–`PLT0150`. |
| `row_letter` | string | — | `A`–`P` (16 rows). |
| `col_number` | int | — | `1`–`24`. |
| `well_type` | category | — | See well types below. |
| `compound_id` | string | — | Foreign key to `compounds.csv`. **Empty for control wells.** |
| `dose_um` | float | µM | Nominal compound concentration in the well. |
| `growth_od600` | float | OD | Optical density at 600 nm. Higher = more growth. **Empty when `well_qc_flag` is `read_error`.** |
| `resazurin_rfu` | float | RFU | Resazurin fluorescence. Higher = more living cells. **Empty when `well_qc_flag` is `read_error`.** |
| `background_rfu` | float | RFU | Cell-free reference read: same compound, same plate map, fully reduced dye, **no cells**. |
| `incubation_hours` | int | h | 24 or 48. Plate-level. |
| `read_temp_c` | float | °C | Plate reader chamber temperature. Plate-level. |
| `operator_id` | category | — | `OP-A`, `OP-B`, `OP-C`. Plate-level. |
| `run_date` | date | — | `YYYY-MM-DD`. Plate-level. |
| `detector_gain` | int | — | Plate reader gain setting. **See "known issues".** |
| `well_qc_flag` | category | — | See QC flags below. |

### Well types

| Value | Count | Meaning |
|---|---|---|
| `compound` | 48,000 | Library compound. Columns 3–22. |
| `solvent_control` | 4,800 | DMSO only, no compound. Untreated growth reference. Columns 1 and 23. |
| `positive_control` | 4,800 | Reference antifungal at 32 µM. Full-kill reference. Columns 2 and 24. |

### QC flags

| Value | Count | Meaning |
|---|---|---|
| `ok` | 45,475 | Nothing flagged. |
| `edge_evaporation` | 11,369 | Well is on the plate perimeter (row A or P, column 1 or 24). These wells lose volume across the incubation and the medium concentrates. |
| `low_volume` | 489 | Dispenser under-delivered into this well. |
| `read_error` | 267 | The reader failed on this well. `growth_od600` and `resazurin_rfu` are empty. |

---

## `followup_assays.csv`

Dose–response confirmation on 1,800 compounds. These are real measurements from
a clean, cell-based assay — this assay does **not** use the fluorescent readout,
so it is not subject to optical interference.

| Column | Type | Unit | Description |
|---|---|---|---|
| `compound_id` | string | — | Foreign key to `compounds.csv`. Unique within this file. |
| `selected_because` | category | — | **How the compound came to be tested.** See below. |
| `assay_replicate_n` | int | count | Independent replicates, 2–4. |
| `mic90_um` | float | µM | Concentration inhibiting 90% of growth. **Empty for 894 of 1,800 compounds — those did not reach 90% inhibition at the highest tested concentration (128 µM).** Missing means "not active up to 128 µM", not "not measured". |
| `hill_slope_fitted` | float | — | Slope of the fitted dose–response curve. |
| `cytotox_cc50_um` | float | µM | Concentration killing 50% of a human cell line. Lower = more toxic to human cells. |
| `confirmed_active` | category | — | `yes` if `mic90_um` ≤ 32 µM, else `no`. |
| `followup_date` | date | — | When the dose–response was run. |

### How compounds were selected for follow-up

| Value | Count | How they were picked |
|---|---|---|
| `top_ranked` | 1,400 | The 1,400 lowest raw `resazurin_rfu` values at 20 µM, averaged per compound. **No plate normalisation, no QC filtering, no background correction** — this was a quick ranking done under time pressure to get the follow-up plates ordered. |
| `random_control` | 400 | Drawn at random from the whole library, independently of any screen result. |

---

## Known issues

These are the ones we know about and have written down. It is not a guarantee
that the list is complete — check the data yourself.

1. **Detector gain changed mid-campaign.** Plates `PLT0071`–`PLT0090` were read
   at `detector_gain = 1000`; every other plate was read at `100`. Fluorescence
   readings scale roughly linearly with gain. The setting is recorded per well
   in `detector_gain`. This affects `resazurin_rfu` and `background_rfu`; it does
   **not** affect `growth_od600`.

2. **Signal drifts down across the campaign.** The lamp aged. Later plates give
   weaker absolute readings than earlier plates for the same biology. Each plate
   carries its own `solvent_control` and `positive_control` wells.

3. **Edge wells evaporate.** Perimeter wells are flagged `edge_evaporation`.
   They are about 20% of every plate. Note that the perimeter includes columns 1
   and 24, which is where the control wells sit: **5,400 of the 9,600 control
   wells (56%) carry this flag.**

4. **Some compounds interfere with the fluorescence read.** A few percent of the
   library either fluoresce in the resazurin channel or absorb at the read
   wavelength. This changes `resazurin_rfu` without changing the biology. The
   `background_rfu` column is the cell-free control we ran to detect this: for a
   non-interfering compound it should sit at the same level as the plate's
   solvent-control wells.

5. **The same molecule can appear more than once** under different
   `compound_id`s and `salt_form`s. Compound names are unique, but closely
   related names may refer to the same parent molecule.

6. **`purity_pct` is missing for ~11% of compounds** because those suppliers do
   not report it.

7. **Incubation time was not the same on every plate.** 112 plates were read at
   24 h and 38 plates at 48 h. The value is recorded per well in
   `incubation_hours`. Cultures are further along at 48 h, so the absolute
   readings are not on the same footing as the 24 h plates.

8. **Read temperature varies** between 28.5 °C and 31.6 °C, recorded per well in
   `read_temp_c`. The incubator was not perfectly stable across the campaign.

9. **Two plates gave us trouble at the bench**, `PLT0088` and `PLT0104`. Ask the
   person who ran the screen what happened on those.

---

## Contact

The screen was run by our lab. Ask us about anything that is unclear —
we know the biology and the instruments, we are not analysts.
