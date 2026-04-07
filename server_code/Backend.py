import sqlite3
import anvil.files
from anvil.files import data_files
import anvil.server


@anvil.server.callable
def get_all():
  """Gibt alle Studios zurück - das Frontend muss kein SQL kennen."""
  query = "SELECT * FROM Studio"
  with sqlite3.connect(data_files["fitness_studio.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def get__by_id(id):
  query = "SELECT * FROM Studio WHERE id = ?"
  with sqlite3.connect(data_files["fitness_studio.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]