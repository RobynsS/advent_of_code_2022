import math


def read_data(filename):
    with open(filename) as f:
        rock_pos = []
        for line in f.read().splitlines():
            # Parse the line to have all coordinates as tuples
            temp = [tuple(map(int, x.split(","))) for x in line.split(" -> ")]

            # For each line, generate the positions
            new_pos = []

            # Loop over each coordinate and generate the positions in between the
            # current and next one
            for idx in range(len(temp) - 1):
                # X coordinate is the same
                if temp[idx][0] == temp[idx + 1][0]:
                    # Multiplier to deal with increase and decrease
                    multip = int(math.copysign(1, temp[idx + 1][1] - temp[idx][1]))
                    temp_pos = [
                        (temp[idx][0], y)
                        for y in range(temp[idx][1], temp[idx + 1][1] + multip, multip)
                    ]
                # Y coordinate is the same
                elif temp[idx][1] == temp[idx + 1][1]:
                    # Multiplier to deal with increase and decrease
                    multip = int(math.copysign(1, temp[idx + 1][0] - temp[idx][0]))
                    temp_pos = [
                        (x, temp[idx][1])
                        for x in range(temp[idx][0], temp[idx + 1][0] + multip, multip)
                    ]

                new_pos.extend(temp_pos)
            rock_pos.extend(new_pos)

    # Remove doubles
    rock_pos = list(dict.fromkeys(rock_pos))

    return rock_pos


def update_sand(sand_pos, rock_pos):
    if (sand_pos[0], sand_pos[1] + 1) not in rock_pos:  # Check if sand can fall down
        return (sand_pos[0], sand_pos[1] + 1)
    elif (
        sand_pos[0] - 1,
        sand_pos[1] + 1,
    ) not in rock_pos:  # Check if sand can fall down - left
        return (sand_pos[0] - 1, sand_pos[1] + 1)
    elif (
        sand_pos[0] + 1,
        sand_pos[1] + 1,
    ) not in rock_pos:  # Check if sand can fall down - right
        return (sand_pos[0] + 1, sand_pos[1] + 1)
    else:
        return (sand_pos[0], sand_pos[1])


def main():
    rock_pos = read_data("input.txt")
    bottom_pos = max([x[1] for x in rock_pos])

    sand_pos = (500, 0)
    sand_at_rest = 0
    while sand_pos[1] < bottom_pos:
        sand_pos_update = update_sand(sand_pos, rock_pos)
        if sand_pos_update == sand_pos:  # Sand comes to rest
            sand_pos = (500, 0)
            rock_pos.append(sand_pos_update)
            sand_at_rest += 1
        else:
            sand_pos = sand_pos_update

    print(sand_at_rest)

    # Add floor
    floor_pos = bottom_pos + 2
    floor_pos = [
        (x, floor_pos)
        for x in range(
            500 - floor_pos - 5, 500 + floor_pos + 1 + 5
        )  # Adding 5 each side to be sure floor is wide enough
    ]
    rock_pos = read_data("input.txt")
    rock_pos.extend(floor_pos)

    sand_pos = (500, 0)
    sand_at_rest = 0
    while True:
        sand_pos_update = update_sand(sand_pos, rock_pos)
        if sand_pos_update == (500, 0):
            sand_at_rest += 1
            break
        if sand_pos_update == sand_pos:  # Sand comes to rest
            sand_pos = (500, 0)
            rock_pos.append(sand_pos_update)
            sand_at_rest += 1
        else:
            sand_pos = sand_pos_update

    print(sand_at_rest)


if __name__ == "__main__":
    main()
