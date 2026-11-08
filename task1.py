def caching_fibonacci():
    """Створює функцію fibonacci(n) з кешем для вже обчислених чисел Фібоначчі."""
    cache = {} # тут зберігаються пораховані значення

    def fibonacci(n):
        """Повертає n-те число Фібоначчі, використовуючи кеш."""
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))