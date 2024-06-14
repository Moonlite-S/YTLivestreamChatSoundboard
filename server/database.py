import sqlite3

def createDatabase():
    conn = sqlite3.connect("users.db")

    c = conn.cursor()

    # SCHEMA (users):
    #   user_id: integer (Primary Key)
    #   name: string

    # SCHEMA (backlog):
    #   message_id: integer (Primary Key)
    #   user_id: integer (Foriegn Key)
    #   user: string
    #   message: string
    #   date: string

    c.execute("""CREATE TABLE IF NOT EXISTS users
            (user_id integer,
            name string name,
            PRIMARY KEY (user_id))""")

    conn.commit()
    conn.close()