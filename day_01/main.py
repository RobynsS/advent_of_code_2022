def read_data(filename):
    with open(filename) as f:
        data = []
        entry = []
        for line in f.read().splitlines():
            if line == "":
                data.append(entry)
                entry = []
            else:
                entry.append(int(line))
        data.append(entry)
    return data


def calc_max_cal(data):
    calc_sums = [sum(entry) for entry in data]
    return max(calc_sums)


def calc_sum_max_3_cal(data):
    calc_sums = [sum(entry) for entry in data]
    calc_sums.sort(reverse=True)
    return sum(calc_sums[:3])


def main():
    data = read_data("input.txt")
    result = calc_max_cal(data)
    print(result)
    result = calc_sum_max_3_cal(data)
    print(result)

if __name__ == "__main__":
    main()
