#JNDB
#Author - LordGhostX

from json import load, loads, dumps
from os import remove, path
from time import strftime as strf

#Event Logger
def event_log(event):
	with open("event-log.txt", "a") as log:
		log.write("{} {} -> {}\n".format(strf("%D"), strf("%T"), event))

#Creating a new jndb Database
#Usage: write(<name of database to create>, <data to save as json>, <password if any>, <indentation to use for JSON output>)
def write(dbname, dbcontent={}, password=None, indent=4):
	if str(type(dbname)) != "<class 'str'>":
		event_log("Error! Expecting dbname to be of type string in function write")
		raise Exception("Expecting dbname to be of type string in function write")
	if str(type(indent)) != "<class 'int'>":
		event_log("Error! Expecting indent to be of type int in function write")
		raise Exception("Expecting indent to be of type int in function write")
	try:
		with open(dbname, "w") as db:
			if password:
				db.write(encryptdb(str(dbcontent), str(password)))
				event_log("Successfully encrypted {}".format(dbname))
			else:
				db.write(dumps(dbcontent, indent=indent, sort_keys=True))
				event_log("Successfully created {}".format(dbname))
	except Exception as e:
		event_log("There was an error creating {} - {}".format(dbname, str(e)))
		raise Exception("Error creating Database\n~ " + str(e))

#Reading an existing jndb Database
#Usage: read(<name of database to read>, <password if any>)
def read(dbname, password=None):
	if str(type(dbname)) != "<class 'str'>":
		event_log("Error! Expecting dbname to be of type string in function read")
		raise Exception("Expecting dbname to be of type string in function read")
	if not path.exists(dbname):
		event_log("Error! {} does not exist when attempting to read".format(dbname))
		raise Exception("{} does not exist when attempting to read".format(dbname))
	try:
		if password:
			with open(dbname, "r") as db:
				dbcontent = decryptdb(db.read(), str(password))
				dbcontent = loads(dumps(dbcontent))
				event_log("Successfully decrypted {}".format(dbname))
		else:
			with open(dbname) as db:
				dbcontent = load(db)
				db.close()
				event_log("Successfully read {}".format(dbname))
		return dbcontent
	except Exception as e:
		event_log("There was an error reading {}- {}".format(dbname, str(e)))
		raise Exception("Error reading Database\n~ " + str(e))

#Convert password to an integer
def encpass(password):
	password = str(password)
	tot = 0
	for p in range(len(password)):
		tot += ord(password[p]) * p
	tot += ord(password[0]) + ord(password[-1])
	return tot % 256

#Encrypt database if password is given
def encryptdb(dbcontent, password):
	values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144][::-1]
	keys = list("<~,.?-}[@*|/")
	dbcontent = dbcontent[::-1]
	key = encpass(password)
	current_count, index = 0, 1
	new_word = ""
	for cur in dbcontent:
		value = ord(cur) + key + (index % len(password))
		index += 1
		while(current_count < value):
			for i in range(len(keys)):
				if current_count + values[i] <= value:
					current_count += values[i]
					new_word += keys[i]
		new_word += ":"
		current_count = 0
	return new_word

#Decrypt database if password is given
def decryptdb(dbcontent, password):
	values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144][::-1]
	keys = list("<~,.?-}[@*|/")
	key = encpass(password)
	new_word = ""
	index = 1
	for current_word in dbcontent.split(":")[:-1]:
		temp_word = 0
		for current in current_word:
			for i in range(len(keys)):
				if current == keys[i]:
					temp_word += values[i]
		new_word += chr(temp_word - key - (index % len(password)))
		index += 1
	return new_word[::-1]

#Find all keys with specified values
#Usage: find(<database to search>, <value to find>)
def find(dbcontent, _query):
	if str(type(dbcontent)) != "<class 'dict'>":
		event_log("Error! Expecting dbcontent to be of type dict in function find")
		raise Exception("Expecting dbcontent to be of type dict in function find")
	keys = []
	for key in dbcontent.keys():
		if dbcontent[key] == _query:
			keys.append(key)
	return keys

#Clone a database (Backing up)
#Usage: clone(<database to clone>, <name of new cloned database>)
def clone(source, destination):
	if str(type(source)) != "<class 'str'>":
		event_log("Error! Expecting source to be of type string in function clone")
		raise Exception("Expecting source to be of type string in function clone")
	if str(type(destination)) != "<class 'str'>":
		event_log("Error! Expecting destination to be of type string in function clone")
		raise Exception("Expecting destination to be of type string in function clone")
	if not path.exists(source):
		event_log("Error! {} does not exist when attempting to clone".format(source))
		raise Exception("{} does not exist when attempting to clone".format(source))
	try:
		with open (source, "r") as db0:
			content = db0.read()
		with open (destination, "w") as db1:
			db1.write(content)
		event_log("Successfully cloned {} to {}".format(source, destination))
	except Exception as e:
		event_log("There was an error cloning {} to {} - {}".format(source, destination, str(e)))
		raise Exception("Error cloning {} to {} - {}".format(source, destination, str(e)))

#Delete a database
#Usage: delete(<database to delete>)
def delete(dbname):
	if str(type(dbname)) != "<class 'str'>":
		event_log("Error! Expecting dbname to be of type string in function delete")
		raise Exception("Expecting dbname to be of type string in function delete")
	if not path.exists(dbname):
		event_log("Error! {} does not exist when attempting to delete".format(dbname))
		raise Exception("{} does not exist when attempting to delete".format(dbname))
	try:
		remove(dbname)
		event_log("Successfully deleted {}".format(dbname))
	except Exception as e:
		event_log("There was an error deleting {} - {}".format(dbname, str(e)))
		raise Exception("Error deleting {} - {}".format(dbname, str(e)))

version = "JNDB v0.0.2"
event_log("JNDB connected successfully.")
