# Choose your flavor

Every method can be used in two ways:

## Create instance and use methods

```python
base = Colorisator("#000091")
print(base.gradient("#E1000F", output=ColorisatorFormat.HEX))
```

## Use static methods

```python
print(Colorisator.gradient("#000091", "#E1000F", output=ColorisatorFormat.HEX))
```

## Same result

![gradient](../_static/gradient.png)
