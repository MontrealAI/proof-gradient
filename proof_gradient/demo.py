import json

from proof_gradient.foundation import build_foundation


def main() -> None:
    print(json.dumps(build_foundation(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
