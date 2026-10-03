def fibonacci(n):
    series = []
    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


n = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
print(*fibonacci(n))
