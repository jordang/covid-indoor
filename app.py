import dash
from flask_talisman import Talisman

"""
app.py is to be imported by other files (default.py, advanced.py, index.py) to be referenced in setup.

"""

# Dash App Setup
app = dash.Dash(__name__, suppress_callback_exceptions=True)

Talisman(app.server, force_https=True)

curr_units = 'british'