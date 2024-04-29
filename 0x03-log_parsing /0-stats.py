#!/usr/bin/env python3

import sys

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()
            if len(parts) == 7:
                ip, _, _, status_code, size = parts
                status_code = int(status_code)
                size = int(size)
                if status_code in status_counts:
                    status_counts[status_code] += 1
                    total_size += size
                    line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
                total_size = 0
                status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
                line_count = 0
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
