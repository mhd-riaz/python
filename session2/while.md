# While loop

**UseCase**:
- when you are not sure about how many loops your code will run, i.e. the loop is based on the user defined count for the loop

**Syntax**:
```py
while condition:
    # code block to execute
    # usually includes an update to the condition
```

**Example using finite check**:
```py
num = int(input("Enter the num, (0 to stop)"))
while num != 0:
    print("Entered number is: ", num)
    num=int(input("Enter the num, (0 to stop)"))
```

**Example using infinite check**:
- using break to exit infinite loop
```py
num = int(input("Enter the num, (0 to stop)"))
while True:
    print("Entered number is: ", num)
    num=int(input("Enter the num, (0 to stop)"))
    if num==0:
        break
```

NOTE: we dont have the keyword `do`, thus the `do while` does not exist