from opslens import parse_log_line


def test_valid_log_line():
    result = parse_log_line("2026-08-18 INFO /login 200 120")
    assert result == ("/login", 200, 120)


def test_incorrect_number_of_parts():
    result = parse_log_line("BROKEN LOG")
    assert result is None


def test_invalid_status_code():
    result = parse_log_line("2026-08-18 INFO /broken ABC 100")
    assert result is None


def test_invalid_response_time():
    result = parse_log_line("2026-08-18 INFO /broken 200 SLOW")
    assert result is None