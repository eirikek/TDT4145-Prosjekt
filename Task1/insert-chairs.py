import sqlite3


def connect():
    return sqlite3.connect('teater.db')


def legg_til_stol(sal_id, rad_nr, stol_nr, omraade):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO Stol (SalID, Nr, RadNr, Omraade) VALUES (?, ?, ?, ?)",
              (sal_id, stol_nr, rad_nr, omraade))
    conn.commit()
    conn.close()


def legg_til_transaksjon_og_billett(sal_id, rad_nr, stol_nr, omraade, dato):
    conn = connect()
    c = conn.cursor()

    c.execute("INSERT INTO Transaksjon (Dato, Tidspunkt, AntallBilletter, KundeID, BillettPrisID) VALUES (?, ?, ?, ?, ?)",
              (dato, '12:00', 1, 1, 1))
    transaksjon_id = c.lastrowid

    c.execute("INSERT INTO Billett (StolNr, RadNr, Omraade, SalID, ForestillingDato, TeaterStykkeID, TransaksjonID) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (stol_nr, rad_nr, omraade, sal_id, dato, 1, transaksjon_id))
    conn.commit()
    conn.close()


hovedscenen = open("hovedscenen.txt", "r")
print(hovedscenen.read())


# Lese hovedscenen.txt.
# Hente ut "dato" fra første linje
# Dele opp galleri og parkett
# Hvis 0 lag ny stol, hvis 1 lag ny stol og transaksjon + billett (knyttet til kundeprofil)
# Hvis newline, radnr += 1
# Hvis x, continue
