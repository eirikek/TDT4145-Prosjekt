CREATE TABLE Sal (
    SalID INTEGER PRIMARY KEY AUTOINCREMENT,
    Navn VARCHAR(255)
);

CREATE TABLE Stol (
    SalID INTEGER NOT NULL,
    Nr INTEGER NOT NULL,
    RadNr INTEGER NOT NULL,
    Omraade VARCHAR(255) NOT NULL,

    FOREIGN KEY (SalID) 
        REFERENCES Sal(SalID)
        ON UPDATE CASCADE,

    PRIMARY KEY (SalID, Nr, RadNr, Omraade)
);

CREATE TABLE TeaterStykke (
    TeaterStykkeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Navn VARCHAR(255),
    Sesong VARCHAR(255),
    SalID INTEGER NOT NULL,
    
    FOREIGN KEY (SalID) 
        REFERENCES Sal(SalID)
        ON UPDATE CASCADE
);

CREATE TABLE Forestilling (
    TeaterStykkeID INTEGER NOT NULL,
    Dato DATE NOT NULL,
    StartTidspunkt TIME,

    FOREIGN KEY (TeaterStykkeID) 
        REFERENCES TeaterStykke(TeaterStykkeID)
        ON UPDATE CASCADE,

    PRIMARY KEY (TeaterStykkeID, Dato)
);

CREATE TABLE Billett (
    BillettID INTEGER PRIMARY KEY AUTOINCREMENT,
    StolNr INTEGER NOT NULL,
    RadNr INTEGER NOT NULL,
    Omraade VARCHAR(255) NOT NULL,
    SalID INTEGER NOT NULL,
    ForestillingDato DATE NOT NULL,
    TeaterStykkeID INTEGER NOT NULL,
    TransaksjonID INTEGER NOT NULL,

    FOREIGN KEY (ForestillingDato, TeaterStykkeID) 
        REFERENCES Forestilling(Dato, TeaterStykkeID)
        ON UPDATE CASCADE,
    
    FOREIGN KEY (TransaksjonID) 
        REFERENCES Transaksjon(TransaksjonID)
        ON UPDATE CASCADE,

    FOREIGN KEY (StolNr, RadNr, Omraade, SalID) 
        REFERENCES Stol(Nr, RadNr, Omraade, SalID)
        ON UPDATE CASCADE
);

CREATE TABLE Kundeprofil (
    KundeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Tlfnr VARCHAR(15),
    Navn VARCHAR(255),
    Addresse VARCHAR(255),
    GruppeID INTEGER NOT NULL,

    FOREIGN KEY (GruppeID) 
        REFERENCES Gruppe(GruppeID)
        ON UPDATE CASCADE
);

CREATE TABLE BillettPris (
    BillettPrisID INTEGER PRIMARY KEY AUTOINCREMENT,
    Pris DECIMAL,
    MinKvantum INTEGER,
    GruppeID INTEGER NOT NULL,
    TeaterStykkeID INTEGER NOT NULL,

    FOREIGN KEY (GruppeID) 
        REFERENCES Gruppe (GruppeID)
        ON UPDATE CASCADE,

    FOREIGN KEY (TeaterStykkeID) 
        REFERENCES TeaterStykke (TeaterStykkeID)
        ON UPDATE CASCADE
);

CREATE TABLE Transaksjon (
    TransaksjonID INTEGER PRIMARY KEY AUTOINCREMENT,
    Dato DATE,
    Tidspunkt TIME,
    AntallBilletter INTEGER,
    KundeID INTEGER NOT NULL,
    BillettPrisID INTEGER NOT NULL,

    FOREIGN KEY (KundeID) 
        REFERENCES KundeProfil (KundeID)
        ON UPDATE CASCADE,

    FOREIGN KEY (BillettPrisID) 
        REFERENCES BillettPris (BillettPrisID)
        ON UPDATE CASCADE
);

CREATE TABLE Gruppe(
    GruppeID INTEGER PRIMARY KEY AUTOINCREMENT,
    GruppeType VARCHAR(50)
);

CREATE TABLE Oppgave(
    OppgaveType VARCHAR(50) PRIMARY KEY
);

CREATE TABLE UtfooresTil(
    TeaterStykkeID INTEGER NOT NULL,
    OppgaveType VARCHAR(50) NOT NULL,

    FOREIGN KEY (TeaterStykkeID)
        REFERENCES TeaterStykke (TeaterStykkeID)
        ON UPDATE CASCADE,

    FOREIGN KEY (OppgaveType)
        REFERENCES Oppgave (OppgaveType)
        ON UPDATE CASCADE,

    PRIMARY KEY (TeaterStykkeID, OppgaveType)
);

CREATE TABLE KunstneriskLag(
    AnsattID INTEGER PRIMARY KEY AUTOINCREMENT,
    Navn VARCHAR(50),
    Epost VARCHAR(50),
    AnsattStatus VARCHAR(100),
    OppgaveType VARCHAR(50),

    FOREIGN KEY (OppgaveType)
        REFERENCES Oppgave (OppgaveType)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE Direktoer(
    AnsattID INTEGER PRIMARY KEY AUTOINCREMENT,
    Navn VARCHAR(50),
    Epost VARCHAR(50),
    AnsattStatus VARCHAR(50)
);

CREATE TABLE Skuespiller(
    AnsattID INTEGER PRIMARY KEY AUTOINCREMENT,
    Navn VARCHAR(50),
    Epost VARCHAR(50),
    AnsattStatus VARCHAR(50)
);

CREATE TABLE Rolle(
    RolleID INTEGER PRIMARY KEY AUTOINCREMENT,
    Navn VARCHAR(50) 
);

CREATE TABLE Spiller(
    AnsattID INTEGER NOT NULL,
    RolleID INTEGER NOT NULL,

    FOREIGN KEY (AnsattID) 
        REFERENCES Skuespiller(AnsattID)
        ON UPDATE CASCADE,

    FOREIGN KEY (RolleID) 
        REFERENCES Rolle(RolleID)
        ON UPDATE CASCADE,

    PRIMARY KEY(AnsattID, RolleID)   
);

CREATE TABLE DeltarI (
    RolleID INTEGER NOT NULL,
    AktNummer INTEGER NOT NULL,
    TeaterStykkeID INTEGER NOT NULL,

    FOREIGN KEY (RolleID)
        REFERENCES Rolle(RolleID)
        ON UPDATE CASCADE,

    FOREIGN KEY (AktNummer)
        REFERENCES Akt(Nummer)
        ON UPDATE CASCADE,

    FOREIGN KEY (TeaterStykkeID)
        REFERENCES TeaterStykke(TeaterStykkeID)
        ON UPDATE CASCADE,

    PRIMARY KEY (RolleID, AktNummer, TeaterStykkeID)
);

CREATE TABLE Akt(
    TeaterStykkeID INTEGER NOT NULL,
    Nummer INTEGER NOT NULL,

    FOREIGN KEY (TeaterStykkeID) 
        REFERENCES TeaterStykke(TeaterStykkeID)
        ON UPDATE CASCADE,
    
    PRIMARY KEY (TeaterStykkeID, Nummer)
);


