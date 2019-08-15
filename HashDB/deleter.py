from os import remove, path
from event_logger import event_log

#deletes a DB file given its name
def remf(dbname):
	try:
		try:
			remove(dbname + ".hashdb")
		except Exception as e:
			event_log("There was an error destroying DB {} - {}".format(dbname, str(e)), dbname)
			return (str(e))
		except Exception as e:
			event_log("There was an error destroying DB {} - {}".format(dbname, str(e)), dbname)
			return (str(e))
		event_log("Successfully deleted DB {}".format(dbname), dbname)
		return None
	except Exception as e:
		event_log("There was an error destroying DB {} - {}".format(dbname, str(e)), dbname)
		return str(e)

#deletes data from the database
def remd(dbcontent, name_, table, id_):
	if id_ and (not (str(type(id_)) in ["<class 'str'>", "<class 'int'>", "<class 'float'>"])):
		event_log("Error! Expecting id_ to be of type string or int or float in function drop", name_)
		return [], "Expecting id_ to be of type string or int or float in function drop"
	if not (str(type(table)) in ["<class 'str'>", "<class 'list'>"]):
		event_log("Error! Expecting table to be of type string or list in function drop", name_)
		return [], "Expecting table to be of type string or list in function drop"
	try:
		if str(type(table)) == "<class 'str'>":
			if id_:
				del dbcontent[table][id_]
				event_log("Successfully dropped id_ {} in table {} in DB {}".format(id_, table, name_), name_)
			else:
				del dbcontent[table]
				event_log("Successfully dropped table {} in DB {}".format(table, name_), name_)
		else:
			for i in table:
				del dbcontent[i]
		return dbcontent, None
	except Exception as e:
		event_log("There was an error droping table {} in DB {} - {}".format(table, name_, str(e)), name_)
		return {}, str(e)

def remdd(name_, dbcontent, table, query_):
	if (str(type(table)) != "<class 'str'>" and str(type(table)) != "<class 'list'>") and table:
		event_log("Error! Expecting table to be of type str or list in function delete", name_)
		return [], "Expecting table to be of type str or list in function delete"
	if str(type(table)) == "<class 'str'>":
		table = [table]
	if str(type(query_)) != "<class 'dict'>" and query_:
		event_log("Error! Expecting query_ to be of type dict in function find", name_)
		return [], "Expecting query_ to be of type dict in function find"
	if (not query_) and (not table):
		del dbcontent
		return {}, None
	elif not query_:
		del dbcontent[table]
		return dbcontent, None
	try:
		if table:
			places_to_search = table
		else:
			places_to_search = list(dbcontent.keys())
		selected = []
		for places in places_to_search:
			for key in dbcontent[places]:
				present = False
				for query in query_:
					try:
						if "or" == query.lower() and (not present):
							for keyy in query_[query]:
								if dbcontent[places][key][keyy] == query_[query][keyy]:
									present = True
					except:
						pass
					try:
						if "or>" == query.lower() and (not present):
							for keyy in query_[query]:
								if dbcontent[places][key][keyy] > query_[query][keyy]:
									present = True
					except:
						pass
					try:
						if "or<" == query.lower() and (not present):
							for keyy in query_[query]:
								if dbcontent[places][key][keyy] < query_[query][keyy]:
									present = True
					except:
						pass
				if present:
					selected.append([places, key])
					continue
				valid = True
				for query in query_:
					try:
						if "and" == query.lower():
							for keyy in query_[query]:
								if dbcontent[places][key][keyy] != query_[query][keyy]:
									valid = False
						elif "not" == query.lower():
							try:
								for keyy in query_[query]:
									if dbcontent[places][key][keyy] == query_[query][keyy]:
										valid = False
							except:
								pass
						elif "like" == query.lower():
							for keyy in query_[query]:
								if not (str(query_[query][keyy]).lower() in str(dbcontent[places][key][keyy]).lower() and str(type(dbcontent[places][key][keyy])) == "<class 'str'>"):
									valid = False
						elif ">" == query:
							for keyy in query_[query]:
								if str(type(query_[query][keyy])) in ["<class 'float'>", "<class 'int'>"]:
									if float(dbcontent[places][key][keyy]) < float(query_[query][keyy]):
										valid = False
						elif "<" == query:
							for keyy in query_[query]:
								if str(type(query_[query][keyy])) in ["<class 'float'>", "<class 'int'>"]:
									if float(dbcontent[places][key][keyy]) > float(query_[query][keyy]):
										valid = False
						else:
							if not query.lower() in "or or> or<".split(" "):
								event_log("Error! Invalid Delete Format", name_)
								return [], "Invalid Delete Format"
							elif query.lower() in "or or> or<".split(" "):
								pass
							else:
								valid = False
					except:
						valid = False
						pass
				if valid:
					selected.append([places, key])	
		for i in selected:
			try:
				del dbcontent[i[0]][i[1]]
			except:
				pass
		event_log("Successfully Deleted data from DB {}".format(name_), name_)
		return dbcontent, None
	except Exception as e:
		return {}, str(e)