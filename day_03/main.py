def read_data(filename):
    with open(filename) as f:
        data = []
        for line in f.read().splitlines():
            length = len(line)
            data.append([line[:int(length / 2)], line[int(length / 2):]])
    return data


def read_data_group(filename):
    with open(filename) as f:
        data = []
        for line in f.read().splitlines():
            data.append(line)

    data_group = [data[i:i + 3] for i in range(0, len(data), 3)]

    return data_group


def get_doubles(data):
    items = []
    for entry in data:
        items.append(''.join(set(entry[0]).intersection(entry[1])))

    return items


def get_triples(data):
    items = []
    for entry in data:
        items.append(''.join(set(entry[0]).intersection(entry[1]).intersection(entry[2])))

    return items


def calc_scores(data):
    scores = []
    for letter in data:
        if letter.islower():
            scores.append(ord(letter) - 96)
        else:
            scores.append(ord(letter) - 38)

    return scores


def main():
    data = read_data("input.txt")
    items = get_doubles(data)
    scores = calc_scores(items)
    print(sum(scores))

    data_group = read_data_group("input.txt")
    items = get_triples(data_group)
    scores = calc_scores(items)
    print(sum(scores))


if __name__ == "__main__":
    main()
