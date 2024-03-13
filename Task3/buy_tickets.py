import sqlite3


def kjop_billetter(teaterstykke_navn, dato, antall_billetter):
    conn = sqlite3.connect('teater.db')
    c = conn.cursor()

    # Sjekk at det finnes en forestilling på den gitte datoen
    # c.execute('''SELECT Forestilling.Dato, Forestilling.TeaterStykkeID
    #                 FROM Forestilling INNER JOIN Teaterstykke
    #                 WHERE Teaterstykke.navn = ? AND Forestilling.Dato = ?

    # ''', (teaterstykke_navn, dato))
    # result = c.fetchone()
    # teaterstykke_id, dato = result if result else (None, None)
    # print(teaterstykke_id, dato)

    # if not teaterstykke_id:
    #     print("Fant ikke forestillingen.")
    #     return

    # Finn sal til dato

    c.execute('''
              SELECT Sal.SalID, Sal.Navn
              FROM Sal 
              INNER JOIN Teaterstykke ON Sal.SalID = TeaterStykke.SalID
              INNER JOIN Forestilling ON TeaterStykke.TeaterStykkeID = Forestilling.TeaterStykkeID
              WHERE Forestilling.Dato = ? AND Teaterstykke.Navn = ?
              ''', (teaterstykke_navn, dato))
    result = c.fetchone()
    sal_id, sal_navn = result if result else (None, None)
    print(f"Sal med id {sal_id} og navn {sal_navn}")

    # # Finn ledige stoler
    # c.execute('''SELECT StolNr, RadNr, Omraade
    # FROM Stol
    # WHERE SalID = ? AND  = 1
    # GROUP BY RadNr
    # HAVING COUNT(StolNr) >= ?
    # LIMIT ?''', (sal_id, antall_billetter, antall_billetter))
    # stoler = c.fetchall()

    # if not stoler:
    #     print("Ingen ledige stoler funnet.")
    #     return

    # # Beregn totalprisen for billettene (antar at pris er definert et sted)
    # c.execute('''SELECT SUM(Pris)
    # FROM BillettPris
    # WHERE TeaterStykkeID = ? AND GruppeID = ?''', (teaterstykke_id, 1))  # Anta at GruppeID 1 er for voksne
    # totalpris = c.fetchone()[0] * antall_billetter

    # print(f"Totalpris for {antall_billetter} billetter: {totalpris} kr")

    # # Her ville du ha logikk for å oppdatere databasen med kjøpte billetter, men vi hopper over det i dette eksemplet.

    conn.close()


kjop_billetter("Storst av alt er kjaerligheten", "2024-02-03", 9)
