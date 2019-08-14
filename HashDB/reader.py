#HashDB
#Author - LordGhostX

from json import load as ll
from ast import literal_eval
from event_logger import event_log
from crypt import decryptdb
from os import path

#Loading an existing HashDB Database
#Usage: load(<name of database to read>, <password if any>)
def load(dbname, password=None):
	if str(type(dbname)) != "<class 'str'>":
		event_log("Error! Expecting dbname to be of type string in function load", 0)
		raise Exception("Expecting dbname to be of type string in function load")
	if not path.exists(dbname + ".hashdb"):
		event_log("Error! {} does not exist when attempting to load".format(dbname), 0)
		raise Exception("{} does not exist when attempting to load".format(dbname))
	try:
		if password:
			with open(dbname + ".hashdb", "r") as db:
				dbcontent = decryptdb(db.read(), str(password), dbname)
				try:
					dbcontent = literal_eval(dbcontent)
					event_log("Successfully loaded DB {}".format(dbname), dbname)
				except:
					dbcontent = {"success": False, "error": "Incorrect Password used in decrypting DB {}".format(dbname)}
					event_log("An incorrect password was used in decrypting DB {}".format(dbname), dbname)
		else:
			with open(dbname + ".hashdb") as db:
				try:
					dbcontent = ll(db)
					event_log("Successfully loaded DB {}".format(dbname), dbname)
				except:
					dbcontent = {"success": False, "error": "A password is required to open DB {}".format(dbname)}
					event_log("A password is required to open DB {}".format(dbname), dbname)
				db.close()
		return dbcontent
	except Exception as e:
		event_log("There was an error loading DB {} - {}".format(dbname, str(e)), dbname)
		print(str(e))