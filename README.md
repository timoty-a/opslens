# OpsLens

OpsLens is a small Python command-line program that reads a log file and summarizes the requests inside it.

I built it to practise working with files, loops, dictionaries, error handling, command-line arguments, Git and automated tests.

## What it does

OpsLens shows:

- Successful and failed request counts
- HTTP status-code counts
- Requests taking longer than 500 ms
- Average response time
- Malformed lines that were skipped

## Log format

Each line should contain:

```text
date log_level endpoint status_code response_time
```

Example:

```text
2026-08-18 INFO /login 200 120
2026-08-18 ERROR /payments 500 850
```

The response time is in milliseconds.

## Running the program

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Run OpsLens with a log file:

```bash
python3 opslens.py logs.txt
```

If the file does not exist, OpsLens displays an error instead of crashing.

## Running the tests

Install the development requirements:

```bash
python3 -m pip install -r requirements-dev.txt
```

Run the tests:

```bash
python3 -m pytest -v
```

## Current limitations

OpsLens expects each log line to contain exactly five space-separated values. It currently treats status codes below 400 as successful and response times above 500 ms as slow.