with open('C:/Github/AdventOfCode/2021Day1/messureData.txt') as f:
    lines = f.readlines()
    f.close()

line_without_newline = []

for line in lines:
    line = line.rstrip("\n")
    line_without_newline.append(line)

larger_measurements = 1
active_value = line_without_newline[0]
for line in line_without_newline:
    if line > active_value:
        larger_measurements += 1
        active_value = line
    else:
        active_value = line
    

print(line_without_newline)
print(f"Larger measurments: {larger_measurements}")

    
    