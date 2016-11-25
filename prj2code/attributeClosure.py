# 
# contains the function necessary to compute the attribute closure of a given
# set of attributes and a table of functional dependencies
# 

from compare import getData
from threenf import minCover, makeClosure





def getAttributeClosure(cursor):
	gettingTables = True
	listOfFds=[]
	while gettingTables:
		tableName = str(raw_input('Enter name of FD table, or enter nothing to finish adding tables >'))

		if len(tableName) == 0:
			gettingTables = False
			break

		else:
			for fd in getData(tableName,cursor):
				listOfFds.append(fd)



	startingClosure = []
	for char in str(raw_input('Enter set of attributes, seperated by a comma, to determine the closure of >')).upper():
		if char.isalpha() and char not in startingClosure:
			startingClosure.append(char)


	closure = makeClosure(minCover(listOfFds), startingClosure)

	return closure




