import argparse
import json
from pathlib import Path

from proof_gradient.models import run_customer_response_demo


def main() -> None:
    parser = argparse.ArgumentParser(prog="proof-gradient")
    sub = parser.add_subparsers(dest="command", required=True)

    demo = sub.add_parser("demo", help="Run the deterministic customer-response safety demo.")
    demo.add_argument("--out", default="", help="Optional JSON output path.")

    args = parser.parse_args()

    if args.command == "demo":
        data = run_customer_response_demo()
        text = json.dumps(data, indent=2, ensure_ascii=False)
        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            Path(args.out).write_text(text + "\n", encoding="utf-8")
        else:
            print(text)


if __name__ == "__main__":
    main()
