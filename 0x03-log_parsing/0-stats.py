#!/usr/bin/python3
"""
    A script that reads in stdin line by line and then computes the metrics
"""
import sys
import re


def extract_input(input_line):
    """
    checks for the input pattern and extracts the relevant information
    from a line of an HTTP request log.
    """
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    """
    Prints the accumulated statistics of the HTTP request log.
    """
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """
    Updates metrics from a given HTTP request log.
    """
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def log_passing():
    """
    Reads stdin line by line and computes metrics.
    """
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    total_file_size = 0
    line_num = 0

    try:
        for line in sys.stdin:
            line_num += 1
            total_file_size = update_metrics(
                line.strip(),
                total_file_size,
                status_codes_stats,
            )
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes_stats)



if __name__ == '__main__':
    log_passing()
