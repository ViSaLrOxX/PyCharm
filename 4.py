print("Please enter the number for the fibonacci sequence:")
x = int(input())
def fib(x):
    if x==0 or x == 1:
        return
    else:
        return fib(x-1) + fib(x-2)
print(fib(x))