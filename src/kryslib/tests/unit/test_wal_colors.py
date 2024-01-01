import pytest
from kryslib.colors.wal_colors import WalColors
from kryslib.colors.color import Color


@pytest.mark.unit
def test_wall_colors(wal_colors_scheme_json):
    wal_colors = WalColors(wal_colors_scheme_json)
    assert wal_colors.background == Color("#0b0310")
    assert wal_colors.foreground == Color("#bfabdb")
    assert wal_colors.cursor == Color("#bfabdb")
    assert wal_colors.color0 == Color("#0b0310")
    assert wal_colors.color1 == Color("#332A6F")
    assert wal_colors.color2 == Color("#49266E")
    assert wal_colors.color3 == Color("#4E4677")
    assert wal_colors.color4 == Color("#402E91")
    assert wal_colors.color5 == Color("#513294")
    assert wal_colors.color6 == Color("#62529F")
    assert wal_colors.color7 == Color("#bfabdb")
    assert wal_colors.color8 == Color("#857799")
    assert wal_colors.color9 == Color("#332A6F")
    assert wal_colors.color10 == Color("#49266E")
    assert wal_colors.color11 == Color("#4E4677")
    assert wal_colors.color12 == Color("#402E91")
    assert wal_colors.color13 == Color("#513294")
    assert wal_colors.color14 == Color("#62529F")
    assert wal_colors.color15 == Color("#bfabdb")
