from cloner import dump
from crypt import encryptdb
from writer import write
from time import time
from finder import find, coun, exist
from event_logger import event_log
from deleter import remf, remd, remdd
from inserter import insA, ins, upd, tab
from reader import load, close, dumps, literal_eval

class connect:
    def __init__(self, dbname, password=None):
        _data, self.state, error = load(dbname, password)
        if str(type(_data)) != "<class 'dict'>":
            error = "A password is required to connect to DB {}".format(dbname)
            event_log(error)
        if error:
            raise Exception(error)
        self.__data = _data
        del _data
        self.__name = str(dbname)
        self.__dataCP = dumps(self.__data)

    def get(self, table=None, id=None, sort=0):
        if table:
            error = None
            if str(type(table)) != "<class 'str'>":
                event_log("Expecting table to be of type str in function get", dbname)
                error = "Expecting table to be of type str in function get"
            if error:
                raise (error)
            try:
                if id:
                    try:
                        d = self.__data[table][id]
                        event_log("Successfully retrieved table_id {} in table {} in DB {} contents".format(id, table, self.__name), self.__name)
                    except:
                        event_log("The table_id {} does not exist in table {} in DB {}".format(id, table, self.__name), self.__name)
                        raise Exception("The table_id {} does not exist in table {} in DB {}".format(id, table, self.__name))
                else:
                    d = self.__data[table]
                    event_log("Successfully retrieved table {} in DB {} contents".format(table, self.__name), self.__name)
                data = d
                del d
            except:
                event_log("The Table {} does not exist! in DB {}".format(table, self.__name), self.__name)
                raise Exception("The Table {} does not exist! in DB {}".format(table, self.__name))
        else:
            event_log("Successfully retrieved DB {} contents".format(self.__name), self.__name)
            data = self.__data
        if int(sort) != 0:
            data2 = {}
            if int(sort) > 0:
                for i in sorted(data):
                    data2[i] = data[i]
            elif int(sort) < 0:
                for i in sorted(data)[::-1]:
                    data2[i] = data[i]
            data = data2
            del data2
        return data

    def tables(self):
        event_log("Successfully retrieved DB {} Tables".format(self.__name), self.__name)
        return list(self.__data.keys())

    def table(self, table_):
        _data = dumps(self.__data)
        data, error = tab(self.__data, table_, self.__name)
        if error:
            raise Exception(error)
        self.__dataCP = _data
        self.__data = data

    def count(self, table=None, id=None):
        if (not table) and (not id):
            event_log("Successfully retrieved count of DB {}".format(self.__name), self.__name)
            return len(self.__data.keys())
        elif (not table) and id:
            error = "Error! Can't get count of table_id without specifying table in function count"
            event_log(error, self.__name)
            raise Exception(error)
        value, error = coun(self.__name, self.__data, table, id)
        if error:
            
            raise Exception(error)
        return value

    def save(self, password=None, prettify=True):
        error = write(self.__name, self.__data, password, prettify)
        if error:
            raise Exception(error)

    def disconnect(self, s=True, password=None, prettify=True):
        if s:
            self.save(password, prettify)
        error = close(self.__name)
        if error:
            raise Exception(error)
        else:
            del self.__data, self.__dataCP, self.__name
  
    def clone(self, destination):
        error = dump(self.__name, destination)
        if error:
            raise Exception(error)

    def insert(self, table, data_, id=None):
        _data = dumps(self.__data)
        data, error = ins(self.__data, data_, table, self.__name, id)
        if error:
            raise Exception(error)
        self.__dataCP = _data
        self.__data = data

    def update(self, table, id, data_=None):
        _data = dumps(self.__data)
        data, error = upd(self.__data, data_, table, self.__name, id)
        if error:
            raise Exception(error)
        self.__dataCP = _data
        self.__data = data

    def exists(self, table=None, id_=None):
        res, error = exist(self.__name, self.__data, table, id_)
        if error:
            event_log("An Error occured when checking if data exists in DB {}".format(self.__name), self.__name)
            raise Exception(error)
        event_log("Successfully checked if data exists in DB {}".format(self.__name), self.__name)
        return res

    def overwrite(self, data_=None):
        _data = dumps(self.__data)
        data, error = insA(data_, self.__name)
        if error:
            raise Exception(error)
        self.__dataCP = _data
        self.__data = data

    def undo(self):
        self.__data = literal_eval(self.__dataCP.replace(": true,", ": True,").replace(": false,", ": False,"))
        event_log("Successfully Reversed Database Action", self.__name)

    def destroy(self):
        error = remf(self.__name)
        if error:
            raise Exception(error)
        self.__data, self.__dataCP = {}, "{}"

    def drop(self, table=None, id=None):
        _data = dumps(self.__data)
        if (not table) and (not id_):
            event_log("Successfully dropped DB {}".format(self.__name), self.__name)
            data_ = {}
        else:
            data_, error = remd(self.__data, self.__name, table, id)
            if error:
                raise Exception(error)
        self.__dataCP = _data
        self.__data = data_

    def delete(self, query_=None, table=None):
        _data = dumps(self.__data)
        data_, error = remdd(self.__name, self.__data, table, query_)
        if error:
            raise Exception(error)
        self.__dataCP = _data
        self.__data = data_

    def select(self, query_=None, table=None, limit=0):
        data_, error = find(self.__name, self.__data, table, query_, limit)
        if error:
            raise Exception(error)
        return data_

def create(dbname, data={}, password=None):
    if password:
        with open(dbname + ".hashdb", "w") as db:
            db.write(encryptdb(str(data), str(password), dbname))
    else:
        with open(dbname + ".hashdb", "w") as db:
            db.write(dumps(data, indent=4))
    event_log("Successfully created new DB {}".format(dbname), dbname)