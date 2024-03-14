import sqlite3


def connect():
    return sqlite3.connect("teater.db")


def find_tickets_sold(dato):
    conn = connect()
    c = conn.cursor()
    c.execute(
        """
            SELECT T.TeaterstykkeID, T.Navn, F.Dato,  COUNT(B.BillettID) AS TotalTickets
            FROM TeaterStykke AS T
            INNER JOIN Forestilling AS F ON T.TeaterStykkeID = F.TeaterStykkeID
            FULL OUTER JOIN Billett AS B ON F.Dato = B.ForestillingDato AND F.TeaterStykkeID = B.TeaterStykkeID
            WHERE F.Dato = ?
            GROUP BY F.TeaterstykkeID
            ORDER BY F.TeaterstykkeID
              """,
        (dato,),
    )
    result = c.fetchall()

    print(result)


find_tickets_sold("2024-02-03")
