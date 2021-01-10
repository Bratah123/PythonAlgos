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

def contains_duplicates(nums):
    numbers_encountered = {}
    for number in nums:
        if numbers_encountered.get(number) is None:
            numbers_encountered[number] = 1
        else:
            numbers_encountered[number] += 1

        if numbers_encountered.get(number) > 1:
            return True

    return False

def duplicate_zeros(self, arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    arr_length = len(arr)
    index = 0
    while index < arr_length:
        if arr[index] == 0:
            arr.insert(index + 1, 0)
            index += 1
        index += 1

    items_to_remove = len(arr) - arr_length

    for i in range(items_to_remove):
        del arr[-1]

class Node:
    """Representing a node in a binary tree

    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Representing a Binary Tree

    """
    def __init__(self, root):
        self.root = Node(root)

    def print_preorder(self, start_root, traverse):
        if start_root:
            traverse += str(start_root.value) + ", "
            traverse = self.print_preorder(start_root.left, traverse)
            traverse = self.print_preorder(start_root.right, traverse)
        return traverse

    def print_inorder(self, start_root, traverse):
        if start_root is not None:
            traverse = self.print_inorder(start_root.left, traverse)
            traverse += str(start_root.value) + ", "
            traverse = self.print_inorder(start_root.right, traverse)
        return traverse

    def inorder_iteratively(self):
        stack = []
        node = self.root
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                print(node.value)
                node = node.right
            else:
                break

    def preorder_list(self, start_root, nodes):
        if start_root:
            # Counting from root->Left->root->Right (preorder)
            nodes.append(start_root.value)
            nodes = self.preorder_list(start_root.left, nodes)
            nodes = self.preorder_list(start_root.right, nodes)
        return nodes

    def count_nodes(self, start_root, count):
        # Counting size of nodes recursively
        if start_root:
            count = self.count_nodes(start_root.left, count + 1)
            count = self.count_nodes(start_root.right, count)
        return count

    def get_size(self, node):
        # getting the size of the node iteratively
        if node is None:
            return 0
        stack = []
        stack.append(node)
        size = 1
        while len(stack) > 0:
            node = stack.pop()
            if node.left:
                size += 1
                stack.append(node.left)
            elif node.right:
                size += 1
                stack.append(node.right)
        return size

    def size(self):
        # brute force method, more efficient/faster?
        return self.count_nodes(self.root, 0)

    def invert(self, root):
        if root:
            left = root.left
            right = root.right
            root.right = left
            root.left = right
            self.invert(root.left)
            self.invert(root.right)

# Arithmetic progression
# Given n numbers return the result of 1 + 2 + 3 + ..... + n
def add_n_with_iter(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result

def add_n_with_math(n):
    return (n*(n+1)) / 2

def add_n_with_recursion(n):
    # Base case
    if n <= 0:
        return n
    return n + add_n_with_recursion(n - 1)

# Initializing Tree
#       1
#     /  \
#   2     2
#  / \   / \
# 3   4 4  3
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.right.left = Node(4)
tree.root.right.right = Node(3)

print(add_n_with_iter(5))
print(add_n_with_math(5))
print(add_n_with_recursion(5))
print(tree.inorder_iteratively())
