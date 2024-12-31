def display(n):
    print("i'm the function one")
    n()
def one():
    print("i'm the first nested function")
def two():
    print("i'm the second nested function")
display(one)
display(two)