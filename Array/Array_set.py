def array_set(arr, target_value):
    array_length = len(arr)
    i = 0
    while i < array_length:
        if arr[i] == target_value:
            arr.append(arr.pop(i))
            array_length -= 1
        else:
            i += 1

array_value = [6, 3, 7, 2, 6, 8, 6, 6, 4, 1, 8, 9, 6, 3, 6, 6]
target_value = 6

array_set(array_value, target_value)
print(array_value)



# Time complexity = o(n^2)
# space complexity=o(1)
