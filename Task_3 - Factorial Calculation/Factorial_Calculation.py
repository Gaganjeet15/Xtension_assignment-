def factorial(num):
    if num < 0:
        return ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, num+1):
        result *= i
    return result
    
print(factorial(5))