import re
from help_functions import get_data
line_without_newline = get_data()

horizontal_value = 0
depth = 0

up = "up"
down = "down"
forward = "forward"

for value in line_without_newline:
    if value.startswith("forward"):
        number_re = re.findall(r'\d+', value)
        number_int = int(number_re[0])
        horizontal_value += number_int
    elif value.startswith("up"):
        number_re = re.findall(r'\d+', value)
        number_int = int(number_re[0])
        depth -= number_int
    elif value.startswith("down"):
        number_re = re.findall(r'\d+', value)
        number_int = int(number_re[0])
        depth += number_int

answer = horizontal_value * depth  
print(horizontal_value)
print(depth)
print(answer)
