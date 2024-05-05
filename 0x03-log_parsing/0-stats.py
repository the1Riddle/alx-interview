#!/usr/bin/python3
"""
A script that reads stdin line by line then computes the metrics
"""
import sys
import re
import signal


def format_check(line):
    """
    Checks for the input format using regex
    skips the line if it does not match.
    """
    pattern = re.compile(
        r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
        r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "
        r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
    )
    return bool(pattern.match(line))


def count_status_codes(lines):
    """
    Counts the occurrence of status codes in the provided lines
    """
    status_code = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    for line in lines:
        status = int(line.split()[-2])
        if status in status_code:
            status_code[status] += 1
    return status_code


def print_stats(total_size, status_code_counts):
    """Function to print the statistics."""
    print("File size: {}".format(total_size))
    for key in sorted(status_code_counts.keys()):
        if status_code_counts[key] != 0:
            print("{}: {}".format(key, status_code_counts[key]))


def signal_handler(signum, frame):
    """Signal handler for printing the stats before exiting."""
    raise KeyboardInterrupt


def log_passing():
    """
    Reads stdin line by line and computes metrics
    """
    total_size = 0
    lines = []

    # Register the signal handler for SIGINT (CTRL + C)
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            if not format_check(line):
                continue

            total_size += int(line.split()[-1])
            lines.append(line)

            if len(lines) == 10:
                status_code_counts = count_status_codes(lines)
                print_stats(total_size, status_code_counts)
                total_size = 0
                lines = []

    except KeyboardInterrupt:
        pass

    finally:
        if lines:
            status_code_counts = count_status_codes(lines)
            print_stats(total_size, status_code_counts)


if __name__ == "__main__":
    log_passing()
