# Operations

```python
color = Colorisator( "#64B5F6")
color = Colorisator( "#6F1")
color = Colorisator( (100, 181, 246) )
# or any color
```

## darken / lighten

```python
c = color.darken(0.3)
c = color.lighten(0.3)
```

![darken](../_static/darken.png)
![lighten](../_static/lighten.png)

## tint / shade

```python
c = color.tint(0.3)
c = color.shade(0.3)
```

![tint](../_static/tint.png)
![shade](../_static/shade.png)

## saturate / desaturate

```python
c = color.saturate(0.3)
c = color.desaturate(0.3)
```

![saturate](../_static/saturate.png)
![desaturate](../_static/desaturate.png)

## adjust_hue

```python
c = color.adjust_hue(30/360)
```

![adjust_hue](../_static/adjust_hue.png)

## grayscale

```python
c = color.grayscale()
```

![grayscale](../_static/grayscale.png)

## complement

```python
c = color.complement()
```

![complement](../_static/complement.png)

## invert

```python
c = color.invert()
```

![invert](../_static/invert.png)
