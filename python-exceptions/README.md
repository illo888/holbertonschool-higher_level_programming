
# Python - Exceptions

In this project, I learned handling errors and exceptions in Python with `try` and `except`.

---

## Tests ✔️
- **tests**: Folder of test files. Provided by Holberton School.

---

## Function Prototypes 💾
Prototypes for functions written in this project:

| File | Prototype |
|------|-----------|
| `0-safe_print_list.py` | `def safe_print_list(my_list=[], x=0):` |
| `1-safe_print_integer.py` | `def safe_print_integer(value):` |
| `2-safe_print_list_integers.py` | `def safe_print_list_integers(my_list=[], x=0):` |
| `3-safe_print_division.py` | `def safe_print_division(a, b):` |
| `4-list_division.py` | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py` | `def raise_exception():` |
| `6-raise_exception_msg.py` | `def raise_exception_msg(message=\"\"):` |

---

## printing
**File:** `0-safe_print_list.py`  
Prints `x` elements of a list on the same line, followed by a new line.  
- `x` can be bigger than the length of `my_list`.  
- Returns the real number of elements printed.  
- Without importing modules or using `len()`.

---

### 1. Safe printing of an integers list
**File:** `1-safe_print_integer.py`  
Prints an integer in `"{:d}".format()` format.  
- Returns `True` if value was printed correctly, `False` otherwise.  
- Without importing modules or using `type()`.

---

### 2. Print and count integers
**File:** `2-safe_print_list_integers.py`  
Prints the first `x` elements of a list that are integers on the same line, followed by a new line.  
- Returns the real number of integers printed.  
- Without importing modules or using `len()`.

---

### 3. Integers division with debug
**File:** `3-safe_print_division.py`  
Divides two integers and prints the result using `finally:`.  
- Returns the value of the division or `None` if error occurs.  
- Without importing modules.

---

### 4. Divide a list
**File:** `4-list_division.py`  
Divides two lists element by element.  
- Returns a new list of length `list_length` with all divisions.  
- Handles errors: wrong type, division by 0, out of range.  
- Without importing modules.

---

### 5. Raise exception
**File:** `5-raise_exception.py`  
Raises a type exception.  
- Without importing modules.

---

### 6. Raise a message
**File:** `6-raise_exception_msg.py`  
Raises a name exception with a message.  
- Without importing modules.
