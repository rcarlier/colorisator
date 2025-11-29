# Palette

## Monochromatic

Generate a monochromatic color palette (same hue, varying lightness).

```python
palette = Colorisator.palette_monochromatic(col, output=ColorisatorFormat.HEX)
```

![palette_monochromatic](../_static/palette_monochromatic.png)

## Analogous

Generate an analogous color scheme (3 adjacent colors on the color wheel).

```python
palette = Colorisator.palette_analogous(col, output=ColorisatorFormat.HEX)
```

![palette_analogous](../_static/palette_analogous.png)

## Hue Shifts (integer, array)

Generate a color palette by shifting hue at specified intervals.

```python
palette = Colorisator.palette_hue_shifts(col, shifts=6, output=ColorisatorFormat.HEX)
palette = Colorisator.palette_hue_shifts(col, shifts=[0, .1, -.1, 0.5], output=ColorisatorFormat.HEX)
```

![palette_hue_shifts_int](../_static/palette_hue_shifts_int.png)
![palette_hue_shifts_array](../_static/palette_hue_shifts_array.png)

## Triadic

Generate a triadic color scheme (3 colors evenly spaced on the color wheel).

```python
palette = Colorisator.palette_triadic(col, output=ColorisatorFormat.HEX)
```

![palette_triadic](../_static/palette_triadic.png)
Generate a tetradic color scheme (4 colors evenly spaced on the color wheel).

## Tetradic

```python
palette = Colorisator.palette_tetradic(col, output=ColorisatorFormat.HEX)
```

![palette_tetradic](../_static/palette_tetradic.png)

## Split Complementary

Generate a split-complementary color scheme (base color + 2 colors adjacent to complement).

```python
palette = Colorisator.palette_split_complementary(col, output=ColorisatorFormat.HEX)
```

![palette_split_complementary](../_static/palette_split_complementary.png)

## Material

Generate a Material Design-style color palette with varying lightness.

```python
palette = Colorisator.palette_material(col, output=ColorisatorFormat.HEX)
```

![palette_material](../_static/palette_material.png)
