from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  @handle("button_anmelden2", "click")
  def button_anmelden2_click(self, **event_args):
    """This method is called when the button is clicked"""
    haupt_form = get_open_form()
    kurs_id = haupt_form.kurs_id

    mitglied_id = self.item['Mitglied_ID']
    anvil.server.call('mitglied_anmelden', kurs_id, mitglied_id)

    haupt_form.refresh_members() #liste im Hauptformular aktulisieren
