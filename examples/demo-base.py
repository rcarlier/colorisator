from colorisator import Colorisator


base = "#11AA22"

color = Colorisator(base)
print(color)
print(color.r, color.g, color.b, color.a)
print(color.h, color.s, color.l)

print("\nNOTATIONS")
print("rgb       :", color.get_rgb())
print("rgba      :", color.get_rgba())
print("rgb255    :", color.get_rgb255())
print("hexa      :", color.get_hex())
print("hexa A    :", color.get_hex_alpha())
print("hsl       :", color.get_hsl())
print("web       :", color.get_web())

print("\nOPERATIONS")
amount = 0.3

print(f"darken     {amount} :", color.darken(amount).get_hex())
print(f"lighten    {amount} :", color.lighten(amount).get_hex())

print(f"tint       {amount} :", color.tint(amount).get_hex())
print(f"shade      {amount} :", color.shade(amount).get_hex())

print(f"saturate   {amount} :", color.saturate(amount).get_hex())
print(f"desaturate {amount} :", color.desaturate(amount).get_hex())

print("adjust_hue +30 :", color.adjust_hue(30/360).get_hex())
print("adjust_hue -30 :", color.adjust_hue(-30/360).get_hex())

print("grayscale      :", color.grayscale().get_hex())
print("complement     :", color.complement().get_hex())
print("invert         :", color.invert().get_hex())


print("\nCOMPARISON")


if Colorisator("#000091") == Colorisator((0, 0, 145)):
    print("The colors are identical")
else:
    print("Hmm?")


if Colorisator("#E1000F") != Colorisator((255, 255, 255)):
    print("The colors are different")
else:
    print("Humm?")


if Colorisator("#E1000F") == "#E1000F":
    print("Humm?")
else:
    print("They are different !!!")
