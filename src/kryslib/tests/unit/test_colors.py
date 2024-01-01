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


@pytest.mark.unit
def test_hex_to_rgba():
    assert Color("#ffffffff").as_rgba() == (255, 255, 255, 255)
    assert Color("#000000ff").as_rgba() == (0, 0, 0, 255)
    assert Color("#ffffff7f").as_rgba() == (255, 255, 255, 127)


@pytest.mark.unit
def test_color_as_str():
    assert str(Color("#ffffff")) == "#ffffffff"
    assert str(Color("#ffffffff")) == "#ffffffff"
    assert str(Color("#000000ff")) == "#000000ff"
    assert str(Color("#ffffff7f")) == "#ffffff7f"
    assert str(Color((255, 255, 255, 255))) == "#ffffffff"
    assert str(Color((0, 0, 0, 255))) == "#000000ff"
    assert str(Color((255, 255, 255, 127))) == "#ffffff7f"


@pytest.mark.unit
def test_color_add():
    assert Color("#ffffff") + Color("#ffffff") == Color("#ffffff")
    assert Color((255, 255, 255, 255)) + Color((255, 255, 255, 255)) == Color(
        (255, 255, 255, 255)
    )
    assert Color((0, 0, 0, 255)) + Color((50, 0, 0, 255)) == Color((50, 0, 0, 255))
    assert Color((0, 0, 0, 255)) + Color((0, 50, 0, 255)) == Color((0, 50, 0, 255))
    assert Color((0, 0, 0, 255)) + Color((0, 0, 50, 255)) == Color((0, 0, 50, 255))
    assert Color((0, 0, 0, 0)) + Color((0, 0, 0, 50)) == Color((0, 0, 0, 50))


@pytest.mark.unit
def test_color_multiply():
    assert Color("#ffffff") * Color("#ffffff") == Color("#ffffff")
    assert Color((255, 255, 255, 255)) * Color((255, 255, 255, 255)) == Color(
        (255, 255, 255, 255)
    )
    assert Color((0, 0, 0, 255)) * Color((50, 0, 0, 255)) == Color((0, 0, 0, 255))
    assert Color((0, 0, 0, 255)) * Color((0, 50, 0, 255)) == Color((0, 0, 0, 255))
    assert Color((0, 0, 0, 255)) * Color((0, 0, 50, 255)) == Color((0, 0, 0, 255))
    assert Color((0, 0, 0, 0)) * Color((0, 0, 0, 50)) == Color((0, 0, 0, 0))
