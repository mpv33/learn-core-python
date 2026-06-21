"""01 — datetime module"""

from datetime import datetime, date, time, timedelta

# Current date/time
now = datetime.now()
today = date.today()
print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Today: {today}")

# Create specific datetime
launch = datetime(2026, 6, 21, 10, 30, 0)
print(f"Launch: {launch}")

# timedelta — date arithmetic
future = today + timedelta(days=30)
weeks_ago = today - timedelta(weeks=2)
print(f"30 days later: {future}")
print(f"2 weeks ago: {weeks_ago}")

# Difference between dates
deadline = date(2026, 12, 31)
days_left = (deadline - today).days
print(f"Days until deadline: {days_left}")

# Parse string to datetime
parsed = datetime.strptime("2026-06-21", "%Y-%m-%d")
print(f"Parsed: {parsed.date()}")

# timezone aware (Python 3.9+)
from datetime import timezone
utc_now = datetime.now(timezone.utc)
print(f"UTC: {utc_now.isoformat()}")

# time module (lower level)
import time
start = time.time()
time.sleep(0.05)
print(f"Elapsed: {time.time() - start:.3f}s")
