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

# print

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