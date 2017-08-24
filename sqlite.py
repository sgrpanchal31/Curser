import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE words
         (ID    INT     PRIMARY KEY     NOT NULL,
         title  TEXT                    NOT NULL);''')
print "Table created successfully";

conn.close()
