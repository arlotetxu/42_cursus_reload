#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    archivist_id = input("\nInput Strean active. Enter archivist ID: ")
    # system_status = input("Input Stream active. Enter status report: ")
    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    system_status = sys.stdin.readline().strip()

    std_message = f"\n{{[}}STANDARD{{]}} Archive status from " \
        f"{archivist_id}: {system_status}"
    sys.stdout.write(std_message)
    alert_message = "\n{[}ALERT{]} System diagnostic: " \
        "Communication channels verified"
    sys.stderr.write(alert_message)
    std_message_2 = "\n{[}STANDARD{]} Data transmission complete"
    sys.stdout.write(std_message_2)

    print("\n\nThree-channel communication test successful.")
