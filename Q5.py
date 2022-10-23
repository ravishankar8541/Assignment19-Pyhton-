# Write a python program to create a function which expects a list as an argument.

def f1(*args):
    for a in args:
        print(a)
list=["pawan","satish",3,7,4]
print(*list)        