# User defined functions

| User defined                                      | Built in                                               |
| :------------------------------------------------ | :----------------------------------------------------- |
| custom function that we define in our own program | are reusable function that were already written for us |

# Functions
- Reuse, blocks of code
- Modularity, bundeling of code

**Syntax**:
```py

def func_name(parameters): # name the function, such that it represents the functionality
    # any body (or)
    pass # placeholder that tells we will comeback and fill this with our own code (or)
    return 

f1(arguments)
```

`:` marks end of function definition
`print...` body of the function, control will go inside only if the function is called
`def func_name` func header
`f1()` - **handle** that points to function's definition; calling statement
`f1` - is a **statement/expression** handle the points to an adress where definition is written
`parameters` - input taken for the function
`arguments` - values that are passed to the function as parameters
`return` - any function that returns value will come in form of tuple for more than 1 return parameter

```py
f2 = f1 # now f2 points to same address that f1 is refering to, thus calling f2 will also yield same result

del f1 # pointer to f1 will be removed

f2() # NOTE: f2 still have value of address where function was defined, so s2 will work
```

## Local scoped variables

```py
def f1():
    a = 10 # here a, b and c are local scoped variables
    b = 20 # these variables are not available outside of this function
    c = a + b # hence these are called local scoped variables
    print(c)

f2()
```

when you dont have anything to do inside the function, just as a placeholder, you can use the keyword `pass`

```py
def f1(a,b):
    return a,b

print(f1(1,2)) # return a tuple of (1, 2)
```


## Global variables
- variables can be accessed between across function, across file throughout the program


## Pass by value used by python
## Pass by Reference does not exist in python, as python handles things based on mutability of inputs passed


## Position parameters:
```py
def f1(a,b,c,d):
    print(a,b,c,d)
f1(1,2,3,4)
```

- here `a-1, b-2,c-3,..` this way of passing params is called position parameters, as the values are passed based on the position
- order does matter!

## Keyword parameters:

- order does not matter
```py
def f1(a,b,c,d):
    print(a,b,c,d)
f1(a=1,c=3,b=2,d=4)
```

## combining paramters (positional + keyword):

- in this combination you will have to pass the positional params first then only pass the keyword based parameters
```py
def f1(a,b,c,d):
    print(a,b,c,d)
f1(1,3,4,b=2)
```

## Default arguments

- if you dont specify, it will take default
- if provided, then the default get overriden

```py
def f1(a,b=[]):
    print(a,b)
f1(44)
```

# Late vs. Early Binding.
## Binding Default Arguments at Definition Time.

Here python uses Early binding
```py
x =222
def f1(a=x):
    print(a)

x = 33
f1()
```

! NOTE: the activation records of the local variables does not gets cleared untill the whole program runtine is over

eg:
```py
def f1(x, a =[]):
    a.append(x)
    print(a)
f1(100)
f1(200)
z = [30, 40]
f1(50, z)
f1(600)
```

This is the "Mutable Default Argument" trap—one of the most famous quirks in Python.

It happens because of the Early Binding we discussed earlier. In Python, default arguments are created once when the function is defined, and that same object is reused for every subsequent call.

  ### The Breakdown:

  - Here is exactly what happens in memory:

  - Definition Time: Python creates the function object f1. It sees a=[] and creates a single list object in the heap. This list is attached to f1 as its permanent default "backpack."

  - f1(100): No a is provided. Python uses the "backpack" list. It appends 100.
      Result: [100]
  - f1(200): No a is provided. Python uses the same "backpack" list from step 1 (which already has 100 in it).
      Result: [100, 200]
  - z = [30, 40] followed by f1(50, z): You provided an explicit argument for a. Python ignores the "backpack" and uses your list z.
      Result: [30, 40, 50] (This matches your expectation for this specific call).
  - f1(600): No a is provided. Python goes back to its "backpack." The last time the backpack was used, it contained [100, 200]. It now appends 600.
      Result: [100, 200, 600]


## Change of global variable from function

Any change in global value inside the function, does not reflect outside of the function. But if you still want to modify the global variable inside a local function, then use this syntax:
`global`
```py
a = 10 
def f1():
    global a
    a = a +10
    print(a)

print(a)
f1()
print(a)
```


## Anonymous/Lambda function

- Functions that do not need reusability, and will be called only once are termed as lambda/anonymous function
- are used when you dont need return type
- only single expression
- do not use multiple conditioning

syntax:
```py
k = lambda a,b:a+b
print(k(10,20))
```

"apply some computation on the items of the list and store it in another list" - use map or lambda
map - 1 on 1 paradime
Syntax: `map(<callable>, iterable)`
<callable> - could be user defined or inbuilt function

NOTE: map is a lazy funtion

**When to use?**
- `map` - apply function to all values
- `filter` - when you want to apply func based on a filter, instead of printing true/false, it output, only the true's value
- `reduce` - when you have a list of values and return 1 single values after computation. eg. "min", "max"
  - the x + y; where the x start from the left 0th index then y (1st index)
  - then the computed value becomes x as 0th index the compute with y, and so on
  - Always set initial value for reduce.
```py
name = "Mohamed Riaz Hello World"

def f1(x,y):
    return str(x+y[0])

# print(f.reduce(f1, name.split(" "))) # here x value will be set to Mohamed, as we have not set initial value
print(f.reduce(lambda x,y:x+y[0], name.split(" "),"")) # Note the last parameter, "" -> this sets the initial value for x
```


## Callbacks

A function calling yet another functions is called callback functions.


## Recursive function

A function that calls itself is called recursive function