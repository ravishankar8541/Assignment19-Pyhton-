"""Write a python program to create a function which expects kwargs arguments."""
def fun_Name(**t):
    for a,k in t.items():
        print(a,k)
dic={"a":8,"b":6,"c":90}
fun_Name(**l)
