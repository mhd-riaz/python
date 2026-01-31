# Tuple

- Tuple items are ordered, unchangeable, and allow duplicate value
- use the parathesis brackets
- are immutable in nature, cannot grow or shrink

Syntax:
```py
t = (1, 2, 3) 
type(t) # <classs 'tuple'>

# NOTE
t =(1)
type(t) # <class 'int'>, this is not a tuple as there is no comma, this is treated as bodmas rule

# How to define for single value?
t = (1,) 
type(t) # <class 'tuple'>
```

## Operations that can be done with tuple
- inbuilt functions like: `sum(t)`, `min`, `max`
- inbuilt methods: `count`, `index`
- can do slicing too

## Special scenarios
- Modifying a list value in a list
```py
t1 = (1, 2, 3, [55, 66, 77], [33, 44])
len(t1)
t1[3][0] # 55 
# BUT
t1[3][0] = 56
t1 # (1, 2, 3, [56, 66, 77], [33, 44]), NOTE the change in value, coz list can be updated
```

- Repetation operation
```py
t = (1,2,3)*2
t # (1, 2, 3, 1, 2, 3)

t = (1, 2, 3)
t = t*2 # NOTE, here the tuple gets replaced with now tuple, but not editing the previous tuple
t # (1, 2, 3, 1, 2, 3)
```