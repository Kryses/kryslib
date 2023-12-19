import json
from pathlib import Path
from kryslib.colors.color import Color


class WalColors(object):
    def __init__(self, walcolor_json: str):
        """Manages from pywal"""
        self._walcolor_json = Path(walcolor_json)
        self._colors_raw = json.load(open(self._walcolor_json, "r"))
        self.background = Color(self._colors_raw["special"]["background"])
        self.foreground = Color(self._colors_raw["special"]["foreground"])
        self.cursor = Color(self._colors_raw["special"]["cursor"])
        self.color0 = Color(self._colors_raw["colors"]["color0"])
        self.color1 = Color(self._colors_raw["colors"]["color1"])
        self.color2 = Color(self._colors_raw["colors"]["color2"])
        self.color3 = Color(self._colors_raw["colors"]["color3"])
        self.color4 = Color(self._colors_raw["colors"]["color4"])
        self.color5 = Color(self._colors_raw["colors"]["color5"])
        self.color6 = Color(self._colors_raw["colors"]["color6"])
        self.color7 = Color(self._colors_raw["colors"]["color7"])
        self.color8 = Color(self._colors_raw["colors"]["color8"])
        self.color9 = Color(self._colors_raw["colors"]["color9"])
        self.color10 = Color(self._colors_raw["colors"]["color10"])
        self.color11 = Color(self._colors_raw["colors"]["color11"])
        self.color12 = Color(self._colors_raw["colors"]["color12"])
        self.color13 = Color(self._colors_raw["colors"]["color13"])
        self.color14 = Color(self._colors_raw["colors"]["color14"])
        self.color15 = Color(self._colors_raw["colors"]["color15"])
