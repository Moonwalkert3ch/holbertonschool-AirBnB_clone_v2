#!/usr/bin/python3

import os
# HBNB_MYSQL_USER=hbnb_dev 
# HBNB_MYSQL_PWD=hbnb_dev_pwd 
# HBNB_MYSQL_HOST=localhost 
# HBNB_MYSQL_DB=hbnb_dev_db
# HBNB_TYPE_STORAGE=db
os.environ["HBNB_MYSQL_USER"] = "hbnb_dev"
os.environ["HBNB_MYSQL_PWD"] = "hbnb_dev_pwd"
os.environ["HBNB_MYSQL_HOST"] = "localhost"
os.environ["HBNB_MYSQL_DB"] = "hbnb_dev_db"
os.environ["HBNB_TYPE_STORAGE"] = "db"

from models import storage

states = storage.all("State")
print("It worked")