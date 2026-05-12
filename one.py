from statistics import mean, median, mode

def list_to_matrix(lst):
    matrix = []
    index = 0

    for i in range(3):
        row = []
        for j in range(3):
            if index < len(lst):
                row.append(lst[index])
            else:
                row.append(None)
            index += 1
        matrix.append(row)

    return matrix

def tuple_statistics(lst):
    t = tuple(lst)

    stats = {
        "Tuple": t,
        "Mean": mean(lst),
        "Median": median(lst),
        "Mode": mode(lst)
    }

    return stats

def final_dictionary(lst):

    while len(lst) < 9:
        lst.append(None)

    numeric_values = [x for x in lst if isinstance(x, (int, float))]

    matrix_result = list_to_matrix(lst)
    stats_result = tuple_statistics(numeric_values)

    result = {
        "Matrix_Function": matrix_result,
        "Statistics_Function": stats_result
    }

    return result

user_list = list(map(int, input("Enter elements separated by space: ").split()))

output = final_dictionary(user_list)

print(output)
