is_empty = 0


tic_tac_toe = (
    ('X', 'O', 'X'),
    (' ', ' ', ' '),
    ('O', ' ', 'O')
)


for row in tic_tac_toe:
    for cell in row:
        if cell == ' ':
            is_empty += 1
print(is_empty)

