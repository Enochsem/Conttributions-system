import sqlite3

connection = sqlite3.connect("contributors.db")
cursor = connection.cursor()

try:
    contributor_table = """CREATE TABLE IF NOT EXISTS contributor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
	contact TEXT NOT NULL,
	amount TEXT NOT NULL,
	beneficiary TEXT NOT NULL
    )"""

    
    
    cursor.execute(contributor_table)
    connection.commit()
except connection.Error:
    print("debug print")
finally:
    if connection:
        connection.close()

def delete_rows(tb_name):
    connection = sqlite3.connect("contributors.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM {}".format(tb_name))
    connection.commit()
    print("done")


delete_rows("contributor")