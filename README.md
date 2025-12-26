# Python Practice

A collection of beginner-friendly Python examples, exercises, and small projects used for hands-on practice and learning.

Contents
--------
- Python_Basics.ipynb — main Jupyter notebook with tutorial sections and exercises (variables, strings, lists, loops, functions, and more).

Getting Started
---------------
1. Install Python (3.8+ recommended): https://www.python.org/
2. Install Jupyter or use VS Code's Jupyter support:

	- To install Jupyter: `pip install jupyter`
	- Start the notebook: `jupyter notebook` or open the workspace in VS Code and open the `.ipynb` file.

What you'll find
-----------------
- Step-by-step annotated examples that cover Python basics.
- Short exercises such as even/odd separation, multiplication tables, and a guess-the-number game.
- Practical usage examples showing input/output and simple control flow.
 
## OOP Notebooks and Assignments

- `OOP.ipynb` — an interactive Jupyter notebook that covers Object-Oriented Programming topics with examples and exercises. Main sections include:
	- Basic Class and Object
	- Class Method and `self`
	- Inheritance
	- Encapsulation (public/protected/private attributes)
	- Polymorphism
	- Class Variables
	- Static Methods
	- Property Decorators
	- Class Inheritance and `isinstance()`
	- Multiple Inheritance

	Open this notebook in Jupyter or VS Code to run cells interactively: [OOP.ipynb](OOP.ipynb)

- `OOP_Major Assignment.py` — a Python script containing the major assignment for the OOP section (exercises, example implementations, and test runs). Open or run it with Python to execute the included examples: [OOP_Major Assignment.py](OOP_Major%20Assignment.py)

Usage
-----

Detailed: `OOP_Major Assignment.py`
---------------------------------
- Purpose: a self-contained script implementing a small OOP example set used as the "major assignment" for the OOP notebook. It demonstrates class design, inheritance, property decorators, class/instance methods, and simple runtime tests.

- Key classes and responsibilities:
	- `Person` — base class with `name`, `age`, `info()` and `from_string()` classmethod.
	- `Student` — derives from `Person`, adds private grade storage with `@property` getter/setter, `school_name` class variable, and `show_details()`.
	- `Teacher` — derives from `Person`, provides `show_details()` and static method `is_eligible(age)`.
	- `Course` — demonstrates property decorators for `course_title` with validation.
	- `Teacher_assistant` — example of multiple inheritance (`Student`, `Teacher`) with a `role()` method.

- Helper function:
	- `check_role(obj)` — returns a short string identifying whether an object is a `Student` or `Teacher` (uses `isinstance`).

- Example runtime behavior (what the script does when executed):
	- Creates sample objects (`Student`, `Teacher`, `Teacher_assistant`).
	- Updates grades via the setter.
	- Prints details and demonstrates `isinstance()` and MRO via `Teacher_assistant.mro()`.

- How to run:

	1. From the repo root run:

		 ```powershell
		 python "OOP_Major Assignment.py"
		 ```

	2. Or open `OOP_Major Assignment.py` in the editor and run the file.

- Notes / suggestions:
	- The script is safe to run with Python 3.8+. No external packages required.
	- The script prints example outputs; use it as a reference or extend it for additional exercises.

- Open [Python_Basics.ipynb](Python_Basics.ipynb) in Jupyter or VS Code and run cells interactively.
- No external dependencies beyond the Python standard library for the included examples.

Contributing
------------
Feel free to add more exercises or improvements. Create a new branch, add your examples, and open a pull request.

License
-------
This repository is for educational use. No license specified — contact the owner for reuse permissions.

