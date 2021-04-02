# Table of Contents

- [Table of Contents](#table-of-contents)
  - [Basic Tips and Tricks](#basic-tips-and-tricks)
    - [1. Enumerate()](#1-enumerate)
  - [Advance Tips and Tricks](#advance-tips-and-tricks)

## Basic Tips and Tricks

### 1. Enumerate()

`enumerate()` can be used to iterate over index and value at the same time.

```python
for i, val in enumerate(["A", 7, {1, 2}]):
    print(i, val)

# Output
# 0 String
# 1 10
# 2 {1, 2}
```

`enumerate()` accepts an optional argument where you can specify starting index of `idx`

```python
for i, val in enumerate(["A", 7, {1, 2}], 100):
    print(i, val)

# Output
# 100 String
# 101 10
# 102 {1, 2}
```


## Advance Tips and Tricks

https://book.pythontips.com/en/latest/enumerate.html
Similar repo: https://github.com/alexghergh/python-tricks
