# Question 4:
def create_zero_matrix(m, n):
    matrix = []
    for i in range(m):
        matrix.append([0] * n)
    return matrix


def find_min(list_point):
    min_value = float("inf")
    for i in range(len(list_point)):
        if list_point[i] < min_value:
            min_value = list_point[i]
    return min_value


def calculate_distance_levenshtein(string_source, string_target):
    levenshtein_distance = 0
    string_source_change = "#" + string_source
    string_target_change = "#" + string_target
    matrix_d = create_zero_matrix(len(string_source_change), len(string_target_change))
    # Filling value in matrix
    for row in range(len(string_target_change)):
        matrix_d[0][row] = row
    for col in range(len(string_source_change)):
        matrix_d[col][0] = col
    for i in range(1, len(string_target_change), 1):
        for j in range(1, len(string_source_change), 1):
            define_value_replace = matrix_d[j - 1][i - 1]
            if string_source_change[j] == string_target_change[i]:
                define_value_replace += + 0
            else:
                define_value_replace += + 1
            list_cost = [matrix_d[j - 1][i] + 1, matrix_d[j][i - 1] + 1, define_value_replace]
            matrix_d[j][i] = find_min(list_cost)
    # Finding min distance
    levenshtein_distance = matrix_d[len(string_source)][len(string_target)]
    print(matrix_d)
    return levenshtein_distance


print(f"Minimum distance Levenshtein: {calculate_distance_levenshtein("hola", "hello")}")
