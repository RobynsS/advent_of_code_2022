import json
from functools import cmp_to_key


def read_data(filename):
    with open(filename) as f:
        pairs = []
        temp = []
        for line in f.read().splitlines():
            if line != "":
                temp.append(json.loads(line))
            else:
                pairs.append(tuple(temp))
                temp = []
        pairs.append(tuple(temp))
    return pairs


def check_order(pair):
    for idx in range(len(pair[0])):
        try:  # To catch when index is out of bounds if the first pair is longer than the second one
            if isinstance(pair[0][idx], int) and isinstance(pair[1][idx], int):
                if pair[0][idx] > pair[1][idx]:
                    return False
                if pair[0][idx] < pair[1][idx]:
                    return True
                continue
            elif isinstance(pair[0][idx], list) and isinstance(pair[1][idx], list):
                result = check_order((pair[0][idx], pair[1][idx]))
                if result is not None:
                    return result
            else:
                if isinstance(pair[0][idx], int):
                    result = check_order(([pair[0][idx]], pair[1][idx]))
                    if result is not None:
                        return result
                else:
                    result = check_order((pair[0][idx], [pair[1][idx]]))
                    if result is not None:
                        return result
        except IndexError:
            return False
    if len(pair[1]) > len(pair[0]):
        return True
    else:
        return None


def compare(item1, item2):
    result = check_order((item1, item2))
    if result is None:
        return 0
    else:
        if result:
            return -1
        else:
            return 1


def main():
    pairs = read_data("input.txt")
    results = []
    index = 1

    for pair in pairs:
        if check_order(pair):
            results.append(index)
        index += 1

    print(sum(results))

    packets = [entry for pair in pairs for entry in pair]
    packets.append([[2]])
    packets.append([[6]])

    packets_sorted = sorted(packets, key=cmp_to_key(compare))
    print((packets_sorted.index([[2]]) + 1) * (packets_sorted.index([[6]]) + 1))


if __name__ == "__main__":
    main()
