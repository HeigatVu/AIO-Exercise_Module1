from collections import defaultdict


# Question 2:
string_1 = "Happiness"
string_2 = "smiles"


def character_count(string):
    dict_word = defaultdict()
    for i in range(0, len(string), 1):
        if string[i] in dict_word:
            dict_word[string[i]] += 1
        else:
            dict_word[string[i]] = 1
    return dict_word


print(character_count(string_1))
print(character_count(string_2))