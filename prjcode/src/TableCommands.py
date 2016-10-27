import hashlib as hl


# Function allows sys-admin to add users
def addUser(cursor):
    id = raw_input("Enter staff ID >")
    role = raw_input("Enter role (D, N, A) >").upper()
    name = raw_input("Enter the full name of the person you would like to add >")
    username = raw_input("Enter desired username >")

    password = passwordConf = None
    while password != passwordConf:
        password = raw_input("Enter desired password >")
        passwordConf = raw_input("Re-enter password to confirm >")

        if password == passwordConf:

            hashPass = hl.sha224(password)

            cursor.execute('''
                            INSERT INTO staff VALUES
                            (?,?,?,?,?);''', (id, role, name, username, hashPass,))
            cursor.commit()
        else:
            print "Passwords do not match!"
