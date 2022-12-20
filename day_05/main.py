import queue
import re


class Move:
    def __init__(self, amount, loc_from, loc_to):
        self.amount = int(amount)
        self.loc_from = int(loc_from)
        self.loc_to = int(loc_to)

    def execute_9000(self, lifos):
        for _ in range(self.amount):
            temp = lifos[self.loc_from - 1].get()
            lifos[self.loc_to - 1].put(temp)

    def execute_9001(self, lifos):
        temp = []
        for _ in range(self.amount):
            temp.append(lifos[self.loc_from - 1].get())
        for item in reversed(temp):
            lifos[self.loc_to - 1].put(item)


def read_data(filename):
    with open(filename) as f:
        crates = []
        move_lines = []
        for line in f.read().splitlines():
            if line.strip() == "":
                pass
            elif line.strip()[0] == "[":
                crates.append(line)
            elif line.strip()[0] == "m":
                move_lines.append(line)
            elif line.strip()[0].isdecimal():
                nr_stacks = line.strip()[-1]

    lifos = [queue.LifoQueue() for _ in range(int(nr_stacks))]
    for entry in reversed(crates):
        temp = entry.replace("    ", "[#] ")
        stack_entries = re.findall(r'\[.*?\]', temp)
        for i in range(len(stack_entries)):
            item = stack_entries[i][1]
            if item != "#":
                lifos[i].put(item)

    moves = []
    for entry in move_lines:
        res = re.findall(r'\d+', entry)
        moves.append(Move(res[0], res[1], res[2]))

    return lifos, moves


def main():
    (lifos, moves) = read_data("input.txt")
    for move in moves:
        move.execute_9000(lifos)
    result = "".join([lifo.queue[-1] for lifo in lifos])
    print(result)
    (lifos, moves) = read_data("input.txt")
    for move in moves:
        move.execute_9001(lifos)
    result = "".join([lifo.queue[-1] for lifo in lifos])
    print(result)

if __name__ == "__main__":
    main()
