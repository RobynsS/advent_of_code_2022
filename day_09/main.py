import math


class Rope:
    def __init__(self, knots) -> None:
        self.segment_pos = [(0, 0) for _ in range(knots)]
        self.tail_vis = {(0, 0)}

    def update_rope(self):
        for index in range(len(self.segment_pos) - 1):
            self.update_segment(index + 1)

    def update_segment(self, index):
        head_pos = self.segment_pos[index - 1]
        tail_pos = self.segment_pos[index]
        dist_x = tail_pos[0] - head_pos[0]
        dist_y = tail_pos[1] - head_pos[1]

        # Do nothing if head and tail are close enough
        if abs(dist_x) > 1 and abs(dist_y) <= 1:
            tail_pos = (
                int(tail_pos[0] - math.copysign(1, dist_x)),
                head_pos[1],
            )

        elif abs(dist_y) > 1 and abs(dist_x) <= 1:
            tail_pos = (
                head_pos[0],
                int(tail_pos[1] - math.copysign(1, dist_y)),
            )
        elif abs(dist_y) > 1 and abs(dist_x) > 1:
            tail_pos = (
                int(tail_pos[0] - math.copysign(1, dist_x)),
                int(tail_pos[1] - math.copysign(1, dist_y)),
            )

        self.segment_pos[index] = tail_pos

    def move(self, direction):
        # Move the head of the rope
        head_pos = self.segment_pos[0]
        if direction == "R":
            head_pos = (head_pos[0] + 1, head_pos[1])
        elif direction == "L":
            head_pos = (head_pos[0] - 1, head_pos[1])
        elif direction == "U":
            head_pos = (head_pos[0], head_pos[1] + 1)
        elif direction == "D":
            head_pos = (head_pos[0], head_pos[1] - 1)
        self.segment_pos[0] = head_pos

        # Move the tail of the rope
        self.update_rope()

        # Store tail position of new
        self.tail_vis.add(self.segment_pos[-1])


def read_data(filename):
    with open(filename) as f:
        moves = []
        for line in f.read().splitlines():
            temp = line.split(" ")
            moves.append((temp[0], int(temp[1])))

    return moves


def main():
    # Initialization
    moves = read_data("input.txt")
    rope_short = Rope(2)
    rope_long = Rope(10)

    # Perform rope moves
    for move in moves:
        direction, count = move
        for _ in range(count):
            rope_short.move(direction)
            rope_long.move(direction)

    print(len(rope_short.tail_vis))
    print(len(rope_long.tail_vis))


if __name__ == "__main__":
    main()
