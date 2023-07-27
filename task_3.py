# ✔Создайте функцию генератор чисел Фибоначчи


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()
for _ in range(100):
    print(next(fib))