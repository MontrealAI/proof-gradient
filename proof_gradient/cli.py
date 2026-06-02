import argparse
import json
from pathlib import Path

from proof_gradient.foundation import build_foundation


def main() -> None:
    parser = argparse.ArgumentParser(prog="proof-gradient")
    sub = parser.add_subparsers(dest="command", required=True)

    demo = sub.add_parser("demo", help="Run the deterministic Proof Gradient sovereign swarm demo.")
    demo.add_argument("--out", default="", help="Optional JSON output path.")

    args = parser.parse_args()

    if args.command == "demo":
        data = build_foundation()
        text = json.dumps(data, indent=2, ensure_ascii=False)
        if args.out:
            output = Path(args.out)
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(text + "\n", encoding="utf-8")
        else:
            print(text)


if __name__ == "__main__":
    main()
