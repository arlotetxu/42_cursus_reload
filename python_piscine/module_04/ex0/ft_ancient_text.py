#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    f_path = "ancient/ancient_fragment.txt"
    print(f"\nAccessing Storage Vault: {f_path}")
    fd = open(f_path, mode='r')
    fd_data: str = fd.read()
    fd.close()
    print("Connection established...")

    print("\nRECOVERED DATA:")
    for c in fd_data:
        if c == '[':
            c = "{[}"
        elif c == ']':
            c = "{]}"
        print(c, end="")

    print("\n\nData recovery complete. Storage unit disconnected.")
