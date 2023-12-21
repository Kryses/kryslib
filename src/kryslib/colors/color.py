from icecream import ic


class HexTypes:
    DECIMAL_ALPHA = "decimal"
    NO_ALPHA = "non-alpha"
    HEX_ALPHA = "non-decimal-alpha"

    def __init__(self, hex: str):
        self.hex = hex
        self.hex_type = self.get_hex_type()

    def get_hex_type(self):
        if "." in self.hex:
            return self.DECIMAL_ALPHA
        elif len(self.hex) == 8:
            return self.HEX_ALPHA
        elif len(self.hex) == 6:
            return self.NO_ALPHA
        else:
            raise ValueError("Invalid hex value")


class Color(object):
    def __init__(self, color: str | tuple):
        """Object for dealing with colors for qtile.

        Args:
            color (str | tuple): Color in hex or rgba format.
        """
        self.color = color
        if isinstance(color, str):
            self.color = hex_to_rgba(color)

        self.red, self.green, self.blue, self.alpha = self.color

    def __repr__(self):
        return f"Color({self.color})"

    def __str__(self):
        return self.as_hex()

    def as_hex(self):
        return rgba_to_hex(self.color)

    def as_rgba(self):
        return self.color

    def as_clamped_rgba(self):
        return (
            clamp(self.red, 0, 255),
            clamp(self.green, 0, 255),
            clamp(self.blue, 0, 255),
            clamp(self.alpha, 0, 255),
        )

    def __eq__(self, other):
        return self.color == other

    def __iter__(self):
        return iter(self.color)

    def __add__(self, other):
        return Color(add_rgba(self.color, other.color))


def rgba_to_hex(rgba):
    # Ensure the RGB values are within the 0-255 range
    r, g, b, a = rgba

    # Return the hex color
    return "#{:02x}{:02x}{:02x}{:02x}".format(r, g, b, a)


def hex_to_rgba(hex):
    hex = hex.lstrip("#")
    hex_type = HexTypes(hex).hex_type

    if hex_type == HexTypes.DECIMAL_ALPHA:
        hex, alpha = hex.split(".")
        alpha = float("." + alpha)
        alpha = int(alpha * 255)
    elif hex_type == HexTypes.HEX_ALPHA:
        alpha = int(hex[6:], 16)
        hex = hex[:6]
    elif hex_type == HexTypes.NO_ALPHA:
        alpha = 255
        hex = hex
    else:
        raise ValueError("Invalid hex value")

    hlen = len(hex)
    rgba = tuple(int(hex[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)) + (
        int(alpha),
    )
    return rgba


def clamp(x, min, max):
    if x < min:
        return min
    if x > max:
        return max
    return x


def add_rgba(color1, color2):
    return Color(
        (
            clamp(color1[0] + color2[0], 0, 255),
            clamp(color1[1] + color2[1], 0, 255),
            clamp(color1[2] + color2[2], 0, 255),
            clamp(color1[3] + color2[3], 0, 255),
        )
    )


def muliply_rgba(color1, color2):
    return Color(
        (
            clamp(color1[0] * color2[0], 0, 255),
            clamp(color1[1] * color2[1], 0, 255),
            clamp(color1[2] * color2[2], 0, 255),
            clamp(color1[3] * color2[3], 0, 255),
        )
    )
