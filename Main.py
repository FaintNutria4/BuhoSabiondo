import datetime
import time
from WikiReader import read
from TwitterPublisher import publish
running = True

while(running):
    theTime = datetime.datetime.now()
    day = theTime.day
    month = theTime.month
    event = read(day, month)
    print(event)
    publish(event)
    time.sleep(86400) # Wait a 24h