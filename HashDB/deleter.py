#HashDB
#Author - LordGhostX

from os import remove, path
from event_logger import event_log

#Delete a database
#Usage: delete(<database to delete>)
def delete(dbname):
	if str(type(dbname)) != "<class 'str'>":
		event_log("Error! Expecting dbname to be of type string in function delete", 0)
		raise Exception("Expecting dbname to be of type string in function delete")
	if not path.exists(dbname + ".hashdb"):
		event_log("Error! DB {} does not exist when attempting to delete".format(dbname), 0)
		raise Exception("DB {} does not exist when attempting to delete".format(dbname))
	try:
		remove(dbname + ".hashdb")
		event_log("Successfully deleted DB {}".format(dbname), dbname)
	except Exception as e:
		event_log("There was an error deleting DB {} - {}".format(dbname, str(e)), dbname)
		print(str(e))