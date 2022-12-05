response_points_map = {"Rock": 1,
                       "Paper": 2,
                       "Scissors": 3}
encrypted_map_1 = {"A": "Rock",
                   "B": "Paper",
                   "C": "Scissors",
                   "X": "Rock",
                   "Y": "Paper",
                   "Z": "Scissors"}
encrypted_map_2 = {"A": "Rock",
                   "B": "Paper",
                   "C": "Scissors",
                   "X": "L",
                   "Y": "T",
                   "Z": "W"}
result_points_map = {"W": 6,
                     "T": 3,
                     "L": 0}


def read_data(filename):
    with open(filename) as f:
        data = []
        for line in f.read().splitlines():
            data.append(line.split(" "))
    return data


def calc_score_1(entry):
    def calc_result(entry_elf, entry_you):
        if entry_elf == "Rock":
            if entry_you == "Paper":
                return "W"
            elif entry_you == "Scissors":
                return "L"
            else:
                return "T"
        elif entry_elf == "Paper":
            if entry_you == "Paper":
                return "T"
            elif entry_you == "Scissors":
                return "W"
            else:
                return "L"
        else:
            if entry_you == "Paper":
                return "L"
            elif entry_you == "Scissors":
                return "T"
            else:
                return "W"

    # Get score for your response
    response = encrypted_map_1[entry[1]]
    score = response_points_map[response]

    # Get score for result (win-loss-tie)
    score += result_points_map[calc_result(encrypted_map_1[entry[0]], encrypted_map_1[entry[1]])]

    return score


def calc_score_2(entry):
    def calc_response(entry_elf, result):
        if entry_elf == "Rock":
            if result == "W":
                return "Paper"
            elif result == "L":
                return "Scissors"
            else:
                return "Rock"
        elif entry_elf == "Paper":
            if result == "T":
                return "Paper"
            elif result == "W":
                return "Scissors"
            else:
                return "Rock"
        else:
            if result == "L":
                return "Paper"
            elif result == "T":
                return "Scissors"
            else:
                return "Rock"

    # Get score for your response
    response = calc_response(encrypted_map_2[entry[0]], encrypted_map_2[entry[1]])
    score = response_points_map[response]

    # Get score for result (win-loss-tie)
    score += result_points_map[encrypted_map_2[entry[1]]]

    return score


def main():
    data = read_data("input.txt")
    print(sum([calc_score_1(entry) for entry in data]))
    print(sum([calc_score_2(entry) for entry in data]))


if __name__ == "__main__":
    main()
