from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print timedelta(days=365, hours=5, minutes=1)

print "today is: " + str(datetime.now())

print "one year from now it will be: " + str(datetime.now() + timedelta(days=365))

print "in two weeks and 3 days it will be:" + str(datetime.now() + timedelta(weeks=2,days=3))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print "one week ago it was " + s

today = date.today()
afd = date(today.year, 4, 1)
if afd < today:
    print "April Fool's day already went by %d days ago" % ((today-afd).days)
    afd = afd.replace(year=today.year + 1)

time_to_afd = abs(afd - today)
print time_to_afd.days, "days until next April Fool's Day!"