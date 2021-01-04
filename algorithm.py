def quick_sort(my_array):
    # Simple quick sort algo
    # Time complexity O(n log(n)) Average
    # Worst O(n^2)
    if len(my_array) <= 1:
        # If array is 1 or less item, it's already sorted so we return
        return my_array
    pivot = my_array.pop()
    greater_than_pivot = []
    less_than_pivot = []
    for number in my_array:
        if number > pivot:
            greater_than_pivot.append(number)
        else:
            less_than_pivot.append(number)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

def merge(first_array, second_array):
    first_arr_size = len(first_array)
    second_arr_size = len(second_array)
    merged_array = []
    first_index, second_index = 0, 0

    while first_index < first_arr_size and second_index < second_arr_size:
        if first_array[first_index] < second_array[second_index]:
            merged_array.append(first_array[first_index])
            first_index += 1
        else:
            merged_array.append(second_array[second_index])
            second_index += 1

    if first_index == first_arr_size:
        merged_array.extend(second_array[second_index:])
    else:
        merged_array.extend(first_array[first_index:])

    return merged_array

def merge_sort(my_array):
    if len(my_array) <= 1:
        return my_array

    left = merge_sort(my_array[:int(len(my_array)/2)])
    right = merge_sort(my_array[int(len(my_array)/2):])

    return merge(left, right)


def selection_sort(my_array):
    array_length = len(my_array)
    for i in range(array_length):
        for j in range(i, array_length):
            if my_array[i] > my_array[j]:
                inner = my_array[i]
                outer = my_array[j]
                my_array[j] = inner
                my_array[i] = outer
    return my_array


def fizz_buzz():
    for i in range(1, 101):
        # 1 -> 100
        result = str(i)
        if i % 3 == 0:
            result = "Fizz"
        if i % 5 == 0:
            if i % 3 != 0:
                result = "Buzz"
            else:
                result += "Buzz"
        print(result)

def fibonacci(n):
    fib_array = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, b + a
        fib_array.append(a)
    return fib_array

rand_list = [8, 8, 7, 5, 4, 3, 2, 4, 1]

print(fibonacci(12))
