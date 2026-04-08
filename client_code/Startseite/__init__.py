from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.fill_kurs_tabelle()

  def fill_kurs_tabelle(self):
    kurs_daten = anvil.server.call('get_kurs_uebersicht')

    self.repeating_panel_kurse.items = kurs_daten
