import datetime

d = datetime.date(2023,5, 20) #month should not start with 0 as it would force an error  
print(d)

tday= datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.weekday()) #monday 0 sunday 6
print(tday.isoweekday()) #monday 1 sunday 7

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

#date2 = date1 + timedelta
#timedelta = date + date 2

bday= datetime.date(2027, 1, 2)

till_bday = bday- tday 
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

import datetime

t= datetime.time(4,45,57,500000)
print(t.hour)

dt= datetime.datetime(2023,11,26,6,38,42,300000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(days=7)
print(dt + tdelta )

import datetime

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

import datetime
import pytz

dt = datetime.datetime(2021, 8, 23, 11, 35, 50, tzinfo=pytz.UTC)
print(dt)

#dt_today = datetime.datetime.today(tz=pytz.UTC)
dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

#print(dt_today)
print(dt_now)
print(dt_utcnow)

import datetime
import pytz


dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_ist = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_ist)

for tz in pytz.all_timezones:
    print(tz)

import datetime

dt_utcnow = datetime.datetime.now(datetime.UTC)

dt_ist = dt_utcnow.astimezone(
    datetime.timezone(datetime.timedelta(hours=5, minutes=30))
)

print(dt_ist)

import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = datetime.datetime.now()
dt_east= dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_mtn)
print(dt_east)

import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
#print(dt_utcnow)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')

dt_mtn = mtn_tz.localize(dt_mtn)

print(dt_mtn)

dt_east= dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
#print(dt_mtn.isoformat()) 
print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime