def bubble_sort(arr):
    length = len(arr)

    for i in range(length):
        swapped = False

        for j in range(0, length - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

Arr = [50, 40, 30, 20, 10, 60, 70]

print(f"Befor: {Arr}")

bubble_sort(Arr)

print(f"After: {Arr}")