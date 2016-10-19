-- The following commands drop the tables in case you have them
-- from earlier runs.
-- Note the order we are creating the tables and the order we are removing
-- them due to the foreign key constraints.

DROP TABLE IF EXISTS charts;
DROP TABLE IF EXISTS symptoms;
DROP TABLE IF EXISTS diagnoses;
DROP TABLE IF EXISTS medications;
DROP TABLE IF EXISTS reportedallergies;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS dosage;
DROP TABLE IF EXISTS inferredallergies;
DROP TABLE IF EXISTS drugs;

CREATE TABLE staff (
  staff_id	CHAR(5),
  role		CHAR(1),
  name		CHAR(15),
  login		CHAR(8),
  password	CHAR(30),
  PRIMARY KEY (staff_id)
);
CREATE TABLE patients (
  hcno		CHAR(5),
  name		CHAR(15),
  age_group	CHAR(5),
  address	CHAR(30),
  phone		CHAR(10),
  emg_phone	CHAR(10),
  PRIMARY KEY (hcno)
);
CREATE TABLE charts (
  chart_id	CHAR(5),
  hcno		CHAR(5),
  adate		DATE,
  edate		DATE,
  PRIMARY KEY (chart_id),
  FOREIGN KEY (hcno) REFERENCES patients
);
CREATE TABLE symptoms (
  hcno		CHAR(5),
  chart_id	CHAR(5),
  staff_id	CHAR(5),
  obs_date	DATE,
  symptom	CHAR(15),
  PRIMARY KEY (hcno, chart_id, staff_id, symptom, obs_date),
  FOREIGN KEY (hcno) REFERENCES patients,
  FOREIGN KEY (chart_id) REFERENCES charts,
  FOREIGN KEY (staff_id) REFERENCES staff
);
CREATE TABLE diagnoses (
  hcno		CHAR(5),
  chart_id	CHAR(5),
  staff_id	CHAR(5),
  ddate		DATE,
  diagnosis	CHAR(20),
  PRIMARY KEY (hcno, chart_id, staff_id, diagnosis, ddate),
  FOREIGN KEY (hcno) REFERENCES patients,
  FOREIGN KEY (chart_id) REFERENCES charts,
  FOREIGN KEY (staff_id) REFERENCES staff
);
CREATE TABLE drugs (
  drug_name	CHAR(15),
  category	CHAR(25),
  PRIMARY KEY(drug_name)
);
CREATE TABLE dosage (
  drug_name	CHAR(15),
  age_group	CHAR(5),
  sug_amount	INT,
  PRIMARY KEY (drug_name, age_group),
  FOREIGN KEY (drug_name) REFERENCES drugs
);
CREATE TABLE medications (
  hcno		CHAR(5),
  chart_id	CHAR(5),
  staff_id	CHAR(5),
  mdate		DATE,
  start_med	DATE,
  end_med	DATE,
  amount	INT,
  drug_name	CHAR(15),
  PRIMARY KEY (hcno,chart_id,staff_id,mdate,drug_name),
  FOREIGN KEY (hcno) REFERENCES patients,
  FOREIGN KEY (chart_id) REFERENCES charts,
  FOREIGN KEY (staff_id) REFERENCES staff,
  FOREIGN KEY (drug_name) REFERENCES drugs
);
CREATE TABLE reportedallergies (
  hcno		CHAR(5),
  drug_name	CHAR(15),
  PRIMARY KEY(hcno, drug_name),
  FOREIGN KEY (hcno) REFERENCES patients,
  FOREIGN KEY (drug_name) REFERENCES drugs
);
CREATE TABLE inferredallergies (
  alg		CHAR(15),
  canbe_alg	CHAR(15),
  PRIMARY KEY(alg, canbe_alg),
  FOREIGN KEY (alg) REFERENCES drugs,
  FOREIGN KEY (canbe_alg) REFERENCES drugs
);
