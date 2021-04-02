This is a Work in Progress

# Table of Contents

- [Table of Contents](#table-of-contents)
  - [Basic Tips and Tricks](#basic-tips-and-tricks)
    - [Enumerate()](#enumerate)
    - [List Comprehension](#list-comprehension)
    - [Dictionary and Set Comprehension](#dictionary-and-set-comprehension)
  - [Advance Tips and Tricks](#advance-tips-and-tricks)
    - [Conditional Comprehensions](#conditional-comprehensions)

## Basic Tips and Tricks

### Enumerate()

`enumerate()` can be used to iterate over **index and value** at the same time.

```python
for i, val in enumerate(["A", 7, {1, 2}]):
    print(i, val)

# Output
# 0 String
# 1 10
# 2 {1, 2}
```

`enumerate()` accepts an **optional argument** where you can specify **starting index** of `idx`

```python
for i, val in enumerate(["A", 7, {1, 2}], 100):
    print(i, val)

# Output
# 100 String
# 101 10
# 102 {1, 2}
```

### List Comprehension

**Cleaner and faster** way to do `for` loop

```python
nums = [i for i in range(1, 5)]
print(nums)

# Output
# [1,2,3,4]
```

2 `for` loops:

```python
nums = [i * j for i in range(1, 5) for j in range(10, 12)]
print(nums)

# Output
# [10, 11, 20, 22, 30, 33, 40, 44]
```

2 **NESTED** `for` loops

```python

matrix = [[i * j for i in range(1, 5)] for j in range(10, 12)]
print(matrix)

# Output
# [[10, 20, 30, 40], [11, 22, 33, 44]]
```

Example use cases:

- [Matrix Initialization](./examples/list_comprehension/matrix_initilization.py)

### Dictionary and Set Comprehension

Dictionary also has comprehension.

```python
my_dict = {val : i for i, val in enumerate([10, 20, 30])}
print(my_dict)

# Output
# {10: 0, 20: 1, 30: 2}
```

Set also has comprehension

```python
nums = [1,1,1,2,2,3,3,4]
my_set = {num for num in nums}
print(my_set)

# Output
# {1, 2, 3, 4}
```

You might ask why bother with Set Comprehension when we could do this: `print(set(nums))`. The answer is because of [Conditional Comprehensions](#conditional-comprehensions)


## Advance Tips and Tricks

### Conditional Comprehensions


To Add: 
- one-line if
- unpack and iterate at the same time
- collections
  - defaultdict
  - queue
  - Counter
- itertools
  - chain
  - zip longest
- functools
  - map
  - filter
- pprint
- set
- list
- dictionary
- decorator
- access variable outside of function
- https://book.pythontips.com/en/latest/enumerate.html
- https://github.com/alexghergh/python-tricks
