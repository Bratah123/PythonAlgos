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

def two_sum(nums, target):
    nums_length = len(nums)
    cache_list = nums
    for number in cache_list:
        for i in range(cache_list.index(number) + 1, nums_length):
            if number + nums[i] == target:
                return [cache_list.index(number), i]

def roman_to_int(s):
    str_length = len(s)
    num = 0
    grouped_symbols = []
    roman_symbols ={
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    if str_length == 1:
        return roman_symbols[s]

    index = 0
    while index < str_length - 1:
        current_symbol = s[index]
        symbol_ahead = s[index+1]

        if roman_symbols.get(current_symbol + symbol_ahead) is not None:
            grouped_symbols.append(current_symbol + symbol_ahead)
            index += 2
        else:
            grouped_symbols.append(current_symbol)
            index += 1

    for group in grouped_symbols:
        num += roman_symbols[group]

    if roman_symbols.get(s[-2:]) is None:
        num += roman_symbols[s[-1]]

    print(grouped_symbols)
    return num

rand_list = [8, 8, 7, 5, 4, 3, 2, 4, 1]

print(roman_to_int('D'))
