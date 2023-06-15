# x = int(input("What's x ? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(input("What's x ? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


# this returns a number divided by 2 to equal 0 and if it does it's even and if not it's odd. This automatically creates and True and False answer or a boolean
def is_even(n):
    return n % 2 == 0


main()
