-- SAL 
INSERT INTO Sal (Navn) VALUES 
    ('Hovedscenen'),
    ('Gamle Scene');


-- TEATERSTYKKE 
INSERT INTO TeaterStykke (Navn, Sesong, SalID) VALUES 
    ('Størst av alt er kjærligheten', 'Vaar', 2),
    ('Kongsemnene', 'Vaar', 1);


-- FORESTILLING
-- Kongsemne
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES 
    (2, '2024-02-01', '19:00:00'),
    (2, '2024-02-02', '19:00:00'),
    (2, '2024-02-03', '19:00:00'),
    (2, '2024-02-05', '19:00:00'),
    (2, '2024-02-06', '19:00:00');

-- Størst av alt er kjærligheten
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES 
    (1, '2024-02-03', '18:30:00'),
    (1, '2024-02-06', '18:30:00'),
    (1, '2024-02-07', '18:30:00'),
    (1, '2024-02-12', '18:30:00'),
    (1, '2024-02-13', '18:30:00'),
    (1, '2024-02-14', '18:30:00');


-- AKT
-- Størst av alt er kjærligheten
INSERT INTO Akt (TeaterStykkeID, Nummer) VALUES (1, 1);

-- Kongsemne
INSERT INTO Akt (TeaterStykkeID, Nummer) VALUES 
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5);


-- SKUESPILLERE
-- Kongsemne
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) VALUES 
    ('Arturo Scotti', NULL, 'Fast'),
    ('Ingunn Beate Strige Øyen', NULL, 'Fast'),
    ('Hans Petter Nilsen', NULL, 'Fast'),
    ('Madeleine Brandtzæg Nilsen', NULL, 'Fast'),
    ('Synnøve Fossum Eriksen', NULL, 'Fast'),
    ('Emma Caroline Deichmann', NULL, 'Fast'),
    ('Thomas Jensen Takyi', NULL, 'Fast'),
    ('Per Bogstad Gulliksen', NULL, 'Fast'),
    ('Isak Holmen Sørensen', NULL, 'Fast'),
    ('Fabian Heidelberg Lunde', NULL, 'Fast'),
    ('Emil Olafsson', NULL, 'Fast'),
    ('Snorre Ryen Tøndel', NULL, 'Fast');

-- Størst av alt er kjærligheten
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) VALUES 
    ('Sunniva Du Mond Nordal', NULL, 'Fast'),
    ('Jo Saberniak', NULL, 'Fast'),
    ('Marte M. Steinholt', NULL, 'Fast'),
    ('Tor Ivar Hagen', NULL, 'Fast'),
    ('Trond-Ove Skrødal', NULL, 'Fast'),
    ('Natalie Grøndahl Tangen', NULL, 'Fast'),
    ('Håsmund Flaten', NULL, 'Fast');


-- GRUPPE
INSERT INTO Gruppe (GruppeType) VALUES
    ('Ordinær'),
    ('Honnør'),
    ('Student'), 
    ('Barn');


-- ROLLE
-- Kongsemne
INSERT INTO Rolle (Navn) VALUES
    ('Haakon Haakonssønn'),
    ('Dagfinn Bonde'),
    ('Inga fra Vartejg'), 
    ('Skule jarl'), 
    ('Fru Ragnhild'), 
    ('Margrete'), 
    ('Sigrid'),
    ('Ingebjørg'),
    ('Biskop Nikolas'),
    ('Gregorius Jonssønn'),
    ('Paal Flida'),
    ('Trønder'), 
    ('Baard Bratte'), 
    ('Jatgeir Skald'),
    ('Peter');

-- Størst av alt er kjærligheten
INSERT INTO Rolle (Navn) VALUES
    ('Sunniva Du Mond Nordal'),
    ('Jo Saberniak'),
    ('Marte M. Steinholt'),
    ('Tor Ivar Hagen'),
    ('Trond-Ove Skrødal'),
    ('Natalie Grøndahl Tangen'),
    ('Håsmund Flaten');


--DELTAR I
INSERT INTO DeltarI (RolleID, AktNummer, TeaterStykkeID) VALUES

    -- Kongsemne

    -- Håkon håkonsson
    (1, 1, 2),
    (1, 2, 2),
    (1, 3, 2),
    (1, 4, 2),
    (1, 5, 2),

    -- Dagfinn bonde
    (2, 1, 2),
    (2, 2, 2),
    (2, 3, 2),
    (2, 4, 2),
    (2, 5, 2),

    -- Inga fra Vartejg
    (3, 1,2),
    (3, 3, 2),

    -- Skule Jarl
    (4,1,2),
    (4,2,2),
    (4,3,2),
    (4,4,2),
    (4,5,2),

    -- Ragnhild
    (5, 1, 2),
    (5, 5, 2),

    -- Margrete
    (6,1,2),
    (6,2,2),
    (6,3,2),
    (6,4,2),
    (6,5,2),

    -- Sigrid
    (7,1,2),
    (7,2,2),
    (7,5,2),

    -- Ingebjørg
    (8, 4, 2),

    -- Biskop Nikolas
    (9, 1, 2),
    (9, 2, 2),
    (9,3,2),

    -- Gregorius
    (10, 1, 2),
    (10, 2, 2),
    (10, 3, 2),
    (10, 4, 2),
    (10, 5, 2),

    -- Paal Flida
    (11,1,2),
    (11,2,2),
    (11,3,2),
    (11,4,2),
    (11,5,2),

    -- Jatgeir skald
    (14, 4, 2),

    -- Peter
    (15,3,2),
    (15,4,2),
    (15,5,2),

    -- Størst av alt er kjærligheten
    (16,1,1),
    (17,1,1),
    (18,1,1),
    (19,1,1),
    (20,1,1),
    (21,1,1),
    (22,1,1);


-- SPILLER
INSERT INTO Spiller (AnsattID, RolleID) VALUES
-- Kongsemne
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 9),
    (8, 10),
    (9, 11),
    (9, 12),
    (10, 12),
    (10, 13),
    (11, 2),
    (11, 14),
    (12, 15),

-- Størst av alt er kjærligheten
    (13, 16),
    (14, 17),
    (15, 18),
    (16, 19),
    (17, 20),
    (18, 21),
    (19, 22);


-- KUNDEPROFIL
INSERT INTO Kundeprofil(Tlfnr, Navn, Addresse, GruppeID) VALUES(96893214, 'Pål', 'Kule gata 3', 1);


-- BILLETTPRIS
-- Størst av alt er kjærligheten
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES 
    (350, 1, 1, 1),
    (300, 1, 2, 1),
    (220, 1, 3, 1),
    (220, 1, 4, 1),
    (320, 10, 1, 1),
    (270, 10, 2, 1);


-- Kongsemne
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES 
    (450, 1, 1, 2),
    (380, 1, 2, 2),
    (280, 1, 3, 2),
    (420, 10, 1, 2),
    (360, 10, 2, 2);


-- KUNSTNERISK LAG
INSERT INTO KunstneriskLag (Navn, AnsattStatus, OppgaveType) VALUES
-- Kongsemne
('Yury Butusov', 'Fast', 'Regi og musikkutvelgelse'),
('Aleksandr Shishkin-Hokusai', 'Fast', 'Scenografi og kostymer'),
('Eivind Myren', 'Fast', 'Lysdesign'),
('Mina Rype Stokke', 'Fast', 'Dramaturg'),

-- Størst av alt er kjærligheten
('Jonas Corell Petersen', 'Fast', 'Regi'),
('David Gehrt', 'Fast', 'Scenografi og kostymer'),
('Gaute Tønder', 'Fast', 'Musikalsk ansvarlig'),
('Magnus Mikaelsen', 'Fast', 'Lysdesign'),
('Kristoffer Spender', 'Fast', 'Dramaturg');


-- OPPGAVE
INSERT INTO Oppgave (OppgaveType) VALUES 
('Regi'),
('Scenografi og kostymer'),
('Musikalsk ansvarlig'),
('Lysdesign'),
('Dramaturg'),
('Regi og musikkutvelgelse');


-- UTFØRES TIL
INSERT INTO UtfooresTil (TeaterStykkeID, OppgaveType) VALUES
-- Størst av alt er kjærligheten
(1, 'Regi'),
(1, 'Scenografi og kostymer'),
(1,'Musikalsk ansvarlig'),
(1,'Lysdesign'),
(1,'Dramaturg'),

-- Kongsemne
(2, 'Regi og musikkutvelgelse'),
(2, 'Scenografi og kostymer'),
(2,'Lysdesign'),
(2, 'Dramaturg');


--DIREKTØR
INSERT INTO Direktoer (Navn, Epost, AnsattStatus) VALUES ('Elisabeth Egseth Hansen', NULL, 'Fast');