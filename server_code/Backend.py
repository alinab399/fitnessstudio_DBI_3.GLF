import sqlite3
import anvil.files
from anvil.files import data_files
import anvil.server


@anvil.server.callable
def mitglied_anmelden(kurs_id, mitglied_id):
  sql = "INSERT INTO besuchen (Kurs_ID, Mitglied_ID) VALUES (?, ?)"

  with sqlite3.connect(data_files["Bischof_Alina_fitnessstudio.db"]) as conn:
    cur = conn.cursor()
    cur.execute(sql, (kurs_id, mitglied_id))
    conn.commit()
  return True
  
@anvil.server.callable
def get_nichtangemeldet(kurs_id):
  query = """
        SELECT 
            m.Mitglied_ID,
            m.Nachname || ' ' || m.Vorname AS Mitglied
        FROM Mitglied AS m
        WHERE m.Mitglied_ID NOT IN (
            SELECT b.Mitglied_ID 
            FROM besuchen b 
            WHERE b.Kurs_ID = ?
        )
    """
  with sqlite3.connect(data_files["Bischof_Alina_fitnessstudio.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query, (kurs_id, )).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def get_kurs_uebersicht():
  query = """
        SELECT 
            k.Kurs_ID,
            k.Bezeichnung, 
            k.Wochentage, 
            k.Uhrzeit, 
            t.Nachname || ' ' || t.Vorname AS Trainer,
            (SELECT COUNT(*) FROM besuchen b WHERE b.Kurs_ID = k.Kurs_ID) || '/' || k.Max_Teilnehmeranzahl AS Teilnehmer
        FROM Kurs AS k
        JOIN Trainer t ON k.Trainer_ID = t.Trainer_ID
        ORDER BY 
            CASE 
                WHEN k.Wochentage = 'Montag' THEN 1
                WHEN k.Wochentage = 'Dienstag' THEN 2
                WHEN k.Wochentage = 'Mittwoch' THEN 3
                WHEN k.Wochentage = 'Donnerstag' THEN 4
                WHEN k.Wochentage = 'Freitag' THEN 5
                WHEN k.Wochentage = 'Samstag' THEN 6
                WHEN k.Wochentage = 'Sonntag' THEN 7
            END, k.Uhrzeit
    """
  with sqlite3.connect(data_files["Bischof_Alina_fitnessstudio.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

