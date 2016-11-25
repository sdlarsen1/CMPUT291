#
# contains code for bcnf conversion
#

from threenf import minCover, makeClosure



# function determines if a specified FD violates BCNF
# fd violates bcnf if fd[0] is not a key and if fd is not trivial
def violatesbcnf(inFDs, elements, fd):

	trivial = True
	for char in fd[1]:
		if char not in fd[0]:
			trivial = False

	# if the LHS of fd is a key then the fd does not violate bcnf
	if len(elements) == len(makeClosure(minCover(inFDs), fd[0] )):
		isKey = True

	# else if the fd is trivial the fd does not violate bcnf
	else:
		isKey = False


	if isKey or trivial:
		return False
	else:
		return True





# function populates the new tables
def populateTable(cursor, relation, inTable,fdDict, inRows):

	name = "Output"+inTable+'_'+''.join(relation[0])

	for row in inRows:
		valueStr = ''
		for element in relation[0]:
			valueStr += "'" + str(row[fdDict[element]]) + "'" + ','
		valueStr = valueStr[:-1]

		try:
			cursor.execute('''
						INSERT INTO %s VALUES (%s)''' %(name, valueStr))
		except Exception, e:
			# print e
			pass



# create new tables based on the new FDs
def makeTable(cursor,relation, inTable):
	elements = relation[0]

	keyList=[]

	for fd in relation[1]:
		for char in fd[0]:
			keyList.append(char)



	name = "Output"+inTable+'_'+''.join(elements)
	fdName = "Output_FDs"+inTable+'_'+''.join(elements)
	attStr = ','.join(elements)
	keyStr = ','.join(keyList)


	if len(keyList) != 0:
	 	cursor.execute('''
						CREATE TABLE %s (%s, PRIMARY KEY (%s));''' %(name, attStr, keyStr))

		cursor.execute('''
						CREATE TABLE %s (LHS, RHS);''' %(fdName))

		for fd in relation[1]:
			cursor.execute('''
							INSERT INTO %s VALUES (%s, %s);''' %(fdName, "'"+fd[0]+"'", "'"+fd[1]+"'"))
		
	else:
		cursor.execute('''
						CREATE TABLE %s (%s);''' %(name, attStr))




# make a list of all elements
# inFDs is a list of tuples of the fds, ie [(LHS,RHS),(LHS,RHS),...]
def makeElements(inFDs):
    elements = []



    for fd in inFDs:
    	for side in fd:
    		for char in side:
    			if char not in elements:
    				elements.append(char)
    return elements



# recursive BCNF converter
# inFDs is a list of tuples of the fds, ie [(LHS,RHS),(LHS,RHS),...]
# elements is a list of the elements, ie ['a','b',...]
def converter(elements, inFDs):
	debug = False

	if len(inFDs) == 0:
		return [[elements,[] ] ]

	for fd in inFDs:
		if debug:
			print 'old fds is >',inFDs
			print "fd is >",fd
			print 'elements is >',elements

		if violatesbcnf(inFDs, elements, fd):
			
			A = [[makeElements([fd]), [fd]]]
			if debug:
				print 'violatesBCNF'
				print 'A is >',A


			for char in fd[1]:
				try:
					elements.remove(char)
				except:
					pass
			newFDs = []
			inFDs.remove(fd)
			if debug:
				print 'elements is now >', elements

			for fd in inFDs:
				violatesLHS = False
				for char in fd[0]:
					if char not in elements:
						violatesLHS = True
				if violatesLHS:
					continue

				newFD = [fd[0], '']
				for char in fd[1]:
					if char in elements:
						newFD[1] += char

				if len(newFD[1]) > 0:
					newFDs.append(newFD)
			if debug:
				print 'new fds is >',newFDs
				raw_input('press enter to continue >')

			for relation in converter(elements, newFDs):
				A.append(relation)
			return A
	

	return []



# main function for convertbcnf
def convertbcnf(inRows, inFDs, cursor, conn, fdDict, inTable):


	elements = makeElements(inFDs)  # get elements

	listOfRelations = converter(elements,inFDs)

	for relation in listOfRelations:

		makeTable(cursor, relation, inTable)
		conn.commit()

	# needs a choice
	choice = str(raw_input("Would you like to populate the table(s)?\n1. Yes\n2. No\n"))
	if choice == '1':
		for relation in listOfRelations:
			populateTable(cursor, relation, inTable,fdDict, inRows)
			conn.commit()
