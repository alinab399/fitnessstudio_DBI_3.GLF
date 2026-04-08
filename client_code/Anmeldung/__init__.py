from ._anvil_designer import AnmeldungTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Anmeldung(AnmeldungTemplate):
  def __init__(self, selected_kurs_id, **properties):
    self.init_components(**properties)
    self.kurs_id = selected_kurs_id
    self.refresh_members()

  def refresh_members(self):
    self.repeating_panel_anmeldung.items = anvil.server.call('get_nichtangemeldet', self.kurs_id)

  @handle("button_zurueck", "click")
  def button_zurueck_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite')

