#!/bin/bash

TMPFILE=$(mktemp)

#ARCHITECTURE
echo "- Architecture: $(uname -a)" | tee -a "$TMPFILE"
#PHISICAL CPUs
echo "- Physical CPUs: $(lscpu | grep '^Core(s) per socket:' | awk '{print $4}')" | tee -a "$TMPFILE"
#VIRTUAL CPUs
echo "- Virtual CPUs: $(lscpu | grep '^CPU(s):' | awk '{print $2}')" | tee -a "$TMPFILE"
#MEMORY USAGE
echo "- Memory usage: $(free -m | grep '^Mem:' | awk '{printf "%s/%sMB (%.2f%%)\n", $3, $2, ($3/$2)*100}')" | tee -a "$TMPFILE"
#DISK USAGE
echo "- Disk usage: $(df -m --total | grep 'total' | awk '{printf "%.2f/%.2fGB (%.2f%%)\n", $3/1000, $2/1000, ($3/$2)*100}')" | tee -a "$TMPFILE"
#CPU LOAD
echo "- CPU Load: $(top -bn1 | grep 'load' | awk '{printf "%.2f%s\n", $(NF-2), "%"}')" | tee -a "$TMPFILE"
#LAST BOOT
echo "- Last boot: $(who -b | awk '{printf "%s, %s\n", $3, $4}')" | tee -a "$TMPFILE"
#LVM
echo "- LVM?: $(if [ $(lsblk | grep 'lvm' | wc -l) -eq 0 ] ; then echo "no"; else echo "yes"; fi)" | tee -a "$TMPFILE"
#TCP CONNECTIONS
echo "- TCP Connections: $(ss -s | grep 'TCP' | awk 'NR == 2 {printf "%d Established\n", $3}')" | tee -a "$TMPFILE"
#USER LOGS
echo "- User Logs: $(w -h | wc -l)" | tee -a "$TMPFILE"
#NETWORK
echo "- Network: $(hostname -I) $(ip link | grep 'link/ether' | awk '{printf "(%s)\n", $2}')" | tee -a "$TMPFILE"
#SUDO
echo "- Sudo commands: $(cat /var/log/sudo/sudo_logs | grep 'USER' | wc -l)" | tee -a "$TMPFILE"

for tty in $(who | grep "pts/" | awk '{print $3}'); do
	if [ -w "/dev/$tty" ]; then
		cat "$TMPFILE" > /dev/$tty
	fi
done

rm "$TMPFILE"
