import sqlite3
from datetime import date, datetime


def connect():
    return sqlite3.connect("teater.db")


def hent_teaterstykke_id(teaterstykke):
    conn = connect()
    c = conn.cursor()
    c.execute(
        "SELECT TeaterStykkeID FROM Teaterstykke WHERE Navn = ?", (teaterstykke,))
    teaterstykke_id = c.fetchone()[0]
    conn.close()
    return teaterstykke_id


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
        SELECT RadNr, Omraade
        FROM Stol
        WHERE SalID = (SELECT SalID FROM TeaterStykke WHERE TeaterStykkeID = ?)
        GROUP BY RadNr, Omraade
    """, (teaterstykke_id,))
    potensielle_rader = c.fetchall()

    for rad_nr, omraade in potensielle_rader:
        c.execute("""
            SELECT COUNT(*)
            FROM Stol
            WHERE RadNr = ?
            AND Omraade = ?
            AND SalID = (SELECT SalID FROM TeaterStykke WHERE TeaterStykkeID = ?)
            AND NOT EXISTS (
                SELECT 1 FROM Billett
                WHERE StolNr = Stol.Nr
                AND RadNr = Stol.RadNr
                AND Omraade = Stol.Omraade
                AND SalID = Stol.SalID
                AND ForestillingDato = ?
            )
        """, (rad_nr, omraade, teaterstykke_id, dato))

        antall_ledige = c.fetchone()[0]
        if antall_ledige >= antall_billetter:
            c.execute("""
                SELECT Nr FROM Stol
                WHERE RadNr = ?
                AND Omraade = ?
                AND SalID = (SELECT SalID FROM TeaterStykke WHERE TeaterStykkeID = ?)
                AND NOT EXISTS (
                    SELECT 1 FROM Billett
                    WHERE StolNr = Stol.Nr
                    AND RadNr = Stol.RadNr
                    AND Omraade = Stol.Omraade
                    AND SalID = Stol.SalID
                    AND ForestillingDato = ?
                )
                ORDER BY Nr
                LIMIT ?
            """, (rad_nr, omraade, teaterstykke_id, dato, antall_billetter))
            ledige_stoler = c.fetchall()
            conn.close()
            return rad_nr, omraade, [stol[0] for stol in ledige_stoler]

    conn.close()
    return None, None, []


def opprett_transaksjon_og_billetter(rad_nr, omraade, stolnumre, teaterstykke_id, dato, antall_billetter, kunde_id):
    if not stolnumre:
        print("Ingen ledige stoler funnet på angitt rad.")
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

    for stol_nr in stolnumre:
        c.execute("""
            INSERT INTO Billett (StolNr, RadNr, Omraade, SalID, ForestillingDato, TeaterStykkeID, TransaksjonID)
            VALUES (?, ?, ?, (SELECT SalID FROM TeaterStykke WHERE TeaterStykkeID = ?), ?, ?, ?)
        """, (stol_nr, rad_nr, omraade, teaterstykke_id, dato, teaterstykke_id, transaksjon_id))

    conn.commit()
    conn.close()


def main():
    teaterstykke_navn = "Størst av alt er kjærligheten"
    teaterstykke_id = hent_teaterstykke_id(teaterstykke_navn)
    dato = '2024-02-03'
    kunde_id = 1
    antall_billetter = 9

    rad_nr, omraade, stolnumre = finn_ledige_stoler_paa_samme_rad(
        teaterstykke_id, dato, antall_billetter)

    if rad_nr and omraade and stolnumre:
        opprett_transaksjon_og_billetter(
            rad_nr, omraade, stolnumre, teaterstykke_id, dato, antall_billetter, kunde_id)
    else:
        print("Det var ikke mulig å finne en rad med nok ledige stoler.")


if __name__ == "__main__":
    main()
