# input

- input - waits for the user (NOTE: cursor blinks)

- print(input) - not a good practise

- by default the return values of the input is a string

Eg. 1
```py
print(input()+input()) 
# 30
# 40
# OP: 3040
```

- if we want to use other than string, always typecast value
Eg. 2
```py
print(int(input())+int(input())) 
# 30
# 40
# OP: 70
```

- can take hints for input
Eg. 3
```py
input("enter a number: ")
# OP: enter a number: 
```

- storing user provided value in a variable
Eg. 4
```py
a = int(input("enter the number")) # explicit type casting
b = int(input("enter the number"))
c = a + b
print("result of a + b is ", c)
```

- when you try to add a string and int it throws TypeError: regarding concatenation

- but when you try to add a float with int, it typecasts the result value into a float value

- unpack values using split function
NOTE: when you have more/lesser than expected values to unpack, then it throws ValueError
```py
a,b = input().split() # by default splits by empty space ' '
print(a)
print(b)
```
EXCEPTION: 
  - when you use the split with '\n', it throws error, as `input()` behavior: It reads from standard input until it encounters a newline (\n), returns the string, and discards the newline.

`a,b = int(input().split(","))`

NOTE:
  - the .split() method returns an array of string 
  i.e. returns a list of strings (e.g., ['1', '2']), but the int() function can only convert a single string or number at a time. It cannot convert an entire list at once.
  - solution: use map(int, input().split(',')) - this will typecast each item in the array