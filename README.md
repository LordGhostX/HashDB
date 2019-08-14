```
#
#   ██╗ ██╗  █████╗ ███████╗██╗  ██╗      ██████╗ ██████╗
#  ████████╗██╔══██╗██╔════╝██║  ██║      ██╔══██╗██╔══██╗
#  ╚██╔═██╔╝███████║███████╗███████║█████╗██║  ██║██████╔╝
#  ████████╗██╔══██║╚════██║██╔══██║╚════╝██║  ██║██╔══██╗
#  ╚██╔═██╔╝██║  ██║███████║██║  ██║      ██████╔╝██████╔╝
#   ╚═╝ ╚═╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═════╝
#                                                                             
```
# HashDB

This library is an implementation for a NOSQL Database using JSON for storing of data.

Check the ChangeLog for info on what has changed.

## Installation
Windows / Linux / MAC

On Windows, Linux and MAC, you can install this package easily by placing the py file in your project folder (not available via pip)

## Usage
* Add the line of code to include JNDB and all its functions
```python
import jndb
```

## HashDB Banner
```python
import hashdb
hashdb.banner() # This will display HashDB awesome banner! Try it out someday
```

## Features
* Database Creation and Encryption
* Database Deletion
* Database Reading and Decryption
* Database Cloning
* Data Location
* Event Logging

## Database Creation and Encryption
The create function creates a new database and takes in 4 arguments
```python
create(dbname, dbcontent, password, indent)
```
create([name of database to create], [data to save as json], [password if any], [indentation to use for JSON output])
  * dbname: This is the name of the database to be created, It is of type string. It has no specified extension and can be named anything e.g -> "sample.jndb", "test.txt", "database.database"

  * dbcontent: This is an optional parameter. It is the database content to be included in the newly created database file, It is of type dict. If it is omitted the new database will be empty {} e.g -> {"Name": "JNDB", "Description": "NOSQL Database"}

  * password: This is an optional parameter. It is the password to be used to encrypt the database, It can be either string or float or integer. If it is omitted the database will not be encrypted but left in plain JSON e.g -> "password", 674893, 876.56789

  * indent: This is an optional parameter. This is the indentation of the output JSON file if the database is not encrypted. It is of type integer. If it is omitted the value 4 will be used. e.g -> 4, 7, 2

	```python
  jndb.create("example.jndb") # This will create an empty database named "example.jndb"

  jndb.create("example.jndb", {"Languages": ["Python", "C", "PHP"]}, password="ExamplePassword") # This will create an encrypted database
  ```

## Database Deletion
The delete function deletes an existing database and takes in 1 argument
```python
delete(dbname)
```
delete([name of database to delete])
  * dbname: This is the name of the database to be deleted, It is of type string. e.g -> "sample.jndb"
	```python
  jndb.delete("sample.jndb") # This will delete the existing database "sample.jndb"
  ```

## Database Reading and Decryption
The read function reads an existing database to a python dictionary and takes in 2 arguments and returns dict
```python
read(dbname, password)
```
read([name of database to read], [password to decrypt database if any])
  * dbname: This is the name of the database to be read. It is of type string e.g -> "sample.jndb"

  * password: This is the password to decrypt the database with if there is any. It can be either string or float or integer e.g -> "password", 567843, 9876.5432
	```python
  db = jndb.read("sample.jndb") # This will read the "sample.jndb" file and store it in variable db which will become a dictionary

	db = jndb.read("sample.jndb", password="ExamplePassword") # This will decrypt "sample.jndb" with the given password
  ```

## Database Cloning
The clone function creates a copy of an existing database. You can also regard this as backing up a database. It takes in 2 arguments
```python
read(source, destination)
```
read([name of database to clone], [name of new database])
  * source: This is the name of the database to be cloned. It is of type string e.g -> "database1.jndb"

  * destination: This is the name of new cloned database. It is of type string. If it exists it will be overwritten e.g -> "database2.jndb"
	```python
  jndb.clone("database1.jndb", "database2.jndb") # This will clone all the contents in "database1.jndb" to "database2.jndb"
  ```

## Data Location
The find function returns a list of keys that have a specific value. It takes in 2 arguments
```python
find(dbcontent, _query)
```
find([data to search], [what to search for])
  * dbcontent: This is the data to search. It is of type dict e.g -> {"Python": "Interpreted", "C": "Compiled", "PHP": "Interpreted", "JS": "Interpreted"}
  * _query: This is the data to be searched for. It can be any datatype e.g -> "Interpreted", 5, True, [1, 2, 3], {"Animal": "Goat"}
	```python
  db = {"Python": "Interpreted", "C": "Compiled", "Ruby": "Interpreted", "JS": "Interpreted"} # Data to be searched

	print(jndb.find(db, "Interpreted")) # Output: ["Python", "PHP", "JS"]
  ```

## Event Logging
JNDB features an Event Logging feature that will record every action taken by a user and store in `event-log.txt`. It helps in locating DB errors

This feature is always active and not called by the user. You can access the log by locating the `event-log.txt`

## Version
0.0.3

## License
[**MIT**](https://opensource.org/licenses/MIT)

## Author
LordGhostX
