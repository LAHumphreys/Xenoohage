tile_map = {
    'A': 0,
    '*': 1,
    '=': 2,
    '^': 3
}
inverse_tile_map = {tile_map[key]: key for key in tile_map}

def map_values(board, mapping):
    def map_row(row):
        return [mapping[col] for col in row]
    return [map_row(row) for row in board]

def hit_button(board, buttons):
    values = map_values(board, tile_map)

    for row_index, column_index in buttons:
        for row_i in range(3):
            for col_i in range(3):
                if row_i == row_index or col_i == column_index:
                    values[row_i][col_i] = (values[row_i][col_i] +1) % 4

    result = map_values(values, inverse_tile_map)
    return result

def all_buttons():
    result = []
    for i in range(3):
        for j in range(3):
            result.append((i,j))
    return result

def find_path(start_board, final_board, max_depth, depth=0, start_path=[]):
    result = []
    end_of_phase = []
    current_depth = depth + 1
    for button in all_buttons():
        result_board = hit_button(start_board, [button])
        if matches(final_board, result_board):
            result = start_path + [button]
            break
        elif current_depth < max_depth:
            end_of_phase.append((start_path + [button], result_board))

    while not result and end_of_phase:
        phase = end_of_phase.pop()
        result = find_path(phase[1], final_board, max_depth, current_depth, phase[0])

    return result

def matches(board, expected):
    for row_index in range(3):
        for col_index in range(3):
            if board[row_index][col_index] != expected[row_index][col_index]:
                return False
    return True


def print_board(board):
    for row in board:
        print ("|{0}|{1}|{2}|".format(row[0], row[1], row[2]))

def print_path(board, path):
    print ("start")
    print_board(board)
    while path:
        button = path.pop(0)
        board = hit_button(board, [button])
        print ("Row, Column: {0}, {1}".format(button[0], button[1]))
        print_board(board)

def archers_line():
    start_board = [
        ["A", "A", "^"],
        ["=", "A", "^"],
        ["^", "*", "^"]
    ]
    final_board = [
        ["A", "A", "A"],
        ["A", "A", "A"],
        ["A", "A", "A"]
    ]
    path = find_path(start_board, final_board, 5)
    print_path(start_board, path)

archers_line()
