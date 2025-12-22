# Python Input/Output Project

## 📚 Project Overview

This project dives into file handling, JSON serialization, and data persistence in Python. Through practical implementation, students master reading/writing files, working with JSON for data exchange, and building robust object serialization systems.

---

## 🎯 Learning Goals

### File Operations
* **Reading Files** - Extract data from text files efficiently
* **Writing Files** - Create and modify file contents
* **Context Managers** - Use `with` statement for safe file handling
* **Error Handling** - Manage file permission and existence issues

### Data Serialization
* **JSON Conversion** - Transform Python objects to/from JSON
* **Object Persistence** - Save and restore object states
* **Class Serialization** - Implement custom serialization methods
* **Data Interchange** - Exchange data between systems

### Advanced Concepts
* **Command Line Arguments** - Process user input from terminal
* **Algorithm Design** - Build Pascal's triangle generator
* **Text Processing** - Parse and analyze log files
* **Pattern Matching** - Search and modify file contents

---

## 💻 Technical Requirements
```
Language:    Python 3.8.5
Style Guide: PEP 8 (pycodestyle 2.7.*)
Permissions: All files executable (chmod +x)
Context:     Use 'with' statement for files
Encoding:    UTF-8 for all file operations
```

---

## 📂 Project Structure
```
python-input_output/
│
├── 0-read_file.py              # File reading basics
├── 1-write_file.py             # File writing with count
├── 2-append_write.py           # Append to files
├── 3-to_json_string.py         # Object to JSON
├── 4-from_json_string.py       # JSON to object
├── 5-save_to_json_file.py      # Save JSON to file
├── 6-load_from_json_file.py    # Load JSON from file
├── 7-add_item.py               # CLI list manager
├── 8-class_to_json.py          # Class to dict converter
├── 9-student.py                # Basic Student class
├── 10-student.py               # Filtered serialization
├── 11-student.py               # Full persistence cycle
├── 12-pascal_triangle.py       # Triangle generator
├── 100-append_after.py         # Pattern-based insertion
└── 101-stats.py                # Log parser with stats
```

---

## 🔧 Task Breakdown

### Core File Operations (Tasks 0-2)

**Task 0: Read File**
```python
def read_file(filename=""):
    # Read and print file contents
```

**Task 1: Write File**
```python
def write_file(filename="", text=""):
    # Write text and return character count
```

**Task 2: Append to File**
```python
def append_write(filename="", text=""):
    # Append text and return added count
```

---

### JSON Serialization (Tasks 3-7)

**Task 3-4: String Conversion**
- Convert Python objects to JSON strings
- Parse JSON strings back to Python objects

**Task 5-6: File Persistence**
- Save objects to JSON files
- Load objects from JSON files

**Task 7: CLI Integration**
- Manage persistent lists via command line
- Combine file I/O with system arguments

---

### Object Serialization (Tasks 8-11)

**Task 8: Generic Class Converter**
```python
def class_to_json(obj):
    # Convert any class instance to dictionary
```

**Task 9-11: Student Class Evolution**
1. Basic serialization (`to_json()`)
2. Filtered attributes (`to_json(attrs)`)
3. Deserialization (`reload_from_json()`)

---

### Advanced Tasks (Task 12, 100-101)

**Task 12: Pascal's Triangle**
- Algorithm implementation
- List of lists structure
- Mathematical computation

**Task 100: Smart Text Insertion**
- Pattern matching in files
- Conditional line insertion
- File modification

**Task 101: Log Analysis**
- Stream processing (stdin)
- Real-time statistics
- Keyboard interrupt handling

---

## ⚙️ Installation & Usage

### Setup
```bash
# Clone repository
git clone https://github.com/illo888/holbertonschool-higher_level_programming.git

# Navigate to project
cd holbertonschool-higher_level_programming/python-input_output

# Make files executable
chmod +x *.py
```

### Example Usage
```python
# JSON Serialization
from task_00_basic_serialization import serialize_and_save_to_file

data = {"name": "Alice", "age": 25}
serialize_and_save_to_file(data, 'output.json')

# Student Class
from task_09_student import Student

student = Student("John", "Doe", 23)
print(student.to_json())
```

---

## 🎓 Key Takeaways

By completing this project, you will understand:

✅ How to safely handle file operations in Python  
✅ The importance of context managers (`with` statement)  
✅ JSON as a universal data interchange format  
✅ Object serialization for data persistence  
✅ Stream processing for large datasets  
✅ Error handling in file I/O operations

---

## 👩‍💻 Developer

**Student Developer**
- GitHub: [@illo888](https://github.com/illo888)
- Email: shadeenn1424@gmail.com
- Project: Python Input/Output

---

## 📖 Resources

- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [JSON Module](https://docs.python.org/3/library/json.html)
- [Context Managers](https://docs.python.org/3/reference/compound_stmts.html#with)
- [Sys Module](https://docs.python.org/3/library/sys.html)
