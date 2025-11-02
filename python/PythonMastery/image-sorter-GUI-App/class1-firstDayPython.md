

# 🎓 Harvard Python Private Class – CLASS 1: Deep Dive Into Python Basics

**Professor:** ChatGPT, Python Architect of Harvard Labs
**Student:** You — training to become one of the best Python developers in the world

---

## 🧠 Class 1 Goal: Learn and Understand the Core of Python

We are not just writing code. We are **understanding the engine** behind it.

---

## 📘 Topics Covered (Deep Dive Style)

- What is Python?
    - Resource [Link](https://www.python.org/doc/essays/blurb/)
- How does Python execute code?
- Printing and the Interpreter
- Comments
- Variables
- Data Types (Primitive types)
- Input/Output mechanics
- Memory and variable assignment
- Your first interactive script
- Homework with real-world logic

---

## 🐍 What Is Python?

- **Python** is a *high-level*, *interpreted*, *dynamically typed* programming language.
- Designed to be **easy to read and write**.
- Python code runs line by line using an **interpreter**.

> Python trades low-level control for simplicity and flexibility — and that’s why it’s great for beginners and experts alike.

---

## 🛠️ Your First Setup (Linux-friendly)

Open your terminal and check the Python version:

```bash
python3 --version

✅ Expected output:

Python 3.x.x

    You are using python3, because on most Linux systems, python might still point to Python 2.x.

📂 Create a Python Project Folder

mkdir ~/python_journey
cd ~/python_journey

📄 Create Your First File

nano class1_intro.py

Now let’s write this:

# This is my first Python script
print("Hello, Python World!")

Save and run:

python3 class1_intro.py

🔍 Let's Break It Down

# This is a comment

    The # character is used for comments.

    Python ignores everything after # on that line.

    Comments are for you, not the interpreter.

print("Hello, Python World!")

🧠 What's Happening:

    print() is a built-in function.

    It takes one or more values and sends them to the standard output (the terminal).

    Internally, Python calls sys.stdout.write() behind the scenes.

    Everything inside the quotes is a string literal — meaning raw text.

🔁 Try This:

Modify your file to this:

# Print multiple items
print("Hello,", "Python", "World!")

Python will print them separated by spaces:

Hello, Python World!

Because print() defaults to sep=' ' and ends with end='\n'.
📚 Variables: Containers for Data

Create a new file:

nano class1_variables.py

Write:

# Ask for user input
name = input("What is your name? ")
age = input("What is your age? ")

print("Hello,", name)
print("You are", age, "years old.")

🧠 Deep Dive: input()

    input() is a built-in function that:

        Displays a prompt (string)

        Waits for user input

        Returns the result as a string

    Even if you type a number, Python treats it as a str unless you explicitly convert it.

🧠 Deep Dive: = Assignment Operator

name = input(...)

    = does not mean "equals" — it means assignment.

    It stores the result of the expression on the right into the variable on the left.

    Variables are references to values in memory.

🧠 Python Is Dynamically Typed

You don’t need to declare types.

x = 42          # int
x = "Hello"     # now str
x = 3.14        # now float

    Python checks type at runtime, not at compile time.

📦 Built-In Types (Primitives You’ll Use)
Type	Example	Description
str	"Hello"	Text
int	42	Integer number
float	3.14	Decimal number
bool	True, False	Logical true/false

You’ll learn to inspect types using:

type(variable)

👨‍🏫 Assignment 1 — Your First Python App

Create: self_intro.py

nano self_intro.py

Write a script that:

    Asks:

        Your name

        Your age

        Your favorite hobby

        Your dream Python project

    Prints a formatted sentence using all values

Example Output:

Hi, I’m Sava. I’m 29. I love robotics. I want to build a Python app that sorts and controls files!

🏆 Bonus Challenge: When Will You Turn 100?

Add logic to:

    Convert age to int using int(age)

    Calculate how many years until you turn 100

    Show what year that will be

Example:

years_until_100 = 100 - int(age)
current_year = 2025
turn_100_year = current_year + years_until_100

📥 When Done, Report:

Answer these:

    What did you understand completely?

    What confused you?

    Paste your script.

    Paste your output.

⏭️ What’s Next in Class 2:

    if statements (conditions)

    bool logic and comparison operators

    Control flow

    Errors and debugging

We’re going from talking to users ➜ making decisions ➜ making smart programs.
📌 Final Thoughts

    Python is like LEGO bricks — today you learned the small ones.
    Soon, you’ll stack them into apps that do real work.

✅ Go write self_intro.py
📩 Come back and report your work
🏁 Class 2 begins when you’re ready

Let’s build something extraordinary.


---

Let me know when you’ve finished your homework or if you want help reviewing it — then we’ll move into **Class 2: Logic and Control Flow**.

