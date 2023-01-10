import math

import parse


class Monkey:
    def __init__(self, items, operation, test, monkeys) -> None:
        self.items = items
        self.operation_fun = operation
        self.test_fun = test
        self.monkeys = monkeys
        self.count = 0

    def take_turn(self, worry_level):
        len_items = len(self.items)
        for i in range(len_items):
            item = self.items.pop(0)
            self.count += 1
            item = self.operation_fun(item)

            # To deal with too high numbers, perform modulo of product of prime from 2 to 23
            item = (
                item % 223092870 if worry_level == 1 else math.floor(item / worry_level)
            )
            monkey_receiver = self.test_fun(item)
            self.monkeys[monkey_receiver].items.append(item)


def make_operation_func(func_str):
    def f(old):
        return eval(func_str)

    return f


def make_test_func(test_div, test_true, test_false):
    def f(x):
        return int(test_false) if x % int(test_div) else int(test_true)

    return f


def read_data(filename):
    monkeys = []
    with open(filename) as f:
        for monkey_line in f.read().split("\n\n"):
            lines = monkey_line.split("\n")

            items_str = parse.parse("  Starting items: {}", lines[1])[0].split(", ")
            items = [int(item) for item in items_str]

            operation = make_operation_func(
                parse.parse("  Operation: new = {}", lines[2])[0]
            )

            test_div = parse.parse("  Test: divisible by {}", lines[3])[0]
            test_true = parse.parse("    If true: throw to monkey {}", lines[4])[0]
            test_false = parse.parse("    If false: throw to monkey {}", lines[5])[0]

            test = make_test_func(test_div, test_true, test_false)

            monkeys.append(Monkey(items, operation, test, monkeys))

    return monkeys


def main():
    monkeys = read_data("input.txt")
    for _ in range(20):
        for monkey in monkeys:
            monkey.take_turn(3)

    counts = [monkey.count for monkey in monkeys]
    counts.sort(reverse=True)
    print(counts[0] * counts[1])

    monkeys = read_data("input.txt")
    for _ in range(10000):
        for monkey in monkeys:
            monkey.take_turn(1)

    counts = [monkey.count for monkey in monkeys]
    counts.sort(reverse=True)
    print(counts[0] * counts[1])


if __name__ == "__main__":
    main()
