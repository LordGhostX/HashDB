#HashDB
#Author - LordGhostX

from os import path
from event_logger import event_log

#Clone a database (Backing up)
#Usage: clone(<database to clone>, <name of new cloned database>)
def clone(source, destination):
	if str(type(source)) != "<class 'str'>":
		event_log("Error! Expecting source to be of type string in function clone", 0)
		raise Exception("Expecting source to be of type string in function clone")
	if not path.exists(source + ".hashdb"):
		event_log("Error! {} does not exist when attempting to clone".format(source), 0)
		raise Exception("{} does not exist when attempting to clone".format(source))
	if str(type(destination)) != "<class 'str'>":
		event_log("Error! Expecting destination to be of type string in function clone", dbname)
		raise Exception("Expecting destination to be of type string in function clone")
	if len(destination) == 0:
		event_log("Error! Destination cannot be empty in function clone", source)
		raise Exception("Destination cannot be empty in function clone")
	try:
		with open (source + ".hashdb", "r") as db0:
			content = db0.read()
		with open (destination + ".hashdb", "w") as db1:
			db1.write(content)
		event_log("Successfully cloned DB {} to {}".format(source, destination))
	except Exception as e:
		event_log("There was an error cloning DB {} to {} - {}".format(source, destination, str(e)), source)
		print(str(e))