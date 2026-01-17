# dictionaries/maps

- are mutable in nature
- slicing is not allowed in dict, due to hashing reasons
NOTE: 
- As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
**syntax**:
`d = {key: value}`
key: str, int (anything that is immutable and unique; can be key value)
value: any

**example**:
```py
d = {}
type(d) # <class 'dict'>

d = { 
    1:2,
    2:4,
    3:9,
    4:16
}

# if you use list as key value
d = {[1,2] : "hello"} # TypeError: unhashable type: 'list'
```



**length of dict**: `len(dict)`
**max**: `max(dict)`, here max is done based on keys; keys has to be homogeneous 
**min**: `min(dict)`, here min is done based on keys; keys has to be homogeneous 
**sum**: `sum(dict)`, here sum is done based on keys; keys has to be homogeneous 
**indexing**: `d[2]`, is on key

**adding value to dict**
```py
d={}
d[6]=36
# d => {6: 36}

# replacing value
d[6]=25

# if try for key that does not exists, then
d[16] # KeyError
```

## methods
`.items()` - give a list of tuples(key,value) pair
`.pop(keyName)` - removes the item and return item name
`.popitem()` - removes item and returns tuple of (key, value); usage is discouraged as it might pop anything as per hash queue
`.values()` - gives dict_value(2, 4, 5) of dict




