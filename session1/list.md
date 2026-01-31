# list

- python stores list in a different way i.e. python stores the address of value in the list rather than value itself inorder to manage memory

- is mutable in nature, i.e. can grow or shrink
- heterogenious(diff data type)/homogeneous(same data type) in nature
```py
l = [10, 20, 30, 50.5, "str"] # heterogenious

a = [10, 20, 30, 50] # homogeneous
```
- is indexable, starts with 0th index
- ordered (has a defined order and is maintained)
- can contain duplicates

syntax:
`l=[]`

Refer more [here](https://www.w3schools.com/python/python_lists.asp)

- in order to perform some functions like min or max, the data has to be homogeneous in nature, else it will throw error

```py
n = [1, 2, 3 ]
l = ['a', 'b', 'c' ]

l + n # ['a', 'b', 'c', 1, 2, 3]
l * 2 # ['a', 'b', 'c', 'a', 'b', 'c']
n * 2 # [1, 2, 3, 1, 2, 3 ]
l *-2 # [] is empty list (zero value)
```

### Methods

`.append()` - add an element to the array at the end of the list
`.count()` - count/frequency of the element's occurance
`.index()` - what at specified index; throws `ValueError` if you are looking at something which is not present
`.insert(position, value)` - insert element at specified index
`.extend([])` - join list with another list, input must always be an iterable (bulk insert of append)
`.pop()` - removes last element from the list and return the value
`.remove(value)` - removes the first occurance of the value, but does not return any value
`.sort()` - default in ascending order; `.sort(reverse=True)` for descending; uses `Timsort` algorithm; can sort only homogeneous list; inline sorting (i.e. impacts the original list)
`.reverse()` - reverses the index of item and gives the list

### functions
`sorted()` - is a generic function; can sort heterogeneous list; creates a new list (does not impacts the original list); 

## Membership operators
`in`
`not in`
```py
l = [1, 6, 8, 9]
20 in l # False
6 in l # True
```