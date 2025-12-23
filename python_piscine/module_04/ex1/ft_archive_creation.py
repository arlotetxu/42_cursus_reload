#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    storage = "new_discovery.txt"
    print(f"\nInitializing new storage unit: {storage}")
    fd = open(storage, mode='w', encoding='utf-8')
    print("Storage unit created successfully...")

    message = "{[}ENTRY 001{]} New quantum algorithm discovered\n" \
        "{[}ENTRY 002{]} Efficiency increased by 347%\n" \
        "{[}ENTRY 003{]} Archived by Data Archivist trainee joflorid"

    print("\nInscribing preservation data...")
    print(f"{message}")
    fd.write(message)
    fd.close()

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{storage}' ready for long-term preservation.")
