#HashDB
#Author - LordGhostX

from event_logger import event_log
from crypt import encryptdb
from json import dumps
from time import time

#Creating a new HashDB Database
#Usage: write(<name of database to create>, <data to save as json>, <password if any>, <indentation to use for JSON output>)
def write(dbname, dbcontent, password=None, prettify=True):
	try:
		with open(dbname + ".hashdb", "w") as db:
			if password:
				db.write(encryptdb(str(dbcontent), str(password), dbname))
				event_log("Successfully saved DB {}".format(dbname), dbname)
			else:
				if prettify:
					db.write(dumps(dbcontent, indent=4))
				else:
					db.write(dumps(dbcontent))
				event_log("Successfully saved DB {}".format(dbname), dbname)
		return None
	except Exception as e:
		event_log("There was an error editing DB {} - {}".format(dbname, str(e)), dbname)
		return str(e)