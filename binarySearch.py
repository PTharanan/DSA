def binary_search(arr, target):

    start_index = 0
    last_index = len(arr) -1

    while start_index <= last_index:
        mid_index = (last_index+start_index) //2

        if arr[mid_index] == target:
            print(f"{target} Finded, index: {mid_index}")
            return
        elif arr[mid_index]  < target:
            start_index = mid_index + 1
        else:
            last_index = mid_index - 1
    print(f"{target} not find")

arr = [1, 3, 5, 7, 9, 11]
binary_search(arr, 71)