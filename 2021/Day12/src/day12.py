from IO.IO_module import read_input_lines


graph = []
visited = dict()
nodes = set()


def adjacent_nodes(node: str) -> set:
    global graph
    adjacents = set()
    for current_path in graph:
        if node in current_path:
            adjacents = adjacents.union(current_path.difference({node}))

    return adjacents


def single_cave(node: str) -> bool:
    global visited, nodes

    single_visit = True
    for key, value in visited.items():
        if key.islower():
            single_visit = single_visit and value < 2

    return single_visit


def check_visited(node: str, case: int) -> bool:
    global visited

    if case == 2:
        if node == 'start' or node == 'end':
            return visited[node] > 0
        elif node.islower() and single_cave(node):
            return visited[node] > 1
    return not (node.isupper() or visited[node] == 0)


def depth_first_search(start_node: str, end_node: str, case: int) -> int:
    global visited, graph

    if start_node == end_node:
        return 1

    visited[start_node] += 1
    adjacents = adjacent_nodes(start_node)
    count = 0
    for adj_node in adjacents:
        if not check_visited(adj_node, case):
            count += depth_first_search(adj_node, end_node, case)

    visited[start_node] -= 1
    return count


def part1(input_lines: list) -> int:
    global graph, nodes, visited
    graph = [set(line.split('-')) for line in input_lines]
    nodes = set().union(*graph)
    for node in nodes:
        visited[node] = 0
    return depth_first_search('start', 'end', 1)


def part2(input_lines: list) -> int:
    global graph, nodes, visited
    graph = [set(line.split('-')) for line in input_lines]
    nodes = set().union(*graph)
    for node in nodes:
        visited[node] = 0
    return depth_first_search('start', 'end', 2)


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(f'Part one solution: {part1(input_lines)}')
    print(f'Part two solution: {part2(input_lines)}')


if __name__ == '__main__':
    main()
