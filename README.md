# matrices-multiplier

## [OTUS](https://otus.ru) homework

### Goal:
Create program using multithreading to resolve problem. 

### Description:
#### multiply_matrices
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

To run tests:
```bash
$ python -m unittest tests
```


#### P.S
Actually there is no true multithreading because of python GIL in this program. 
But I tried to demonstrate some basic principles of creating a multithreading program!