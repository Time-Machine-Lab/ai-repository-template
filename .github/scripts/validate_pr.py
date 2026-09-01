import argparse
import json
import re
from pathlib import Path


def parse_metadata(body):
    block = re.search(r"<!--\s*multica(.*?)-->", body or "", re.S | re.I)
    if not block:
        raise ValueError("PR must contain a multica metadata block")

    fields = {}
    for line in block.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def validate(event, policy):
    pull_request = event.get("pull_request") or {}
    body = pull_request.get("body") or ""
    head_ref = pull_request.get("head", {}).get("ref") or ""
    base_ref = pull_request.get("base", {}).get("ref") or ""
    failures = []

    if base_ref != policy["default_branch"]:
        failures.append(
            f"target branch must be {policy['default_branch']}, got {base_ref or '<empty>'}"
        )

    if not re.fullmatch(policy["branch_pattern"], head_ref):
        failures.append(f"branch name does not match policy: {head_ref or '<empty>'}")

    try:
        metadata = parse_metadata(body)
    except ValueError as exc:
        failures.append(str(exc))
        metadata = {}

    for field in policy.get("required_pr_metadata", []):
        value = metadata.get(field, "")
        if not value or value.startswith("<"):
            failures.append(f"missing PR metadata: {field}")

    return failures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", required=True)
    parser.add_argument("--policy", required=True)
    args = parser.parse_args()

    event = json.loads(Path(args.event).read_text(encoding="utf-8"))
    policy = json.loads(Path(args.policy).read_text(encoding="utf-8"))
    failures = validate(event, policy)

    if failures:
        for failure in failures:
            print(f"FAILED: {failure}")
        raise SystemExit(1)

    print("Git governance policy passed")


if __name__ == "__main__":
    main()
