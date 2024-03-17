--Sal 
INSERT INTO Sal (Navn) VALUES ('Hovedscenen');
INSERT INTO Sal (Navn) VALUES ('Gamle Scene');


--Teaterstykke 
INSERT INTO TeaterStykke (Navn, Sesong, SalID)  VALUES ('Størst av alt er kjærligheten', 'Vaar', 2);
INSERT INTO TeaterStykke (Navn, Sesong, SalID)  VALUES ('Kongsemnene', 'Vaar', 1);

--Forestilling

--Kongsemnene
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-02-01', '19:00:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-02-02', '19:00:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-02-03', '19:00:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-02-05', '19:00:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-02-06', '19:00:00');

--Storst av alt er kjaerligheten
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-02-03', '18:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-02-06', '18:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-02-07', '18:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-02-12', '18:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-02-13', '18:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-02-14', '18:30:00');

--Akt

--Storst av alt
INSERT INTO Akt (TeaterStykkeID, Nummer) VALUES (1, 1);

-- Kongsemne
INSERT INTO Akt (TeaterStykkeID, Nummer) VALUES (2, 1);
INSERT INTO Akt (TeaterStykkeID, Nummer) VALUES (2, 2);
INSERT INTO Akt (TeaterStykkeID, Nummer) VALUES (2, 3);
INSERT INTO Akt (TeaterStykkeID, Nummer) VALUES (2, 4);
INSERT INTO Akt (TeaterStykkeID, Nummer) VALUES (2, 5);

--Skuespillere

-- KONGSEMNENE
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Arturo Scotti', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Ingunn Beate Strige Øyen', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Hans Petter Nilsen', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Madeleine Brandtzæg Nilsen', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Synnøve Fossum Eriksen', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Emma Caroline Deichmann', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Thomas Jensen Takyi', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Per Bogstad Gulliksen', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Isak Holmen Sørensen', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Emil Olafsson', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Snorre Ryen Tøndel', NULL, 'Fast');

--STØRST AV ALT ER KJÆRLIGHETEN
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Sunniva Du Mond Nordal', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Jo Saberniak', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Marte M. Steinholt', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Tor Ivar Hagen', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Trond-Ove Skrødal', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Natalie Grøndahl Tangen', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Håsmund Flaten', NULL, 'Fast');


--Bilettpris
INSERT INTO Gruppe (GruppeType)
VALUES
    ('Ordinær'),
    ('Honnør'),
    ('Student'), 
    ('Barn');

--Rolle

-- Kongsemnene
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


-- Kongsemnene
INSERT INTO DeltarI (RolleID, AktNummer, TeaterStykkeID) VALUES

    --Kongsemnene

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
    --Inga fra Vartejg
    (3, 1,2),
    (3, 3, 2),

    -- Skule Jarl
    (4,1,2),
    (4,2,2),
    (4,3,2),
    (4,4,2),
    (4,5,2),

    --Ragnhild
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

    --Ingebjørg
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


INSERT INTO Spiller (AnsattID, RolleID) VALUES
--Kongsemnene
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
    (10, 2),
    (10, 14),
    (11, 15),

--Størst av alt er kjærligheten

    (12, 16),
    (13, 17),
    (14, 18),
    (15, 19),
    (16, 20),
    (17, 21),
    (18, 22);

INSERT INTO Kundeprofil(Tlfnr, Navn, Addresse, GruppeID) VALUES(96893214, 'Pål', 'Kule gata 3', 1);

--Størst av alt er kjærligheten
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (350, 1, 1, 1);
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (300, 1, 2, 1);
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (220, 1, 3, 1);
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (220, 1, 4, 1);
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (320, 10, 1, 1);
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (270, 10, 2, 1);


--Kongsemne

INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (450, 1, 1, 2);
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (380, 1, 2, 2);
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (280, 1, 3, 2);
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (420, 10, 1, 2);
INSERT INTO Billettpris(Pris, MinKvantum, GruppeID, TeaterstykkeID) VALUES (360, 10, 2, 2);


-- Oppgave

-- UtføresTil

-- KunstneriskLag


