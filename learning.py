# Ask user for their name
name = input("What's your name? ").strip().title()

#Split user first name and last name
first, last = name.split(" ")

#Say hello to user
print("Hello", first + "!")

#Say hello to the user again
print(f"Hello {name}!")

#Another way
def hello(to= "world"):
    print(f"Hello {to}!")
hello()
name = input("What's your name? ").strip().title()
hello(name)
#Conditionals (if, elif, else)
#Concept: Conditional statements
# allow your program to make decisions
# and execute different blocks of code
# based on whether a certain condition
# is true or false.
#Example:
x = 5
y = 10
if x < y:
    print("x is less than y")
#elif statement:
# Short for "else if," it allows you to
# check for an additional condition if
# the preceding if or elif conditions
# were False.
#Example:
x = 10
y = 5
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
#else statement: Provides a fallback
# block of code to execute if none of
# the preceding if or elif conditions
# were True. It doesn't have a
# condition itself.
#Example:
x = 5
y = 5
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
"""Comparison Operators
Concept: These symbols are used 
to compare two values and return a 
Boolean result (True or False).
Operators and Examples:
> (greater than)
>= (greater than or equal to)
< (less than)
<= (less than or equal to)
== (equal to) - 
Crucially, use two equal signs 
for comparison, one for assignment.
!= (not equal to)
Example:"""
a = 10
b = 5
print(a > b)
# True print(a == b)
# False print(a != b)
"""3. Logical Operators (or, and)
Concept: These operators combine 
multiple Boolean expressions to form a 
more complex condition.
Or operator: Returns True if at least
 one of the conditions it connects is 
 True. """
#Example:
temperature = 25
is_raining = True
if temperature < 20 or is_raining:
        print("Might need a jacket "
              "or umbrella.")
"""And operator: Returns True only if 
all the conditions it connects are 
True."""
#Example:
score = 95
attendance = 100
if score >= 90 and attendance == 100:
    print("Excellent performance!")
"""4. Indentation and Colons
Concept: Python uses indentation 
(typically 4 spaces or one tab) 
and colons to define code blocks, 
unlike many other languages that use 
curly braces. This is a strict 
requirement for Python code to execute
 correctly."""
#Example:
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
"""5. Modulo Operator (%) 
Concept: The modulo operator returns 
the remainder of a division. It's 
particularly useful for determining if 
a number is even or odd, or if it's a 
multiple of another number."""
#Example (determining even/odd):
number = 7
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
"""6. Boolean Expressions and Boolean Type
Concept: A Boolean expression is any
 expression that evaluates to either 
 True or False. Python has a built-in
Boolean data type (bool) that can only 
hold these two values (True or False, 
capitalized)."""
#Example
is_hot = True
if is_hot:
    print("Wear light clothes.")
    result = (5 > 3)
    print(result)
"""7. Pythonic Expressions (Chaining Comparison Operators)
Concept: Python allows for a more 
concise way to express range checks 
by chaining comparison operators, 
making the code more readable and 
similar to mathematical notation. 
This is not common in other languages."""
#Example: Less Pythonic:
score = 85
if score >= 80 and score < 90:
    print("Grade B")
#More Pythonic (Chained):
score = 85
if 80 <= score < 90:
    print("Grade B")
"""8. Functions Returning Boolean Values 
Concept: You can define your own 
functions that return True or False 
based on some internal logic. This 
encapsulates complex checks and makes 
your main code cleaner."""
#Example (is_even function):
def is_even(number):
    if number % 2 == 0:
       return True
    else:
       return False
if is_even(number):
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

_ = 3
while _ != 0:
    print(f"{_} is an odd number.")
    _ = _ - 1
_ = 0
while _ < 3:
    print(f"{_} is an odd number.")
    _ += 1   #equals to _ = _ + 1
for _ in (0,1,2):
    print(f"{_} is an odd number.")
for i in range (0,3):
    print(f"{_} is an odd number.")
print(f"{_} is an odd number.\n"* 3, end="")
while True:
    n= int(input("Enter a number: "))
    if n > 0:
        break
for n in range (n):
    print("meow")
def main():
    number1 = get_number
    meow(number1)



def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            return n


def meow(number1):
    for n in range (number1):
        print("meow")



students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)
for r in range(len(students)):
    print(r + 1, students[r])

students1 = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor" ,
    "Ron": "Gryffindor"  ,
    "Draco": "Slytherin" ,
}

for student in students1:
    print(student, students1[student], sep=", ")
students2 = [
    {"name": "Hermione" ,
     "house": "Gryffindor",
     "patronus": "Otter"},
    {"name": "Harry" ,
     "house": "Gryffindor" ,
     "patronus" : "Stag"} ,
    {"name": "Ron" ,
     "house": "Gryffindor" ,
     "patronus": "Jack Russel terrier",},
    {"name": "Draco" ,
     "house": "Slytherin" ,
     "patronus": None}
]
for student in students2:
    print(student["name"], student["house"], student["patronus"], sep=", ")
