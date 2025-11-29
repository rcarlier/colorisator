
from colorisator import Colorisator, ColorisatorFormat

col = "#3543ca"
base = Colorisator(col)

print("\nSTATIC")
print("Monochromatic       :", Colorisator.palette_monochromatic(col, output=ColorisatorFormat.HEX))
print("Monochromatic n=3   :", Colorisator.palette_monochromatic(col, n=3, output=ColorisatorFormat.HEX))
print("Monochromatic Δ .3  :", Colorisator.palette_monochromatic(col, max_delta=.3, output=ColorisatorFormat.HEX))



print("Analogous           :", Colorisator.palette_analogous(col, output=ColorisatorFormat.HEX))
print("Triadic             :", Colorisator.palette_triadic(col, output=ColorisatorFormat.HEX))
print("Tetradic            :", Colorisator.palette_tetradic(col, output=ColorisatorFormat.HEX))
print("Split-complementary :", Colorisator.palette_split_complementary(col, output=ColorisatorFormat.HEX))
print("Custom 6            :", Colorisator.palette_hue_shifts(col, shifts=6, output=ColorisatorFormat.HEX))
print("Custom []           :", Colorisator.palette_hue_shifts(col, shifts=[0, .1, -.1, 0.5], output=ColorisatorFormat.HEX))
print("Material            :", Colorisator.palette_material("#3543ca", n=9, max_delta=0.4, output=ColorisatorFormat.HEX))
print("Material n=9        :", Colorisator.palette_material("#3543ca", n=9, output=ColorisatorFormat.HEX))
print("Material n=9  Δ=0.4 :", Colorisator.palette_material("#3543ca", n=9, max_delta=0.4, output=ColorisatorFormat.HEX))

print("\nINSTANCE")
print("Monochromatic       :", base.palette_monochromatic(n=3, output=ColorisatorFormat.HEX))
print("Monochromatic n=3   :", base.palette_monochromatic(n=3, output=ColorisatorFormat.HEX))
print("Monochromatic Δ=.3  :", base.palette_monochromatic(max_delta=.3, output=ColorisatorFormat.HEX))
print("Analogous           :", base.palette_analogous(output=ColorisatorFormat.HEX))
print("Triadic             :", base.palette_triadic(output=ColorisatorFormat.HEX))
print("Tetradic            :", base.palette_tetradic(output=ColorisatorFormat.HEX))
print("Split-complementary :", base.palette_split_complementary(output=ColorisatorFormat.HEX))
print("Custom 6            :", base.palette_hue_shifts(shifts=6, output=ColorisatorFormat.HEX))
print("Custom []           :", base.palette_hue_shifts(shifts=[0, .1, -.1, 0.5], output=ColorisatorFormat.HEX))
print("Material            :", base.palette_material(output=ColorisatorFormat.HEX))
print("Material n=9        :", base.palette_material(n=9, output=ColorisatorFormat.HEX))
print("Material n=9  Δ=0.4 :", base.palette_material(n=9, max_delta=0.4, output=ColorisatorFormat.HEX))

