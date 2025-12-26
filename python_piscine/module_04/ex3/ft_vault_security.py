#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    path_read = "../tools/classified_data.txt"
    print("\nInitiating secure vault access...")
    try:
        with open(path_read, mode='r') \
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
    except (FileNotFoundError, FileExistsError, PermissionError):
        print("ERROR. Vault connection couldn't be established... "
              "Closing connection.")

    path_write = "../tools/security_protocols.txt"
    message_write = "{[}CLASSIFIED{]} New security protocols archived"
    print("\n\nSECURE PRESERVATION:")
    try:
        with open(path_write, mode='w') \
                as fd:
            fd.write(message_write)
        print(message_write)
        print("Vault automatically sealed upon completion")
    except (FileExistsError, FileNotFoundError, PermissionError):
        print("ERROR. Vault couldn't be sealed properly... "
              "Closing connection.")

    print("\nAll vault operations completed with maximum security.")
