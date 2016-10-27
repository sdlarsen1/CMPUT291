import os
from LogInOut import logout


def doctorCommands(cursor, conn, staff_id):

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
            getPatientChartInfo(cursor)
            raw_input("Press Enter to go back to menu.")  # return to menu

        elif choice == 2:
            recordSymptom(cursor, conn, staff_id)
            raw_input("Press Enter to go back to menu.")  # return to menu

        elif choice == 3:
            recordDiagnosis(cursor, conn, staff_id)
            raw_input("Press Enter to go back to menu.")  # return to menu

        elif choice == 4:
            recordMedication(cursor, conn, staff_id)
            raw_input("Press Enter to go back to menu.")  # return to menu

        else:
            loggedOut = logout()


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
			print "Patient #%s Does Not Exist" %hcno
		else:
			break


	print "Patient Charts for %s\nChart ID|Chart Status" %hcno
	for row in charts:
		if row[1] == None:
			status = "Open"
		else:
			status = "Closed"

		print "%-8s|%s" %(row[0],(status),)


	chartNotSelected = True
	while chartNotSelected:
		chart_id = raw_input("Select Chart Number >")

		for row in charts:
			if chart_id == row[0]:
				chartNotSelected = False
				break
		if chartNotSelected:
			print "Patient Chart #%s Does Not Exist" %chart_id


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

	print "Chart #%s for Patient #%s" %(chart_id ,hcno)

	print "Symptoms\nStaff ID|Observation Date   |Symptom"

	for row in symptoms:
		print "%-8s|%-19s|%s" %(row[0],row[1],row[2])
	print "----------------------------------------------"
	print "Diagnosis\nStaff ID|Diagnosis Date     |Diagnosis"
	for row in diagnoses:
		print "%-8s|%-19s|%s" %(row[0],row[1],row[2])

	print "----------------------------------------------"
	print "Medications\nStaff ID|Precsription Date  |Med Start Date     |Med End Date       |Amount per day|Drug Name"
	for row in meds:
		print "%-8s|%-19s|%-19s|%-19s|%-14s|%s" %(row[0],row[1],row[2],row[3],row[4],row[5])
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
            print "Patient #%s does not have an open chart" %hcno
            choice = raw_input("Enter 'quit' to exit task or enter anything to try another Health care number >").lower()
            if choice == 'quit':
                return False

    while chartNotSelected:
		chart_id = raw_input("Enter Patients Chart Number >")

		if (hcno, chart_id) in patientCharts:
			chartNotSelected = False
		else:
			print "Patient #%s does not have a chart #%s that is open" %(hcno,chart_id)
            choice = raw_input("Enter 'quit' to exit task or enter anything to try another chart number >").lower()
            if choice == 'quit':
                return False

    symptom = raw_input("Enter Patient Symptom >")

	cursor.execute('''
		insert into symptoms values (?,?,?,datetime('now'),?);
		''', (hcno, chart_id, staff_id, symptom, ))

	conn.commit()


def recordDiagnosis(cursor, conn, staff_id):  # doctor 3

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
			print "Patient #%s does not have an open chart" %hcno

            choice = raw_input("Enter 'quit' to exit task or enter anything to try another Health care number >").lower()
            if choice == 'quit':
                return False

    while chartNotSelected:
		chart_id = raw_input("Enter Patients Chart Number >")

		if (hcno,chart_id) in patientCharts:
			chartNotSelected = False
		else:
			print "Patient #%s does not have a chart #%s that is open" %(hcno,chart_id)
            choice = raw_input("Enter 'quit' to exit task or enter anything to try another chart number >").lower()
            if choice == 'quit':
                return False

    diagnosis = raw_input("Enter Diagnosis >")

	cursor.execute('''
		insert into diagnoses values (?,?,?,datetime('now'),?);
		''', (hcno, chart_id, staff_id, diagnosis, ))

	conn.commit()


def recordMedication(cursor, conn, staff_id): # doctor 4

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
            print "Patient #%s does not have an open chart" %hcno
            choice = raw_input("Enter 'quit' to exit task or enter anything to try another Health care number >").lower()
            if choice == 'quit':
                return False

    while chartNotSelected:
		chart_id = raw_input("Enter Patients Chart Number >")

		if (hcno,chart_id) in patientCharts:
			chartNotSelected = False
		else:
			print "Patient #%s does not have a chart #%s that is open" %(hcno,chart_id)
            choice = raw_input("Enter 'quit' to exit task or enter anything to try another chart number >").lower()
            if choice == 'quit':
                return False

    medication = raw_input("Enter Drug Name >").lower()


	cursor.execute('''
		select lower(drug_name)
		from reportedallergies
		where hcno = ?
		;
		''', (hcno,))

	directAllergies = cursor.fetchall()

	cursor.execute('''
		select lower(r.drug_name), lower(i.canbe_alg)
		from reportedallergies r, inferredallergies i
		where r.hcno = ?
		and r.drug_name = i.alg
		''', (hcno,))

	inferredAllergies = cursor.fetchall()

	if medication in directAllergies:
		print "Warning Patient is allergic to %s" %medication
		# override = raw_input("Do you wish to procede")

	for row in inferredAllergies:
		if medication == row[1]:
			print "Warning Patient is allergic to %s and therefore could be allergic to %s" %(row[0], row[1])
			# maybe select a new med
			break



	cursor.execute('''
		select d.sug_amount
		from dosage d, patients p
		where p.hcno = ?
		and lower(d.drug_name) = ?
		and d.age_group = p.age_group;
		''', (hcno,medication,))

	sugestedDosage = cursor.fetchall()

	while 1:
		amount = raw_input("Enter dosage amount >")

		if amount > str(sugestedDosage[0][0]):
			print "Amount entered is greater then the recommended dosage of %s for this Patients age group" %sugestedDosage[0][0]
			procede = raw_input("continue with this dosage(y) or enter new dosage(n) >").lower()

			if procede == 'y':
				break
			else:
				continue
		else:
			break


	numOfDays = raw_input("Enter the number of day for the medication >")

	daymodifer = str('+'+str(numOfDays)+' days')

	# (hcno, chart_id, staff_id, mdate, start_med, end_med, amount, drug_name)
	cursor.execute('''
		insert into medications values (?,?,?,datetime('now'),datetime('now'),datetime('now', ?),?,?);
		''', (hcno, chart_id, staff_id, daymodifer, amount, medication, ))
	conn.commit()

