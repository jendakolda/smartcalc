# write your code here
def operation(x):
    input_line = list(x.split())
    operands = []
    operators = []
    total = int(input_line[0])

    for element in range(len(input_line)):
        if input_line[element].lstrip('-').isnumeric():
            operands.append(int(input_line[element]))
        else:
            operators.append(add_or_sub(input_line[element]))

    for element in range(0, len(operators)):
        if operators[element] == '+':
            total += operands[element + 1]
        elif operators[element] == '-':
            total -= operands[element + 1]
    return total


def add_or_sub(operator):
    if operator.count('-') % 2 == 0:
        return '+'
    if operator.count('-') % 2 == 1:
        return '-'
    return print('input an operator')


while True:
    raw_input = input('')
    if raw_input == '/exit':
        print('Bye!')
        break
    elif raw_input == '/help':
        print('The program calculates the sum of numbers')
        continue
    elif not raw_input:
        continue
    else:
        print(operation(raw_input))
