import sqlite3
from datetime import date
from datetime import datetime


def connect():
    return sqlite3.connect("teater.db")


def legg_til_stol(sal_id, rad_nr, stol_nr, omraade):
    conn = connect()
    c = conn.cursor()
    c.execute(
        "INSERT INTO Stol (SalID, Nr, RadNr, Omraade) VALUES (?, ?, ?, ?)",
        (sal_id, stol_nr, rad_nr, omraade),
    )
    conn.commit()
    conn.close()


def legg_til_transaksjon_og_billett(
    sal_id, rad_nr, stol_nr, omraade, dato, teaterstykke, kundeprofil
):

    conn = connect()
    c = conn.cursor()

    transaksjon_dato = date.today()
    tidspunkt = datetime.now().strftime('%H:%M:%S')

    c.execute(
        """
        SELECT BillettPrisID
        FROM BillettPris INNER JOIN TeaterStykke
        ON BillettPris.TeaterStykkeID = TeaterStykke.TeaterStykkeID
        INNER JOIN Gruppe 
        ON Gruppe.GruppeID = BillettPris.GruppeID
        INNER JOIN Kundeprofil
        ON Kundeprofil.GruppeID = BillettPris.GruppeID
        WHERE Kundeprofil.KundeID = ?
        """,
        (kundeprofil,)
    )
    billett_pris_id = c.fetchone()[0]

    c.execute(
        "INSERT INTO Transaksjon (Dato, Tidspunkt, AntallBilletter, KundeID, BillettPrisID) VALUES (?, ?, ?, ?, ?)",
        (transaksjon_dato, tidspunkt, 1, kundeprofil, billett_pris_id),
    )
    transaksjon_id = c.lastrowid

    c.execute(
        "INSERT INTO Billett (StolNr, RadNr, Omraade, SalID, ForestillingDato, TeaterStykkeID, TransaksjonID) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (stol_nr, rad_nr, omraade, sal_id, dato, teaterstykke, transaksjon_id),
    )
    conn.commit()
    conn.close()


def add_row_to_scene_hoved():

    file = "Task1_Task2/hovedscenen.txt"
    omraade = None
    rad_nr = 0
    stol_nr = 505
    stol_nr_par = 504
    rad_nr_par = 18

    with open(file, "r") as scene:

        for lines in scene.readlines():

            if "Dato" in lines:
                dato = lines.split(" ")[1].strip()

            if len(lines) == 8:
                omraade = lines.strip()

            if (
                lines.startswith("0") or lines.startswith("1")
            ) and omraade == "Galleri":

                for seat in lines.strip():
                    legg_til_stol(1, rad_nr, stol_nr, omraade)
                    stol_nr += 1

            if (
                lines.startswith("0") or lines.startswith(
                    "1") or lines.startswith("x")
            ) and omraade == "Parkett":

                for seat in lines.strip()[::-1]:

                    if seat == "0":
                        legg_til_stol(1, rad_nr_par, stol_nr_par, omraade)
                        stol_nr_par -= 1

                    if seat == "1":
                        legg_til_stol(1, rad_nr_par, stol_nr_par, omraade)
                        legg_til_transaksjon_og_billett(
                            1, rad_nr_par, stol_nr_par, omraade, dato, 2, 1
                        )
                        stol_nr_par -= 1

                    if seat == "x":
                        stol_nr_par -= 1

                rad_nr_par -= 1


def add_row_to_scene_gamle(scene, omraader, sal_id, dato):

    rad_nr = 1
    omraader_current = []
    omraade_index = 0

    for line in scene:
        line = line.strip()
        if line in omraader:
            omraader_current.append(line)

    for line in scene:
        line = line.strip()
        if line in omraader:
            if omraade_index == len(omraader_current) - 1:
                break
            omraade_index += 1
            rad_nr = 1
            try:
                int(line)
            except ValueError:
                continue

        section = omraader_current[omraade_index]
        for stol_nr, status in enumerate(line, start=1):
            legg_til_stol(sal_id, rad_nr, stol_nr, section)
            if status == "1":
                legg_til_transaksjon_og_billett(
                    2, rad_nr, stol_nr, section, dato, 1, 1)
        rad_nr += 1


def main():
    gamle_scene = open("Task1_Task2/gamle-scene.txt", "r")

    lines_gamle_scene = gamle_scene.readlines()
    lines_gamle_scene.reverse()
    dato = lines_gamle_scene[-1].strip().split(" ")[1]

    omraader_gamle_scene = {"Parkett": [], "Balkong": [], "Galleri": []}
    add_row_to_scene_gamle(
        lines_gamle_scene, omraader_gamle_scene, sal_id=2, dato=dato)
    gamle_scene.close()

    add_row_to_scene_hoved()


if __name__ == "__main__":
    main()
