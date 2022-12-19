def nested_set(dic, keys, val):
    for key in keys[:-1]:
        if key not in dic:
            dic[key] = {}
        dic = dic[key]
    dic[keys[-1]] = val


def read_data(filename):
    with open(filename) as f:
        data = {}
        curr_dir = []
        lines = f.read().splitlines()
        for line in lines:
            if line.startswith("$ cd"):
                if line != "$ cd ..":
                    direc = line.split(" ")[-1]
                    curr_dir.append(direc)
                    nested_set(data, curr_dir, {})
                else:
                    curr_dir.pop(-1)
            elif not line.startswith("$ ls"):
                file = line.split(" ")
                if file[0] == "dir":
                    nested_set(data, curr_dir + [file[1]], {})
                else:
                    nested_set(data, curr_dir + [file[1]], file[0])

    return data


def calc_dict_sizes(dic, sizes, name=None):
    size = 0

    for key, value in dic.items():
        if isinstance(value, dict):
            size += calc_dict_sizes(dic[key], sizes, key)
        else:
            size += int(value)

    if name:
        sizes.append(size)
    return size


def main():
    data = read_data("input.txt")
    print(data)
    sizes = []
    calc_dict_sizes(data, sizes)
    print(sum([vals for vals in sizes if vals <= 100000]))
    sizes.sort()
    required_size = 30000000 - (70000000 - sizes[-1])
    sizes_ok = [size for size in sizes if size >= required_size]
    print(sizes_ok[0])



if __name__ == "__main__":
    main()
