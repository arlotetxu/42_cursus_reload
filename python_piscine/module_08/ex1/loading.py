#!/usr/bin/env python3

from types import ModuleType
from typing import Optional


def ft_imports(pack_name: str) -> Optional[ModuleType]:
    """
    Attempts to import a module by its name.

    Args:
        pack_name (str): The name of the package to import.
    Returns:
        Optional[ModuleType]: The imported module if successful.
        None otherwise.
    """
    try:
        module: ModuleType = __import__(pack_name)
        return module
    except ImportError:
        print(f"[MISSING MODULE] - '{pack_name}'. Module not found!!")
        return None


def ft_initial_checks() -> None:
    """
    Verifies that all required third-party packages are installed.

    Raises:
        ImportError: If any of the required packages are missing.
    """
    pack_names: list = ["pandas", "requests", "matplotlib"]
    packs_checked: list = []
    for pack in pack_names:
        packs_checked.append(ft_imports(pack))
    if None in packs_checked:
        print()
        print("-To install the required dependencies using pip:")
        print("\tpip install -r requirements.txt")
        print("-To install them using Poetry instead:")
        print("\tpoetry install")
        raise ImportError("Missing dependencies")

    for pack in packs_checked:
        if pack.__name__ == "pandas":
            purpose: str = "Data manipulation"
        elif pack.__name__ == "requests":
            purpose = "Network access"
        elif pack.__name__ == "matplotlib":
            purpose = "Visualization"
        print(f"[OK] {pack.__name__} ({pack.__version__}) - {purpose} ready")


def ft_get_weather() -> None:
    """
    Fetches hourly temperature data for Llodio, Spain from the Open-Meteo API
    and generates a visualization plot saved as a JPG file.
    """
    print("\nAnalyzing Matrix data......")
    # Imports are safe here because ft_initial_checks passed
    import matplotlib.pyplot as plt
    import pandas as pd
    import requests

    # Open-Meteo API (Free, no key required)
    # Coordinates for Llodio, Spain (approx)
    url = (
        "https://api.open-meteo.com/v1/forecast?latitude=43.1432&"
        "longitude=-2.962&hourly=temperature_2m"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Converts data to a python dictionary from a json file
        data: dict = response.json()

        # Create DataFrame taking data from 'hourly' key
        df = pd.DataFrame(data["hourly"])

        # Convert time string to datetime objects for better plotting
        df["time"] = pd.to_datetime(df["time"])

        print(f"Processing {len(df)} data points...")

        # Plotting
        print("Generating visualization...")
        plt.figure(figsize=(10, 6))
        plt.plot(
            df["time"], df["temperature_2m"],
            color="b",
            label="Temperature (2m)"
            )
        plt.title("Hourly Temperature Forecast (Llodio)")
        plt.xlabel("Time")
        plt.ylabel("Temperature (°C)")
        plt.grid(True)
        plt.legend()
        plt.xticks(
            rotation=45,
        )
        plt.tight_layout()

        # Save to JPG
        print()
        print("Analysis complete!")
        output_file: str = "Llodio_weather_plot.jpg"
        plt.savefig(output_file)
        print(f"Results saved to '{output_file}'")

    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")


def ft_main() -> None:
    """
    Main entry point of the script. Orchestrates dependency checks and
    data fetching.
    """
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    try:
        ft_initial_checks()
    except ImportError:
        return

    ft_get_weather()


if __name__ == "__main__":
    ft_main()
