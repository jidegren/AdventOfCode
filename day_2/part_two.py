import re
from help_functions import get_data
line_without_newline = get_data()

horizontal = 0
depth = 0
aim = 0

up = "up"
down = "down"
forward = "forward"

for value in line_without_newline:
    if value.startswith("forward"):
        number_re = re.findall(r'\d+', value)
        number_int = int(number_re[0])
        horizontal += number_int
        depth += aim * number_int
    elif value.startswith("up"):
        number_re = re.findall(r'\d+', value)
        number_int = int(number_re[0])
        aim -= number_int
    elif value.startswith("down"):
        number_re = re.findall(r'\d+', value)
        number_int = int(number_re[0])
        aim += number_int

answer = depth * horizontal

print(answer)