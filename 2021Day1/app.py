with open('C:/Github/AdventOfCode/2021Day1/messureData.txt') as f:
    lines = f.readlines()
    f.close()

line_without_newline = []

for line in lines:
    line = line.rstrip()
    line_without_newline.append(line)


print(line_without_newline)

    
    