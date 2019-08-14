#HashDB
#Author - LordGhostX

from event_logger import event_log
from crypt import encryptdb
from json import dumps
from os import path

#Creating a new HashDB Database
#Usage: write(<name of database to create>, <data to save as json>, <password if any>, <indentation to use for JSON output>)
def write(dbname, dbcontent={}, password=None, indent=4):
	if str(type(dbname)) != "<class 'str'>":
		event_log("Error! Expecting dbname to be of type string in function write", 0)
		raise Exception("Expecting dbname to be of type string in function write")
	if str(type(indent)) != "<class 'int'>":
		event_log("Error! Expecting indent to be of type int in function write", 0)
		raise Exception("Expecting indent to be of type int in function write")
	try:
		with open(dbname + ".hashdb", "w") as db:
			if path.exists(dbname + ".hashdb"):
				ex = True
			if password:
				db.write(encryptdb(str(dbcontent), str(password), dbname))
				if ex:
					event_log("Successfully edited DB {}".format(dbname), dbname)
				else:
					event_log("Successfully created DB {}".format(dbname), dbname)
			else:
				db.write(dumps(dbcontent, indent=indent))
				if ex:
					event_log("Successfully edited DB {}".format(dbname), dbname)
				else:
					event_log("Successfully created DB {}".format(dbname), dbname)
	except Exception as e:
		event_log("There was an error creating DB {} - {}".format(dbname, str(e)), dbname)
		print(str(e))