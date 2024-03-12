def draw_pattern(size):
    row = 1

    while row <= size:
        col = 1

        while col <= size:
            if col == row or col == size - row + 1:
                print("O ", end="")
            else:
                print(". ", end="")

            col += 1

        print()
        row += 1

draw_pattern(7)
