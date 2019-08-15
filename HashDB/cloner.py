from os import path
from reader import literal_eval, dumps
from event_logger import event_log

#cloner.py handles DB cloning; takes in 2 arguments (name of database to clone, new database name)

def dump(source, destination):
    #Ensure the destination is a string or int or float
	if not str(type(destination)) in ["<class 'str'>", "<class 'float'>", "<class 'int'>"]:
		event_log("Error! Expecting destination to be of type string or int or float in function clone", source)
		return {}, "Error! Expecting destination to be of type string or int or float"
	#Converts to a string incase it is a float or int
	destination = str(destination)
	if len(destination) == 0:
		event_log("Error! Destination cannot be empty in function clone", source)
		return "Destination cannot be empty in function clone"
	if source == destination:
		e = "Error! destination cant be the same as source in function clone!"
		event_log(e, source)
		return e
	try:
		#Basically read and write the database stored on the disk
		with open (source + ".hashdb", "r") as db0:
			content = db0.read()
		with open (destination + ".hashdb", "w") as db1:
			db1.write(dumps(content))
		event_log("Successfully cloned DB {} to {}".format(source, destination), source)
		return None
	except Exception as e:
		event_log("There was an error cloning DB {} to {} - {}".format(source, destination, str(e)), source)
		return str(e)