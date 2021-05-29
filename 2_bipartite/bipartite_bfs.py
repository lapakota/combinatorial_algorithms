from enum import Enum


class Color(Enum):
    RED = 0
    BLUE = 1


class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.parts_list = []

    def check_bipartite_with_bfs(self, start):
        explored = []
        colored = {}
        queue = [Node(start, Color.RED)]

        while queue:
            node = queue.pop(0)
            if not self.is_node_explored(node, explored):
                explored.append(node)
                neighbours = self.graph[node.value]
                for neighbour in neighbours:
                    if neighbour not in [x.value for x in colored.values()]:
                        neighbour_node = Node(neighbour, self.get_opposite_color(node))
                        colored[neighbour] = neighbour_node
                        queue.append(neighbour_node)
                    elif colored[neighbour].color == node.color:
                        return False

        self.parts_list = self.get_parts_list(explored)
        return True

    def get_parts_list(self, explored):
        red_list = self.get_values_with_one_color(explored, Color.RED)
        blue_list = self.get_values_with_one_color(explored, Color.BLUE)
        return self.get_lists_in_right_order(red_list, blue_list)

    @staticmethod
    def get_opposite_color(node):
        return Color.RED if node.color == Color.BLUE else Color.BLUE

    @staticmethod
    def is_node_explored(node, explored):
        return (node.value, node.color) in [(x.value, x.color) for x in explored]

    @staticmethod
    def get_values_with_one_color(explored, color):
        return sorted([x.value for x in explored if x.color == color])

    @staticmethod
    def get_lists_in_right_order(red_list, blue_list):
        return [red_list, blue_list] \
            if min(red_list) < min(blue_list) \
            else [blue_list, red_list]


class FilesHandler:
    def __init__(self, in_filename, out_filename):
        self.in_filename = in_filename
        self.out_filename = out_filename

    def parse_data_from_file(self):
        with open(self.in_filename, 'r') as file:
            nodes_count = int(file.readline())
            graph = {}
            for line, number in zip(file, range(1, nodes_count + 1)):
                nodes = line.replace('\n', '').split()[:-1]
                graph.update({number: [int(x) for x in nodes]})
            return graph

    def write_data_to_file(self, graph, is_bipartite):
        with open(self.out_filename, 'w') as file:
            if not is_bipartite:
                file.write('N')
            else:
                result_string = 'Y\n'
                for part in graph.parts_list:
                    for node in part:
                        result_string += f'{str(node)} '
                    result_string = result_string[:-1]
                    result_string += '\n0\n'
                file.write(result_string[:-2])


def main():
    files_handler = FilesHandler('in.txt', 'out.txt')
    graph = Graph(files_handler.parse_data_from_file())
    is_bipartite = graph.check_bipartite_with_bfs(1)
    files_handler.write_data_to_file(graph, is_bipartite)


if __name__ == '__main__':
    main()
