# set
- used for de-duplication structure, Sets cannot have two items with the same value.
- A set is a collection which is unordered, unchangeable*, and unindexed.
- **unchangeable***: Once a set is created, you cannot change its items, but you can add new items.
- no order is preserved, thus no indexing
- can contain both homogeneous and heterogeneous data
- NOTE: `1` and `True` are considered same, `0` == `False`
- its case sensitive, i.e. ABC != abc
- Will not allow you to add a list into tuple, coz list values are mutable
i.e.
```py
s = {1, "hello", 34, 44 }
s.add("dd") # allowed
s.add((1,2,3)) # allowed
s.add([1,2,3]) # not allowed
```

**Syntax**:

```py
mySet = { x, y, z}
# or
mySet = set((1,2,1,3))
mySet # {1, 2, 3}
```

**Type**:
returns a type of `<class 'set'>`

**Constructor**: `set()`

| Dict             | Set                 |
| ---------------- | ------------------- |
| Keys with values | keys without values |

**Methods**:
- `.add()` adds an element in the set
    NOTE: will allowed you to add only 1 element at a time, whereas, update method allows you to add more than 1 at a time
    e.g. 
    ```py
    s = set([1,2,3,4,1,2])
    s.add(5)
    s # 1,2,3,4,5
    ```

- `.update()` To add items from another set into the current set
    NOTE: The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
    e.g. 
    ```py
    s = set([1,2,3,4,1,2])
    s.add(5)
    s # 1,2,3,4,5
    r = set(6,7)
    s.update(r)
    s # 1,2,3,4,5,6,7
    ```


- `.remove(val)` to remove value from a set
  NOTE: If the item to remove does not exist, remove() will raise an error.
```py
s = set([1,2,3,4,1,2])
s.remove(1)
s # 2,3,4
```

- difference the set s1 from s using `.difference()` or `-`
```py
s = set([1,2,3,4,1,2])
s1 = {2,4}

s-s1 # {1, 3}
```

- `.difference_update()` -> find the difference and updates in the tuple
```py
s = set([1,3,4,1,2])
s1 = {2,4}

s-s1 # {1, 3}
s.difference_update(s1)
s # 1, 3
```

- `.symmentric_difference()` or `^` -> method will keep only the elements that are NOT present in both sets. i.e. remove item that are common in both set
```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
```

- common in both using `.intersection()` or `&`
```py
s = set([1,2,3,4,1,2])
s1 = {2,4}

s&s1 # {2, 4}
```

- Add both using `.union()` or `|`
```py
s = set([1,2,3,4,1,2])
s1 = {2,4}

s|s1 # {1, 2, 3, 4}

# if you want to join multiple, use union
s.union(s1, s2, s3)
```

- `issubset()` or `<=`
  - Returns True if all items of this set is present in another set
  ```py
    s = set([1,2,3,4,1,2])
    s1 = {2,4}
    s.issubset(s1) # True
    s1.issubset(s) # False
    ```
- `issuperset()` or `>=` 
  - Returns True if all items of another set is present in this set
    ```py
    s = set([1,2,3,4,1,2])
    s1 = {2,4}

    print(s.issuperset(s1)) # True
    s1.issuperset(s) # False
    ```

# frozenset

Unlike sets, elements cannot be added or removed from a frozenset.
```py
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
```