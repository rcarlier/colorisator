from colorisator import Colorisator, ColorisatorFormat


start = Colorisator("#FF0000")
end = Colorisator("#0000FF")
print(Colorisator.gradient("#FF0000", "#0000FF", 5))
print(Colorisator.gradient(start, end, 5, ColorisatorFormat.HEX))
print(start.gradient(end, 5, ColorisatorFormat.HEX))
print(Colorisator.gradient("#FF0000", "#0000FF", 5, ColorisatorFormat.HEX))

print("\n")

start = Colorisator("#000091")
middle = Colorisator("#FFF")
end = Colorisator("#E1000F")

print(Colorisator.gradient_stops([start, middle, end], steps=5, output=ColorisatorFormat.HEX))
print(start.gradient_stops([middle, end], steps=5, output=ColorisatorFormat.HEX))
print(start.gradient_stops([middle, end], steps=6, output=ColorisatorFormat.HEX))

print("\n")

for steps in range(3, 11, 2):
    print(start.gradient_stops([middle, end], steps=steps, output=ColorisatorFormat.HEX))


print(Colorisator.gradient("#00009100", "#E1000FFF", 5, output=ColorisatorFormat.HEXALPHA))
print(Colorisator.gradient("#00009100", "#E1000FFF", 5, output=ColorisatorFormat.RGBA))

print(Colorisator.gradient_stops(["#00009100", "#E1000FFF"], 5, output=ColorisatorFormat.HEXALPHA))
print(Colorisator.gradient_stops(["#00009100", "#E1000FFF"], 5, output=ColorisatorFormat.RGBA))
