# WHU-FirstDang GFP Design Submission

This repository contains the reproducible code and output files for the 2026 SynBio GFP protein-design challenge submission from team `WHU-FirstDang`.

Goal: design six GFP-family amino-acid sequences that balance high initial fluorescence in CFPS and fluorescence retention after 72 C heat treatment.

## Contents

- `outputs/submission.csv`: final six amino-acid sequences for submission.
- `outputs/candidate_metadata.csv`: candidate family, mutations, brightness proxy, and rationale.
- `outputs/validation_report.json`: independent format and exclusion-list validation summary.
- `scripts/generate_submission.py`: regenerates the final submission CSV from the selected candidate metadata.
- `scripts/validate_submission.py`: validates length, alphabet, `M` start, duplicates, and exact exclusion-list matches.
- `requirements.txt`: minimal Python dependencies.

The official competition data are not committed here. To rerun exclusion-list validation, download the official package and pass the path to `Exclusion_List.csv`.

## Quick Start

```bash
python -m pip install -r requirements.txt
python scripts/generate_submission.py --output-dir outputs
python scripts/validate_submission.py --submission outputs/submission.csv --exclusion "PATH_TO_OFFICIAL/Exclusion_List.csv" --json-out outputs/validation_report.json
```

## Design Summary

The final set is a diversified portfolio rather than six near-identical variants:

1. Two cgreGFP variants selected for high official brightness-table values.
2. Two ppluGFP/TGP-family variants selected to hedge thermal-stability risk.
3. One amacGFP variant selected for strong brightness improvement.
4. One sfGFP-centered literature-guided variant retained as a conservative stability slot.

Mutation numbering in the official `GFP_data.xlsx` brightness table was treated as mature-protein numbering: data position 1 maps to full submitted-sequence position 2 after the initiating methionine.

Validation status for the final CSV: `ok=true`, `errors=[]`.
