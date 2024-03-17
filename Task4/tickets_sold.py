import sqlite3


def connect():
    return sqlite3.connect("../teater.db")


def find_tickets_sold(dato1, dato2):
    conn = connect()
    c = conn.cursor()
    c.execute(
        """
            SELECT T.TeaterstykkeID, T.Navn, F.Dato,  COUNT(B.BillettID) AS AntallSolgteBilletter
            FROM TeaterStykke AS T
            INNER JOIN Forestilling AS F ON T.TeaterStykkeID = F.TeaterStykkeID
            INNER JOIN Billett AS B ON F.Dato = B.ForestillingDato AND F.TeaterStykkeID = B.TeaterStykkeID
            WHERE F.Dato = ?
            GROUP BY F.TeaterstykkeID
          
            
            UNION
            
            SELECT T2.TeaterStykkeID, T2.Navn, F2.Dato, COUNT(B2.BillettID) AS AntallSolgteBilletter
            FROM BILLETT AS B2
            INNER JOIN TeaterStykke AS T2 ON T2.TeaterStykkeID = B2.TeaterStykkeID
            LEFT JOIN Forestilling AS F2 ON F2.Dato = B2.ForestillingDato AND F2.TeaterStykkeID = B2.TeaterStykkeID
            WHERE F2.Dato = ?
            GROUP BY F2.TeaterStykkeID
            HAVING AntallSolgteBilletter = 0

            
              """,
        (dato1, dato2)
    )
    result = c.fetchall()

    print(result)
    conn.close()


find_tickets_sold("2024-02-03", "2024-02-03")
