Notes on how to launch mongodb server on a laptop
===================================

#DATABASE
The database is the set of all documents gathered from Netflow, NowTV etc.

##Assumptions
* You have created an empty directory to store the database in /path/db
* You have downloaded the mongodb dump (see email 10/07/2015 11:18) and unzip it into /path/dump

##Command lines
1/ mongod --dbpath /path/db
2/ mongorestore --db phoenix /path/dump/phoenix/

##Access the database
mongo
show dbs #show the list of available databases
use phoenix #select the relevant database
show collections

These last commands are meant to be exploratory. You might prefere to use pymongo instead to access all the python features.



#TWEETS
Found in phoenix-tweets-2 on cyberduck (see same email than above)
2 folders for 1 month
each tweet has an incremental identifier with its attached metadata and events.
You should use the python module pickle to read the tweets/metas/events contents.
