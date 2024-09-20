def fibonacci(n):
    if n <= 0:
        return ValueError("Input should be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence
    
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))