# Сложные моменты и исключения в стеке вызовов функции
def personal_sum(numbers):
    s, in_corect = 0, 0
    for i in numbers:
        try:
             s += i
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            in_corect += 1
    return s, in_corect

def calculate_average(numbers):
    try:
        sum, count = personal_sum(numbers)
        return round(sum / (len(numbers) - count), 2)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
