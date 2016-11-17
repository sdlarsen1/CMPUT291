# File contains to read table and collect FDs
def parse(inTable, inFD, cursor):
    cursor.execute('''
                    SELECT * FROM ?;''', (inTable,))

    rows = cursor.fetchall()
