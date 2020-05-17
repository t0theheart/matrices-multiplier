# matrices-multiplier

## [OTUS](https://otus.ru) homework

### Goals:
1. Create program using multithreading to resolve problem.
2. Implement OOP pattern "Singleton".

### Description:
**multiply_matrices** is a function which allow you to multiply two matrix.
```python
from matrices_multiplier import multiply_matrices

matrix_1 = [
    [5, 8, -4], 
    [6, 9, -5], 
    [4, 7, -3]
]
matrix_2 = [
    [3, 2, 5], 
    [4, -1, 3], 
    [9, 6, 5]
]

multiply_matrices(matrix_1, matrix_2) 
# [
#   [11, -22, 29], 
#   [9, -27, 32], 
#   [13, -17, 26]
# ]
```

#### Multithreading
There is a multithreadig logic for multiplication within. 
Every line in result of **multiply_matrices** function calculates in separate thread which knows where it should put its calculated result. 

```python
_threads = [
    threading.Thread(target=put_line_in_result, args=(result_matrix, matrix_1, verticals_from_matrix_2, x)).start()
    for x in range(len(result_matrix))
]
```


Parent thread will wait until all child threads finish calculating and put theirs result in matrix then the function will return answer. 

```python
while not all(result_matrix):
    pass

return result_matrix
```

#### Singleton
Singleton is implement in Logger class. Only one instance of this class will be while program is running.
```python
class Logger:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
```
Every thread writes a message in the log.txt. Writing into file operation should lock others threads to write too.
So **lock** object is here to acquire and release lock!
```python
lock = threading.Lock()

with lock:
    logger.write(f'thread №{x}: put this {result_matrix[x]} with index {x} in the result array')
```

To run program:
```bash
$ python start.py
```

To run tests:
```bash
$ python -m unittest tests
```


#### P.S
Actually there is no true multithreading because of python GIL in this program. 
But I tried to demonstrate some basic principles of creating a multithreading program!