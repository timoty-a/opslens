
import sys
def parse_log_line(log_line):
    parts = log_line.split()

    if len(parts) != 5:
        return None

    try:
        endpoint = parts[2]
        status_code = int(parts[3])
        response_time = int(parts[4])
    except ValueError:
        return None

    return endpoint, status_code, response_time
def main():
    status_counts = {}
    count_success = 0
    count_failure = 0
    count_skipped = 0
    count_slow = 0
    total_response_time = 0

    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <log_file>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        log_file = open(filename, "r")
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        sys.exit(1)

    with log_file:
        for log_line in log_file:
            parsed_log = parse_log_line(log_line)

            if parsed_log is None:
                print(f"Skipping malformed log: {log_line.strip()}")
                count_skipped += 1
                continue

            endpoint, status_code, response_time = parsed_log
            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1
            if status_code < 400:
                count_success += 1
                print("Result: Successful")
            else:
                count_failure += 1
                print("Result: Failed")
            if response_time > 500:
                count_slow += 1
            total_response_time += response_time

            print(f"Endpoint: {endpoint}")
            print(f"Status code: {status_code}")
            print(f"Response time: {response_time} ms")
            print()
    total_valid_requests = count_success + count_failure
    if total_valid_requests > 0:
        average_response_time = total_response_time / total_valid_requests
    else:
        average_response_time = 0
    print(f"Summary\n Successful requests: {count_success}\n Failed requests: {count_failure}\n Skipped requests: {count_skipped}\n slow requests: {count_slow}")
    print(f"Average response time: {average_response_time} ms")
    print(f"Status code counts: {status_counts}")

if __name__ == "__main__":
    main()