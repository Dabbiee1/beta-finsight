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





def hello(to= "world"):
    print(f"Hello {to}!")