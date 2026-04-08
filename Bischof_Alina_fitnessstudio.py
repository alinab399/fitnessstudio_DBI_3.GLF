import sqlite3

# Konfiguration: Dateiname für die Datenbank
db_name = "Bischof_Alina_fitnessstudio.db"

def setup_database():
    # Verbindung zur Datenbank herstellen (wird erstellt, falls nicht vorhanden)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Foreign Key Unterstützung aktivieren
    cursor.execute("PRAGMA foreign_keys = ON;")

    # --- 1. Tabellen erstellen ---

    # Tabelle Trainer
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Trainer (
            Trainer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Vorname TEXT NOT NULL,
            Nachname TEXT NOT NULL,
            Spezialgebiet TEXT
        )
    ''')

    # Tabelle Kurs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Kurs (
            Kurs_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Bezeichnung VARCHAR(20) NOT NULL,
            Wochentage VARCHAR(10),
            Uhrzeit TEXT,
            Max_Teilnehmeranzahl INTEGER,
            Trainer_ID INTEGER,
            FOREIGN KEY (Trainer_ID) REFERENCES Trainer(Trainer_ID)
        )
    ''')

    # Tabelle Mitglied
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Mitglied (
            Mitglied_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            EMail_Adresse TEXT,
            Vorname TEXT NOT NULL,
            Nachname TEXT NOT NULL,
            Beitrittsdatum TEXT
        )
    ''')

    # Tabelle besuchen (Verknüpfungstabelle)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS besuchen (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Anmeldedatum TEXT,
            Kurs_ID INTEGER,
            Mitglied_ID INTEGER,
            FOREIGN KEY (Kurs_ID) REFERENCES Kurs(Kurs_ID),
            FOREIGN KEY (Mitglied_ID) REFERENCES Mitglied(Mitglied_ID)
        )
    ''')

    # --- 2. Beispieldaten einfügen ---

    # Trainer (mehr als 3)
    trainer_data = [
        ('Max', 'Muskel', 'Krafttraining'),
        ('Susi', 'Stretch', 'Yoga'),
        ('Tom', 'Turbo', 'HIIT'),
        ('Lisa', 'Lauf', 'Ausdauer')
    ]
    cursor.executemany('INSERT INTO Trainer (Vorname, Nachname, Spezialgebiet) VALUES (?, ?, ?)', trainer_data)

    # Kurse (mehr als 5)
    kurs_data = [
        ('Pump It', 'Montag', '18:00', 15, 1),
        ('Yoga Flow', 'Dienstag', '09:00', 10, 2),
        ('Intervall-X', 'Mittwoch', '17:30', 20, 3),
        ('Rückenfit', 'Donnerstag', '19:00', 12, 1),
        ('Morning Run', 'Freitag', '07:00', 25, 4),
        ('Zumba Party', 'Freitag', '20:00', 30, 2)
    ]
    cursor.executemany('INSERT INTO Kurs (Bezeichnung, Wochentage, Uhrzeit, Max_Teilnehmeranzahl, Trainer_ID) VALUES (?, ?, ?, ?, ?)', kurs_data)

    # Mitglieder (mehr als 8)
    mitglied_data = [
        ('hans@mail.de', 'Hans', 'Meier', '2023-01-10'),
        ('anna@web.de', 'Anna', 'Schmidt', '2023-02-15'),
        ('peter@gmx.de', 'Peter', 'Huber', '2023-03-20'),
        ('julia@mail.com', 'Julia', 'Wagner', '2023-04-05'),
        ('kevin@web.de', 'Kevin', 'Müller', '2023-05-12'),
        ('sarah@gmx.net', 'Sarah', 'Becker', '2023-06-18'),
        ('marc@mail.de', 'Marc', 'Schulz', '2023-07-22'),
        ('elena@web.de', 'Elena', 'Hoffmann', '2023-08-30'),
        ('tim@gmx.de', 'Tim', 'Bauer', '2023-09-14')
    ]
    cursor.executemany('INSERT INTO Mitglied (EMail_Adresse, Vorname, Nachname, Beitrittsdatum) VALUES (?, ?, ?, ?)', mitglied_data)

    # Anmeldungen (besuchen) (mehr als 10)
    besuchen_data = [
        ('2024-01-01', 1, 1), ('2024-01-02', 1, 2),
        ('2024-01-03', 2, 3), ('2024-01-04', 2, 4),
        ('2024-01-05', 3, 5), ('2024-01-06', 3, 6),
        ('2024-01-07', 4, 7), ('2024-01-08', 4, 8),
        ('2024-01-09', 5, 9), ('2024-01-10', 5, 1),
        ('2024-01-11', 6, 2), ('2024-01-12', 6, 3)
    ]
    cursor.executemany('INSERT INTO besuchen (Anmeldedatum, Kurs_ID, Mitglied_ID) VALUES (?, ?, ?)', besuchen_data)

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()
    print(f"Datenbank '{db_name}' wurde erfolgreich erstellt und befüllt.")

if __name__ == "__main__":
    setup_database()