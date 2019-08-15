from event_logger import event_log

def insA(data_, dbname):
    try:
        if not data_:
            event_log("Successfully overwritten data in DB {}".format(dbname), dbname)
            return {}, None
        if str(type(data_)) == "<class 'dict'>" or str(type(data_)) == "<class 'str'>":
            if str(type(data_)) == "<class 'str'>":
                data_ = {"data": data_}
            event_log("Successfully overwritten data in DB {}".format(dbname), dbname)
            return data_, None
        else:
            event_log("Expecting data_ to be of type dict or str in function overwrite", dbname)
            return {}, "Error! Expecting data_ to be of type dict or str"
    except Exception as e:
        event_log("There was an error overwriting data in DB {} - {}".format(dbname, str(e)), dbname)
        return {}, str(e)

def ins(data, data_, table, dbname, id_):
    try:
        if str(type(data_)) != "<class 'dict'>":
            event_log("Expecting data_ to be of type dict in function insert", dbname)
            return {}, "Error! Expecting data_ to be of type dict"
        if str(type(table)) != "<class 'str'>":
            event_log("Expecting table to be of type str in function insert", dbname)
            return {}, "Error! Expecting table to be of type str"
        if str(type(id_)) != "<class 'str'>" and id_:
            event_log("Expecting id_ to be of type str in function insert", dbname)
            return {}, "Error! Expecting id_ to be of type str"
        if not id_:
            id_ = "id_{}".format(len(data[table]))
        try:
            data[table]
        except:
            event_log("table {} does not exist in DB {}".format(table, dbname), dbname)
            return {}, "table {} does not exist in DB {}".format(table, dbname)
        data[table][str(id_)] = data_
        event_log("Successfully inserted data into DB {} in table {}".format(dbname, table), dbname)
        return data, None        
    except Exception as e:
        event_log("There was an error inserting data into DB {} in table {} - {} does not exist".format(dbname, table, str(e)), dbname)
        return {}, str(e) + "does not exist"

def upd(data, data_, table, dbname, id_):
    try:
        if str(type(data_)) != "<class 'dict'>":
            event_log("Expecting data_ to be of type dict in function update", dbname)
            return {}, "Error! Expecting data_ to be of type dict"
        if str(type(table)) != "<class 'str'>":
            event_log("Expecting table to be of type str in function update", dbname)
            return {}, "Error! Expecting table to be of type str"
        if not str(type(id_)) in ["<class 'str'>", "<class 'int'>"]:
            event_log("Expecting id_ to be of type str or int in function update", dbname)
            return {}, "Error! Expecting id_ to be of type str or int"
        if not data_:
            data_ = {}
        try:
            if str(type(id_)) == "<class 'int'>":
                bin_ = data[table][list(data[table].keys())[id_]]
                del bin_
                data[table][list(data[table].keys())[id_]] = data_
            else:
                bin_ = data[table][str(id_)]
                del bin_
                data[table][str(id_)] = data_
        except:
            event_log("There is no table_id with {} in table {} in DB {}".format(id_, table, dbname), dbname)
            return {}, "table_id {} does not exist in table {}".format(id_, table)
        event_log("Successfully updated data into DB {} in table {} with id {}".format(dbname, table, id_), dbname)
        return data, None        
    except Exception as e:
        event_log("There was an error updating data in DB {} in table {} with id_ {} - {}".format(dbname, table, id_, str(e)), dbname)
        return {}, str(e)

def tab(data_, table_, name_):
    try:
        if str(type(table_)) != "<class 'str'>":
            event_log("Expecting table to be of type str in function table", dbname)
            return {}, "Error! Expecting table to be of type str"
        data_[table_] = {}
        event_log("Successfully created table {} in DB {}".format(table_, name_), name_)
        return data_, None
    except Exception as e:
        event_log("There was an error creating table {} in DB {} - {}".format(table_, name_, str(e)), name_)
        return {}, str(e)