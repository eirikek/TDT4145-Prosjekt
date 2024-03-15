--Sal 
INSERT INTO Sal (Navn) VALUES ('Hovedscenen');

INSERT INTO Sal (Navn) VALUES ('Gamle Scene');


--Teaterstykke 
INSERT INTO TeaterStykke (Navn, Sesong, SalID)  VALUES ('Storst av alt er kjaerligheten', 'Vaar', 2);
INSERT INTO TeaterStykke (Navn, Sesong, SalID)  VALUES ('Kongsemnene', 'Vaar', 1);

--Forestilling

--Kongsemnene
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-03-08', '18:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-03-09', '17:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-03-12', '18:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-03-19', '18:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-04-02', '18:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (2, '2024-02-03', '19:30:00');

--Storst av alt er kjaerligheten
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-03-07', '19:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-03-08', '19:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-03-11', '19:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-03-12', '19:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-03-18', '19:30:00');
INSERT INTO Forestilling (TeaterStykkeID, Dato, StartTidspunkt) VALUES (1, '2024-02-03', '19:30:00');

--Akt

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
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Fabian Heidelberg Lunde', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Emil Olafsson', NULL, 'Fast');
INSERT INTO Skuespiller (Navn, Epost, AnsattStatus) Values ('Snorre Ryen Tøndel', NULL, 'Fast');

--STØRST AV ALT ER KJØRLIGHETEN
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
INSERT INTO Rolle (Navn) Values 
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

INSERT INTO DeltarI (RolleID, AktNummer, TeaterStykkeID) VALUES
    (1, 1, 2),
    (1, 2, 2),
    (1, 3, 2),
    (1, 4, 2),
    (1, 5, 2),
    (2, 1, 2),
    (2, 2, 2),
    (2, 3, 2),
    (2, 4, 2),
    (2, 5, 2),
    (14, 4, 2);

INSERT INTO Spiller (AnsattID, RolleID) VALUES
    (1, 1),
    (11, 2),
    (11, 14);


    


INSERT INTO Kundeprofil(Tlfnr, Navn, Addresse, GruppeID) VALUES(96893214, 'Pål', 'Kule gata 3', 3);

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
