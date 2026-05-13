def tozalangan_elementlar(ro'yhat, to'plam):
    return [element for element in ro'yhat if element not in to'plam]

ro'yhat = [1, 2, 3, 4, 5]
to'plam = {2, 4}

print(tozalangan_elementlar(ro'yhat, to'plam))
```

```python
def tozalangan_elementlar(ro'yhat, to'plam):
    return [element for element in ro'yhat if element not in to'plam]

ro'yhat = ['a', 'b', 'c', 'd', 'e']
to'plam = {'b', 'd'}

print(tozalangan_elementlar(ro'yhat, to'plam))
