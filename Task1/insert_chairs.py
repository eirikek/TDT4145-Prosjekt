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


hovedscenen = open("Task1/hovedscenen.txt", "r")
hovedscenen.close()

gamle_scene = open("Task1/gamle-scene.txt", "r")


# Initialize the dictionary
# Initialize the dictionary


def add_row_to_scene(scene_list, seating, sal_id, dato):

    # Initialize variables
    section = None
    rad_nr = 1

    for line in scene_list:
        line = line.strip()  #
        if line in seating:
            section = line
        elif line and section is not None:
            for stol_nr, status in enumerate(line, start=1):
                if status == "1":
                    legg_til_stol(sal_id, rad_nr, stol_nr, section)
                    legg_til_transaksjon_og_billett(
                        sal_id, rad_nr, stol_nr, section, dato
                    )
            rad_nr += 1
            # seating[section].append(line)

    # for section, rows in seating.items():
    #     seating[section] = {str(i + 1): row for i, row in enumerate(reversed(rows))}


# Open the file and read the lines
def main():
    hovedscenen = open("Task1/hovedscenen.txt", "r")
    gamle_scene = open("Task1/gamle-scene.txt", "r")

    lines_gamle = gamle_scene.readlines()
    seating_gamle = {"Galleri": [], "Balkong": [], "Parkett": []}
    add_row_to_scene(lines_gamle, seating_gamle, sal_id=2, dato="2024-02-03")

    lines_hoved = hovedscenen.readlines()
    seating_hoved = {"Galleri": [], "Parkett": []}
    add_row_to_scene(lines_hoved, seating_hoved, sal_id=1, dato="2024-02-03")

    hovedscenen.close()
    gamle_scene.close()


if __name__ == "__main__":
    main()

# Lese hovedscenen.txt.
# Hente ut "dato" fra første linje
# Dele opp galleri og parkett
# Hvis 0 lag ny stol, hvis 1 lag ny stol og transaksjon + billett (knyttet til kundeprofil)
# Hvis newline, radnr += 1
# Hvis x, continue
