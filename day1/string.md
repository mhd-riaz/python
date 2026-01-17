# Data type: string

- assignment & type checking
```py
s="python"
type(s)
#op : <clas 'str'>
```
- can be used with single quotes and double quotes too

- if it starts with single quote, end with single quote, combination of single and doube quotes is not allowed
```py
s = 'python' # valid
s = "python" # valid
s = 'python" # invalid
```

- `'''` is used for block comment/documentation
```py
'''
This is a sample documentation comment
'''
```

- if triple quotes comment is assgined to a variable, then it becomes a multi line variable

- `__doc__` is a special function, called dunder func and variable, coz it used double underscore

```py
print(__doc__) # prints the documentation of the file
```
- if no documentation string is provided then the `__doc__` return `None`

- single line comment `#`

- multi line comment 
```py
'''
print("hello")
print("world")
'''
print("!")
# op: !
```

- escape sequence `\` 
```py
# the below line will throw error
s = 'Riaz's program' 
# coule be written as
s = 'Riaz\'s program' 
# or
s = "Riaz's program"
```

- view function of strings using `dir(str)`

- length of string using: `len(s)` NOTE: len function counts spaces, chars too

- `max(s)` gives char having max ascii value

- `ord('t')` gives ordinal values of any string, outputs 116

- `char(116)` gives chart with ordinal number 116 i.e. 't'

- string concatination using `+`, as `+` is polymorphic, why?
  - with int it does addition
  - with str it does string concatination

- similarly `10*'3'` or `'3'*10` while repeat char for n time, here n is 3

- `'10' * '3'` or `10 + '3'` will give you `TypeError` as you can multiply two strings or add string with int

- python is case sensitive i.e. `e != E`

- any operation can be performed like `True + True`, outputs `2`

| Mutability     | Im-mutability     |
| :------------- | :---------------- |
| can be changed | cannot be changed |

- strings are im-mutable, in programming it looks like we are modifying content of a string, but in reality, they values are replaced and stored in new memory location. Thus strings are considered immutable in nature after saved.
```py
s = "python"
id(s)
print("old: ",id(s))

s=s+'3'
s
print("new: ",id(s))

# old:  4319192064
# new:  4369616976
```

- iterable - can loop over it, thus strings are iterable

- indexing starts from 0; python support both positive and negative indexing

## print

`print(*arg, sep=' ', end='\n', file=None, flush=False)`

where:
arg = could be 0 to n inputs
sep = separator inserted bw two values
file = file like object; defaults to sys.stdout
flush = whether to force flush stream (write into the screen immediately)

## writing in a file instead of output screen(stdout)
```py
f1 = open("new_file.txt", 'w')
print("file written at file", file=f1)
f1.close()
```
here w - write mode, if your file already has content, then it will overwrite the contents of the file

**Lazy functions vs Eager function**
Eager functions perform their computations immediately when they are called or their expression is defined, while lazy functions (or lazy evaluations) defer computation until the result is actually needed.
Lazy keywords: `range, yield, import`
Eager keywords: rest other keywords apart from lazy keywords

| Feature     | Lazy Loading/Evaluation                   | Eager Loading/Evaluation               |
| :---------- | :---------------------------------------- | :------------------------------------- |
| Timing      | On-demand (when accessed)                 | Immediately (upfront)                  |
| Initial     | Load	Faster                               | Slower (all data loaded)               |
| Performance | Better for large datasets                 | Better for small, frequently used data |
| Memory      | /Usage	Conserves resources                | Uses more resources initially          |
| Complexity  | More complex (can lead to N+1 problem)    | Simpler (all data available)           |
| Risk        | Potential for "lazy" errors (NullPointer) | Inefficient if data is never used      |


**keyword**
  - Reserved: You cannot use them for your own naming purposes.
  - Case-sensitive: For example, if is a keyword, but If or IF is not (though it's best practice to avoid names that look like keywords).
  - Always available: They do not need to be imported (unlike some functions or modules).

```md
The list of keywords are: 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## string operations

1. `startswith()` - yeilds bool output
```py
s = "execProgram"
s.startswith('E') # false
s.startswith('e') # true
```

2. `index()` - walking through the iterable using indexing
```py
p = "python program"
print(p[1]) # accessing via index value
# NOTE it give only first occurance of the index
# op : y

# ------------
# now if we want to know what is the index of y, then use
p.index('y')

# op: 1
``` 

3. `upper()` - transforms to upper case
```py
s = "python"
s.upper() # give "PYTHON"
s # is still python, as strings are immutable
```
4. `lower()` - transforms to lower case
5. `isupper()` - check if its upper case
6. `islower()` - check if its lower case
7. `count()` - counts number of occurance
```py
s = "python pip"
s.count('p') # 2
```
8.  `split()` - splits strin as per given param, default to " " (space)
```py
s = "python is great"
s.split()
# ['python', 'is', 'great']

# ---------------

s = "python is great"
s.split('t')
# ['py', 'hon is grea'] 
# NOTE: when you do split over a character, then that char is lost
```
9. `strip()` - removes leading and trailing spaces
```py
s =" p E   SS. "
s.strip
# "p E   SS." NOTE: the spaces inbetween will not be removed
```

10. `isdigit()` - checks if the char is a digit (numeric)
11. `isalpha()` - checks if the char is a alphabet
12. `isalnum()` - check if the char is alpha numeric


## Comparison operation
```py
'''
Priority order
1. ascii
2. if same chara - then only length
'''

'cat' > 'car'
# true, if len is same, then comparison is done by ascii value

'cat' > 'cattle'
# false, has same char, but due to length

'car' == 'Car'
# False, coz it case sensitive

'apple' > 'z'
# False, as ascii value of a is compared with z

'a' > 'A'
# True, as upper case has lower ascii value i.e A=65, a=97
```

## `Range` operation
syntax: `range(start, end, stepIndex)`
```py
for i in range(0,10):
    print(i)

# op: 0 to 9

# -----------

# using step function
for i in range(0,10, 2):
  print(i)
# op: 0 2 4 6 8

# -----------

# using neg step index
for i in range(0,10, -1):
  print(i)
# op: nothing, coz there is no
# this is an symantic error

# -----------

# using neg step index
for i in range(10,0, -1):
  print(i)
# op: 
# 10 
# 9 
# 8 ...

# -----------

# using string range
for i in "python":
  print(i,end=" ")
# op: p y t h o n

# -----------

# using string range
for i in 1947:
  print(i,end=" ")
# op: TypeError, coz integer is not iterable
```

| syntax error                                                                                                                                                                                                 | symantic error                                                                                                                                                                                                                          |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| syntax error occurs when the code violates the formal rules and grammar of the programming language. The compiler or interpreter cannot understand the instruction.                                          | A semantic error occurs when a statement is syntactically valid but does not make sense or follow the intended logic of the program. The code has a legal form, but an incorrect meaning.                                               |
| These errors are typically detected during the compilation or parsing phase and prevent the program from running. The system will provide an explicit error message pointing to the location of the mistake. | Some semantic errors, like type mismatches or using undeclared variables, can be caught by the compiler. Others, often referred to as logical errors, are only detected at runtime (during execution) and are harder to find and debug. |


