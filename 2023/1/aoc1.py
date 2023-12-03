import re

with open("./input.txt") as input_file:
    lines = input_file.readlines()


line: str

intsums: int = 0

for line in lines:
    newline: str = re.sub(r'[a-zA-Z]+','', line.strip())
    stringint: str = f'{newline[0]}{newline[-1]}'
    intsums += int(stringint)

print(f'total: {intsums}')