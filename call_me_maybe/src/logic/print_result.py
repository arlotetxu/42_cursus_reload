from typing import Dict, Any


def print_result(
    prompt: str | None,
    func_name: str,
    func_params: Dict[str, Any]
) -> None:

    print(f"prompt: {prompt}\n"
          f"name: {func_name}\n"
          f"parameters: {func_params}\n"
          f"{'=' * 60}")
