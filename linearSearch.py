def linear_search(array, traget):
    for i in range(len(array)):
        if array[i] == traget:
            return i
            break
    return -1


def find(array, target):
    val = linear_search(array, target)
    if val > -1:
        print(f"Value of index: {val}")
    else:
        print("Value not fond")


Arr = [10, 20, 30 ,40, 50]

find(Arr, 50)

print(Arr[4])
