#!/usr/bin/python3
def print_stats(size, status_codes):
    print(f"File size: {size}")
    for key, value in sorted(status_codes.items()):
        print(f"{key}: {value}")

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            count = count + 1 if count < 10 else 1

            try:
                size += int(line.split()[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = line.split()[-2]
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except IndexError:
                pass

            if count == 10:
                print_stats(size, status_codes)

        if count != 0:
            print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
