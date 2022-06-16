def get_data():

    with open('C:/Github/AdventOfCode/day_3/puzzle_input.txt') as f:
        lines = f.readlines()
        f.close()

    line_without_newline = []

    for line in lines:
        line = line.rstrip("\n")
        line_without_newline.append(line)
    
    return line_without_newline