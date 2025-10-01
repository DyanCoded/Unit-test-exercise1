def main():
    n = int(input("Enter a number: "))
    factorial(n)
    fibonacci(n)
    fizzbuzz(n)
    print(factorial(n))
    print(fibonacci(n))
    print(fizzbuzz(n))

def factorial(n):
    if n < 0:
        raise ValueError("Negative values are not allowed.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result = result * i
        return result

def fibonacci(n):
    if n < 0:
        raise ValueError("Input should be a positive integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fizzbuzz(n):
    list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(str(i))
    return list

if __name__ == "__main__":
    main()