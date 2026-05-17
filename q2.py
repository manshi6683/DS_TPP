def add(a, b):
    return a + b

def check_values(lst, a, b):

    s = add(a, b)

    mid_index = len(lst) // 2
    mid_value = lst[mid_index]

    if s > mid_value:
        print(set(lst[:mid_index]))

    elif s == mid_value:
        print({mid_index: mid_value})

    else:
        print(tuple(lst[mid_index + 1:]))


lst = list(map(int, input("Enter list elements: ").split()))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

check_values(lst, a, b)
