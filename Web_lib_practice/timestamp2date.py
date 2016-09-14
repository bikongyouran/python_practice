import os
import pytz
from datetime import datetime

#PST timestamp to date
timestamp = 1153267200
tz = pytz.timezone('US/Pacific')
dateArray = datetime.fromtimestamp(int(timestamp),tz)
real_time = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print real_time;