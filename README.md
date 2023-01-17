This is a Work in Progress

## What is this ?

Initially, I created this list to show my friends how cool Python is. Now, this list contains Python Tips and Tricks I learned and collected from years of solving [Leetcode](https://leetcode.com/JummyEgg/) problems. The purpose of this list is to show you the best practices in writing Pythonic code.

This uses `python >= 3.6` unless specified.

How should you read this list: I separate the list into topics. Topics appear later down in the list require understandings of topics appear earlier. Thus, it's best for you to read this list from top to bottom. At the end of some topics, I have link to examples or link to more advanced topics. You can follow the links or simply ignore those for now (because you will see them later on).

Please enjoy.

## Table of Contents

- [What is this ?](#what-is-this-)
- [Table of Contents](#table-of-contents)
- [Basic Tips and Tricks](#basic-tips-and-tricks)
  - [Swap 2 variables](#swap-2-variables)
  - [Python Unpacking](#python-unpacking)
  - [Enumerate()](#enumerate)
  - [Quick Initilization](#quick-initilization)
  - [List Comprehension](#list-comprehension)
  - [Dictionary and Set Comprehension](#dictionary-and-set-comprehension)
  - [`lambda` Function](#lambda-function)
  - [Key Functions](#key-functions)
  - [`zip()`](#zip)
- [Built-in Libraries](#built-in-libraries)
  - [collections](#collections)
    - [defaultdict](#defaultdict)
    - [deque](#deque)
    - [Counter](#counter)
    - [Queue](#queue)
  - [itertools](#itertools)
    - [accumulate](#accumulate)
    - [dropwhile](#dropwhile)
    - [takewhile](#takewhile)
    - [groupby](#groupby)
    - [chain](#chain)
    - [zip\_longest](#zip_longest)
  - [string](#string)
  - [random](#random)
  - [heapq](#heapq)
  - [bisect](#bisect)
- [Functional Programming](#functional-programming)
  - [functools](#functools)
    - [reduce](#reduce)
    - [cache](#cache)
- [Extended Tips and Tricks](#extended-tips-and-tricks)
  - [Python Unpacking with `*`](#python-unpacking-with-)
  - [Iterate through matrix by column](#iterate-through-matrix-by-column)
  - [Conditional Comprehensions](#conditional-comprehensions)
  - [Multiple Statements on 1 line](#multiple-statements-on-1-line)

## Basic Tips and Tricks

### Swap 2 variables

In other languages, when we want to swap 2 variables, we tend to use `temp` to store the value. However, in Python, there is a cleaner way to do this:

```python
a = 10
b = 20
c = 30
a, b, c = c, a, b    # <--- all three assignments are done at the same time
print(a, b, c)

# Output:
# 30 10 20
```

### Python Unpacking

Unpack values from a tuple or a list:

```python
first, second, last = [10, 20, 30]
print(first, second, last)

# Output:
# 10 20 30
```

**Nested** Unpacking:

```python
matrix = [[1, 2], ["A", "B"]]
(one, two), (three, four) = matrix
print(one, two, three, four)

# Output:
# 1 2 A B
```

Unpacking inside a loop:

```python
matrix = [[1, 2], [3, 4], [5, 6]]
for val1, val2 in matrix:
    print(val1, val2)

# Output:
# 1 2
# 3 4
# 5 6
```

<!-- Add example how to unpack values from function -->
More: [Python Unpacking with `*`](#python-unpacking-with-)

### Enumerate()

When writing Python, the clean way to iterate over **index and value** at the same time is to use `enumerate()` like this:

```python
for i, val in enumerate(["A", "B", "C"]):  # <--- this has python unpacking
    print(i, val)

# Output:
# 0 A
# 1 B
# 2 C
```

`enumerate()` accepts an **optional argument** where you can specify **starting index** of `i`:

```python
for i, val in enumerate(["Monday", "Tuesday", "Wednesday"], 2):
    print(i, val)

# Output:
# 2 Monday
# 3 Tuesday
# 4 Wednesday
```

Example:

- [Leetcode 1779](examples/leetcode_problems/1779.py)

### Quick Initilization

In Python, you can quickly create a string or a list like this:

```python
my_str = "a" * 5
my_list = [0] * 5
print(my_str)
print(my_list)

# Output:
# aaaaa
# [0, 0, 0, 0, 0]
```

However, **NEVER** do as follows:

```python
my_list = [[0] * 5] * 2   # <--- DO NOT DO THIS. This is shallow copy
print(my_list)

# Output:
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

my_list[0][0] = 5    # <--- All inner arrays will change
print(my_list)

# Output:
# [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0]] 
```

To initialize a matrix, the best way is [here](examples/list_comprehension/matrix_initilization.py)

### List Comprehension

**Cleaner and faster** way to do `for` loop:

```python
nums = [i for i in range(1, 5)]
print(nums)

# Output:
# [1, 2, 3, 4]
```

2 `for` loops. 

```python
nums = [i * j for i in range(1, 5) for j in range(10, 12)]
print(nums)

# Output:
# [10, 11, 20, 22, 30, 33, 40, 44]

# Equivalent to:
nums = []
for i in range(1, 5):
    for j in range(10, 12):
        nums.append(i * j)
print(nums)
```

In the example above, notice that `for i` is the outer loop and `for j` is the inner loop

2 **Nested** `for` loops:

```python
matrix = [[i * j for j in range(10, 12)] for i in range(1, 5)]
print(matrix)

# Output:
# [[10, 11], [20, 22], [30, 33], [40, 44]]

# Equivalent to:
matrix = []
for i in range(1, 5):
    row = []
    for j in range(10, 12):
        row.append(i * j)
    matrix.append(row)
print(matrix)
```

In the example above, pay attention to the order of `for i` and `for j`. Although `for i` is the outer loop, it appears after `for j` in the list comprehension

Examples:

- [Matrix Initialization](./examples/list_comprehension/matrix_initilization.py)

### Dictionary and Set Comprehension

Dictionary also has comprehension:

```python
my_dict = {val : i for i, val in enumerate([10, 20, 30])}
print(my_dict)

# Output:
# {10: 0, 20: 1, 30: 2}
```

Set also has comprehension:

```python
nums = [1,1,1,2,2,3,3,4]
my_set = {num for num in nums}
print(my_set)

# Output:
# {1, 2, 3, 4}
```

You might ask why bother with Set Comprehension in this case when we could do this: `set(nums)`. The answer is because of [Conditional Comprehensions](#conditional-comprehensions)

### `lambda` Function

`lambda` function or anonymous function is a different way to write function. The following 2 ways are equivalent:

```python
# Normal function
def my_func1(x):
  return x * 2

# Lambda function
my_func2 = lambda x: x * 2

print(my_func1(1))
print(my_func2(1))

# Output:
# 2
# 2
```

`lambda` function are used a lot in [Key Functions](#key-functions) like `min()`, `max()`, `sort()` and [Functional Programming](#functional-programming) like `map()`, `filter()`, `reduce()`

### Key Functions

Key functions are functions that take parameter `key` as input. `key` receives a function that can be a `lambda`. Some key functions that appear often are `min()`, `max()`, `sort()`, `sorted()`. Here are some examples:

Find longest string in array:

```python
array = ["a", "ab", "abc"]
print(max(array, key=len)) # Note that len() itself is a function

# Output:
# "abc"
```

Sort array by squared value, e.g. `(-2)**2 = 4`

```python
array = [-2, 0, 1]
print(sorted(array, key=lambda x:x**2)) # Note that we use lambda function here

# Output:
# [0, 1, -2]
```

You can read more about this from [Real Python](https://realpython.com/python-lambda/#key-functions)

### `zip()`

`zip()` is a clean and quick way to iterate through multiple arrays at the same time.

```python
chars = "abc"
nums = [1, 2, 3]

for char, num in zip(chars, nums):
  print(char, num)

# Output:
# a 1
# b 2
# c 3
```

As you can see, `char` and `num` takes value from `zip(chars, nums)` which iterate through both `chars` and `nums` at once. This is particularly useful when you have to deal with multiple iterable objects. However, be mindful of arrays with different length:

```python
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9, 10]

for n1, n2, n3 in zip(nums1, nums2, nums3):
  print(n1, n2, n3)

# Output
# 1 4 7
# 2 5 8
# 3 6 9
```

There are two important things to note from the above examples:

- `zip()` takes as many array as you want
- `zip()` only iterates up to the shortest array

More:

- There is another variant of `zip()` called [zip_longest](#zip_longest) which iterates up to the longest array
- One of use case of `zip()`: [Iterate through matrix by column](#iterate-through-matrix-by-column)

## Built-in Libraries

### collections

#### defaultdict

#### deque

#### Counter

#### Queue

### itertools

#### accumulate

#### dropwhile

#### takewhile

#### groupby

#### chain

#### zip_longest

Read this first: [`zip()`](#zip)

### string

When you need to get a list of characters quickly, you can get in from `string`. All letters:

```python
print(string.ascii_lowercase)
print(string.ascii_letters)

# Output:
# abcdefghijklmnopqrstuvwxyz
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```

Or just digits:

```python
print(string.digits)
print(string.hexdigits)

# Output:
# 0123456789
# 0123456789abcdefABCDEF
```

Or just punctuation:

```python
print(string.punctuation)

# Output:
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

[Example](examples/string_examples.py)

### random

### heapq

### bisect

## Functional Programming

### functools

#### reduce

#### cache

## Extended Tips and Tricks

### Python Unpacking with `*`

While unpacking, you can use `*` to greedy match as much as it can and return a **list**

```python
first, second, *rest = [1, 2, 3, 4, 5, 6]
print(first, second, rest)

# Output:
# 1 2 [3, 4, 5, 6]
# Notice that rest is a list

first, *mid, last = [1, 2, 3, 4, 5, 6]
print(first, mid, last)

# Output:
# 1 [2, 3, 4, 5] 6
```

Because `*` is greedy (matches as much as it can), you cannot use two `*` in one unpack

```python
first, *mid, *rest = [1, 2, 30, 40, 50, 60]
print(first, mid, rest)

# Output
# SyntaxError: two starred expressions in assignment
```

### Iterate through matrix by column

### Conditional Comprehensions

Conditional Comprehensions allow us to add `if else` statement into list/set/dict comprehensions.

`if` statement in List Comprehension:

``` python
nums = [i for i in range(10) if i % 2]           # <--- "if" is placed at the end 
print(nums)

# Output:
# [1, 3, 5, 7, 9]
```

`if else` statement in List Comprehension. Notice that `if else` is placed in the **front**.

``` python
nums = [i if i % 2 else 0 for i in range(10)]    # <--- "if", "else" are placed in the front
print(nums)

# Output:
# [0, 1, 0, 3, 0, 5, 0, 7, 0, 9]
```

### Multiple Statements on 1 line

Although in Python, we don't use `;` often, it can help with writing multiple lines of code on the same line like this:

```python
for i in range(3): print(i); print("--")

# Output:
# 0
# --
# 1
# --
# 2
# --
```

However, as you can imagine, this can be hard to read if you overuse it. So please use it with care. I tend to only use it for variable initilization.

To Add:

- one-line if
- for else
- while else
- unpack and iterate at the same time
- f-string
- *args, **kwargs
- Counter, | &
- string slicing
- == vs is
- string, tuple comparison
- immutable vs mutable
- ord vs chr
- tuple: 1,2,
- class
- Generator
- Iterator
- pprint
- decorator
- access variable outside of function
- https://github.com/chiphuyen/python-is-cool
- https://book.pythontips.com/en/latest/enumerate.html
- https://github.com/alexghergh/python-tricks
- https://towardsdatascience.com/100-helpful-python-tips-you-can-learn-before-finishing-your-morning-coffee-eb9c39e68958
