# PYTHON
## Lecturer : Chitra G

### Why Python? 
out of popularity, robust libraries for Ai & ML.

**Key notes**:
- dynamically typed language

- has no restriction with the int

- floats are a bit cumbersome, as `0.3` will be interpreted as `0.3000000000001` due to memory allocation

- multi variable initialization and assignment
```python
a, b, c = 1, 2, 3

# op: a = 1; b = 2; c = 3;
```

- `help(print)` : help provides info on built-in function

- `dir(__builtin__)` : show list of available builtin functions

- `import` : used to consume something written outside of the file/function
```python
# example for import
import math # one time per file
math.e
# op: 2.7182
```

- to see whats inside the math do `dir(math)` after importing

- to see definition of each method or variable inside math class, use `help(math.factorial)`

- how to find size/amount of memory allocated 
`getsizeof` - module that returns the size of an object in bytes.
`getrefcount` - The reference count indicates the number of references points to the object in memory. This method is useful for debugging memory management issues and understanding object lifespan in Python's memory.
```py
import sys
a=10
sys.getsizeof(a) # give size
# 28

sys.getrefcount(a) # number of references made
# 4294967295

b=a
sys.getrefcount(b)

```