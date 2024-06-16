# Question 1:
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]


def find_max_value(list_to_find_max):
    max_value = 0
    for i in range(0, len(list_to_find_max), 1):
        if list_to_find_max[i] > max_value:
            max_value = list_to_find_max[i]
    return max_value


def sliding_window_finding_max_value(list_with_sliding):
    k_value = 3
    start_flat = 0
    end_flat = start_flat + k_value
    while end_flat <= len(list_with_sliding):
        print(
            f"Max value in three value {list_with_sliding[start_flat:end_flat]} is {find_max_value(list_with_sliding[start_flat:end_flat])}")
        start_flat += 1
        end_flat += 1


sliding_window_finding_max_value(num_list)