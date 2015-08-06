# this script works out both activities per day over time and activities at 
# different hours of the day
import pymongo
import datetime
import time
import math
import numpy as np
import matplotlib.pyplot as plt

client = pymongo.MongoClient("localhost", 27017) #client to local server
db = client.phoenix #create a database when call first time

SECINADAY = 86400.0  # 86400 seconds in a day
timestamps = []
hourtemp = [] #hour temp stores the time of date of each action

# convert datetime into timestamp
for q in db.user_log.find():
    d = q["date"]
    hourtemp.append(d.hour)
    datetemp = math.floor(time.mktime(d.timetuple()) / SECINADAY)
    timestamps.append(int(datetemp))

# removing intercept st the timestamp begins from 0
timestamps = np.array(timestamps)
intercept = min(timestamps)
timestamps = timestamps - intercept

timebin = [0 for x in range(max(timestamps)+1)]
hourbin = [0 for x in range(24)] #this bins actions at different time of day
timeaxis = []

# bin the actions
for i in range(len(timestamps)): timebin[timestamps[i]] += 1
for i in range(len(hourtemp)): hourbin[hourtemp[i]] += 1

# convert the bin number back to timestamp and datetime structure
actualtime = (range(max(timestamps)+1) + intercept) * SECINADAY
for i in range(len(actualtime)): 
    temp = datetime.datetime.fromtimestamp(actualtime[i])
    timeaxis.append(temp.date())

# plot
fig = plt.figure()    
plt.bar(range(max(timestamps)+1),timebin)
plt.ylabel('number of actions')
fig.suptitle('Actions in user_log per day')
xax = range(max(timestamps)+1)
plt.xticks(xax[1:len(actualtime):20],timeaxis[1:len(actualtime):20])
fig.autofmt_xdate()
plt.savefig("activityovertime.pdf")


# plot
fig = plt.figure()    
plt.bar(range(24),hourbin)
plt.ylabel('number of actions')
fig.suptitle('Number of activities at different time of day')
fig.autofmt_xdate()
plt.savefig("activityoverday.pdf")
