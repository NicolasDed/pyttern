# Python Hole

![Tests Status](https://github.com/JulienLie/python-hole/actions/workflows/python-app.yml/badge.svg?event=push)

Python Hole (or PyHole) is a python library to create patterns file for Python code.

## Syntax

We extended the python syntax to create patterns file. Our new syntax include the following elements:

| Wildcard | Description                                       |
|----------|---------------------------------------------------|
| ?        | Match 1 element                                   |
| ?*       | Match 0 or more elements                          |
| ?{name}  | Match 1 element and bind it to {``name``}         |
| ?:       | Match 1 element with a body                       |
| ?*:      | Match the body of the wildcard in any indentation |

## Usage

```python
from pyhole import Matcher

code = "code_file.py"
pattern = "pattern_file.py"
match = Matcher.match_files(code, pattern)
if match:
    print("We found a match")
else:
    print("No match")
```

## Example

### Pattern file:
```python
def multiplicatons(n):
    ?*
    ?var1 = ?       # We want to have a initial variable
    ?*
    ?*:
        ?*
        ?var1 = ?   # This variable has to be updated somewhere
        ?*
    return ?var1    # And we want to return it
```

### Python code:
```python
def multiplications(n):
    """
    pre:  n is a positive integer
    post: Return the number of distinct decompositions a,b 
          such that n == a*b == b*a
    """
    b=n
    a=1
    c=0
    while a*b==n:
        c=a*(b/a)
        a+=1
    return c
```
