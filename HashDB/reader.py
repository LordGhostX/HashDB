from json import dumps
from json import load as ll
from ast import literal_eval
from event_logger import event_log
from crypt import decryptdb
from os import path

#Loading an existing HashDB Database
#Usage: load(<name of database to read>, <password if any>)
def load(dbname, password=None):
	if not str(type(dbname)) in ["<class 'str'>", "<class 'float'>", "<class 'int'>"]:
		event_log("Error! Expecting dbname to be of type string or int or float in function connect", 0)
		return {}, 0, "Error! Expecting dbname to be of type string or int or float"
	dbname = str(dbname)
	try:
		res = 0
		if not path.exists(dbname + ".hashdb"):
			with open(dbname + ".hashdb", "w") as db:
				db.write("{}")
				res = 1
		if password:
			with open(dbname + ".hashdb", "r") as db:
				try:
					dbcontent = decryptdb(db.read(), str(password), dbname)
					dbcontent = literal_eval(dbcontent.replace(": true,", ": True,").replace(": false,", ": False,"))
					event_log("Successfully connected to DB {}".format(dbname), dbname)
				except Exception as e:
					event_log("An incorrect password was used in connecting to DB {} or the DB is corrupted".format(dbname), dbname)
					return {}, 0, "An incorrect password was used in connecting to DB {} or the DB is corrupted".format(dbname)
		else:
			with open(dbname + ".hashdb") as db:
				try:
					dbcontent = ll(db)
				except Exception as e:
					event_log("A password is required to connect to DB {} - {}".format(dbname, str(e)), dbname)
					return {}, 0, "A password is required to connect to DB {}".format(dbname)
				db.close()
		
		event_log("Successfully connected to DB {}".format(dbname), dbname)
		return dbcontent, res, None
	except Exception as e:
		event_log("There was an error connecting to DB {} - {}".format(dbname, str(e)), dbname)
		return {}, 0, str(e)

def close(dbname):
	try:
		event_log("Successfully disconnected from DB {}".format(dbname), dbname)
		return None
	except Exception as e:
		event_log("There was an error disconnecting from DB {}, Possibly due to Database Corruption - {}".format(dbname, str(e)), dbname)
		return str(e)