# Edutech Solution - Python Development Internship
## Task 1: Python Environment & Syntax Basics

## 📋 Project Overview

This repository contains the solution for **Task 1: Python Environment & Syntax Basics** from the Edutech Solution Python Development Internship program.

### What's Included:
- ✅ Python script demonstrating Hello World
- ✅ Variable experiments and data type exploration
- ✅ PEP 8 compliant code
- ✅ Answers to interview questions
- ✅ Environment setup documentation

---

## 📁 Files in This Repository

```
.
├── hello_world.py          # Main Python script with all demonstrations
├── README.md               # This file with documentation
└── screenshots/            # Folder containing setup screenshots
    └── setup_screenshot.png
```

---

## 🚀 How to Run This Project

### Prerequisites:
- Python 3.x installed on your system
- VS Code or PyCharm (optional IDE)
- Git installed for version control

### Installation Steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/s2hruti5/edutech-python-task1.git
   cd edutech-python-task1
   ```

2. **Check Python installation:**
   ```bash
   python --version
   python3 --version
   ```

3. **Run the script:**
   ```bash
   python hello_world.py
   ```
   or
   ```bash
   python3 hello_world.py
   ```

### Expected Output:
```
Hello, World!
Welcome to Python Programming!

Name: Shruti, City: Pune
Age: 21, Student ID: 12345
CGPA: 9.85, Height: 5.6m
...
[More output as shown in the script]
```

---

## 📚 Interview Questions & Answers

### ❓ Question 1: Difference between Python 2 and Python 3

#### **Python 2 vs Python 3: Key Differences**

| Feature | Python 2 | Python 3 |
|---------|----------|----------|
| **Release Year** | 2000 | 2008 |
| **EOL (End of Life)** | January 1, 2020 | Still Active |
| **Print Function** | `print "Hello"` | `print("Hello")` |
| **String Encoding** | ASCII by default | Unicode (UTF-8) by default |
| **Division** | `/` gives integer if both operands are integers | `/` always gives float |
| **Integer Division** | `/` for integer division | `//` for integer division |
| **Unicode** | Limited support (`u"text"`) | Full Unicode support |
| **Range Function** | `range()` returns a list | `range()` returns an iterator |
| **Dictionary Methods** | `.keys()`, `.values()`, `.items()` return lists | Return dict_keys, dict_values, dict_items objects |
| **Exception Syntax** | `except Exception, e:` | `except Exception as e:` |
| **Input Function** | `raw_input()` for strings | `input()` for strings |
| **Type System** | Old-style and new-style classes | Only new-style classes |
| **Library Support** | Many third-party libraries | Better and modern libraries |

#### **Why Python 3?**
- ✅ Better Unicode support for international characters
- ✅ Cleaner syntax and semantics
- ✅ Improved performance
- ✅ Better error handling
- ✅ Modern language features (type hints, async/await)
- ✅ Still actively maintained and updated
- ✅ Industry standard for new projects
- ⚠️ Python 2 is no longer supported (EOL: January 1, 2020)

#### **Example Code Comparison:**

**Python 2:**
```python
print "Hello, World!"
name = raw_input("Enter your name: ")
print "Your name is " + name
```

**Python 3:**
```python
print("Hello, World!")
name = input("Enter your name: ")
print(f"Your name is {name}")
```

---

### ❓ Question 2: What are PEP 8 Guidelines?

#### **PEP 8: Style Guide for Python Code**

**PEP** stands for **Python Enhancement Proposal**. **PEP 8** is the official style guide for writing Python code that is readable, consistent, and maintainable.

#### **Key PEP 8 Guidelines:**

##### **1. Naming Conventions**
```python
# ✅ Good
student_name = "Alice"
total_marks = 95
is_active = True
MAXIMUM_ATTEMPTS = 5

# ❌ Bad
studentName = "Alice"  # Camel case (use snake_case)
totalmarks = 95        # No underscore
IsActive = True        # Class style for variable
max_attempts = 5       # Should be MAXIMUM_ATTEMPTS for constants
```

**Rules:**
- **Variables & Functions:** `snake_case` (lowercase with underscores)
- **Classes:** `PascalCase` (capitalize first letter of each word)
- **Constants:** `UPPER_CASE` (all uppercase with underscores)
- **Avoid:** Single-letter variable names (except `i`, `j`, `k` in loops)

##### **2. Indentation**
```python
# ✅ Good - Use 4 spaces
def calculate_gpa(scores):
    if scores:
        total = sum(scores)
        count = len(scores)
        gpa = total / count
        return gpa
    else:
        return 0.0

# ❌ Bad - Inconsistent indentation or tabs
def calculate_gpa(scores):
  if scores:
      total = sum(scores)
        count = len(scores)
```

**Rules:**
- Use **4 spaces** per indentation level
- Never mix tabs and spaces
- Most editors have auto-indentation

##### **3. Line Length**
```python
# ✅ Good - Keep lines under 79 characters
def long_function_name(parameter1, parameter2, parameter3,
                       parameter4, parameter5):
    pass

# ❌ Bad - Line too long
def long_function_name(parameter1, parameter2, parameter3, parameter4, parameter5):
    pass
```

**Rules:**
- Maximum line length: **79 characters**
- Comments & docstrings: **72 characters**
- Long lines can be broken using parentheses

##### **4. Whitespace**
```python
# ✅ Good
age = 25
result = x + y
my_dict = {"name": "Alice", "age": 25}
my_list = [1, 2, 3, 4]

# ❌ Bad
age=25
result=x+y
my_dict = { "name" : "Alice" , "age" : 25 }
my_list=[1,2,3,4]
```

**Rules:**
- Surround operators with single spaces: `x = y + z`
- No space before colon in dictionary
- One space after commas in lists/tuples
- No extra spaces before opening parenthesis

##### **5. Comments & Docstrings**
```python
# ✅ Good
def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Sum of a and b
    """
    return a + b

# Single line comment explaining logic
total = sum(scores) / len(scores)  # Calculate average

# ❌ Bad
def add(a,b):  # This function adds two numbers
    return a+b

# Unclear docstring
def add(a, b):
    """Adds"""
    return a + b
```

**Rules:**
- Use `#` for inline comments
- Use `"""..."""` for docstrings
- Comments should be complete sentences
- Keep docstrings descriptive

##### **6. Imports**
```python
# ✅ Good
import os
import sys
from datetime import datetime
from math import sqrt, pi

# ❌ Bad
import os, sys
from datetime import *  # Never use wildcard imports
import os; import sys   # Don't put multiple imports on one line
```

**Rules:**
- One import per line (or related imports from same module)
- Standard library imports first
- Third-party imports second
- Local imports third
- Use absolute imports
- Avoid wildcard imports

##### **7. Blank Lines**
```python
# ✅ Good
class Student:
    """Student class"""
    
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        """Display student information"""
        print(self.name)


def calculate_average(scores):
    """Calculate average score"""
    return sum(scores) / len(scores)
```

**Rules:**
- 2 blank lines between top-level functions/classes
- 1 blank line between methods in a class
- Use blank lines sparingly inside functions

