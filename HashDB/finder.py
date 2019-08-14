#HashDB
#Author - LordGhostX

from event_logger import event_log

#Find all keys with specified values
#Usage: find(<database to search>, <value to find>)
def find(dbcontent, _query):
	if str(type(dbcontent)) != "<class 'dict'>":
		event_log("Error! Expecting dbcontent to be of type dict in function find", 0)
		raise Exception("Expecting dbcontent to be of type dict in function find")
	try:
		keys = []
		for key in dbcontent.keys():
			if dbcontent[key] == _query:
				keys.append(key)
		return keys
	except Exception as e:
		raise Exception("Error finding given data in the database " + str(e))
		return []