import calc_art
print(calc_art.logo)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    print("Welcome to Calculator")
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    o=input("Enter operation: + - * /: ")
    if o == "+":
        r=add(a,b)
    elif o == "-":
        r=sub(a,b)
    elif o == "*":
        r=mul(a,b)
    elif o == "/":
        r=div(a,b)
    else:
        print("Invalid operation")

    print("The result is",r)

    choice = input("Do you want to continue? (y/n): ")
    if choice in "nN":
        break

