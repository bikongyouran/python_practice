import os
import pytz
from datetime import datetime

#PST date to timestamp
input_date = '2016-2-22 1:30:00'
tz = pytz.timezone('US/Pacific')
dt = datetime.strptime(input_date, '%Y-%m-%d %H:%M:%S')
dt_with_tz = tz.localize(dt, is_dst=None)
#dt_with_tz = tz.localize(datetime(2016, 2, 22, 1, 44, 00), is_dst=None)
ts = (dt_with_tz - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds()
print ts;