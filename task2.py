from typing import Callable, Iterator


def generator_numbers(text: str) -> Iterator[float]:
    """Генератор: по одному повертає всі дійсні числа з тексту."""
    for word in text.split():  # розрізаємо текст на окремі слова
        try:
            yield float(word)  # слово — число: віддаємо його
        except ValueError:
            continue           # не число: пропускаємо


def sum_profit(text: str, func: Callable) -> float:
    """Повертає суму всіх дійсних чисел у тексті."""
    total = 0.0
    for number in func(text):
        total += number
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")