from PIL import Image, ImageDraw, ImageFont
import os
from colorisator import Colorisator, ColorisatorFormat

def generate_palette(title, base_col, palette_colors, filename, width=100, height=None, sep=None, min_width=1200):
    if height is None:
        height = width
    if sep is None:
        sep = width
    elif sep < 50:
        sep = 50

    text_padding = 40
    title_padding = 40
    padding = 20
    margin = 20
    border_width = 1

    if base_col:
        num_squares = 1 + len(palette_colors)
    else:
        num_squares = len(palette_colors)

    if base_col:
        total_width = (num_squares * width) + (2 * padding) + sep
    else:
        total_width = (num_squares * width) + (2 * padding)

    if total_width < min_width:
        total_width = min_width

    total_height = height + text_padding + title_padding + (2 * padding)

    img = Image.new("RGB", (total_width + 2 * margin, total_height + 2 * margin), "white")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("Arial.ttf", 17)
        title_font = ImageFont.truetype("Arial.ttf", 24)
    except OSError:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()

    draw.text((padding + margin, padding + margin), title, fill="black", font=title_font)

    def draw_square(x, y, color):
        draw.rectangle(
            [(x, y), (x + width, y + height)],
            fill=color,
            outline="black",
            width=border_width
        )

        text_bbox = draw.textbbox((0, 0), color, font=font)
        text_w = text_bbox[2] - text_bbox[0]
        text_x = x + (width - text_w) / 2
        draw.text((text_x, y + height + 10), color, fill="black", font=font)

    if base_col:
        draw_square(padding + margin, padding + margin + title_padding, base_col)
        offset_x = margin + padding + width + sep
    else:
        offset_x = margin + padding

    if base_col:
        arrow = "=>"
        bbox = draw.textbbox((0, 0), arrow, font=title_font)
        arrow_w = bbox[2] - bbox[0]
        arrow_h = bbox[3] - bbox[1]

        arrow_x = margin + padding + width + (sep - arrow_w) / 2
        arrow_y = margin + padding + title_padding + (height - arrow_h) / 2

        draw.text((arrow_x, arrow_y), arrow, fill="black", font=title_font)

    for i, color in enumerate(palette_colors):
        x = offset_x + (i * width)
        draw_square(x, padding + margin + title_padding, color)

    draw.rectangle(
        [(margin, margin), (total_width + margin - 1, total_height + margin - 1)],
        outline="black",
        width=border_width
    )

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img.save(filename)
    print(f"Image générée : {filename}")

""" 

"""
col = "#FF8080"
folder = "docs/source/_static/"

# Note: Palettes
palette = Colorisator.palette_monochromatic(col, output=ColorisatorFormat.HEX)
generate_palette("palette_monochromatic()", col, palette, folder + "palette_monochromatic.png")

palette = Colorisator.palette_triadic(col, output=ColorisatorFormat.HEX)
generate_palette("palette_triadic()", col, palette, folder + "palette_triadic.png")

palette = Colorisator.palette_material(col, output=ColorisatorFormat.HEX)
generate_palette("palette_material()", col, palette, folder + "palette_material.png")

palette = Colorisator.palette_analogous(col, output=ColorisatorFormat.HEX)
generate_palette("palette_analogous()", col, palette, folder + "palette_analogous.png")

palette = Colorisator.palette_tetradic(col, output=ColorisatorFormat.HEX)
generate_palette("palette_tetradic()", col, palette, folder + "palette_tetradic.png")

palette = Colorisator.palette_split_complementary(col, output=ColorisatorFormat.HEX)
generate_palette("palette_split_complementary()", col, palette, folder + "palette_split_complementary.png")

palette = Colorisator.palette_hue_shifts(col, shifts=6, output=ColorisatorFormat.HEX)
generate_palette("palette_hue_shifts()", col, palette, folder + "palette_hue_shifts_int.png")

palette = Colorisator.palette_hue_shifts(col, shifts=[0, .1, -.1, 0.5], output=ColorisatorFormat.HEX)
generate_palette("palette_hue_shifts()", col, palette, folder + "palette_hue_shifts_array.png")

gradient = Colorisator.gradient("#000091", "#E1000F", output=ColorisatorFormat.HEX)
generate_palette("gradient( '#000091', '#E1000F' )", None, gradient, folder + "gradient.png")


gradient = Colorisator.gradient_stops(["#000091", "#FFF", (225, 0, 15)], 10, output=ColorisatorFormat.HEX)
generate_palette('gradient_stops( [ "#000091", "#FFF", (225, 0, 15) ], 10 )', None, gradient, folder + "gradient_stops.png")

""" 


"""


# Note: Not a palette, but a single color
generate_palette(
    "complement()",
    col,
    [Colorisator.complement(col, output=ColorisatorFormat.HEX)],
    folder + "complementary.png",
    width=250, height=100, sep=30
)

generate_palette(
    "darken()",
    col,
    [Colorisator.darken(col, .2, output=ColorisatorFormat.HEX)],
    folder + "darken.png",
    width=250, height=100, sep=30
)

generate_palette(
    "lighten()",
    col,
    [Colorisator.lighten(col, .2, output=ColorisatorFormat.HEX)],
    folder + "lighten.png",
    width=250, height=100, sep=50
)

generate_palette(
    "tint()",
    col,
    [Colorisator.tint(col, .2, output=ColorisatorFormat.HEX)],
    folder + "tint.png",
    width=250, height=100, sep=50
)

generate_palette(
    "shade()",
    col,
    [Colorisator.shade(col, .2, output=ColorisatorFormat.HEX)],
    folder + "shade.png",
    width=250, height=100, sep=50
)

generate_palette(
    "saturate()",
    "#64B5F6",
    [Colorisator.saturate("#64B5F6", amount=.2, output=ColorisatorFormat.HEX)],
    folder + "saturate.png",
    width=250, height=100, sep=50
)

generate_palette(
    "desaturate()",
    "#64B5F6",
    [Colorisator.desaturate("#64B5F6", amount=.2, output=ColorisatorFormat.HEX)],
    folder + "desaturate.png",
    width=250, height=100, sep=50
)

generate_palette(
    "grayscale()",
    col,
    [Colorisator.grayscale(col, output=ColorisatorFormat.HEX)],
    folder + "grayscale.png",
    width=250, height=100, sep=50
)

generate_palette(
    "adjust_hue()",
    col,
    [Colorisator.adjust_hue(col, .2, output=ColorisatorFormat.HEX)],
    folder + "adjust_hue.png",
    width=250, height=100, sep=50
)

generate_palette(
    "complement()",
    col,
    [Colorisator.complement(col, output=ColorisatorFormat.HEX)],
    folder + "complement.png",
    width=250, height=100, sep=50
)

generate_palette(
    "invert()",
    col,
    [Colorisator.invert(col, output=ColorisatorFormat.HEX)],
    folder + "invert.png",
    width=250, height=100, sep=30
)



c = Colorisator("#FF0000").invert()
print(c.get_hex())
# Output: #00FFFF

# Using the static call
inv2 = Colorisator.invert("#00FF00", output=ColorisatorFormat.HEX)
print(inv2)
# Output: #00FFFF


base = Colorisator("#000091")
print(base.gradient("#E1000F", output=ColorisatorFormat.HEX))

print(Colorisator.gradient("#000091", "#E1000F", output=ColorisatorFormat.HEX))
