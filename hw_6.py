def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, val):
    n = len(arr)
    result_ok = False
    first = 0
    last = n - 1
    pos = -1

    while first <= last:
        middle = (first + last) // 2
        if arr[middle] == val:
            result_ok = True
            pos = middle
            break
        elif val > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        print(f"Элемент найден на позиции {pos}.")
        return pos
    else:
        print("Элемент не найден.")
        return -1


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print(f"Отсортированный список: {sorted_list}")

target = 25
binary_search(sorted_list, target)