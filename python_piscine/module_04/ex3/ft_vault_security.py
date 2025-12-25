#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("\nInitiating secure vault access...")
    try:
        with open("../trainning_resources/classified_data.txt", mode='r') \
                as fd:
            fd_data = fd.read()
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            for c in fd_data:
                if c == '[':
                    c = "{[}"
                elif c == ']':
                    c = "{]}"
                print(c, end="")
    except (FileNotFoundError, FileExistsError):
        print("ERROR. Vault connection couldn't be established... "
              "Closing connection.")

    print("\n\nSECURE PRESERVATION:")
    try:
        with open("../trainning_resources/security_protocols.txt", mode='w') \
                as fd:
            fd.write("{[}CLASSIFIED{]} New security protocols archived")
        print("Vault automatically sealed upon completion")
    except (FileExistsError, FileNotFoundError):
        print("ERROR. Vault couldn't be sealed properly... "
              "Closing connection.")

    print("\nAll vault operations completed with maximum security.")
