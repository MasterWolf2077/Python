#Ex 1
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()

#Ex 2
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")

#Ex 3
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")

#Ex 4
# def add_numbers(a, b=2, c):    #SyntaxError: non-default argument follows default argument
#    print(a + b + c)

#add_numbers(a=1, c=3)