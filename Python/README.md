# 🐍 Python Programming

Python is a general-purpose language widely used in automation, backend development, data science, and AI.

## Setup

Install Python from [python.org](https://www.python.org/downloads/). Check the installation:

```bash
python --version
```

Run a script:

```bash
python main.py
```

## Variables and types

```python
name = "Ronit"
age = 20
cgpa = 7.94
is_learning = True

print(name, age, cgpa, is_learning)
print(type(age))
```

Common built-in types include `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, and `dict`.

## Conditions and loops

```python
number = 12

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

for value in range(1, 6):
    print(value)

count = 3
while count > 0:
    print(count)
    count -= 1
```

## Functions

```python
def calculate_area(length: float, width: float) -> float:
    return length * width

print(calculate_area(5, 3))
```

Prefer small functions with clear names and one main responsibility.

## Collections

```python
numbers = [4, 2, 8]
numbers.append(10)
print(numbers[0])

student = {"name": "Ronit", "year": 3}
print(student["name"])

unique_values = {1, 2, 2, 3}
print(unique_values)

coordinates = (10, 20)
print(coordinates[0])
```

- `list`: ordered, mutable collection.
- `tuple`: ordered, immutable collection.
- `set`: collection of unique values.
- `dict`: key-value mapping.

## List comprehension

```python
squares = [n * n for n in range(1, 6)]
even_numbers = [n for n in range(10) if n % 2 == 0]
```

## Object-oriented programming

```python
class Student:
    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score

    def introduce(self) -> str:
        return f"I am {self.name}; my score is {self.score}."

student = Student("Ronit", 92)
print(student.introduce())
```

Learn classes, objects, encapsulation, inheritance, polymorphism, and composition. Prefer composition when it models the relationship more clearly.

## Exceptions and files

```python
try:
    value = int(input("Enter an integer: "))
    print(100 / value)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Zero cannot be used as the divisor.")
```

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python")
```

The `with` statement closes the file automatically.

## Virtual environments

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install and record dependencies:

```bash
python -m pip install requests
python -m pip freeze > requirements.txt
```

## Practice exercises

1. Build a temperature converter.
2. Count word frequencies in a text file.
3. Create a contact book using a dictionary.
4. Build a bank account class.
5. Fetch data from a public API and display selected fields.
6. Create a command-line expense tracker.

## Official resource

[Python Tutorial](https://docs.python.org/3/tutorial/)
