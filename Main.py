import datetime
import time
from WikiReader import read
from TweeterPublisher import publish
running = True

wikiweb ="https://en.wikipedia.org/wiki/"

while(running):
    theTime = datetime.datetime.now()
    month = theTime.strftime("%B")
    day = str(theTime.day)
    event = read(wikiweb+month+day)
    publish(event)
    time.sleep(86400) # Wait a 24h
