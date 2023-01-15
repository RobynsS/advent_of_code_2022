import numpy as np
import math


class Nodes:
    def __init__(self, data):
        self.data = np.array(data)
        self.current = self.find_start()
        self.target = self.find_end()

    def get_neighbours(self, pos):
        # Get the neighbours based on who is next to it and if travel is allowed
        neighbours = []

        up = (pos[0] - 1, pos[1]) if pos[0] - 1 >= 0 else None
        down = (pos[0] + 1, pos[1]) if pos[0] + 1 < self.data.shape[0] else None
        right = (pos[0], pos[1] + 1) if pos[1] + 1 < self.data.shape[1] else None
        left = (pos[0], pos[1] - 1) if pos[1] - 1 >= 0 else None

        for direction in [up, down, left, right]:
            if direction:
                if self.get_height(direction) <= self.get_height(pos) + 1:
                    neighbours.append(direction)

        return neighbours

    def get_height(self, index):
        char = self.data[index]
        if char == "S":
            char = "a"
        elif char == "E":
            char = "z"
        return ord(char)

    def find_val(self, val):
        result = np.where(self.data == val)
        return result[0][0], result[1][0]

    def find_start(self):
        return self.find_val("S")

    def find_end(self):
        return self.find_val("E")

    def find_a(self):
        result = np.where(self.data == "a")
        return [(result[0][i], result[1][i]) for i in range(len(result[0]))]

    def set_start(self, pos):
        self.current = pos


def read_data(filename):
    with open(filename) as f:
        nodes = []
        for line in f.read().splitlines():
            temp = []
            for char in line:
                temp.append(char)
            nodes.append(temp)
    return np.array(nodes)


def main():
    def get_min_dist_unvisited(dist_mat, unvisited_mat):
        temp = dist_mat
        np.copyto(temp, unvisited_mat, where=unvisited == math.inf)
        found = np.where(temp == np.min(temp))
        return found[0][0], found[1][0]

    # Initialization
    nodes = Nodes(read_data("input.txt"))
    dist = np.empty(shape=nodes.data.shape)
    dist.fill(math.inf)
    dist[nodes.current] = 0
    unvisited = np.empty(shape=nodes.data.shape)
    unvisited.fill(1)

    # Implementation of Dijkstra's algorithm
    while True:
        u = get_min_dist_unvisited(dist, unvisited)
        if u == nodes.target:
            result = dist[u]
            break
        unvisited[u] = math.inf

        for n in nodes.get_neighbours(u):
            dist_temp = dist[u] + 1
            if dist_temp < dist[n]:
                dist[n] = dist_temp

    print(int(result))

    # Initialization
    nodes = Nodes(read_data("input.txt"))
    get_a_pos = nodes.find_a()
    i = 0
    for start in get_a_pos:
        i += 1
        print(f'{str(i)}/{len(get_a_pos)}')
        nodes.set_start(start)
        dist = np.empty(shape=nodes.data.shape)
        dist.fill(math.inf)
        dist[nodes.current] = 0
        unvisited = np.empty(shape=nodes.data.shape)
        unvisited.fill(1)

        while True:
            u = get_min_dist_unvisited(dist, unvisited)
            if u == nodes.target:
                temp = dist[u]
                break
            # Optimization: break if distance is already bigger
            # than found with other starting point
            if dist[u] > result:
                temp = math.inf
                break
            unvisited[u] = math.inf

            for n in nodes.get_neighbours(u):
                dist_temp = dist[u] + 1
                if dist_temp < dist[n]:
                    dist[n] = dist_temp

        if temp < result:
            result = temp

    print(int(result))


if __name__ == "__main__":
    main()
