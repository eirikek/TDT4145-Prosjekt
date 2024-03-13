import sqlite3


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


def legg_til_transaksjon_og_billett(sal_id, rad_nr, stol_nr, omraade, dato):
    conn = connect()
    c = conn.cursor()

    c.execute(
        "INSERT INTO Transaksjon (Dato, Tidspunkt, AntallBilletter, KundeID, BillettPrisID) VALUES (?, ?, ?, ?, ?)",
        (dato, "12:00", 1, 1, 1),
    )
    transaksjon_id = c.lastrowid

    c.execute(
        "INSERT INTO Billett (StolNr, RadNr, Omraade, SalID, ForestillingDato, TeaterStykkeID, TransaksjonID) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (stol_nr, rad_nr, omraade, sal_id, dato, 1, transaksjon_id),
    )
    conn.commit()
    conn.close()


def add_row_to_scene_hoved(file, seating, sal_id):

    with open(file, "r") as scene:

        rad = scene.readline()

        if "Dato" in rad:
            rad[5:-1]


def add_row_to_scene_gamle(scene_list, seating, sal_id, dato):

    section = None
    rad_nr = 1
    omraader = []
    omraade_index = 0

    for line in scene_list:
        line = line.strip()
        if line in seating:
            omraader.append(line)

    for line in scene_list:
        line = line.strip()
        if line in seating:
            if omraade_index == len(omraader) - 1:
                break
            omraade_index += 1
            rad_nr = 1
            try:
                int(line)
            except ValueError:
                continue

        section = omraader[omraade_index]
        for stol_nr, status in enumerate(line, start=1):
            legg_til_stol(sal_id, rad_nr, stol_nr, section)
            if status == "1":
                legg_til_transaksjon_og_billett(
                    2, rad_nr, stol_nr, section, dato)
        rad_nr += 1


def main():
    hovedscenen = open("Task1/hovedscenen.txt", "r")
    gamle_scene = open("Task1/gamle-scene.txt", "r")

    lines_gamle = gamle_scene.readlines()
    lines_gamle.reverse()
    dato = lines_gamle[-1].strip().split(" ")[1]

    seating_gamle = {"Parkett": [], "Balkong": [], "Galleri": []}
    add_row_to_scene_gamle(lines_gamle, seating_gamle,
                           sal_id=2, dato=dato)

    hovedscenen.close()
    gamle_scene.close()


if __name__ == "__main__":
    main()
