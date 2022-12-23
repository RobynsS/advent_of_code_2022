import numpy as np


def read_data(filename):
    with open(filename) as f:
        lines = []
        for line in f.read().splitlines():
            lines.append([int(c) for c in line])

    return np.array(lines)


def is_visible(data, i, j):

    left = data[i, 0:j]
    right = data[i, j + 1 :]
    up = data[0:i, j]
    down = data[i + 1 :, j]

    for arr in [left, right, up, down]:
        if arr.size == 0 or max(arr) < data[i, j]:
            return 1

    return 0


def calc_scenic_score(data, i, j):
    scores = []
    left = np.flip(data[i, 0:j])
    right = data[i, j + 1 :]
    up = np.flip(data[0:i, j])
    down = data[i + 1 :, j]

    for arr in [left, right, up, down]:
        if arr.size == 0:
            scores.append(0)
        else:
            score = 0
            for tree in arr:
                score += 1
                if tree >= data[i, j]:
                    break
            scores.append(score)

    return np.prod(scores)


def main():
    data = read_data("input.txt")
    count = 0
    score = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            count += is_visible(data, i, j)
            score = max(score, calc_scenic_score(data, i, j))

    print(count)
    print(score)


if __name__ == "__main__":
    main()
