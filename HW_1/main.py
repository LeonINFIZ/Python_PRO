import colorama
import requests
import functools
from colorama import Fore as Color
from pympler import asizeof

colorama.init()

def measure_memory(f):
    """Декоратор для вимірювання пам'яті"""

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        before_memory = asizeof.asizeof(wrapper._cache)
        print(f"{Color.MAGENTA}Пам'ять до: {before_memory} байт{Color.RESET}")

        # Виконуємо функцію
        result = f(*args, **kwargs)

        after_memory = asizeof.asizeof(wrapper._cache)
        memory_used = after_memory - before_memory
        if memory_used != 0:  # Виводити тільки, якщо змінилась пам'ять
            print(f"{Color.MAGENTA}Пам'ять після: {after_memory} байт{Color.RESET}")
            print(f"{Color.MAGENTA}Використано пам'яті: {memory_used} байт{Color.RESET}")

        return result

    wrapper._cache = {}  # Ініціалізація кешу
    return wrapper


def cache(max_limit=64):
    """Декоратор для кешування"""

    def internal(f):
        @measure_memory
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))  # Формуємо унікальний ключ для кешу

            if cache_key in deco._cache:  # Якщо дані вже в кеші
                result, count = deco._cache[cache_key]  # Отримуємо результат і кількість звернень
                count += 1
                deco._cache[cache_key] = (result, count)  # Оновлюємо кеш
            else:  # Якщо даних немає в кеші
                result = f(*args, **kwargs)
                if len(deco._cache) >= max_limit:  # Якщо кеш переповнений
                    least_used_key = min(deco._cache,
                                         key=lambda k: deco._cache[k][1])  # Знаходимо найменше використаний ключ
                    del deco._cache[least_used_key]  # Видаляємо його з кешу
                deco._cache[cache_key] = (result, 1)  # Додаємо новий результат до кешу
            return deco._cache[cache_key][0]

        deco._cache = {}  # Ініціалізація кешу всередині `cache`
        return deco

    return internal


@cache(3)
def fetch_url(url, first_n=40):
    """Функція для завантаження даних за URL"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


print(f"1 {Color.BLUE}Response from {Color.GREEN}python.org{Color.BLUE}: ", fetch_url("https://www.python.org"), Color.RESET)
print(f"2 {Color.BLUE}Response from {Color.GREEN}python.org{Color.BLUE}: ", fetch_url("https://www.python.org"), Color.RESET)
print(f"3 {Color.BLUE}Response from {Color.GREEN}google.com{Color.BLUE}: ", fetch_url("https://google.com"), Color.RESET)
print(f"4 {Color.BLUE}Response from {Color.GREEN}google.com{Color.BLUE}: ", fetch_url("https://google.com"), Color.RESET)
print(f"5 {Color.BLUE}Response from {Color.GREEN}python.org{Color.BLUE}: ", fetch_url("https://www.python.org"), Color.RESET)
print(f"6 {Color.BLUE}Response from {Color.GREEN}google.com{Color.BLUE}: ", fetch_url("https://google.com"), Color.RESET)
print(f"7 {Color.BLUE}Response from {Color.GREEN}google.com{Color.BLUE}: ", fetch_url("https://google.com"), Color.RESET)
print(f"8 {Color.BLUE}Response from {Color.GREEN}translate.google.com{Color.BLUE}: ", fetch_url("https://translate.google.com"), Color.RESET)
print(f"9 {Color.BLUE}Response from {Color.GREEN}translate.google.com{Color.BLUE}: ", fetch_url("https://translate.google.com"), Color.RESET)
print(f"10 {Color.BLUE}Response from {Color.GREEN}youtube.com{Color.BLUE}: ", fetch_url("https://www.youtube.com"), Color.RESET)
print(f"11 {Color.BLUE}Response from {Color.GREEN}youtube.com{Color.BLUE}: ", fetch_url("https://www.youtube.com"), Color.RESET)
print(f"12 {Color.BLUE}Response from {Color.GREEN}translate.google.com{Color.BLUE}: ", fetch_url("https://translate.google.com"), Color.RESET)
print(f"13 {Color.BLUE}Response from {Color.GREEN}translate.google.com{Color.BLUE}: ", fetch_url("https://translate.google.com"), Color.RESET)
print(f"14 {Color.BLUE}Response from {Color.GREEN}translate.google.com{Color.BLUE}: ", fetch_url("https://translate.google.com"), Color.RESET)
print(f"15 {Color.BLUE}Response from {Color.GREEN}translate.google.com{Color.BLUE}: ", fetch_url("https://translate.google.com"), Color.RESET)
print(f"16 {Color.BLUE}Response from {Color.GREEN}youtube.com{Color.BLUE}: ", fetch_url("https://www.youtube.com"), Color.RESET)
print(f"17 {Color.BLUE}Response from {Color.GREEN}python.org{Color.BLUE}: ", fetch_url("https://www.python.org"), Color.RESET)
