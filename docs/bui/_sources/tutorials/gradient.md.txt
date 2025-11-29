# Gradient

## Linear gradient

```python
gradient = Colorisator.gradient(
    "#000091", "#E1000F",
    output=ColorisatorFormat.HEX
    )
```

![gradient](../_static/gradient.png)

## Linear Gradient with stops

```python
gradient = Colorisator.gradient_stops(
    ["#000091", "#FFF", (225, 0, 15)],
    10,
    output=ColorisatorFormat.HEX
    )
```

![gradient_stops](../_static/gradient_stops.png)
