-- Question 1: Find the names of all drugs in the anti-inflammatory
-- category that have been prescribed to patients in Edmonton.
.print Question 1 - sdlarsen
SELECT d.drug_name
FROM drugs d
WHERE d.category = 'anti-inflammatory'
  AND d.drug_name IN (SELECT m.drug_name
                      FROM patients p, medications m
                      WHERE p.address LIKE '%Edmonton%'
                      AND p.hcno = m.hcno);

-- Question 2: Without using aggregation functions, write a query to find
-- the names of symptoms that have been observed in at least two patients
-- from Edmonton but no patient from Calgary.
.print Question 2 - sdlarsen
SELECT DISTINCT s1.sym_name
FROM symptoms s1, symptoms s2
WHERE s1.sym_name = s2.sym_name
  AND s1.hcno != s2.hcno
  AND s1.hcno IN (SELECT hcno
                  FROM patients
                  WHERE address LIKE '%Edmonton%')

EXCEPT
SELECT s.sym_name
FROM symptoms s, patients p
WHERE s.hcno = p.hcno
AND p.address LIKE '%Calgary%';

-- Question 3: Find the names of all the symptoms that have been observed for
-- a patient within 5 days after the drug niacin was prescribed to that
-- patient. For instance, if the drug is prescribed to a patient on
-- Jan 10, 2015, we are interested in symptoms that have been observed within
-- the period of Jan 11th to 16th.
.print Question 3 - sdlarsen
SELECT s.sym_name
FROM medications m, symptoms s
WHERE m.drug_name = 'niacin'
  AND m.hcno = s.hcno
  AND JULIANDAY(s.obs_date) - JULIANDAY(m.mdate) <= 5
  AND JULIANDAY(s.obs_date) - JULIANDAY(m.mdate) > 0;

-- Question 4: For each Area Code (of the emergency phone numbers), create a
-- list of the names plus the emergency phone numbers of all patients who had
-- a medication of niacin in an amount larger than 200 for more than 20 days.
-- The list per area code should have the form
--    name_1:emg_phone_1 - name_2:emg_phone2 - ... - name_n:emg_phone_n
.print Question 4 - sdlarsen
SELECT p.name ||':'|| p.emg_phone
FROM patients p, medications m
WHERE p.hcno = m.hcno
AND m.drug_name = 'niacin'
GROUP BY SUBSTR(p.emg_phone, 1, 3)
HAVING m.amount > 200
  AND m.days > 20;

-- Question 5: Find patients who have had a medication with an amount exceeding
-- twice the average dose amount of the drug for the patient's age group (the
-- average is obtained from the past medication records). For each qualifying
-- patient and drug, list both the patient heath care number and the drug name.
.print Question 5- sdlarsen
SELECT p.hcno, m.drug_name
FROM medications m, patients p
WHERE m.hcno = p.hcno
GROUP BY p.age_group
HAVING m.amount * m.days > (SELECT 2*AVG(amount * days)
                            FROM medications m, drugs d, patients p
                            WHERE m.drug_name = d.drug_name
                            GROUP BY p.age_group
                            HAVING m.drug_name = d.drug_name);

-- Question 6: Find drugs that have been prescribed to a larger percent
-- of patients in Edmonton than in Toronto. List in the output the drug name
-- and the fractions of patients in Edmonton and Toronto who have obtained
-- the medication.
.print Question 6 - sdlarsen
SELECT t.drug_name
FROM medications m, (SELECT m.drug_name, p.address
                      FROM medications m, patients p
                      WHERE m.hcno = p.hcno
                      AND (p.address LIKE '%Toronto%'
                      OR p.address LIKE '%Edmonton%')) t
GROUP BY t.drug_name
HAVING (COUNT(t.drug_name) / (SELECT COUNT(t.address)
                              WHERE t.address LIKE '%Toronto%'))
        < (COUNT(t.drug_name) / (SELECT COUNT(t.address)
                                  WHERE t.address LIKE '%Edmonton%'))


-- Question 7: Find prescribed drugs that have been prescribed to a patient on
-- the same day the patient had a headache as the only symptom recorded that
-- day, and report for each of these drugs: 1) the name of the drug, 2) the
-- average amount prescribed per day, and 3) the total amount ever prescribed
-- to those patients. BUT: report the information only for those drugs that
-- have an average number of prescribed days greater than 3. Note that the
-- column amount in the medication table stores the amount to be taken per day
-- by a patient. The number of days the patient has to take the medication is
-- stored in the column days of the medication table.
.print Question 7 - sdlarsen
--SELECT drug_name, amount, --?

-- Question 8: Find the health care number of every patient who has
-- reported exactly the same set of drug allergies as the patient with
-- health care number 23769.
.print Question 8 - sdlarsen
SELECT DISTINCT r1.hcno
FROM reportedallergies r1, reportedallergies r2
WHERE r1.drug_name = r2.drug_name
  AND r2.hcno = '23769'
  AND r1.hcno IN (SELECT hcno
                  FROM reportedallergies
                  GROUP BY hcno
                  HAVING COUNT(drug_name) = (SELECT COUNT(drug_name)
                                              FROM reportedallergies
                                              WHERE hcno = '23769'))
EXCEPT
SELECT r1.hcno
FROM reportedallergies r1
WHERE r1.hcno = '23769';

-- Question 9: Create a view called allergies with columns hcno and drug_name
-- that includes for each patient the set of drugs for which the patient can be
-- allergic to. A patient can be allergic to a drug if this is either reported
-- by the patient (in the table reportedallergies) or is inferred from other
-- drugs the patient is reported to be allergic to (using the table
-- inferredallergies). The view should not include patients with no allergies.
.print Question 9 - sdlarsen
CREATE VIEW allergies
AS SELECT DISTINCT r.hcno, d.drug_name
  FROM reportedallergies r, drugs d
  WHERE r.drug_name = d.drug_name
    OR d.drug_name IN (SELECT canbe_alg
                        FROM reportedallergies r, inferredallergies i
                        WHERE r.drug_name = i.alg); -- prints allergies that shouldn't exist

-- Question 10 Using the view, write a query to list all the drugs in the
-- category anti-inflammatory that the patient with health care number 23769 is
-- not allergic to (i.e., an allergy for the drug is neither reported nor can
-- be inferred).
.print Question 10 - sdlarsen
SELECT drug_name
FROM drugs
WHERE drug_name NOT IN (SELECT drug_name
                        FROM allergies
                        WHERE hcno = '23769');
