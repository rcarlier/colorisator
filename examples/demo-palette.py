
from colorisator import Colorisator, ColorisatorFormat

col = "#3543ca"
base = Colorisator(col)

print("\nSTATIC")
print("Monochromatic       :", Colorisator.monochromatic(col, n=3, output=ColorisatorFormat.HEX))
print("Monochromatic Δ .3  :", Colorisator.monochromatic(col, n=3, max_delta=.3, output=ColorisatorFormat.HEX))
print("Analogous           :", Colorisator.analogous(col, output=ColorisatorFormat.HEX))
print("Triadic             :", Colorisator.triadic(col, output=ColorisatorFormat.HEX))
print("Tetradic            :", Colorisator.tetradic(col, output=ColorisatorFormat.HEX))
print("Split-complementary :", Colorisator.split_complementary(col, output=ColorisatorFormat.HEX))
print("Custom 6            :", Colorisator.palette_hue_shifts(col, shifts=6, output=ColorisatorFormat.HEX))
print("Custom []           :", Colorisator.palette_hue_shifts(col, shifts=[0, .1, -.1, 0.5], output=ColorisatorFormat.HEX))
print("Material            :", Colorisator.material_palette("#3543ca", n=9, max_delta=0.4, output=ColorisatorFormat.HEX))
print("Material n=9        :", Colorisator.material_palette("#3543ca", n=9, output=ColorisatorFormat.HEX))
print("Material n=9  Δ=0.4 :", Colorisator.material_palette("#3543ca", n=9, max_delta=0.4, output=ColorisatorFormat.HEX))

print("\nINSTANCE")
print("Monochromatic       :", base.monochromatic(n=3, output=ColorisatorFormat.HEX))
print("Monochromatic Δ=.3  :", base.monochromatic(n=3, max_delta=.3, output=ColorisatorFormat.HEX))
print("Analogous           :", base.analogous(output=ColorisatorFormat.HEX))
print("Triadic             :", base.triadic(output=ColorisatorFormat.HEX))
print("Tetradic            :", base.tetradic(output=ColorisatorFormat.HEX))
print("Split-complementary :", base.split_complementary(output=ColorisatorFormat.HEX))
print("Custom 6            :", base.palette_hue_shifts(shifts=6, output=ColorisatorFormat.HEX))
print("Custom []           :", base.palette_hue_shifts(shifts=[0, .1, -.1, 0.5], output=ColorisatorFormat.HEX))
print("Material            :", base.material_palette(output=ColorisatorFormat.HEX))
print("Material n=9        :", base.material_palette(n=9, output=ColorisatorFormat.HEX))
print("Material n=9  Δ=0.4 :", base.material_palette(n=9, max_delta=0.4, output=ColorisatorFormat.HEX))
