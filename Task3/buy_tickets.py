import sqlite3
from datetime import date, datetime

def connect():
    return sqlite3.connect("../teater.db")

def hent_billettpris_og_id(teaterstykke_id, kunde_id):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT GruppeID FROM Kundeprofil WHERE KundeID = ?", (kunde_id,))
    gruppe_id = c.fetchone()[0]

    c.execute("""
        SELECT BillettPrisID, Pris FROM BillettPris
        WHERE GruppeID = ? AND TeaterStykkeID = ?
        LIMIT 1
    """, (gruppe_id, teaterstykke_id))
    billettpris_info = c.fetchone()
    conn.close()
    if billettpris_info:
        return billettpris_info[0], billettpris_info[1]
    else:
        return None, None

def finn_ledige_stoler_paa_samme_rad(teaterstykke_id, dato, antall_billetter):
    conn = connect()
    c = conn.cursor()
    c.execute("""
        SELECT Stol.RadNr, COUNT(*) AS LedigeStoler
        FROM Stol
        LEFT JOIN Billett ON Stol.Nr = Billett.StolNr AND Stol.RadNr = Billett.RadNr AND Stol.SalID = Billett.SalID AND Billett.ForestillingDato = ?
        WHERE Stol.SalID = (SELECT SalID FROM TeaterStykke WHERE TeaterStykkeID = ?) AND Billett.BillettID IS NULL
        GROUP BY Stol.RadNr
        HAVING LedigeStoler >= ?
    """, (dato, teaterstykke_id, antall_billetter))
    rad_info = c.fetchone()
    conn.close()
    if rad_info:
        return rad_info[0]
    else:
        return None

def opprett_transaksjon_og_billetter(rad_nr, teaterstykke_id, dato, antall_billetter, kunde_id):
    if rad_nr is None:
        print("Ingen tilgjengelige rader med nok ledige stoler.")
        return

    billett_pris_id, pris = hent_billettpris_og_id(teaterstykke_id, kunde_id)
    if not billett_pris_id:
        print("Kunne ikke hente billettpris basert på kundeprofilen.")
        return

    conn = connect()
    c = conn.cursor()

    total_pris = antall_billetter * pris
    print(f"Total pris for billettene: {total_pris} NOK")

    transaksjon_dato = date.today().strftime('%Y-%m-%d')
    tidspunkt = datetime.now().strftime('%H:%M:%S')

    c.execute("""
        INSERT INTO Transaksjon (Dato, Tidspunkt, AntallBilletter, KundeID, BillettPrisID)
        VALUES (?, ?, ?, ?, ?)
    """, (transaksjon_dato, tidspunkt, antall_billetter, kunde_id, billett_pris_id))
    transaksjon_id = c.lastrowid

    c.execute("""
        SELECT Nr FROM Stol
        WHERE SalID = (SELECT SalID FROM TeaterStykke WHERE TeaterStykkeID = ?) AND RadNr = ? AND Nr NOT IN (
            SELECT StolNr FROM Billett WHERE ForestillingDato = ? AND TeaterStykkeID = ?
        )
        LIMIT ?
    """, (teaterstykke_id, rad_nr, dato, teaterstykke_id, antall_billetter))
    ledige_stoler = c.fetchall()

    for stol_nr in ledige_stoler:
        c.execute("""
            INSERT INTO Billett (StolNr, RadNr, SalID, ForestillingDato, TeaterStykkeID, TransaksjonID)
            VALUES (?, ?, (SELECT SalID FROM TeaterStykke WHERE TeaterStykkeID = ?), ?, ?, ?)
        """, (stol_nr[0], rad_nr, teaterstykke_id, dato, teaterstykke_id, transaksjon_id))

    conn.commit()
    conn.close()

def main():
    teaterstykke_id = 1
    dato = '2024-02-03'
    kunde_id = 1
    antall_billetter = 9
    rad_nr = finn_ledige_stoler_paa_samme_rad(teaterstykke_id, dato, antall_billetter)
    if rad_nr is not None:
        opprett_transaksjon_og_billetter(rad_nr, teaterstykke_id, dato,antall_billetter, kunde_id)
    else:
        print("Det var ikke mulig å finne en rad med nok ledige stoler.")

if __name__ == "__main__":
    main()
