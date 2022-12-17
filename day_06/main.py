from collections import Counter


def read_data(filename):
    with open(filename) as f:
        data = f.read()
    return data


def is_unqiue(data):
    freq = Counter(data)
    if len(freq) == len(data):
        return True
    else:
        return False


def main():
    data = read_data("input.txt")
    for i in range(len(data) - 3):
        marker = data[i:i + 4]
        if is_unqiue(marker):
            print("start_of_packet: " + str(i + 4))
            break

    for i in range(len(data) - 13):
        marker = data[i:i + 14]
        if is_unqiue(marker):
            print("start_of_message: " + str(i + 14))
            break


if __name__ == "__main__":
    main()
