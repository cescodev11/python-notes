name = input("What's your name? ").strip().title()

# end removes the space from two different functions by not creating a line
# print("Hello, ", end="")

# remove whitespace from str
# name = name.strip()

# Capitalize Users name
# name = name.capitalize()

# title capatalize things that would be capatilize such as a book and a name
# name = name.title()


# Split users name into first and last name so you can call the first or last name variable instead
first, last = name.split(" ")


# f formates the function in a different manner
print(f"Hello, {name}")
