import argparse
import csv
import json
import re
from pathlib import Path

STD_AA = set("ACDEFGHIKLMNPQRSTVWY")
SEQ_RE = re.compile(r"^[ACDEFGHIKLMNPQRSTVWY]+$")


def load_exclusion(path: Path) -> set[str]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return {row["Sequence"].strip() for row in csv.DictReader(f) if row.get("Sequence")}


def validate(submission: Path, exclusion_csv: Path):
    exclusion = load_exclusion(exclusion_csv)
    rows = list(csv.DictReader(submission.open(newline="", encoding="utf-8-sig")))
    errors = []
    required = ["Team_Name", "Seq_ID", "Sequence"]

    if rows and list(rows[0].keys()) != required:
        errors.append(f"Header must be exactly {required}; observed {list(rows[0].keys())}")
    if len(rows) > 6:
        errors.append(f"At most 6 sequences are allowed; observed {len(rows)}")

    seen_ids = set()
    seen_sequences = set()
    details = []
    for idx, row in enumerate(rows, start=1):
        seq_id = (row.get("Seq_ID") or "").strip()
        seq = (row.get("Sequence") or "").strip()
        row_errors = []
        if seq_id in seen_ids:
            row_errors.append("duplicate Seq_ID")
        seen_ids.add(seq_id)
        if seq in seen_sequences:
            row_errors.append("duplicate Sequence")
        seen_sequences.add(seq)
        if not seq.startswith("M"):
            row_errors.append("does not start with M")
        if not (220 <= len(seq) <= 250):
            row_errors.append(f"length {len(seq)} outside 220-250")
        if not SEQ_RE.fullmatch(seq):
            bad = sorted(set(seq) - STD_AA)
            row_errors.append(f"contains non-standard characters: {bad}")
        if seq in exclusion:
            row_errors.append("exact match in Exclusion_List.csv")
        details.append(
            {
                "row": idx,
                "Seq_ID": seq_id,
                "length": len(seq),
                "starts_M": seq.startswith("M"),
                "standard_aa_only": bool(SEQ_RE.fullmatch(seq)),
                "in_exclusion_list": seq in exclusion,
                "errors": row_errors,
            }
        )
        errors.extend(f"Seq_ID {seq_id}: {err}" for err in row_errors)

    return {"ok": not errors, "errors": errors, "details": details}


def main():
    parser = argparse.ArgumentParser(description="Validate GFP competition submission CSV.")
    parser.add_argument("--submission", type=Path, default=Path("outputs/submission.csv"))
    parser.add_argument("--exclusion", type=Path, required=True)
    parser.add_argument("--json-out", type=Path, default=None)
    args = parser.parse_args()

    result = validate(args.submission, args.exclusion)
    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text, encoding="utf-8")
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
