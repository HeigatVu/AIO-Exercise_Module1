def load_vocab(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(file_path="./vocab.txt")


def levenshtein_distance(token_1, token_2):
    distances = [[0]*(len(token_2) + 1) for i in range(0, len(token_1) + 1, 1)]

    for t1 in range(0, len(token_1), 1):
        distances[t1][0] = t1

    for t2 in range(0, len(token_2), 2):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token_1) + 1, 1):
        for t2 in range(1, len(token_2) + 1, 1):
            if token_1[t1 - 1] == token_2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token_1)][len(token_2)]