def draw_diagonal(size):
    row = 1

    while row <= size:
        col = 1

        while col <= size:
            if col == row:
                print("O ", end="")
            else:
                print(". ", end="")
            
            col += 1

        print()
        row += 1
draw_diagonal(5)       