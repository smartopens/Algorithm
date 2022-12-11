def sort_array(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    left_array = sort_array(left_array)
    right_array = sort_array(right_array)
    i, j, k = 0, 0, 0

    while i < len(left_array) and j < len(right_array):

        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    if i == len(left_array):
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
    if j == len(right_array):
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
    return array


test_case = int(input())
array = []

for _ in range(test_case):
    array.append(int(input()))

array = sort_array(array)

for i in array:
    print(i)
