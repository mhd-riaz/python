# List comprehension
- reduce the amount of time taken to do operations on the list
- Optimization is not done on the loops, but on calling the list methods like `.append`

```py 
# unoptimized function
square = []
for i in range(10):
    if i%2==0:
        square.append(i*i)
print(square)
```

Using list comprehension
```py
square = [i*i for i in range(10); if i%2==0]
print(square)
```