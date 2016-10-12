import os
import pytz
from datetime import datetime

#PST timestamp to date
timestamp = 1476259617
tz = pytz.timezone('US/Pacific')
dateArray=0
if len(str(timestamp)) > 11:
    dateArray = datetime.fromtimestamp(int(timestamp) / 1000, tz)
else:
    dateArray = datetime.fromtimestamp(int(timestamp),tz)
real_time = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print real_time;