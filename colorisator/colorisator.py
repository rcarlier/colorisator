import colorsys
from enum import Enum


class ColorisatorFormat(Enum):
    RGB = "rgb"
    RGBA = "rgba"
    RGB255 = "rgb255"
    HEX = "hex"
    HEXALPHA = "hexalpha"
    HSL = "hsl"
    WEB = "web"
    PROCESSING = "processing"
    UNITY = "unity"


class Colorisator:
    def __init__(self, value, alpha=1.0):
        """Initialize a Colorisator object from various color formats.

        Args:
            value: Color value as hex string (#RGB, #RRGGBB, #RGBA, #RRGGBBAA),
                   tuple/list of RGB values (0-1 or 0-255), or another Colorisator instance
            alpha: Opacity value between 0.0 (transparent) and 1.0 (opaque). Defaults to 1.0.
        """
        self.r, self.g, self.b, self.a = self._parse_input(value, alpha)
        self.h, self.l, self.s = colorsys.rgb_to_hls(self.r, self.g, self.b)

    def __repr__(self):
        return f'Colorisator("{self.get_hex()}")'

    def __eq__(self, other):
        if not isinstance(other, Colorisator):
            return False
        return (
            round(self.r, 4) == round(other.r, 4) and
            round(self.g, 4) == round(other.g, 4) and
            round(self.b, 4) == round(other.b, 4) and
            round(self.a, 4) == round(other.a, 4)
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def _from_any(value):
        if isinstance(value, Colorisator):
            return value
        return Colorisator(value)

    def _parse_input(self, value, alpha):
        if isinstance(value, str):
            v = value.strip().lstrip("#")
            if len(v) == 3:  # #RGB
                r = int(v[0]*2, 16) / 255
                g = int(v[1]*2, 16) / 255
                b = int(v[2]*2, 16) / 255
                return r, g, b, alpha
            elif len(v) == 4:  # #RGBA
                r = int(v[0]*2, 16) / 255
                g = int(v[1]*2, 16) / 255
                b = int(v[2]*2, 16) / 255
                a = int(v[3]*2, 16) / 255
                return r, g, b, a
            elif len(v) == 6:  # #RRGGBB
                r = int(v[0:2], 16) / 255
                g = int(v[2:4], 16) / 255
                b = int(v[4:6], 16) / 255
                return r, g, b, alpha
            elif len(v) == 8:  # #RRGGBBAA
                r = int(v[0:2], 16) / 255
                g = int(v[2:4], 16) / 255
                b = int(v[4:6], 16) / 255
                a = int(v[6:8], 16) / 255
                return r, g, b, a

        if isinstance(value, (list, tuple)):
            if len(value) == 3:
                if max(value) > 1:
                    r, g, b = (v / 255 for v in value)
                    return r, g, b, alpha
                return (*value, alpha)
            if len(value) == 4:
                r, g, b, a = value
                if max(value) > 1:
                    return r/255, g/255, b/255, a/255
                return r, g, b, a

        raise ValueError("Unsupported format")

    def _update_from_hls(self, h, l, s):
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        obj = Colorisator((r, g, b, self.a))
        obj.h, obj.l, obj.s = h, l, s
        return obj

    @staticmethod
    def _format_output(colors, output: ColorisatorFormat = None):
        single = False
        if not isinstance(colors, (list, tuple)):
            colors = [colors]
            single = True

        if isinstance(output, str):
            output = ColorisatorFormat(output.lower())

        if output == ColorisatorFormat.HEX:
            result = [c.get_hex() for c in colors]
        elif output == ColorisatorFormat.HEXALPHA:
            result = [c.get_hex_alpha() for c in colors]
        elif output == ColorisatorFormat.WEB:
            result = [c.get_web() for c in colors]
        elif output == ColorisatorFormat.RGB:
            result = [c.get_rgb() for c in colors]
        elif output == ColorisatorFormat.RGBA:
            result = [c.get_rgba() for c in colors]
        elif output == ColorisatorFormat.RGB255:
            result = [c.get_rgb255() for c in colors]
        elif output == ColorisatorFormat.HSL:
            result = [c.get_hsl() for c in colors]

        elif output == ColorisatorFormat.UNITY:
            if single:
                return colors[0].to_unity()
            result = [c._unity_value() for c in colors]
            return f"private List<Color> palette = new() {{ " + ", ".join(result) + " };"

        elif output == ColorisatorFormat.PROCESSING:
            if single:
                return colors[0].to_processing()
            result = [c._processing_value() for c in colors]
            return f"color[] palette = {{ " + ", ".join(result) + " };"

        else:
            result = colors

        if single:
            return result[0]
        return result

    def _lerp(self_or_start, other, t, output=None):
        if isinstance(self_or_start, Colorisator):
            start = self_or_start
        else:
            start = Colorisator(self_or_start)
        end = Colorisator._from_any(other)

        r = start.r + (end.r - start.r) * t
        g = start.g + (end.g - start.g) * t
        b = start.b + (end.b - start.b) * t
        a = start.a + (end.a - start.a) * t
        new_color = Colorisator((r, g, b, a))
        return Colorisator._format_output(new_color, output)

    def _unity_value(self):
        r, g, b = self.get_rgb()
        return f"new Color({r:.3f}f, {g:.3f}f, {b:.3f}f)"

    def _processing_value(self):
        r, g, b = self.get_rgb255()
        return f"color({r}, {g}, {b})"

    def to_unity(self):
        """Export color as Unity C# Color declaration.

        Returns:
            String containing Unity C# code to declare this color
        """
        return f"private Color colour = {self._unity_value()};"

    def to_processing(self):
        """Export color as Processing color() declaration.

        Returns:
            String containing Processing code to declare this color
        """
        return f"color colour = {self._processing_value()};"

    def get_rgb(self):
        """Get RGB color values normalized between 0.0 and 1.0.

        Returns:
            Tuple of (red, green, blue) as floats between 0.0 and 1.0
        """
        return tuple(round(c, 6) for c in (self.r, self.g, self.b))

    def get_rgba(self):
        """Get RGBA color values normalized between 0.0 and 1.0.

        Returns:
            Tuple of (red, green, blue, alpha) as floats between 0.0 and 1.0
        """
        return tuple(round(c, 6) for c in (self.r, self.g, self.b, self.a))

    def get_rgb255(self):
        """Get RGB color values as integers between 0 and 255.

        Returns:
            Tuple of (red, green, blue) as integers between 0 and 255
        """
        return tuple(int(round(c * 255)) for c in (self.r, self.g, self.b))

    def get_hex(self):
        """Get color as hexadecimal string (without alpha).

        Returns:
            Hex color string in format #RRGGBB
        """
        r, g, b = self.get_rgb255()
        a = int(round(self.a * 255))
        return f"#{r:02X}{g:02X}{b:02X}"

    def get_hex_alpha(self):
        """Get color as hexadecimal string including alpha channel.

        Returns:
            Hex color string in format #RRGGBBAA
        """
        r, g, b = self.get_rgb255()
        a = int(round(self.a * 255))
        return f"#{r:02X}{g:02X}{b:02X}{a:02X}"

    def get_web(self):
        """Get color as web-optimized hex string (shorthand when possible).

        Returns:
            Hex color string in format #RGB or #RRGGBB (shortened when possible)
        """
        hexa = self.get_hex().lstrip("#").upper()
        if len(hexa) == 6 and hexa[0] == hexa[1] and hexa[2] == hexa[3] and hexa[4] == hexa[5]:
            return f"#{hexa[0]}{hexa[2]}{hexa[4]}"
        return f"#{hexa}"

    def get_hsl(self):
        """Get color as HSL (Hue, Saturation, Lightness) values.

        Returns:
            Tuple of (hue, saturation, lightness) as floats between 0.0 and 1.0
        """
        return (self.h, self.s, self.l)

    """ 
    
    """

    def lighten(self_or_color, amount=0.1, output=None):
        """Increase the lightness of a color.

        .. image:: _static/lighten.png
            :width: 600
            :alt: Lighten

        Args:
            self_or_color: Color to lighten (Colorisator instance or any valid color format)
            amount: Amount to lighten (0.0 to 1.0). Defaults to 0.1.
            output: Output format (ColorisatorFormat or string). Defaults to None (returns Colorisator).

        Returns:
            Lightened color in the specified output format
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)

        h, l, s = color.h, color.l, color.s
        l = min(1, l + amount)
        new_color = color._update_from_hls(h, l, s)
        return Colorisator._format_output(new_color, output)

    def darken(self_or_color, amount=0.1, output=None):
        """Decrease the lightness of a color.

        .. image:: _static/darken.png
            :width: 600
            :alt: Darken

        Args:
            self_or_color: Color to darken (Colorisator instance or any valid color format)
            amount: Amount to darken (0.0 to 1.0). Defaults to 0.1.
            output: Output format (ColorisatorFormat or string). Defaults to None (returns Colorisator).

        Returns:
            Darkened color in the specified output format
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)

        h, l, s = color.h, color.l, color.s
        l = max(0, l - amount)
        new_color = color._update_from_hls(h, l, s)
        return Colorisator._format_output(new_color, output)

    def tint(self_or_color, amount=0.1, output=None):
        """Mix color with white to create a tint.

        .. image:: _static/tint.png
            :width: 600
            :alt: Tint

        Args:
            amount: Amount of white to mix (0.0 to 1.0). Defaults to 0.1.

        Returns:
            New Colorisator instance with the tinted color
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)

        r = color.r + (1 - color.r) * amount
        g = color.g + (1 - color.g) * amount
        b = color.b + (1 - color.b) * amount
        new_color = Colorisator((r, g, b))
        return Colorisator._format_output(new_color, output)


    def shade(self_or_color, amount=0.1, output=None):
        """Mix color with black to create a shade.

        .. image:: _static/shade.png
            :width: 600
            :alt: Shade

        Args:
            amount: Amount of black to mix (0.0 to 1.0). Defaults to 0.1.

        Returns:
            New Colorisator instance with the shaded color
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)

        r = color.r * (1 - amount)
        g = color.g * (1 - amount)
        b = color.b * (1 - amount)
        new_color = Colorisator((r, g, b))
        return Colorisator._format_output(new_color, output)

    def saturate(self_or_color, amount=0.1, output=None):
        """Increase the saturation of a color.

        .. image:: _static/saturate.png
            :width: 600
            :alt: Saturate

        Args:
            self_or_color: Color to saturate (Colorisator instance or any valid color format)
            amount: Amount to increase saturation (0.0 to 1.0). Defaults to 0.1.
            output: Output format (ColorisatorFormat or string). Defaults to None (returns Colorisator).

        Returns:
            More saturated color in the specified output format
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)

        h, l, s = color.h, color.l, color.s
        s = min(1, s + amount)
        new_color = color._update_from_hls(h, l, s)
        return Colorisator._format_output(new_color, output)

    def desaturate(self_or_color, amount=0.1, output=None):
        """Decrease the saturation of a color.

        .. image:: _static/desaturate.png
            :width: 600
            :alt: Desaturate

        Args:
            self_or_color: Color to desaturate (Colorisator instance or any valid color format)
            amount: Amount to decrease saturation (0.0 to 1.0). Defaults to 0.1.
            output: Output format (ColorisatorFormat or string). Defaults to None (returns Colorisator).

        Returns:
            Less saturated color in the specified output format
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)

        h, l, s = color.h, color.l, color.s
        s = max(0, s - amount)
        new_color = color._update_from_hls(h, l, s)
        return Colorisator._format_output(new_color, output)

    def adjust_hue(self_or_color, amount, output=None):
        """Shift the hue of a color on the color wheel.

        .. image:: _static/adjust_hue.png
            :width: 600
            :alt: Adjust hue

        Args:
            self_or_color: Color to adjust (Colorisator instance or any valid color format)
            amount: Amount to shift hue (0.0 to 1.0, wraps around)
            output: Output format (ColorisatorFormat or string). Defaults to None (returns Colorisator).

        Returns:
            Color with adjusted hue in the specified output format
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)

        h, l, s = color.h, color.l, color.s
        h = (h + amount) % 1.0
        new_color = color._update_from_hls(h, l, s)
        return Colorisator._format_output(new_color, output)

    def grayscale(self_or_color, output=None):
        """Convert a color to grayscale by removing all saturation.

        .. image:: _static/grayscale.png
            :width: 600
            :alt: Grayscale

        Args:
            self_or_color: Color to convert (Colorisator instance or any valid color format)
            output: Output format (ColorisatorFormat or string). Defaults to None (returns Colorisator).

        Returns:
            Grayscale version of the color in the specified output format
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)

        h, l, s = color.h, color.l, color.s
        s = 0
        new_color = color._update_from_hls(h, l, s)
        return Colorisator._format_output(new_color, output)

    def complement(self_or_color, output=None):
        """Get the complementary color (opposite on the color wheel).

        .. image:: _static/complement.png
            :width: 600
            :alt: Complement

        Args:
            self_or_color: Color to find complement for (Colorisator instance or any valid color format)
            output: Output format (ColorisatorFormat or string). Defaults to None (returns Colorisator).

        Returns:
            Complementary color in the specified output format
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)
        new_color = color.adjust_hue(0.5)
        return Colorisator._format_output(new_color, output)

    def invert(self_or_color, output=None):
        """Invert a color by subtracting each RGB component from 1.0.

        .. image:: _static/invert.png
            :width: 600
            :alt: Invert

        Args:
            self_or_color: Color to invert (Colorisator instance or any valid color format)
            output: Output format (ColorisatorFormat or string). Defaults to None (returns Colorisator).

        Returns:
            Inverted color in the specified output format

        Example:
            .. code-block:: python

                c = Colorisator("#FF0000").invert()
                print(c.get_hex())
                # Output: #00FFFF

                # Using the static call
                inv2 = Colorisator.invert("#00FF00", output=ColorisatorFormat.HEX)
                print(inv2)
                # Output: #00FFFF
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)
        new_color = Colorisator((1 - color.r, 1 - color.g, 1 - color.b, color.a))
        return Colorisator._format_output(new_color, output)

    def palette_hue_shifts(self_or_color, shifts, output=None):
        """Generate a color palette by shifting hue at specified intervals.

        .. image:: _static/palette_hue_shifts_int.png
            :width: 600
            :alt: Triadic palette (from int)

        .. image:: _static/palette_hue_shifts_array.png
            :width: 600
            :alt: Triadic palette (from array)

        Args:
            self_or_color: Base color (Colorisator instance or any valid color format)
            shifts: Number of colors to generate (int) or list of hue shift amounts (list of floats)
            output: Output format (ColorisatorFormat or string). Defaults to None (returns list of Colorisator).

        Returns:
            List of colors with shifted hues in the specified output format
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)
        h, l, s = color.h, color.l, color.s

        if isinstance(shifts, int):
            n = shifts
            shifts = [(i / n) for i in range(n)]

        colors = [color._update_from_hls((h + shift) % 1.0, l, s) for shift in shifts]
        return Colorisator._format_output(colors, output)

    def palette_triadic(self_or_color, output=None):
        """Generate a triadic color scheme (3 colors evenly spaced on the color wheel).

        .. image:: _static/palette_triadic.png
            :width: 600
            :alt: Triadic palette

        Args:
            self_or_color: Base color (Colorisator instance or any valid color format)
            output: Output format (ColorisatorFormat or string). Defaults to None (returns list of Colorisator).

        Returns:
            List of 3 colors forming a triadic scheme
        """
        return Colorisator.palette_hue_shifts(self_or_color, 3, output)

    def palette_tetradic(self_or_color, output=None):
        """Generate a tetradic color scheme (4 colors evenly spaced on the color wheel).

        .. image:: _static/palette_tetradic.png
            :width: 600
            :alt: Tetradic palette

        Args:
            self_or_color: Base color (Colorisator instance or any valid color format)
            output: Output format (ColorisatorFormat or string). Defaults to None (returns list of Colorisator).

        Returns:
            List of 4 colors forming a tetradic scheme
        """
        return Colorisator.palette_hue_shifts(self_or_color, 4, output)

    def palette_split_complementary(self_or_color, output=None):
        """Generate a split-complementary color scheme (base color + 2 colors adjacent to complement).

        .. image:: _static/palette_split_complementary.png
            :width: 600
            :alt: Split-complementary palette

        Args:
            self_or_color: Base color (Colorisator instance or any valid color format)
            output: Output format (ColorisatorFormat or string). Defaults to None (returns list of Colorisator).

        Returns:
            List of 3 colors forming a split-complementary scheme
        """
        return Colorisator.palette_hue_shifts(self_or_color, [0, 5/12, 0.5], output)

    def palette_analogous(self_or_color, output=None):
        """Generate an analogous color scheme (3 adjacent colors on the color wheel).

        .. image:: _static/palette_analogous.png
            :width: 600
            :alt: Split-complementary palette

        Args:
            self_or_color: Base color (Colorisator instance or any valid color format)
            output: Output format (ColorisatorFormat or string). Defaults to None (returns list of Colorisator).

        Returns:
            List of 3 adjacent colors forming an analogous scheme
        """
        return Colorisator.palette_hue_shifts(self_or_color, [0, 1/12, 2/12], output)

    def palette_monochromatic(self_or_color, n=3, max_delta=0.1, output=None):
        """Generate a monochromatic color palette (same hue, varying lightness).

        .. image:: _static/palette_monochromatic.png
            :width: 600
            :alt: Monochromatic palette

        Args:
            self_or_color: Base color (Colorisator instance or any valid color format)
            n: Number of colors to generate. Defaults to 3.
            max_delta: Maximum lightness variation from base color. Defaults to 0.1.
            output: Output format (ColorisatorFormat or string). Defaults to None (returns list of Colorisator).

        Returns:
            List of colors with same hue but different lightness values
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)
        h, l, s = color.h, color.l, color.s
        if n == 1:
            shades = [l]
        else:
            step = 2 * max_delta / (n - 1)
            shades = [min(1, max(0, l - max_delta + i * step)) for i in range(n)]
        colors = [color._update_from_hls(h, new_l, s) for new_l in shades]
        return Colorisator._format_output(colors, output)

    def palette_material(self_or_color, n=5, max_delta=0.2, output=None):
        """Generate a Material Design-style color palette with varying lightness.

        .. image:: _static/palette_material.png
            :width: 600
            :alt: Material palette

        Args:
            self_or_color: Base color (Colorisator instance or any valid color format)
            n: Number of color shades to generate. Defaults to 5.
            max_delta: Maximum lightness variation from base color. Defaults to 0.2.
            output: Output format (ColorisatorFormat or string). Defaults to None (returns list of Colorisator).

        Returns:
            List of colors ranging from darker to lighter shades
        """
        if isinstance(self_or_color, Colorisator):
            color = self_or_color
        else:
            color = Colorisator(self_or_color)
        h, l, s = color.h, color.l, color.s
        step_size = (2 * max_delta) / (n - 1) if n > 1 else 0
        colors = []
        for i in range(n):
            new_l = min(1, max(0, l - max_delta + i * step_size))
            colors.append(color._update_from_hls(h, new_l, s))
        return Colorisator._format_output(colors, output)

    def gradient(self_or_start, end=None, steps=10, output=None):
        """Generate a smooth color gradient between two colors.

        .. image:: _static/gradient.png
            :width: 600
            :alt: Gradient

        Args:
            self_or_start: Starting color (Colorisator instance or any valid color format)
            end: Ending color (Colorisator instance or any valid color format). Defaults to None.
            steps: Number of color steps in the gradient. Defaults to 5.
            output: Output format (ColorisatorFormat or string). Defaults to None (returns list of Colorisator).

        Raises:
            ValueError: If end color is not provided

        Returns:
            List of colors forming a smooth gradient from start to end
        """
        if isinstance(self_or_start, Colorisator) and end is not None:
            start = self_or_start
            end = Colorisator._from_any(end)
        elif not isinstance(self_or_start, Colorisator) and end is not None:
            start = Colorisator._from_any(self_or_start)
            end = Colorisator._from_any(end)
        else:
            raise ValueError("End must be provided for the static call or instance")

        grad = [start._lerp(end, i/(steps-1)) for i in range(steps)]
        return Colorisator._format_output(grad, output)

    def gradient_stops(self_or_start, stops=None, steps=10, output=None):
        """Generate a multi-stop gradient passing through multiple colors.

        .. image:: _static/gradient_stops.png
            :width: 600
            :alt: Gradient stops

        Args:
            self_or_start: Starting color or list of all colors (Colorisator instances or any valid color formats)
            stops: List of intermediate/ending colors. Defaults to None.
            steps: Total number of color steps in the gradient. Defaults to 5.
            output: Output format (ColorisatorFormat or string). Defaults to None (returns list of Colorisator).

        Raises:
            ValueError: If stops is None when calling on an instance, or if less than 2 colors provided

        Returns:
            List of colors forming a smooth gradient through all color stops
        """
        if isinstance(self_or_start, Colorisator):
            if stops is None:
                raise ValueError("You must provide a list of stops when calling on an instance")
            colors = [self_or_start] + [Colorisator._from_any(c) for c in stops]
        else:
            colors = [Colorisator._from_any(c) for c in self_or_start]

        n = len(colors)
        if n < 2:
            raise ValueError("At least two colors are needed for gradient_stops")

        segment_steps = [int(round((steps - 1) * (i + 1) / (n - 1))) - int(round((steps - 1) * i / (n - 1))) for i in range(n - 1)]

        grad = []
        for i in range(n - 1):
            start = colors[i]
            end = colors[i + 1]
            segment = Colorisator.gradient(start, end, segment_steps[i] + 1, output=None)
            if i < n - 2:
                segment = segment[:-1]
            grad.extend(segment)

        return Colorisator._format_output(grad, output)
