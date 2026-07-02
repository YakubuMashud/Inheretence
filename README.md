# Inheritance in OOP

This repository demonstrates object-oriented inheritance using a simple Python example.

## Example: `INHERETANCE.py`

- `Person` is the base class with shared attributes and behavior.
- `Student` and `Lecturer` inherit from `Person`.
- `Student` overrides `display_info()` and adds `enroll_course()`.
- `Lecturer` inherits `display_info()` and adds `teach_course()`.

## Why it matters

Inheritance lets subclasses reuse and extend base class behavior.

- shared data and methods are defined once in the parent class
- subclasses add specialized features
- subclasses can override parent methods when behavior differs

## Running the example

```bash
python INHERETANCE.py
```

Expected output includes student details, enrollment confirmation, lecturer details, and teaching information.
