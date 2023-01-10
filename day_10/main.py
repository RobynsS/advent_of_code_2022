def read_data(filename):
    with open(filename) as f:
        data = []
        for line in f.read().splitlines():
            data.append(line)

    return data


def get_signal_strengths(data):
    cycles = [20, 60, 100, 140, 180, 220]
    cycle = 0
    x = 1
    signal_strengths = []

    for line in data:
        if cycles:

            # Update cycle
            if line == "noop":
                cycle += 1
            else:
                cycle += 2
            if cycle >= cycles[0]:
                signal_strengths.append(cycles[0] * x)
                cycles.pop(0)

            # Update register
            if line != "noop":
                val = int(line.split(" ")[1])
                x += val

        else:
            break

    return signal_strengths


def get_image(data):
    def draw_pixel(image, sprite_pos):
        cycle = len("".join(image.split()))

        if cycle % 40 == 0:
            image += "\n"
        if abs(sprite_pos - (cycle % 40)) <= 1:
            image += "#"
        else:
            image += "."
        return image

    image = ""
    sprite_pos = 1
    for line in data:

        if line == "noop":
            image = draw_pixel(image, sprite_pos)

        else:
            image = draw_pixel(image, sprite_pos)
            image = draw_pixel(image, sprite_pos)
            val = int(line.split(" ")[1])
            sprite_pos += val

    return image


def main():
    # Initialization
    data = read_data("input.txt")
    signal_strenghts = get_signal_strengths(data)
    print(sum(signal_strenghts))
    print(get_image(data))


if __name__ == "__main__":
    main()
