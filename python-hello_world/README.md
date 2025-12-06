# 🐍 Python Basics – Holberton School Tasks

## 📋 Summary Table
| Script | Description |
|--------|-------------|
| `2-print.py` | Print a simple string |
| `3-print_number.py` | Print an integer with text |
| `4-print_float.py` | Print a float with 2 decimal places |
| `5-print_string.py` | Repeat a string and slice it |
| `6-concat.py` | Concatenate two strings |
| `7-edges.py` | Slice a word into parts |
| `8-concat_edges.py` | Create a new string by slicing |
| `9-easter_egg.py` | Print the Zen of Python |

---

## ✅ Scripts & Outputs

### **2-print.py**
```python
print("\"Programming is like building a multilingual puzzle")
```
**Output:**
```
"Programming is like building a multilingual puzzle
```

---

### **3-print_number.py**
```python
number = 98
print(f"{number} Battery street")
```
**Output:**
```
98 Battery street
```

---

### **4-print_float.py**
```python
number = 3.14159
print(f"Float: {number:.2f}")
```
**Output:**
```
Float: 3.14
```

---

### **5-print_string.py**
```python
str = "Holberton School"
print(str * 3)
print(str[:9])
```
**Output:**
```
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

---

### **6-concat.py**
```python
str1 = "Holberton"
str2 = "School"
str1 += " " + str2
print(f"Welcome to {str1}!")
```
**Output:**
```
Welcome to Holberton School!
```

---

### **7-edges.py**
```python
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```
**Output:**
```
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

---

### **8-concat_edges.py**
```python
str = "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
print(str)
```
**Output:**
```
object-oriented programming with Python
```

---

### **9-easter_egg.py**
```python
import this
```
**Output:**
```
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

---
