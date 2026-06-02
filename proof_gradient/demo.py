import json

from proof_gradient.models import run_customer_response_demo


def main() -> None:
    print(json.dumps(run_customer_response_demo(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
