#!/usr/bin/env python3
''' reads stdin line by line and computes metrics '''


import sys
import signal
import re

''' Initialize metrics '''
total_file_size = 0
status_code_counts = {}
line_count = 0

# Regex to match the correct log line format
log_pattern = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

# Function to print statistics
def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

# Signal handler for keyboard interrupt
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Attach signal handler to SIGINT (Ctrl + C)
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin
for line in sys.stdin:
    match = log_pattern.match(line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code not in status_code_counts:
            status_code_counts[status_code] = 0
        status_code_counts[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

# Print final statistics after EOF
print_stats()