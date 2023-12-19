import pytest
from kryslib.colors.color import Color


@pytest.mark.unit
def test_color_from_hex():
    color = Color("#FFFFFF")
    assert color.red == 255
    assert color.green == 255
    assert color.blue == 255
    assert color.alpha == 255

    color = Color("#000000")
    assert color.red == 0
    assert color.green == 0
    assert color.blue == 0
    assert color.alpha == 255

    color = Color("#FFFFFF.5")
    assert color.red == 255
    assert color.green == 255
    assert color.blue == 255
    assert color.alpha == 127

    color = Color("#FFFFFF.25")
    assert color.red == 255
    assert color.green == 255
    assert color.blue == 255
    assert color.alpha == 63

    color = Color("#FFFFFF.75")
    assert color.red == 255
    assert color.green == 255
    assert color.blue == 255
    assert color.alpha == 191

    color = Color("#FFFFFF.0")
    assert color.red == 255
    assert color.green == 255
    assert color.blue == 255
    assert color.alpha == 0

    color = Color("#FFFFFFFF")
    assert color.red == 255
    assert color.green == 255
    assert color.blue == 255
    assert color.alpha == 255


@pytest.mark.unit
def test_color_from_rgba():
    color = Color((255, 255, 255, 255))
    assert color.red == 255
    assert color.green == 255
    assert color.blue == 255
    assert color.alpha == 255

    color = Color((0, 0, 0, 255))
    assert color.red == 0
    assert color.green == 0
    assert color.blue == 0
    assert color.alpha == 255

    color = Color((255, 255, 255, 127))
    assert color.red == 255
    assert color.green == 255
    assert color.blue == 255
    assert color.alpha == 127


@pytest.mark.unit
def test_rgba_to_hex():
    assert Color((255, 255, 255, 255)).as_hex() == "#ffffffff"
    assert Color((0, 0, 0, 255)).as_hex() == "#000000ff"
    assert Color((255, 255, 255, 127)).as_hex() == "#ffffff7f"
