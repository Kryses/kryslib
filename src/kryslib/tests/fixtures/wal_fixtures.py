import pytest
import json


@pytest.fixture(scope="session")
def wal_colors_scheme():
    return {
        "wallpaper": "/home/kryses/wallpaper/whirl-wind.jpg",
        "alpha": "100",
        "special": {
            "background": "#0b0310",
            "foreground": "#bfabdb",
            "cursor": "#bfabdb",
        },
        "colors": {
            "color0": "#0b0310",
            "color1": "#332A6F",
            "color2": "#49266E",
            "color3": "#4E4677",
            "color4": "#402E91",
            "color5": "#513294",
            "color6": "#62529F",
            "color7": "#bfabdb",
            "color8": "#857799",
            "color9": "#332A6F",
            "color10": "#49266E",
            "color11": "#4E4677",
            "color12": "#402E91",
            "color13": "#513294",
            "color14": "#62529F",
            "color15": "#bfabdb",
        },
    }


@pytest.fixture(scope="session")
def wal_colors_scheme_json(wal_colors_scheme, test_data_path):
    wal_colors_scheme_json = test_data_path / "wal_colors_scheme.json"
    wal_colors_scheme_json.write_text(json.dumps(wal_colors_scheme))
    return wal_colors_scheme_json
