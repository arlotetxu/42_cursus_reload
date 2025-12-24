#!/usr/bin/env python3

import sys
'''
Authorized: sys.stdin, sys.stdout, sys.stderr, input(), print(), import sys
'''

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id = input("\nInput Strean active. Enter archivist ID: ")
    message = "Input Stream active. Enter status report: All systems nominal"
    sys.stdout.write(message)

    std_message = f"\n\n{{[}}STANDARD{{]}} Archive status from " \
        f"{archivist_id}: All systems nominal"
    sys.stdout.write(std_message)
    alert_message = "\n{[}ALERT{]} System diagnostic: "
    "Communication channels verified"
    sys.stderr.write(alert_message)
    std_message_2 = "\n{[}STANDARD{]} Data transmission complete"
    sys.stdout.write(std_message_2)

    print("\n\nThree-channel communication test successful.")
