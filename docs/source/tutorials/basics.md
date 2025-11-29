# Basic Usage

## Import the library and create a color

```python
from colorisator import Colorisator

# Choose your color
color = Colorisator( (100, 181, 246) ) # rgb255
color = Colorisator( "#6F1" )          # web
color = Colorisator( "#11AA22" )       # hexa
print(color) # Colorisator("#11AA22")
```

## See components of a color

```python
print(color.r, color.g, color.b, color.a)
# 0.06666666666666667 0.6666666666666666 0.13333333333333333 1.0

print(color.h, color.s, color.l)
# 0.35185185185185186 0.8181818181818182 0.36666666666666664
```

## See notations of a color

```python
print(color.get_rgb())       # (0.066667, 0.666667, 0.133333)
print(color.get_rgba())      # (0.066667, 0.666667, 0.133333, 1.0)
print(color.get_rgb255())    # (17, 170, 34)
print(color.get_hex())       # #11AA22
print(color.get_hex_alpha()) # #11AA22FF
print(color.get_hsl())       # (0.35185185185185186, 0.8181818181818182, 0.36666666666666664)
print(color.get_web())       # #1A2
```
