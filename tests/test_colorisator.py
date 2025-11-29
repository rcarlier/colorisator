"""Tests for the Colorisator class."""

from colorisator import Colorisator, ColorisatorFormat


class TestColorisatorInit:
    """Test Colorisator initialization with various formats."""

    def test_init_hex_rgb(self):
        """Test initialization with #RGB format."""
        color = Colorisator("#F00")
        assert color.get_hex() == "#FF0000"

    def test_init_hex_rrggbb(self):
        """Test initialization with #RRGGBB format."""
        color = Colorisator("#FF0000")
        assert color.get_hex() == "#FF0000"

    def test_init_hex_rgba(self):
        """Test initialization with #RGBA format."""
        color = Colorisator("#F00A")
        assert color.get_hex() == "#FF0000"
        assert round(color.a, 2) == 0.67

    def test_init_hex_rrggbbaa(self):
        """Test initialization with #RRGGBBAA format."""
        color = Colorisator("#FF0000AA")
        assert color.get_hex() == "#FF0000"
        assert round(color.a, 2) == 0.67

    def test_init_tuple_normalized(self):
        """Test initialization with normalized RGB tuple (0-1)."""
        color = Colorisator((1.0, 0.0, 0.0))
        assert color.get_hex() == "#FF0000"

    def test_init_tuple_255(self):
        """Test initialization with RGB tuple (0-255)."""
        color = Colorisator((255, 0, 0))
        assert color.get_hex() == "#FF0000"

    def test_init_with_alpha(self):
        """Test initialization with alpha parameter."""
        color = Colorisator("#FF0000", alpha=0.5)
        assert color.a == 0.5


class TestColorisatorGetters:
    """Test color output methods."""

    def test_get_rgb(self):
        """Test get_rgb method."""
        color = Colorisator("#FF0000")
        assert color.get_rgb() == (1.0, 0.0, 0.0)

    def test_get_rgba(self):
        """Test get_rgba method."""
        color = Colorisator("#FF0000", alpha=0.5)
        assert color.get_rgba() == (1.0, 0.0, 0.0, 0.5)

    def test_get_rgb255(self):
        """Test get_rgb255 method."""
        color = Colorisator("#FF0000")
        assert color.get_rgb255() == (255, 0, 0)

    def test_get_hex(self):
        """Test get_hex method."""
        color = Colorisator((255, 128, 64))
        assert color.get_hex() == "#FF8040"

    def test_get_hex_alpha(self):
        """Test get_hex_alpha method."""
        color = Colorisator("#FF0000", alpha=0.5)
        assert color.get_hex_alpha() == "#FF000080"

    def test_get_web_shorthand(self):
        """Test get_web with shorthand notation."""
        color = Colorisator("#FF0000")
        assert color.get_web() == "#F00"

    def test_get_web_full(self):
        """Test get_web with full notation."""
        color = Colorisator("#FF8040")
        assert color.get_web() == "#FF8040"


class TestColorisatorOperations:
    """Test color manipulation operations."""

    def test_lighten(self):
        """Test lighten operation."""
        color = Colorisator("#808080")
        lighter = color.lighten(0.2)
        assert lighter.l > color.l

    def test_darken(self):
        """Test darken operation."""
        color = Colorisator("#808080")
        darker = color.darken(0.2)
        assert darker.l < color.l

    def test_saturate(self):
        """Test saturate operation."""
        color = Colorisator("#808080")
        saturated = color.saturate(0.2)
        assert saturated.s > color.s

    def test_desaturate(self):
        """Test desaturate operation."""
        color = Colorisator("#FF0000")
        desaturated = color.desaturate(0.2)
        assert desaturated.s < color.s

    def test_grayscale(self):
        """Test grayscale conversion."""
        color = Colorisator("#FF0000")
        gray = color.grayscale()
        assert gray.s == 0

    def test_complement(self):
        """Test complement color."""
        color = Colorisator("#FF0000")
        comp = color.complement()
        assert abs(comp.h - ((color.h + 0.5) % 1.0)) < 0.01

    def test_invert(self):
        """Test color inversion."""
        color = Colorisator("#FF0000")
        inverted = color.invert()
        assert inverted.get_hex() == "#00FFFF"


class TestColorisatorComparison:
    """Test color comparison operations."""

    def test_equality_same_color(self):
        """Test equality with same color."""
        color1 = Colorisator("#FF0000")
        color2 = Colorisator("#FF0000")
        assert color1 == color2

    def test_equality_different_formats(self):
        """Test equality with different input formats."""
        color1 = Colorisator("#FF0000")
        color2 = Colorisator((255, 0, 0))
        assert color1 == color2

    def test_inequality(self):
        """Test inequality."""
        color1 = Colorisator("#FF0000")
        color2 = Colorisator("#00FF00")
        assert color1 != color2

    def test_equality_with_non_colorisator(self):
        """Test equality with non-Colorisator object."""
        color = Colorisator("#FF0000")
        assert color != "#FF0000"
        assert not (color == "#FF0000")


class TestColorisatorPalettes:
    """Test palette generation methods."""

    def test_triadic(self):
        """Test triadic palette generation."""
        color = Colorisator("#FF0000")
        palette = color.palette_triadic()
        assert len(palette) == 3
        assert isinstance(palette[0], Colorisator)

    def test_tetradic(self):
        """Test tetradic palette generation."""
        color = Colorisator("#FF0000")
        palette = color.palette_tetradic()
        assert len(palette) == 4

    def test_analogous(self):
        """Test analogous palette generation."""
        color = Colorisator("#FF0000")
        palette = color.palette_analogous()
        assert len(palette) == 3

    def test_monochromatic(self):
        """Test monochromatic palette generation."""
        color = Colorisator("#FF0000")
        palette = color.palette_monochromatic(n=5)
        assert len(palette) == 5

    def test_material_palette(self):
        """Test material palette generation."""
        color = Colorisator("#FF0000")
        palette = color.palette_material(n=5)
        assert len(palette) == 5


class TestColorisatorGradient:
    """Test gradient generation methods."""

    def test_gradient_basic(self):
        """Test basic gradient generation."""
        start = Colorisator("#FF0000")
        end = Colorisator("#0000FF")
        gradient = start.gradient(end, steps=5)
        assert len(gradient) == 5
        assert gradient[0] == start
        assert gradient[-1] == end

    def test_gradient_with_output_format(self):
        """Test gradient with output format."""
        gradient = Colorisator.gradient("#FF0000", "#0000FF", steps=5, output=ColorisatorFormat.HEX)
        assert len(gradient) == 5
        assert isinstance(gradient[0], str)
        assert gradient[0] == "#FF0000"

    def test_gradient_stops(self):
        """Test multi-stop gradient."""
        colors = ["#FF0000", "#00FF00", "#0000FF"]
        gradient = Colorisator.gradient_stops(colors, steps=7)
        assert len(gradient) == 7


class TestColorisatorOutputFormats:
    """Test different output formats."""

    def test_output_format_hex(self):
        """Test HEX output format."""
        color = Colorisator("#FF0000")
        result = color.lighten(0.1, output=ColorisatorFormat.HEX)
        assert isinstance(result, str)
        assert result.startswith("#")

    def test_output_format_rgb(self):
        """Test RGB output format."""
        color = Colorisator("#FF0000")
        result = color.lighten(0.1, output=ColorisatorFormat.RGB)
        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_output_format_rgb255(self):
        """Test RGB255 output format."""
        color = Colorisator("#FF0000")
        result = color.lighten(0.1, output=ColorisatorFormat.RGB255)
        assert isinstance(result, tuple)
        assert all(isinstance(x, int) for x in result)


class TestColorisatorExport:
    """Test export to other formats."""

    def test_to_unity(self):
        """Test Unity export."""
        color = Colorisator("#FF0000")
        unity_code = color.to_unity()
        assert "private Color colour" in unity_code
        assert "new Color" in unity_code

    def test_to_processing(self):
        """Test Processing export."""
        color = Colorisator("#FF0000")
        processing_code = color.to_processing()
        assert "color colour" in processing_code
        assert "color(255, 0, 0)" in processing_code
