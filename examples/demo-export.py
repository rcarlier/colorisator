from colorisator import Colorisator, ColorisatorFormat


print("\nSpecial Use Case : export to UNITY")

c = Colorisator("#FFE8E0")
print(c.to_unity())
print(c.gradient("#FFDDB3", 3, output=ColorisatorFormat.UNITY))

print("\nSpecial Use Case : export to PROCESSING")

print(c.to_processing())
print(c.gradient("#FFDDB3", 3, output=ColorisatorFormat.PROCESSING))
