#!/usr/bin/python3
"""
A script that reads stdin line by line then computes the metrics
"""
import sys
import re


def format_check(data):
    """
    Checks for the input format using regex,
    skips the line if it does not match.
    """
    pattern = re.compile(
        r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
        r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "
        r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
    )
    return bool(pattern.match(data))


def count_status_codes(data):
    """
    Counts the occurrence of status codes in the provided data
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
    for line in data:
        status = int(line.split()[-2])
        if status in status_code:
            status_code[status] += 1
    return status_code


def log_passing():
    """
    Reads stdin line by line and computes metrics
    """
    total_size = 0
    counter = 0
    data = []

    try:
        for line in sys.stdin:
            if not format_check(line):
                continue
            counter += 1
            data.append(line)
            total_size += int(line.split()[-1])

            if counter == 10:
                print("File size: {}".format(total_size))
                status_code_counts = count_status_codes(data)
                for key in sorted(status_code_counts.keys()):
                    if status_code_counts[key] != 0:
                        print("{}: {}".format(key, status_code_counts[key]))
                counter = 0
                data = []

    except KeyboardInterrupt:
        pass

    finally:
        print("File size: {}".format(total_size))
        status_code_counts = count_status_codes(data)
        for key in sorted(status_code_counts.keys()):
            if status_code_counts[key] != 0:
                print("{}: {}".format(key, status_code_counts[key]))


if __name__ == "__main__":
    log_passing()
