raw_data = open("input4.txt", "r").readlines()
bingo_numbers = [int(n) for n in raw_data[0].split(',')]
boards = []

for start_index in range(2, len(raw_data), 6):
    new_board = []
    for row in range(start_index, start_index + 5):
        new_row = [int(n) for n in raw_data[row].split()]
        new_board.append(new_row)
    boards.append(new_board)




print(boards[0])
chosen_board = boards[0]

print(chosen_board[0][4])
