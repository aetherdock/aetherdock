from datetime import datetime, timezone, timedelta

tz_utc_8 = timezone(timedelta(hours=8))

utc_now = datetime.now(timezone.utc)
now = utc_now.astimezone(tz_utc_8)

print(now)