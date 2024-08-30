n = int(input("Введите количество чисел: "))
numbers = list(map(int, input(f'Введите через пробел {n} чисел: ').split()))

print(len(set(numbers)))
