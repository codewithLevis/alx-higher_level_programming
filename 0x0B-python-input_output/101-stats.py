#!/usr/bin/python3
import sys
import signal


def parse_str(line: str):
    """
    Function to pass a string (line) and remove the size and code
    """
    try:
        idx = line.index('HTTP/1.1"')
    except ValueError:
        return [None, None]

    len_substring = len('HTTP/1.1"')

    code_size_substr = line[idx + len_substring:]
    code_size_substr = code_size_substr.strip()

    code_size_list = [int(_) for _ in code_size_substr.split(" ")]
    return code_size_list


def log_parse():
    """
    Parses log data
    """
    log_dict = {"files_size": 0}
    codes = [200, 301, 400, 401, 403, 404, 405, 500]

    def print_logs():
        sys.stdout.write(f"File size: {log_dict['files_size']}\n")

        for _ in codes:
            if _ in log_dict.keys():
                sys.stdout.write(f"{_}: {log_dict[_]}\n")
        sys.stdout.flush()
    default_signint = signal.getsignal(signal.SIGINT)

    def sigint_handler(sig, frame):
        """
        Handles CTRL C
        """
        print_logs()
        default_signint(sig, frame)

    signal.signal(signal.SIGINT, sigint_handler)

    line = sys.stdin.readline()
    counter = 1

    while line != "":
        code, size = parse_str(line)

        if not code or not size:
            break
        log_dict["files_size"] += size

        if code in codes:
            if code in log_dict.keys():
                log_dict[code] += 1
            else:
                log_dict[code] = 1
        else:
            counter += 1
            continue

        if counter == 10:
            print_logs()
            counter = 1

        line = sys.stdin.readline()
        counter += 1


log_parse()

sys.stdin.close()
