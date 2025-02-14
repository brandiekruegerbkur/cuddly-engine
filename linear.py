def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

arr = list(map(int, input("Введите массив через пробел: ").split()))
target = int(input("Введите число для поиска: "))

index = linear_search(arr, target)
if index != -1:
    print(f"Число {target} найдено в массиве на позиции {index}.")
else:
    print(f"Число {target} не найдено в массиве.")