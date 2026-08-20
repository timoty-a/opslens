log_lines = [
    "2026-08-18 INFO /login 200 120",
    "2026-08-18 ERROR /payments 500 850",
    "2026-08-18 INFO /profile 404 230",
    "2026-08-18 INFO /dashboard 200 95",
]
status_counts = {}
count_success = 0
count_failure = 0
for log_line in log_lines:
    parts = log_line.split()
    endpoint = parts[2]
    status_code = int(parts[3])
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
    response_time = parts[4]

    print(f"Endpoint: {endpoint}")
    print(f"Status code: {status_code}")
    print(f"Response time: {response_time} ms")
    print()

print(f"Summary\n Successful requests: {count_success}\n Failed requests: {count_failure}")
print(f"Status code counts: {status_counts}")