#HashDB
#Author - LordGhostX

from time import strftime as strf

#Event Logger
#Logs every event that happens in HashDB
def event_log(event, dbname=0):
	d, t = strf("%D"), strf("%T")
	if dbname == 0:
		with open("HashDB-event-log.txt".format(dbname), "a") as log:
			log.write("{} {} -> {}\n".format(d, t, event))
	else:
		with open("{}-event-log.txt".format(dbname), "a") as log:
			log.write("{} {} -> {}\n".format(d, t, event))