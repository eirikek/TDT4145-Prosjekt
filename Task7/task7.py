import sqlite3


def finn_skuespillerkolleger(skuespillernavn):
    conn = sqlite3.connect('teater.db')
    cur = conn.cursor()

    query = """
    SELECT DISTINCT s1.Navn, s2.Navn AS SkuespillerNavn, ts.Navn AS TeaterStykkeNavn

    FROM Skuespiller s1
    INNER JOIN Spiller p1 ON s1.AnsattID = p1.AnsattID
    INNER JOIN DeltarI d1 ON p1.RolleID = d1.RolleID

    INNER JOIN TeaterStykke ts ON d1.TeaterStykkeID = ts.TeaterStykkeID
    INNER JOIN DeltarI d2 ON ts.TeaterStykkeID = d2.TeaterStykkeID AND d1.AktNummer = d2.AktNummer

    INNER JOIN Spiller p2 ON d2.RolleID = p2.RolleID
    INNER JOIN Skuespiller s2 ON p2.AnsattID = s2.AnsattID
    WHERE s1.Navn = ? AND s1.AnsattID != s2.AnsattID;
    """

    cur.execute(query, (skuespillernavn,))
    resultat = cur.fetchall()

    for rad in resultat:
        print(f" Skuespiller:{rad[0]}, Spiller med skuespiller: {rad[1]}, Teaterstykke: {rad[2]}")

    cur.close()
    conn.close()


finn_skuespillerkolleger("Arturo Scotti")
