def read_data(filename):
    with open(filename) as f:
        data = []
        for line in f.read().splitlines():
            temp = line.split(",")
            data.append([temp[0], temp[1]])
    return data


def calc_full_overlap(data):
    count = 0
    for entry in data:
        range1 = range(int(entry[0].split("-")[0]), int(entry[0].split("-")[1]) + 1)
        range2 = range(int(entry[1].split("-")[0]), int(entry[1].split("-")[1]) + 1)

        if (range1.start in range2 and range1[-1] in range2) or (range2.start in range1 and range2[-1] in range1):
            count += 1

    return count


def calc_overlap(data):
    count = 0
    for entry in data:
        range1 = range(int(entry[0].split("-")[0]), int(entry[0].split("-")[1]) + 1)
        range2 = range(int(entry[1].split("-")[0]), int(entry[1].split("-")[1]) + 1)

        if range1.start <= range2[-1] and range2.start <= range1[-1]:
            count += 1

    return count


def main():
    data = read_data("input.txt")
    print(calc_full_overlap(data))
    print(calc_overlap(data))


if __name__ == "__main__":
    main()
