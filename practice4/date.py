#1

from datetime import datetime, timedelta

today = datetime.now()
print(today)

five_dayago = today - timedelta(days=5)
print(five_dayago)
#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)


#3
from datetime import datetime

now = datetime.now()
print(now)

new_time = now.replace(microsecond=0)
print(new_time)

#4
from datetime import datetime

date1 = datetime(2007, 11, 19, 1, 0, 0)
date2 = datetime(2026, 2, 24, 0, 0, 0)

difference = date2 - date1

seconds = difference.total_seconds()

print(seconds)