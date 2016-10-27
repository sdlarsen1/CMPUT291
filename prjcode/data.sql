INSERT INTO staff VALUES
('12345', 'A', 'Admin', 'admin', 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01'),
('12346', 'A', 'Admin01', 'admin01', 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01'),
('12347', 'A', 'Admin02', 'admin02', 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01'),

('12348', 'D', 'Doctor', 'doctor', 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01'),
('12349', 'D', 'Doctor01', 'doctor01', 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01'),
('12350', 'D', 'Doctor02', 'doctor02', 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01'),

('12351', 'N', 'Nuse', 'nurse', 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01'),
('12352', 'N', 'Nurse01', 'nurse01', 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01'),
('12353', 'N', 'Nurse02', 'nurse02', 'd63dc919e201d7bc4c825630d2cf25fdc93d4b2f0d46706d29038d01');

INSERT INTO patients VALUES
('12345', 'Patient01', '18-23', '116 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5050', '780-423-4567'),
('12346', 'Patient02', '18-23', '117 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5051', '780-423-4568'),

('12347', 'Patient03', '24-30', '118 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5052', '780-423-4569'),
('12348', 'Patient04', '24-30', '119 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5053', '780-423-4570'),

('12349', 'Patient05', '31-36', '120 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5054', '780-423-4571'),
('12350', 'Patient06', '24-30', '121 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5055', '780-423-4572');

INSERT INTO drugs VALUES
('Abarelix', 'category01'),
('Abatacep', 'category01'),
('Pacerone', 'category02'),
('Pancrelipase', 'category02');

-- (chart_id, hcno, adate, edate)
INSERT INTO charts VALUES
('22345', '12345', '2016-10-14', '2016-10-20'),
('22346', '12346', '2016-10-14', '2016-10-20'),

('22347', '12347', '2016-11-14', '2016-10-15'),
('22348', '12348', '2016-11-14', '2016-10-15'),

('22349', '12349', '2016-10-15', '2016-10-16'),

('22350', '12345', '2016-09-14', '2016-10-12'),
('22351', '12345', '2016-10-25', '2016-10-30');

-- (hcno, chart_id, staff_id, ddate, diagnosis)
INSERT INTO diagnoses VALUES
('12345', '22345', '12348', '2016-10-14', 'Ebola'),
('12345', '22346', '12349', '2016-10-12', 'T-Virus'),
('12345', '22345', '12348', '2016-10-15', 'The Abyss');

-- (hcno, chart_id, staff_id, obs_date, symptom)
INSERT INTO symptoms VALUES
('12345', '22345', '12348', '2016-10-14', 'Not breathing'),
('12345', '22345', '12348', '2016-10-18', 'Broken arm');

-- Prescribed by doctor
-- (hcno, chart_id, staff_id, mdate, start_med, end_med, amount, drug_name)
INSERT INTO medications VALUES
('12345', '22345', '12348', '2016-10-14', '2016-10-14', '2016-10-30', 30, 'Abarelix'),
('12345', '22345', '12348', '2016-10-17', '2016-10-17', '2016-11-30', 20, 'Pancrelipase'),
('12345', '22345', '12348', '2016-10-19', '2016-10-19', '2016-11-30', 20, 'Abatacep'),

('12346', '22346', '12349', '2016-10-14', '2016-10-14', '2016-10-30', 30, 'Abatacep'),
('12349', '22349', '12349', '2016-10-14', '2016-10-14', '2016-10-25', 15, 'Abatacep'),
('12348', '22348', '12350', '2016-11-14', '2016-11-14', '2016-11-25', 40, 'Pancrelipase');
