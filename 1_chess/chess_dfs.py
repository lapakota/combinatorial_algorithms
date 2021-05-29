letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = [x for x in range(1, 9)]
deltas_sequence = [(1, 1), (-1, 1),
                   (-2, 0), (-2, -2),
                   (-1, -3), (1, -3),
                   (2, -2), (2, 0)]
pawn_deltas = [(-1, -2), (1, -2)]


class ChessFigure:
    def __init__(self, pos_letter, pos_number):
        self.letter = pos_letter
        self.number = pos_number


def is_win(knight, pawn):
    return knight.letter == pawn.letter\
           and knight.number == pawn.number


def is_right_index(figure, delta):
    return 0 <= letters.index(figure.letter) + delta[0] < 8 \
           and 0 <= figure.number + delta[1] < 8


def is_dead_move(next_pos_letter_index, next_pos_number_index, pawn):
    for delta in pawn_deltas:
        pawn_next_pos_letter_index, \
        pawn_next_pos_number_index = get_next_pos_indexes(pawn, delta)
        if next_pos_letter_index == pawn_next_pos_letter_index \
                and next_pos_number_index == pawn_next_pos_number_index:
            return True
    return False


def get_next_pos_indexes(figure, delta):
    return letters.index(figure.letter) + delta[0], figure.number + delta[1]


def get_neighbours(knight, pawn):
    neighbours = []
    for delta in deltas_sequence:
        next_letter_index, next_number_index = get_next_pos_indexes(knight, delta)
        if is_right_index(knight, delta) \
                and not is_dead_move(next_letter_index, next_number_index, pawn):
            neighbours.append((letters[next_letter_index], numbers[next_number_index]))
    return neighbours


def get_route_with_dfs(pawn, visited, stack, route):
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.append(node)
        remove_node = True
        knight_next_position = ChessFigure(node[0], node[1])
        if is_win(knight_next_position, pawn):
            return route
        for next_neighbour in get_neighbours(knight_next_position, pawn):
            if next_neighbour not in visited:
                stack.append(next_neighbour)
                route.append(next_neighbour)
                remove_node = False
                break
        if remove_node:
            stack.pop()
            route.pop()


def parse_data_from_file(filename):
    with open(filename, 'r') as file:
        file_data = file.read().split('\n')
        knight = ChessFigure(file_data[0][0], int(file_data[0][1]))
        pawn = ChessFigure(file_data[1][0], int(file_data[1][1]))
    return knight, pawn


def write_data_to_file(filename, final_route):
    with open(filename, 'w') as file:
        for route in final_route:
            file.write(f"{route[0]}{str(route[1])}\n")


def print_chess_field():
    field = ""
    for i in numbers[::-1]:
        for j in letters:
            field += f"{j}{i} "
        field += "\n"
    print(field)


def main():
    # print_chess_field()
    knight, pawn = parse_data_from_file('in.txt')

    visited = [(knight.letter, knight.number)]
    stack = [(knight.letter, knight.number)]
    route = [(knight.letter, knight.number)]

    final_route = get_route_with_dfs(pawn, visited, stack, route)

    write_data_to_file('out.txt', final_route)


if __name__ == '__main__':
    main()
