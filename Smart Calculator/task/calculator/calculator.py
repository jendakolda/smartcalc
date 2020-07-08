# Program Calculator: Jetbrains Hyperskill Hard project
# (c) JendaKolda 2020
# calculator function


# def operation(x):
#     input_line = list(x.lstrip('+').split())
#     expr_check(input_line)
#     operands = []
#     operators = []
#     total = int(input_line[0])
#
#     for element in range(len(input_line)):
#         if input_line[element].lstrip('-').isnumeric():
#             operands.append(int(input_line[element]))
#         else:
#             operators.append(add_or_sub(input_line[element]))
#
#     for element in range(0, len(operators)):
#         if operators[element] == '+':
#             total += operands[element + 1]
#         elif operators[element] == '-':
#             total -= operands[element + 1]
#     return total
#
#
# # function expr_check to confirm correct format of input
# def expr_check(input_line):
#     if len(input_line) % 2 == 0:
#         print('Invalid expression')
#
#
# # function add_or_sub to evaluate the operators
# def add_or_sub(operator):
#     if operator.count('-') % 2 == 0:
#         return '+'
#     if operator.count('-') % 2 == 1:
#         return '-'
#     return print('input an operator')
#
#
# # function command for selection of commands
# def command(todo):
#     if todo == 'exit':
#         print('Bye!')
#         exit()
#     elif todo == 'help':
#         print('The program calculates the sum of numbers')
#     else:
#         print('Unknown command')
#
#
# # program main body
# while True:
#     raw_input = input('')
#     if raw_input.startswith('/'):
#         command(raw_input.lstrip('/'))
#         continue
#     elif not raw_input:
#         continue
#     else:
#         try:
#             print(operation(raw_input))
#         except:
#             print('Invalid expression')


# write your code here
def calculate_numbers(a, b, operation):
    if "+" in operation:
        return int(a) + int(b)
    if "-" in operation:
        return int(a) - int(b)


def calculate_equation(numbers):
    numbers = numbers.split()
    total = numbers[0]
    counter = 2
    while counter < len(numbers):
        total = calculate_numbers(total, numbers[counter], examine_operation(numbers[counter - 1]))
        counter += 2
    return total


def examine_operation(operation):
    if (len(operation) % 2 != 0 and "-" in operation) or operation == "-":
        return "-"
    else:
        return "+"


def is_knwown_command(command, all_commands):
    return command[0] == "/" and command in all_commands


def is_command(command):
    return command[0] == "/"


while True:
    all_commands = ["/exit", "/help"]
    numbers = input()

    try:
        if numbers == "":
            pass
        elif is_command(numbers):
            assert is_knwown_command(numbers, all_commands)
            if numbers == all_commands[0]:
                print("Bye!")
                break
            elif numbers == all_commands[1]:
                print("The program calculates the sum and subtraction of numbers")
        elif len(numbers.split()) == 1 and int(numbers):
            print(int(numbers))
        else:
            print(calculate_equation(numbers))
    except AssertionError:
        print("Unknown command")
    except ValueError:
        print("Invalid expression")
    else:
        continue