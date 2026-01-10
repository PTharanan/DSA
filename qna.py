def bubble_sort(arr):
    length = len(arr)

    for i in range(length):
        swapped = False;

        for j in range(0, length - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

def linear_search(arr, target):
    length = len(arr)
    found = False
    for i in range(length):
        if arr[i] == target:
            print(f"{arr[i]} கண்டுபிடிக்கப்பட்டது, index = {i}")
            found = True
            break
    if not found:
        print("no")

def binart_search(arr, target):

    start_index = 0
    last_index = len(arr) -1

    while start_index <= last_index:

        mid_index = (last_index+start_index) // 2

        if arr[mid_index] == target:
            print(f"{arr[mid_index]} கிடைத்தது, index = {mid_index}")
            return
        elif arr[mid_index] > target:
            last_index = mid_index -1
        else:
            start_index = mid_index +1

    print(f"{target} இல்லை")


arr = [5, 10, 15, 20, 25, 30, 35]
targetb = 25
print(arr)
binart_search(arr,targetb)


numbers = [10, 25, 30, 45, 50, 60]
target = 44
linear_search(numbers,target)

marks = [56, 12, 89, 43, 77, 23]
print(marks)
bubble_sort(marks)
print(marks)