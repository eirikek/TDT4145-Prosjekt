import sqlite3

conn = sqlite3.connect('prosjekt.db')
cursor = conn.cursor()


def legg_til_stoler_for_hovedscenen(sal_id, antall_plasser):
    for stol_nr in range(1, 504):
        cursor.execute('INSERT INTO Stol (SalID, Nr, RadNr, Omraade) VALUES (?, ?, ?, ?)',
                       (sal_id, stol_nr, (stol_nr-1)//28 + 1, 'Hovedomraade'))

    for stol_nr in range(505, 515):
        cursor.execute('INSERT INTO Stol (SalID, Nr, RadNr, Omraade) VALUES (?, ?, ?, ?)',
                       (sal_id, stol_nr, 0, 'Galleri Nedre'))

    for stol_nr in range(515, 525):
        cursor.execute('INSERT INTO Stol (SalID, Nr, RadNr, Omraade) VALUES (?, ?, ?, ?)',
                       (sal_id, stol_nr, 0, 'Galleri Øvre'))


def generer_seter_for_seksjon(sal_id, seksjon, seter_per_rad, start_rad, slutt_rad):
    seter = []
    for rad in range(start_rad, slutt_rad + 1):
        for sete in range(1, seter_per_rad[rad - start_rad] + 1):
            seter.append((sal_id, sete, rad, seksjon))
    return seter


# Angi antall seter per rad for hver seksjon
# Dette antallet må korrigeres basert på den faktiske saloppsettet
parkett_seter_per_rad = [18, 16, 17, 18, 18, 17, 18,
                         17, 17, 14]  # Eksempel: Rad 1 til 10 i Parkett
balkong_seter_per_rad = [28, 27, 22, 17]  # Eksempel: Rad 1 til 4 i Balkong
galleri_seter_per_rad = [33, 18, 17]  # Eksempel: Rad 1 til 3 i Galleri

# Generer setene for hver seksjon
parkett_seter = generer_seter_for_seksjon(
    2, 'Parkett', parkett_seter_per_rad, 1, 10)
balkong_seter = generer_seter_for_seksjon(
    2, 'Balkong', balkong_seter_per_rad, 1, 4)
galleri_seter = generer_seter_for_seksjon(
    2, 'Galleri', galleri_seter_per_rad, 1, 3)

# Kombiner alle setene i en liste
alle_seter = parkett_seter + balkong_seter + galleri_seter

# Sett inn alle seter i gamle Scene
cursor.executemany(
    'INSERT INTO Stol (SalID, Nr, RadNr, Omraade) VALUES (?, ?, ?, ?)', alle_seter)


# Legg til stoler for Hovedscenen
legg_til_stoler_for_hovedscenen(1, 524)  # Anta at sal_id for Hovedscenen er 1

# Forplikt endringene og lukk forbindelsen
conn.commit()
conn.close()
