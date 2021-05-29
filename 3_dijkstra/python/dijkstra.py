import sys


class Graph:
    def __init__(self, vertices_count, adj_matrix):
        self.vertices_count = vertices_count
        self.graph = adj_matrix

    def dijkstra(self, start):
        visited = [False for _ in range(self.vertices_count)]
        distance = [sys.maxsize for _ in range(self.vertices_count)]
        prev = [0 for _ in range(self.vertices_count)]

        distance[start - 1] = 0
        for i in range(self.vertices_count):
            vertex = self.get_min_vertex(visited, distance)

            if vertex == float('-inf'):
                continue

            visited[vertex] = True
            for adj_vertex in range(self.vertices_count):
                if self.graph[vertex][adj_vertex] >= 0 \
                        and not visited[adj_vertex]:
                    new_key = self.graph[vertex][adj_vertex] + distance[vertex]
                    if new_key < distance[adj_vertex]:
                        distance[adj_vertex] = new_key
                        prev[adj_vertex] = vertex + 1
        # print(distance, prev)
        return distance, prev

    def get_min_vertex(self, visited, distance):
        min_key = sys.maxsize
        vertex = float('-inf')
        for i in range(self.vertices_count):
            if not visited[i] and min_key > distance[i]:
                min_key = distance[i]
                vertex = i
        return vertex

    def get_route(self, distance, prev, start, end):
        dist = distance[end - 1]

        if dist == sys.maxsize:
            return 'N'

        vertex = end
        output = f'{end} '
        for i in range(self.vertices_count):
            vertex = prev[vertex - 1]
            output += f'{vertex} '
            if vertex == start:
                break
        return 'Y\n' + ' '.join(reversed(output.split())) + f'\n{dist}'


class FileParser:
    @staticmethod
    def parse_file(name):
        with open(name) as file:
            content = file.read().split('\n')
            start = content[-2]
            end = content[-1]
            vertices_count = int(content[0])
            adj_matrix = [[float('-inf') for _ in range(vertices_count)]
                          for _ in range(vertices_count)]
            for i in range(1, len(content) - 1):
                info = content[i].split()
                for j in range(0, len(info) - 1, 2):
                    v_from = int(info[j])
                    v_in = i
                    price = int(info[j + 1])
                    adj_matrix[v_from - 1][v_in - 1] = price
            # [print(x) for x in adj_matrix]
            return vertices_count, adj_matrix, int(start), int(end)


def main():
    count, adj_matrix, start, end = FileParser().parse_file('in.txt')
    graph = Graph(count, adj_matrix)

    distance, prev = graph.dijkstra(start)

    answer = graph.get_route(distance, prev, start, end)

    with open('out.txt', 'w') as file:
        file.write(answer)


if __name__ == '__main__':
    main()
