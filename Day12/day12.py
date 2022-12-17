from IO.IO_module import read_input_lines
import numpy as np


def add_node(a: (int, int), b: (int, int)) -> (int, int):
    return a[0] + b[0], a[1] + b[1]


def parse_graph(graph_str: list) -> (np.ndarray, tuple, tuple):
    graph = []
    src, dst = 0, 0
    for row, line in enumerate(graph_str):
        aux_list = list(line)
        if 'S' in aux_list:
            idx = aux_list.index('S')
            src = (row, idx)
            aux_list[idx] = 'a'
        if 'E' in aux_list:
            idx = aux_list.index('E')
            dst = (row, idx)
            aux_list[idx] = 'z'

        graph.append([ord(v) - ord('a') for v in aux_list])

    return np.array(graph), src, dst


def initialize_dijkstra(graph: np.ndarray, src: tuple) -> (np.ndarray, dict, list):
    num_rows, num_cols = np.shape(graph)
    dist = np.full(np.shape(graph), np.inf, dtype=int)
    prev = {}
    q = [(i, j) for i in range(num_rows) for j in range(num_cols)]
    dist[src[0]][src[1]] = 0

    return dist, prev, q


def find_min(dist: np.ndarray, q: list) -> tuple:
    possibilities = [(dist[item[0], item[1]], item) for item in q]

    return sorted(possibilities, key=lambda x: x[0])[0][1]


def neighbours(node: tuple, q: list) -> list:
    possibilities = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    nodes = [add_node(node, p) for p in possibilities]
    return list(filter(lambda x: x in q, nodes))


def dijkstra(graph: np.ndarray, src: tuple) -> (np.ndarray, dict):
    dist, prev, q = initialize_dijkstra(graph, src)

    while q:
        u = find_min(dist, q)
        q.remove(u)

        for neighbour in neighbours(u, q):
            alt = dist[u[0], u[1]] + 1
            if graph[neighbour[0]][neighbour[1]] - graph[u[0]][u[1]] < 2 and alt < dist[neighbour[0]][neighbour[1]]:
                dist[neighbour[0]][neighbour[1]] = alt
                prev[neighbour] = u

    return dist, prev


def main():
    input_lines = read_input_lines()
    graph, src, dst = parse_graph(input_lines)
    dist, _ = dijkstra(graph, src)

    print(f'{dist[dst[0]][dst[1]]=}')


if __name__ == '__main__':
    main()
