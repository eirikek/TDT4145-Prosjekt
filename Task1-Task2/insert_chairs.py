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


def legg_til_transaksjon_og_billett(
    sal_id, rad_nr, stol_nr, omraade, dato, teaterstykke
):
    conn = connect()
    c = conn.cursor()

    c.execute(
        "INSERT INTO Transaksjon (Dato, Tidspunkt, AntallBilletter, KundeID, BillettPrisID) VALUES (?, ?, ?, ?, ?)",
        (dato, "12:00", 1, 1, 1),
    )
    transaksjon_id = c.lastrowid

    c.execute(
        "INSERT INTO Billett (StolNr, RadNr, Omraade, SalID, ForestillingDato, TeaterStykkeID, TransaksjonID) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (stol_nr, rad_nr, omraade, sal_id, dato, teaterstykke, transaksjon_id),
    )
    conn.commit()
    conn.close()


def add_row_to_scene_hoved(sal_id):

    file = "Task1-Task2/hovedscenen.txt"
    området = None
    rad_nr = 0
    stol_nr = 505
    stol_nr_par = 504
    rad_nr_par = 18

    with open(file, "r") as scene:

        for lines in scene.readlines():

            if "Dato" in lines:
                dato = lines.split(" ")[1].strip()

            if len(lines) == 8:
                området = lines.strip()

            if (
                lines.startswith("0") or lines.startswith("1")
            ) and området == "Galleri":

                for seat in lines.strip():
                    legg_til_stol(1, rad_nr, stol_nr, området)
                    stol_nr += 1

            if (
                lines.startswith("0") or lines.startswith("1") or lines.startswith("x")
            ) and området == "Parkett":

                for seat in lines.strip()[::-1]:

                    if seat == "0":
                        legg_til_stol(1, rad_nr_par, stol_nr_par, området)
                        stol_nr_par -= 1

                    if seat == "1":
                        legg_til_stol(1, rad_nr_par, stol_nr_par, området)
                        legg_til_transaksjon_og_billett(
                            1, rad_nr_par, stol_nr_par, området, dato, 2
                        )
                        stol_nr_par -= 1

                    if seat == "x":
                        stol_nr_par -= 1

                rad_nr_par -= 1


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
                legg_til_transaksjon_og_billett(2, rad_nr, stol_nr, section, dato, 1)
        rad_nr += 1


def main():
    gamle_scene = open("Task1-Task2/gamle-scene.txt", "r")

    lines_gamle = gamle_scene.readlines()
    lines_gamle.reverse()
    dato = lines_gamle[-1].strip().split(" ")[1]

    seating_gamle = {"Parkett": [], "Balkong": [], "Galleri": []}
    add_row_to_scene_gamle(lines_gamle, seating_gamle, sal_id=2, dato=dato)
    add_row_to_scene_hoved(sal_id=1)

    gamle_scene.close()


if __name__ == "__main__":
    main()
