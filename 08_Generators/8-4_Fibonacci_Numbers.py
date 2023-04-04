# Fibonacci of a number N (fib(N)) is equal to fib(N-1)+fib(N-2)

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


fib_20 = fib(20)
print(list(fib_20))
