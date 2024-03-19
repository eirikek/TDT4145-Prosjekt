import datetime
import sqlite3


def connect():
    return sqlite3.connect("teater.db")


def hent_forestillinger_og_billetter(dato):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Forestilling.TeaterStykkeID, Teaterstykke.Navn, Forestilling.Dato
        FROM Forestilling INNER JOIN Teaterstykke
        ON Forestilling.TeaterStykkeID = TeaterStykke.TeaterStykkeID
        WHERE Dato = ?
        ORDER BY Navn
    """, (dato,))

    forestillinger = cursor.fetchall()

    if not forestillinger:
        print(f"Det er ingen forestillinger den {dato}.")
        return

    for forestilling in forestillinger:
        teaterstykke_id = forestilling[0]
        cursor.execute("""
            SELECT COUNT(*)
            FROM Billett
            WHERE TeaterStykkeID = ? AND ForestillingDato = ?
        """, (teaterstykke_id, dato))

        antall_solgte_billetter = cursor.fetchone()[0]
        # fmt: off
        print(f"Forestilling: {forestilling[1]}, Dato: {forestilling[2]}, Solgte billetter: {antall_solgte_billetter}")

    conn.close()


if __name__ == "__main__":
    dato = input("Skriv inn en dato (ÅÅÅÅ-MM-DD): ")
    try:
        datetime.date.fromisoformat(dato)
        hent_forestillinger_og_billetter(dato)
    except:
        print("Ugyldig dato")
