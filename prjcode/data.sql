INSERT INTO staff VALUES
('12345', 'A', 'Admin', 'admin', '$6$rounds=656000$ZIJXVzcCG.NOUjQ1$VEstY9Dk6v.h40zQDy02f8Vusqz4b3OYj4vGE3lirOtb4A41XpVoiusPxc24gqniw7NWqjQGX3ULa65iGkHnG.'),
('12346', 'A', 'Admin01', 'admin01', '$6$rounds=656000$6EOlHE8Qb3DuIq8d$DOJPSbsp5juO6.YywdAa21VajkNha3Cv7NGRSCDBhY5rIy3wLo7qmZZovycP8NgFQGIbwjaKhL2i08VigxUPK0'),
('12347', 'A', 'Admin02', 'admin02', '$6$rounds=656000$8SHX8pHNoo9QrX6K$chwr9oPUl0fCUXJju.WI2bj5UgVqB/TO5ZQboc4f1ElTgGLwxHgraxkwIxhWxl7QArZl6aG1idr/KoL1Y9/vH.'),

('12348', 'D', 'Doctor', 'doctor', '$6$rounds=656000$Wcxmpt6gHB/ukwAa$BxQdnqeDZbuRf9588j9EjlLWNwqsCaqpxGsQJ1zO95oiJ.da/P34jc1F9wfhLZ6c37MH/1fD.9YnTKSff68TJ1'),
('12349', 'D', 'Doctor01', 'doctor01', '$6$rounds=656000$Wcxmpt6gHB/ukwAa$BxQdnqeDZbuRf9588j9EjlLWNwqsCaqpxGsQJ1zO95oiJ.da/P34jc1F9wfhLZ6c37MH/1fD.9YnTKSff68TJ1'),
('12350', 'D', 'Doctor02', 'doctor02', '$6$rounds=656000$Y4VI8UPii0HIzR.y$kJcuNRBwTQocrlqQn8nfoAusf/tmPfNM7TNhkxkoDEG1lq77h4OSb8hX..lNCvlF5VL.RGlEgdHBLdM5fOE5L0'),

('12351', 'N', 'Nurse', 'nurse', '$6$rounds=656000$yZZGQMRTWO3UNVcU$1YxOuGvwTwIZjYJhhQtbcBpMX.kVwM3ET.7L2DTxCSkctNkcFfW3Bbou3yxk3Dn0C4WQ/CYn28CknNr2AZ.La0'),
('12352', 'N', 'Nurse01', 'nurse01', '$6$rounds=656000$WSftywkXHWBSuWTy$3gkhDF6HjOdkIVuStxv4/ufj1H7Z5QGdj7XIie17URjqCBWMKhazlrGUwD8qmVezLDaiCkFsoyT6Mbfj2oPit1'),
('12353', 'N', 'Nurse02', 'nurse02', '$6$rounds=656000$1L8Sg6vaj9JHGwp5$yj69B43SqbuOaQNqWJNXNH16Fv0/enr6lpdNRZTEV0v2c8quOOeZIK7Gt6bHlp1MEzUbTW1xrIOaCNQAf2B7k.');

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

-- (hcno, chart_id, staff_id, osb_date, symptom)
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
