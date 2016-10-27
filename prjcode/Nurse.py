import os
import random
from LogInOut import logout


def nurseCommands(cursor, conn, staff_id):

    loggedOut = False

    while not loggedOut:

        os.system("clear")
        choice = int(raw_input('''Type integer value of desired task:
                            1. Perform task 1
                            2. Perform task 2
                            3. Perform task 3
                            4. Perform task 4
                            5. Log out\n'''))

        if choice == 1:
            admitPatient(cursor, conn)
            raw_input("Press Enter to go back to menu.")  # return to menu

        elif choice == 2:
            dischargePatient(cursor, conn)
            raw_input("Press Enter to go back to menu.")  # return to menu

        elif choice == 3:
            getPatientChartInfo(cursor)
            raw_input("Press Enter to go back to menu.")  # return to menu

        elif choice == 4:
            recordSymptom(cursor, conn, staff_id)
            raw_input("Press Enter to go back to menu.")  # return to menu

        else:
            loggedOut = logout()


def admitPatient(cursor,conn): # nurse 1

	patientNotSelected = True
	while patientNotSelected: # for selecting the patient hcno
		name = raw_input("Enter name of Patient >")

		cursor.execute('''
			select *
			from patients
			where lower(name) = lower(?);
			''', (name,))

		listOfPatients = cursor.fetchall()

		print "Patients with name: %s\nHCNO |Name           |Age Group|Address                       |Phone Number|Emergency Phone" %name
		for row in listOfPatients:
			print "%-5s|%-15s|%-9s|%-30s|%-12s|%s" %(row[0],row[1],row[2],row[3],row[4],row[5])

		while patientNotSelected:
			choice = raw_input("Enter the HCNO of the patient, or if not found, enter 'retry' to try a different name, or 'new' to make a new patient file >").lower()

			if choice == "retry":
				break
			elif choice == "new":
				hcno = newPatient(cursor,conn, name)
				patientNotSelected = False

			else:
				for row in listOfPatients:
					if choice == row[0]:
						patientNotSelected = False
						hcno = choice
						break

				if patientNotSelected:
					print "Unkown Input"


	cursor.execute('''
		select hcno, chart_id
		from charts
		where edate is Null
		and hcno = ?;
		''',(hcno,))

	openCharts = cursor.fetchall()

	if len(openCharts) > 0 :
		print "Patient already has a chart open"
		choice = raw_input("Enter 'C' to continue with the existing chart or, enter 'N' to close the existing chart and make a new chart >").lower()
		if choice == 'n':
			cursor.execute('''
				update charts
				set edate = datetime('now')
				where hcno = ? and edate is Null;
				''',(hcno,))
			conn.commit()

		else:
			return True

	cursor.execute('''
		select chart_id
		from charts ;
		''')
	usedChartIDs = cursor.fetchall()

	chartIdNotCreated = True
	while chartIdNotCreated:
		chart_id = str(random.randrange(10000,99999))
		if chart_id not in usedChartIDs:
			chartIdNotCreated = False

	cursor.execute('''
		insert into charts values (?,?,datetime('now'),Null);
		''', (chart_id,hcno,))
	conn.commit()


def newPatient(cursor,conn, name):  # used in admit patient


	cursor.execute('''
		select hcno
		from patients;
		''')
	usedHcnos = cursor.fetchall()

	hcnoNotCreated = True
	while hcnoNotCreated:
		hcno = str(random.randrange(10000,99999) )

		if hcno not in usedHcnos:
			hcnoNotCreated = False

	age_group = raw_input("Enter patient age group >").lower()

	address = raw_input("Enter patient address >").lower()

	phone = raw_input("Enter patient phone number >")

	emerPhone = raw_input("Enter patient emergency phone number >")

	cursor.execute('''
		insert into patients values (?,?,?,?,?,?);
		''', (hcno, name, age_group,address,phone,emerPhone,))
	conn.commit()

	return hcno


def dischargePatient(cursor, conn):  # nurse 2

	patientNotSelected = True
	while patientNotSelected: # for selecting the patient hcno
		name = raw_input("Enter name of Patient >")

		cursor.execute('''
			select *
			from patients
			where lower(name) = lower(?);
			''', (name,))

		listOfPatients = cursor.fetchall()

		print "Patients with name: %s\nHCNO |Name           |Age Group|Address                       |Phone Number|Emergency Phone" %name
		for row in listOfPatients:
			print "%-5s|%-15s|%-9s|%-30s|%-12s|%s" %(row[0],row[1],row[2],row[3],row[4],row[5])

		while patientNotSelected:
			choice = raw_input("Enter the HCNO of the patient, or if not found, enter 'retry' to try a different name >").lower()

			if choice == "retry":
				break

			else:
				for row in listOfPatients:
					if choice == row[0]:
						patientNotSelected = False
						hcno = choice
						break

				if patientNotSelected:
					print "Unkown Input"

	cursor.execute('''
		update charts set edate = datetime('now') where hcno = ? and edate is Null;
		''',(hcno,))
	conn.commit()


def getPatientChartInfo(cursor):  # doctor 1, nurse 3

    while 1:
        hcno = raw_input("Enter Patient Health Care Number >").lower()

        cursor.execute('''
    			select chart_id, edate
    			from charts
    			where hcno = ?
    			order by adate;
    			''', (hcno,))

        charts = cursor.fetchall()

        if len(charts) < 1:
            print "Patient #%s Does Not Exist" % hcno
        else:
            break

    print "Patient Charts for %s\nChart ID|Chart Status" % hcno
    for row in charts:
        if row[1] == None:
            status = "Open"
        else:
            status = "Closed"

        print "%-8s|%s" % (row[0], (status),)

    chartNotSelected = True
    while chartNotSelected:
        chart_id = raw_input("Select Chart Number >")

        for row in charts:
            if chart_id == row[0]:
                chartNotSelected = False
                break
        if chartNotSelected:
            print "Patient Chart #%s Does Not Exist" % chart_id

    cursor.execute('''
    		select staff_id, obs_date, symptom
    		from symptoms
    		where chart_id = ?
    		order by obs_date;
    		''', (chart_id,))

    symptoms = cursor.fetchall()

    cursor.execute('''
    		select staff_id, ddate, diagnosis
    		from diagnoses
    		where chart_id = ?
    		order by ddate;
    		''', (chart_id,))

    diagnoses = cursor.fetchall()

    cursor.execute('''
    		select staff_id, mdate, start_med, end_med, amount, drug_name
    		from medications
    		where chart_id = ?
    		order by mdate;
    		''', (chart_id,))

    meds = cursor.fetchall()

    print "Chart #%s for Patient #%s" % (chart_id, hcno)

    print "Symptoms\nStaff ID|Observation Date   |Symptom"

    for row in symptoms:
        print "%-8s|%-19s|%s" % (row[0], row[1], row[2])
    print "----------------------------------------------"
    print "Diagnosis\nStaff ID|Diagnosis Date     |Diagnosis"
    for row in diagnoses:
        print "%-8s|%-19s|%s" % (row[0], row[1], row[2])

    print "----------------------------------------------"
    print "Medications\nStaff ID|Precsription Date  |Med Start Date     |Med End Date       |Amount per day|Drug Name"
    for row in meds:
        print "%-8s|%-19s|%-19s|%-19s|%-14s|%s" % (row[0], row[1], row[2], row[3], row[4], row[5])
    print "----------------------------------------------"


def recordSymptom(cursor, conn, staff_id):  # doctor 2, nurse 4

    cursor.execute('''
    		select hcno, chart_id
    		from charts
    		where edate is Null;
    		''')

    patientCharts = cursor.fetchall()

    chartNotSelected = True
    patientNotSelected = True
    while patientNotSelected:
        hcno = raw_input("Enter Patient Health Care Number >")
        for row in patientCharts:
            if hcno == row[0]:
                patientNotSelected = False
                break
        if patientNotSelected:
            print "Patient #%s does not have an open chart" % hcno

            choice = raw_input("Enter 'quit' to exit task or enter anything to try another Health care number >").lower()
            if choice == 'quit':
                return False


    while chartNotSelected:
        chart_id = raw_input("Enter Patients Chart Number >")

        if (hcno, chart_id) in patientCharts:
            chartNotSelected = False
        else:
            print "Patient #%s does not have a chart #%s that is open" % (hcno, chart_id)
            choice = raw_input("Enter 'quit' to exit task or enter anything to try another chart number >").lower()
            if choice == 'quit':
                return False

    symptom = raw_input("Enter Patient Symptom >")

    cursor.execute('''
    		insert into symptoms values (?,?,?,datetime('now'),?);
    		''', (hcno, chart_id, staff_id, symptom,))

    conn.commit()