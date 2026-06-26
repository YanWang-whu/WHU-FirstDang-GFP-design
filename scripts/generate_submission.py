import argparse
import csv
import json
from pathlib import Path

FINAL_CANDIDATES = [
    {
        "Seq_ID": "1",
        "family": "cgreGFP",
        "source": "official_brightness_table",
        "mutations": "I31V:A168V",
        "sequence": "MTALTEGAKLFEKEIPYITELEGDVEGMKFIVKGEGTGDATTGTIKAKYICTTGDLPVPWATILSSLSYGVFCFAKYPRHIADFFKSTQPDGYSQDRIISFDNDGQYDVKAKVTYENGTLYNRVTVKGTGFKSNGNILGMRVLYHSPPHAVYILPDRKNGGMKIEYNKVFDVMGGGHQMARHAQFNKPLGAWEEDYPLYHHLTVWTSFGKDPDDDETDHLTIVEVIKAVDLETYR",
        "brightness": 4.60300263267077,
        "stability_prior": 0.64,
    },
    {
        "Seq_ID": "2",
        "family": "ppluGFP",
        "source": "official_brightness_table",
        "mutations": "E19G:G68D:F167S:L199H",
        "sequence": "MPAMKIECRITGTLNGVEFGLVGGGEGTPEQGRMTNKMKSTKGALTFSPYLLSHVMGYGFYHFGTYPSDYENPFLHAINNGGYTNTRIEKYEDGGVLHVSFSYRYEAGRVIGDFKVVGTGFPEDSVIFTDKIIRSNATVEHLHPMGDNVLVGSFARTFSLRDGGYYSSVVDSHMHFKSAIHPSILQNGGPMFAFRRVEEHHSNTELGIVEYQHAFKTPIAFA",
        "brightness": 4.4450590815284,
        "stability_prior": 0.92,
    },
    {
        "Seq_ID": "3",
        "family": "amacGFP",
        "source": "official_brightness_table",
        "mutations": "V11L:I122V:C202S",
        "sequence": "MSKGEELFTGILPVLIELDGDVHGHKFSVRGEGEGDADYGKLEIKFICTTGKLPVPWPTLVTTLSYGILCFARYPEHMKMNDFFKSAMPEGYIQERTIFFQDDGKYKTRGEVKFEGDTLVNRVELKGMDFKEDGNILGHKLEYNFNSHNVYIMPDKANNGLKVNFKIRHNIEGGGVQLADHYQTNVPLGDGPVLIPINHYLSSQTAISKDRNETRDHMVFLEFFSACGHTHGMDELYK",
        "brightness": 4.27158058609648,
        "stability_prior": 0.72,
    },
    {
        "Seq_ID": "4",
        "family": "ppluGFP",
        "source": "official_brightness_table",
        "mutations": "N79S:F113I:L199H",
        "sequence": "MPAMKIECRITGTLNGVEFELVGGGEGTPEQGRMTNKMKSTKGALTFSPYLLSHVMGYGFYHFGTYPSGYENPFLHAINSGGYTNTRIEKYEDGGVLHVSFSYRYEAGRVIGDIKVVGTGFPEDSVIFTDKIIRSNATVEHLHPMGDNVLVGSFARTFSLRDGGYYSFVVDSHMHFKSAIHPSILQNGGPMFAFRRVEEHHSNTELGIVEYQHAFKTPIAFA",
        "brightness": 4.42820913304687,
        "stability_prior": 0.92,
    },
    {
        "Seq_ID": "5",
        "family": "cgreGFP",
        "source": "official_brightness_table",
        "mutations": "D90Y:K167M",
        "sequence": "MTALTEGAKLFEKEIPYITELEGDVEGMKFIIKGEGTGDATTGTIKAKYICTTGDLPVPWATILSSLSYGVFCFAKYPRHIADFFKSTQPYGYSQDRIISFDNDGQYDVKAKVTYENGTLYNRVTVKGTGFKSNGNILGMRVLYHSPPHAVYILPDRKNGGMKIEYNMAFDVMGGGHQMARHAQFNKPLGAWEEDYPLYHHLTVWTSFGKDPDDDETDHLTIVEVIKAVDLETYR",
        "brightness": 4.59947018069374,
        "stability_prior": 0.64,
    },
    {
        "Seq_ID": "6",
        "family": "sfGFP",
        "source": "literature_guided_design",
        "mutations": "S202D:V206K:H231L",
        "sequence": "MSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNFNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPVLLPDNHYLDTQSKLSKDPNEKRDHMVLLEFVTAAGITLGMDELYK",
        "brightness": None,
        "stability_prior": 0.90,
    },
]


def write_submission(team_name: str, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    submission_path = output_dir / "submission.csv"
    metadata_path = output_dir / "candidate_metadata.json"

    with submission_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Team_Name", "Seq_ID", "Sequence"])
        writer.writeheader()
        for candidate in FINAL_CANDIDATES:
            writer.writerow(
                {
                    "Team_Name": team_name,
                    "Seq_ID": candidate["Seq_ID"],
                    "Sequence": candidate["sequence"],
                }
            )

    metadata_path.write_text(json.dumps(FINAL_CANDIDATES, indent=2, ensure_ascii=False), encoding="utf-8")
    return submission_path, metadata_path


def main():
    parser = argparse.ArgumentParser(description="Regenerate the WHU-FirstDang GFP submission files.")
    parser.add_argument("--team-name", default="WHU-FirstDang")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()

    submission_path, metadata_path = write_submission(args.team_name, args.output_dir)
    print(f"Wrote {submission_path}")
    print(f"Wrote {metadata_path}")


if __name__ == "__main__":
    main()
