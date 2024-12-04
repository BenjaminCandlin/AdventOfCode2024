import numpy as np


wordsearch = []

# Import data
with open(r"Day4\day4_input.txt", "r") as data:
    lines = data.readlines()
    for line in lines:
        row = []
        for char in line.strip():
            row.append(char)
        wordsearch.append(row)


wordsearch = np.array(wordsearch)

search = np.nditer(wordsearch, flags=["multi_index"])

total = 0

for x in search:
    if x == "X":
        x_index = search.multi_index

        # Find next places to search
        search2 = [
            (x_index[0], x_index[1] + 1),
            (x_index[0] + 1, x_index[1] + 1),
            (x_index[0] + 1, x_index[1]),
            (x_index[0] + 1, x_index[1] - 1),
            (x_index[0], x_index[1] - 1),
            (x_index[0] - 1, x_index[1] - 1),
            (x_index[0] - 1, x_index[1]),
            (x_index[0] - 1, x_index[1] + 1),
        ]

        for m in search2:
            if m[0] < 0 or m[1] < 0:
                continue
            if m[0] >= wordsearch.shape[0]:
                continue
            if m[1] >= wordsearch.shape[1]:
                continue
            elif wordsearch[m] == "M":
                vector = (m[0] - x_index[0], m[1] - x_index[1])
                search3 = (m[0] + vector[0], m[1] + vector[1])

                if search3[0] < 0 or search3[1] < 0:
                    continue
                if search3[0] >= wordsearch.shape[0]:
                    continue
                if search3[1] >= wordsearch.shape[1]:
                    continue
                elif wordsearch[search3] == "A":
                    search4 = (search3[0] + vector[0], search3[1] + vector[1])
                    if search4[0] < 0 or search4[1] < 0:
                        continue
                    if search4[0] >= wordsearch.shape[0]:
                        continue
                    if search4[1] >= wordsearch.shape[1]:
                        continue
                    elif wordsearch[search4] == "S":
                        total += 1

print(total)


# Task 2

total2 = 0

# X-mas form

x_mas = np.array([["M", 0, "S"], [0, "A", 0], ["M", 0, "S"]])

for row in range(wordsearch.shape[0] - 2):
    for column in range(wordsearch.shape[1] - 2):
        sample = np.array(
            [
                [wordsearch[row, column], wordsearch[row, column + 1], wordsearch[row, column + 2]],
                [wordsearch[row + 1, column], wordsearch[row + 1, column + 1], wordsearch[row + 1, column + 2]],
                [wordsearch[row + 2, column], wordsearch[row + 2, column + 1], wordsearch[row + 2, column + 2]],
            ]
        )
        for i in range(4):

            sample = np.rot90(sample)

            cleaned_sample = np.array(
                [[sample[(0, 0)], 0, sample[(0, 2)]], [0, sample[(1, 1)], 0], [sample[(2, 0)], 0, sample[(2, 2)]]]
            )
            if np.array_equal(cleaned_sample, x_mas) is True:
                total2 += 1
                continue

print(total2)
