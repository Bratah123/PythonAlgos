def quick_sort(my_array):
    # Simple quick sort algo
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

def merge_sort(my_array):
    pass

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
    pass

def fibonacci():
    pass

rand_list = [8, 8, 7, 5, 4, 3, 2, 4, 1]

print("Selection Sort:", selection_sort(rand_list))
