# 14th Feb 2026 - Session 3

Jupyter Notebook [link](./../notebook/3.ipynb)

1st half:
- import statements
- numpy
- 

2nd half:
- assignments


---

# Import statements
```py
# can be called module/library
import random # returns everything from random library
# methods/values from the library can be accessed by
random.randint(1,5)

# this is importing with alias name
import random as r
# methods/values from the library can be accessed by
r.randint(1,5)

# selective import
from random import randint
# methods/values from the library can be accessed by
randint(1,5)

# import everything from random
from random import *
# methods/values from the library can be accessed by
randint(1,5)
```


---

# PANDAS

| Numpy          | Pandas              |
| -------------- | ------------------- |
| for scientific | for structured data |


import command:
`import pandas as pd`

if not installed do
`pip install pandas`

to check if pandas is installed or no use
`pd.__version__`

Series: 1 column with labels

Dataframe: more than 1 column with labels

```py
p = pd.Series([11,22,33,44,55])
print(p)
```

output:
```bash
0    11
1    22
2    33
3    44
4    55
dtype: int64
```

Note: the 0, 1, 2 ... - represents the index positions