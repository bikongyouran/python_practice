import os
import pytz
from datetime import datetime

#PST timestamp to date
timestamp = 1456133400000
tz = pytz.timezone('US/Pacific')
dateArray = datetime.fromtimestamp(int(timestamp)/1000,tz)
real_time = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print real_time;