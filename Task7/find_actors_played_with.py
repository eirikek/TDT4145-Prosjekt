import sqlite3


def finn_skuespillerkolleger(skuespillernavn):
    if not skuespillernavn.replace(" ", "").isalpha():
        print("Ugyldig input. Skriv inn et gyldig navn.")
        return

    conn = sqlite3.connect('teater.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM Skuespiller WHERE Navn = ?", (skuespillernavn,))
    if not cur.fetchone():
        print(f"Ingen skuespillere med navn {skuespillernavn}.")
        return

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
    cur.close()
    conn.close()

    if resultat:
        # fmt: off
        string = f"{resultat[0][0]} har i {resultat[0][2]} spilt i samme akt som:"
        skuespillere = set([rad[1] for rad in resultat])
        for navn in skuespillere:
            string += f"\n{navn}"

        print(string)
    else:
        print(f"Ingen registrerte kolleger funnet for {skuespillernavn}.")


if __name__ == "__main__":
    navn = input("Skriv inn navn på en skuespiller: ")
    finn_skuespillerkolleger(navn)
