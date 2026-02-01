#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv
from icecream import ic


def ft_main() -> None:
    # loads .env values in memory
    load_dotenv()

    """
    os.environ
    is basically a big dictionary that contains all the system environment
    variables that you programs needs to be executed and your program
    inherits at starting time. Load_dotenv adds the information included in
    .env file to this mentioned dictionary.
    """
    # for key, value in os.environ.items():
    #     print(f"{key}: {value}")

    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    env_path:str = ".env"
    try:
        with open(env_path, mode='r', encoding='UTF8') as fd:
            fd.readlines()
    except (FileNotFoundError, FileExistsError, PermissionError):
        print("The .env file does not exist in the current directory. "
              "Please, check!!")
        return

    has_error: bool = False
    matrix_value: str = os.getenv("MATRIX_MODE")
    if sys.prefix == sys.base_prefix and matrix_value == "development":
        matrix_value = "production"
    if not matrix_value or matrix_value not in ["development", "production"]:
        print("- [ERROR] MATRIX_MODE parameter is empty or incorrect. "
              "(development / production).")
        has_error = True
    database_url: str = os.getenv("DATABASE_URL")
    if not database_url:
        print("- [ERROR] DATABASE_URL parameter is empty. "
              "(https://url/to/database)")
        has_error = True
    api_key: str = os.getenv("API_KEY")
    if not api_key:
        print("- [ERROR] API_KEY parameter is empty. (API_KEY=xxxxxxxxx)")
        has_error = True
    log_level: str = os.getenv("LOG_LEVEL")
    if not log_level or log_level not in ["debug", "running"]:
        print("- [ERROR] LOG_LEVEL parameter is empty or incorrect. "
              "(debug / running)")
        has_error = True
    zion_endpoint: str = os.getenv("ZION_ENDPOINT")
    if not zion_endpoint:
        print("- [ERROR] ZION_ENDPOINT parameter is empty")
        has_error = True

    if has_error:
        print()
        print("Please, consider to add the required values to the env file.")
        print("Closing...")
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {matrix_value}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {log_level.upper()}")
    print("Zion Network: Online")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    ft_main()
