"""
12 — datetime module

THEORY
------
What: The datetime module provides date, time, datetime, timedelta, and timezone types
      for representing and manipulating dates and times.
Why:  Nearly every application needs timestamps, scheduling, or date arithmetic.
Key rules:
  - datetime.now() is naive (no tz); use datetime.now(timezone.utc) for aware datetimes.
  - timedelta supports days, seconds, weeks — not months (use dateutil or manual logic).
  - strftime formats out; strptime parses in.
When to use: Logging timestamps, deadlines, age calculation, scheduling, API date fields.
Common mistakes: Mixing naive and aware datetimes; assuming local timezone; off-by-one
                 with date ranges; using time.time() when datetime is clearer.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/12_datetime.py
"""

from datetime import datetime, date, time, timedelta, timezone  # date/time types and UTC
import time as time_module  # wall-clock timing utilities (aliased to avoid name clash)


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Current date and time")  # section header
    print("=" * 50)  # close header divider
    now = datetime.now()  # capture current local date and time
    today = date.today()  # capture today's date without time component
    print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")  # format and print full timestamp
    print(f"Today: {today}")  # print today's date

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — Create specific datetime")  # section header
    print("=" * 50)  # close header divider
    launch = datetime(2026, 6, 21, 10, 30, 0)  # build a fixed datetime for a scheduled event
    print(f"Launch: {launch}")  # display the launch datetime

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — timedelta arithmetic")  # section header
    print("=" * 50)  # close header divider
    future = today + timedelta(days=30)  # add 30 days to today
    weeks_ago = today - timedelta(weeks=2)  # subtract two weeks from today
    print(f"30 days later: {future}")  # show date one month ahead
    print(f"2 weeks ago: {weeks_ago}")  # show date two weeks in the past

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Difference between dates")  # section header
    print("=" * 50)  # close header divider
    deadline = date(2026, 12, 31)  # define a target deadline date
    days_left = (deadline - today).days  # compute whole days remaining until deadline
    print(f"Days until deadline: {days_left}")  # print countdown in days

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Parse string to datetime")  # section header
    print("=" * 50)  # close header divider
    parsed = datetime.strptime("2026-06-21", "%Y-%m-%d")  # convert ISO date string to datetime
    print(f"Parsed: {parsed.date()}")  # print only the date portion of parsed value

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — Timezone-aware datetime")  # section header
    print("=" * 50)  # close header divider
    utc_now = datetime.now(timezone.utc)  # get current time with UTC timezone attached
    print(f"UTC: {utc_now.isoformat()}")  # print ISO 8601 formatted UTC timestamp

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 7 — time module for elapsed seconds")  # section header
    print("=" * 50)  # close header divider
    start = time_module.time()  # record epoch timestamp before delay
    time_module.sleep(0.05)  # pause execution for 50 milliseconds
    print(f"Elapsed: {time_module.time() - start:.3f}s")  # print elapsed seconds since start


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
