-- Zichun Lin
-- michaellin@ualberta.ca
-- Oct 5, 2016
INSERT INTO drugs VALUES
('ABC', 'anti-inflammatory'),
('XXX', 'anti-inflammatory'),
('DEF', 'anti-inflammatory'),
('niacin', 'anti-inflammatory'),
('Adravil', 'fictional'),
('lalala', 'blablabla'),
('cmput291', 'cmput');

INSERT INTO patients VALUES
('12345', 'John Doe 1', '18-20', '1234-120 ST, Edmonton, Alberta', '780-123-456', '780-123-456'),
('12346', 'John Doe 2', '18-20', '4390-105 ST, Calgary, Alberta', '123-456-789', '123-456-789'),
('12347', 'John Doe 3', '18-20', '1224-120 ST, Edmonton, Alberta', '123-567-789', '123-567-789'),
('12348', 'John Doe 4', '18-20', '1134-190 ST, Calgary, Alberta', '123-234-789', '123-234-789'),
('12349', 'John Doe 5', '25-30', '1239-12 ST, Edmonton, Alberta', '780-654-789', '780-654-789'),
('12350', 'John Doe 6', '18-20', '4444-34 ST, Calgary, Alberta', '780-098-312', '780-098-312'),
('12351', 'John Doe 7', '18-20', '234-102 ST, Edmonton, Alberta', '520-449-000', '520-449-000'),
('12352', 'John Doe 8', '18-20', '1204-130 ST, Toronto, Ontario', '530-098-123', '780-098-123'),
('23769', 'John Doe 9', '18-20', '214-330 ST, Edmonton, Alberta', '780-098-123', '780-000-123');

INSERT INTO dosage VALUES
('niacin', '18-20', 2, 3),
('Adravil', '18-20', 10, 11),
('ABC', '18-20', 5, 7);

INSERT INTO medications VALUES
('12345', '2016-10-01', 9, 99, 'ABC'),
('12345', '2015-09-30', 2, 10, 'ABC'), -- 9.30

('12345', '2016-10-01', 9, 99, 'XXX'),
('12345', '2015-09-30', 2, 10, 'XXX'), -- 9.30

('12346', '2016-10-01', 50, 1, 'DEF'),
('23769', '2015-09-29', 100, 1, 'DEF'),
('23769', '2013-09-01', 50, 1, 'DEF'),

('12345', '2015-01-10', 201, 21, 'niacin'),
('12345', '2015-01-12', 300, 21, 'niacin'),
('12346', '2016-01-20', 400, 21, 'niacin'),
('12350', '2015-10-20', 200, 21, 'niacin'),

('12349', '2015-10-30', 500, 2, 'niacin'), --


('12352', '2015-01-11', 9, 1, 'Adravil'), -- Toronto
('12345', '2016-10-01', 200, 1,  'Adravil'), -- Edmonton
('12346', '2016-10-01', 3, 1, 'Adravil'), -- Calgary
('12347', '2016-10-01', 20, 1, 'Adravil'); -- Edmonton

INSERT INTO symptoms VALUES
('12345', '2015-01-11', 'Ebola'), -- Edmonton
('12349', '2015-01-17', 'Ebola'), -- Edmonton
('12346', '2016-10-01', 'Ebola'), -- Calgary
('12347', '2016-09-09', 'The Abyss'), -- Edmonton
('12349', '2016-10-02', 'The Abyss'), -- Edmonton
('12345', '2016-10-02', 'The Abyss'), -- Edmonton
('12352', '2016-03-04', 'The Abyss'), -- Toronto
('12345', '2016-10-02', 't-Virus'), -- Edmonton
('12351', '2016-10-02', 't-Virus'), -- Edmonton
('12349', '2016-10-02', 't-Virus'), -- Edmonton
('12345', '2015-09-30', 'headache'),
('12345', '2015-09-29', 'headache'),
('12345', '2015-09-29', 'blablabla');

INSERT INTO reportedallergies VALUES
('23769', 'Adravil'),
('23769', 'XXX'),
('12345', 'Adravil'),
('12345', 'XXX'),
('12352', 'Adravil'),
('12352', 'XXX'),
('12346', 'Adravil'),
('12346', 'XXX'),
('12346', 'lalala'),
('12349', 'Adravil'),
('12351', 'lalala'),
('12351', 'niacin');


INSERT INTO inferredallergies VALUES
('Adravil', 'DEF'),
('XXX', 'ABC'),
('ABC', 'niacin'),
('lalala', 'cmput291');
