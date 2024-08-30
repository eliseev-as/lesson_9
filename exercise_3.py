numbers = set()

for i in input("Введите через пробел последовательность чисел: ").split():
    if i not in numbers:
        numbers.add(i)
        print(f'Число {i} - NO')
    else:
        print(f'Число {i} - YES')
