#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    file1_name = "list_archive.txt"
    file1_path = "../tools/" + file1_name
    print(f"\nCRISIS ALERT: Attempting access to '{file1_name}'...")
    try:
        with open(file1_path, mode='r') as fd1:
            fd1_data = fd1.read()
    except (FileNotFoundError):
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable")

    '''
    Warning, the file showed in example does not exist in the
    data_generator_tools. I changed the file name. For testing pourpose,
    it is needed to remove the file read permission to classified_data.txt
    '''
    file2_name = "classified_data.txt"
    file2_path = "../tools/" + file2_name
    print(f"\nCRISIS ALERT: Attempting access to '{file2_name}'...")
    try:
        with open(file2_path, mode='r') as fd2:
            fd2_data = fd2.read()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")

    file3_name = "standard_archive.txt"
    file3_path = "../tools/" + file3_name
    print(f"\nCRISIS ALERT: Attempting access to '{file3_name}'...")
    try:
        with open(file3_path, mode='r') as fd3:
            fd3_data = fd3.read()
            print(f"SUCCESS: Archive recovered - ``{fd3_data}''")
            print("STATUS: Normal operations resumed")
    except (PermissionError, FileNotFoundError, FileExistsError):
        print("RESPONSE: Security protocols deny access or Archive not found")

    print("\nAll crisis scenarios handled successfully. Archives secure.")
