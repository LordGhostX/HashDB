#ASCII ART!

from event_logger import event_log
from hashlib import sha512

#Convert password to an integer	
def encpass(password, dbname):
	password = str(password)
	password = sha512((password + password + (password[0] * len(password))).encode()).hexdigest()
	try:
		tot = 0
		for p in range(len(password)):
			tot += ord(password[p]) * p
		tot += ord(password[0]) + ord(password[-1])
		return (tot % 512)
	except Exception as e:
		event_log("There was an error parsing given password for DB {} - {}".format(dbname, str(e)), dbname)
		return str(e)
	
#Encrypt database if password is given	
def encryptdb(dbcontent, password, dbname):
	try:
		values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144][::-1]
		keys = list("<~,.?-}[@*|/")
		dbcontent = dbcontent[::-1]
		key = encpass(password, dbname)
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
	except Exception:
		return "{}"
	
#Decrypt database if password is given
def decryptdb(dbcontent, password, dbname):
	try:
		if dbcontent == "{}":	return "{}"
		values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144][::-1]
		keys = list("<~,.?-}[@*|/")
		key = encpass(password, dbname)
		new_word = ""
		index = 1
		for current_word in dbcontent.split(":")[:-1]:
			temp_word = 0
			for current in current_word:
				for i in range(len(keys)):
					if current == keys[i]:
						temp_word += values[i]
			val = temp_word - key - (index % len(password))
			if val <= 0:
				val = 0
			new_word += chr(val)
			index += 1
		return new_word[::-1]
	except Exception:
		return "{}"