from collections import defaultdict


# Question 3:
def word_count(string):
    list_word_count = string.split(" ")
    dict_word = defaultdict()
    for i in range(0, len(list_word_count), 1):
        if list_word_count[i] in dict_word:
            dict_word[list_word_count[i]] += 1
        else:
            dict_word[list_word_count[i]] = 1
    return dict_word


with open("homework_question_3", "r") as file:
    string_in_txt = file.read()
    print(word_count(string_in_txt))