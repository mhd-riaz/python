import func
# from mods import methods
import mods.methods as m

func.sayHello()
# methods.greetUser()
m.greetUser()

"""
# Refer notebook: 3.ipynb
import numpy as np
import time

start = time.time()
n = 1000000
l = []
lst = range(n)

for i in lst:
    l.append(i*2)
print(l)

end = time.time()
print(end-start)


# same using numpy
start = time.time()
a=np.array(np.array(n))
print(a*2)
print(a)
end = time.time()
print(end-start)

"""