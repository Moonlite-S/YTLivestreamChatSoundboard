import sqlite3
import config
import Users

conn = sqlite3.connect("users.db")

c = conn.cursor()

# SCHEMA (users):
#   name: string (Primary Key)
# (Maybe add like an ID or rank?)
c.execute("""CREATE TABLE IF NOT EXISTS users
          id integer,
          name string name,
          PRIMARY KEY (id)""")