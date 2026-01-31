#!/usr/bin/env python3

from typing import Any, Optional


def ft_imports(pack_name: str) -> Optional[Any | None]:

    try:
        module = __import__(pack_name)

        return module
    except ImportError:
        print(f"[MISSING MODULE] - '{pack_name}'. Module not found!!")
        return None


def ft_initial_checks() -> None:
    pack_names = ['pandas', 'requests', 'matplotlib']
    packs_checked = []
    for pack in pack_names:
        packs_checked.append(ft_imports(pack))
    if None in packs_checked:
        print()
        print("-To install the required dependencies using pip:")
        print("\tpip install -r requirements.txt")
        print("-To install them using Poetry instead:")
        print("\tpoetry install")
        raise (ImportError)

    print()
    print("LOADING STATUS: Loading programs...")
    print()
    for pack in packs_checked:
        if pack.__name__ == "pandas":
            pourpose: str = "Data manipulation"
        elif pack.__name__ == "requests":
            pourpose = "Network access"
        elif pack.__name__ == "matplotlib":
            pourpose = "Visualization"
        # print(f"[OK] {pack.__name__} ({pack.__version__}) -
        # {pack.__doc__.split("\n")[1]}")
        print(f"[OK] {pack.__name__} ({pack.__version__}) - {pourpose} ready")


def ft_get_weather() -> None:
    print("\n[PROCESSING] Fetching weather data...")
    # Imports are safe here because ft_initial_checks passed
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt

    # Open-Meteo API (Free, no key required)
    # Coordinates for Llodio, Spain (approx)
    url = "https://api.open-meteo.com/v1/forecast?latitude=43.1432&" \
        "longitude=-2.962&hourly=temperature_2m"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Converts data to a python dictionary from a json file
        data = response.json()

        # Create DataFrame taking data from 'hourly' key
        df = pd.DataFrame(data['hourly'])

        # Convert time string to datetime objects for better plotting
        df['time'] = pd.to_datetime(df['time'])

        print(f"[DATA] DataFrame created with {len(df)} rows.")
        print(df.head())

        # Plotting
        print("[PLOTTING] Generating temperature chart...")
        plt.figure(figsize=(10, 6))
        plt.plot(
            df['time'], df['temperature_2m'], color='b',
            label='Temperature (2m)')
        plt.title("Hourly Temperature Forecast (Llodio)")
        plt.xlabel("Time")
        plt.ylabel("Temperature (°C)")
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45,)
        plt.tight_layout()

        # Save to JPG
        output_file = "Llodio_weather_plot.jpg"
        plt.savefig(output_file)
        print(f"[SUCCESS] Plot saved as '{output_file}'")

    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")


def ft_main() -> None:

    try:
        ft_initial_checks()
    except ImportError:
        return

    ft_get_weather()


if __name__ == "__main__":
    ft_main()
