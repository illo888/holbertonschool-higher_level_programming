## 📋 Summary Table
| Script | Description |
|--------|-------------|
| `1-last_digit.py` | Print last digit of a random number with conditions |
| `2-print_alphabet.py` | Print lowercase alphabet |
| `3-print_alphabt.py` | Print lowercase alphabet except q and e |
| `4-print_hexa.py` | Print numbers 0 to 98 in decimal and hex |
| `5-print_comb2.py` | Print numbers from 00 to 99 |
| `6-print_comb3.py` | Print all possible different combinations of two digits |
| `7-islower.py` | Check if a character is lowercase |
| `8-uppercase.py` | Convert string to uppercase |
| `9-print_last_digit.py` | Print and return last digit of a number |
| `10-add.py` | Add two integers |
| `11-pow.py` | Compute a to the power of b |
| `12-fizzbuzz.py` | Print numbers from 1 to 100 with FizzBuzz rules |

---

## ✅ Scripts & Outputs

### **1-last_digit.py**
```python
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else number % -10
string = f"Last digit of {number} is {last_digit}"
if last_digit > 5:
    print(f"{string} and is greater than 5")
elif last_digit == 0:
    print(f"{string} and is 0")
else:
    print(f"{string} and is less than 6 and not 0")
```
**Output (Example):**
```
Example: Last digit of -1234 is -4 and is less than 6 and not 0
```

---

### **2-print_alphabet.py**
```python
for i in range(97, 123):
    print("{}".format(chr(i)), end="")
```
**Output (Example):**
```
abcdefghijklmnopqrstuvwxyz
```

---

### **3-print_alphabt.py**
```python
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
```
**Output (Example):**
```
abcdfghijklmnoprstuvwxyz
```

---

### **4-print_hexa.py**
```python
for i in range(99):
    print("{} = {}".format(i, hex(i)))
```
**Output (Example):**
```
0 = 0x0
1 = 0x1
...
98 = 0x62
```

---

### **5-print_comb2.py**
```python
for i in range(100):
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
```
**Output (Example):**
```
00, 01, 02, ..., 99
```

---

### **6-print_comb3.py**
```python
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
```
**Output (Example):**
```
01, 02, ..., 89
```

---

### **7-islower.py**
```python
def islower(c):
    ascii_val = ord(c)
    return ascii_val >= ord('a') and ascii_val <= ord('z')
```
**Output (Example):**
```
islower('a') -> True, islower('A') -> False
```

---

### **8-uppercase.py**
```python
def uppercase(str):
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
```
**Output (Example):**
```
uppercase('best') -> BEST
```

---

### **9-print_last_digit.py**
```python
def print_last_digit(number):
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
```
**Output (Example):**
```
print_last_digit(-1024) -> prints 4 and returns 4
```

---

### **10-add.py**
```python
def add(a, b):
    return a + b
```
**Output (Example):**
```
add(1, 2) -> 3
```

---

### **11-pow.py**
```python
def pow(a, b):
    return a ** b
```
**Output (Example):**
```
pow(2, 3) -> 8
```

---

### **12-fizzbuzz.py**
```python
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
```
**Output (Example):**
```
1 2 Fizz 4 Buzz ... FizzBuzz
```

---
