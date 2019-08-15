# HashDB
# Author - LordGhostX

from event_logger import event_log

# Find all keys with specified values
# Usage: find(<database to search>, <value to find>)
def find(name_, dbcontent, table, query_, limit):
    if str(type(table)) != "<class 'str'>" and str(type(table)) != "<class 'list'>" and table:
        event_log("Error! Expecting table to be of type str or type list in function select", name_)
        return [], "Expecting table to be of type str or type list in function select"
    if str(type(limit)) != "<class 'int'>":
        event_log("Error! Expecting limit to be of type int in function select", name_)
        return [], "Expecting limit to be of type int in function select"
    if limit < 0:
        event_log("Error! Expecting limit to be a positive integer in function select", name_)
        return [], "Expecting limit to be be a positive integer in function select"
    if str(type(query_)) != "<class 'dict'>" and query_:
        event_log("Error! Expecting query_ to be of type dict in function select", name_)
        return [], "Expecting query_ to be of type dict in function select"
    if (not query_) and (not table):
        return list(dbcontent.items()), None
    elif not query_:
        return list(dbcontent[table].items()), None
    if str(type(table)) == "<class 'str'>":
        table = [table]
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
                    selected.append({places: {key: dbcontent[places][key]}})
                    if len(selected) >= limit and limit > 0:
                        return selected, None
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
                                event_log("Error! Invalid Select Format", name_)
                                return [], "Invalid Select Format"
                            elif query.lower() in "or or> or<".split(" "):
                                pass
                            else:
                                valid = False
                    except:
                        valid = False
                        pass
                if valid:
                    selected.append({places: {key: dbcontent[places][key]}})
                    if len(selected) == limit and limit > 0:
                        return selected, None
        event_log("Successfully Selected data from DB {}".format(name_), name_)
        return selected, None
    except Exception as e:
        event_log("Unable to Select data from DB".format(name_), name_)
        return [], str(e)


def coun(name, data, table, index):
    try:
        if str(type(table)) != "<class 'str'>":
            event_log("Error! Expecting table to be of type str in function count", name)
            return 0, "Expecting table to be of type str in function count"
        try:
            d = data[table]
        except:
            event_log("Error! table {} does not exist in DB {}".format(table, name), name)
            return 0, "Error! table {} does not exist in DB {}".format(table, name)
        if index:
            try:
                d = data[table][index]
            except:
                event_log("Error! table_id {} does not exist in table {} in DB {}".format(index, table, name), name)
                return 0, "Error! table_id {} does not exist in table {} in DB {}".format(index, table, name)
            event_log("Successfully retrieved count of table_id {} in table {} in DB {}".format(index, table, name),
                          name)
            return len(data[table][index].keys()), None
        else:
            event_log("Successfully retrieved count of table {} in DB {}".format(table, name), name)
            return len(data[table].keys()), None
    except Exception as e:
        return 0, str(e)


def exist(name, data_, table, id_):
    try:
        if table and id_:
            try:
                value = data_[table][id_]
                del value
                return True, None
            except:
                return False, None
        elif table and (not id_):
            try:
                value = data_[table]
                del value
                return True, None
            except:
                return False, None
        elif (not table) and id_:
            return None, "table cannot be absent when id is specified in function exists"
    except:
        return None, "An error occured when checking if data exists in DB {}".format(name)