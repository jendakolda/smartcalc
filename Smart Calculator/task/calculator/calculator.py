# # Program Calculator: Jetbrains Hyperskill Hard project
# # (c) JendaKolda 2020
# # calculator function
#
#
# def operation(x):
#     input_line = list(x.lstrip('+').split())
#     expr_check(input_line)
#     operands = []
#     operators = []
#     # total = int(input_line[0])
#
#     for element in range(len(input_line)):
#         if input_line[element].lstrip('-').isnumeric():
#             operands.append(int(input_line[element]))
#         elif input_line[element].lstrip('-').isalpha() and (input_line[element].lstrip('-') in calc_memory):
#             # print(calc_memory[input_line[element]])
#             operands.append(int(calc_memory[input_line[element]]))
#         else:
#             operators.append(add_or_sub(input_line[element]))
#
#     total = int(operands[0])
#
#     for element in range(len(operators)):
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
#         print('Invalid expression 1')
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
# def command(message):
#     if message == 'exit':
#         print('Bye!')
#         exit()
#     elif message == 'help':
#         print('The program calculates the sum of numbers')
#     else:
#         print('Unknown command')
#
#
# calc_memory = {}
#
#
# def memory_store(raw_input):
#     if raw_input.count('=') != 1:
#         print('Invalid assignment')
#     else:
#         inter_mem = list(raw_input.split('='))
#         if inter_mem[1].strip().isalpha() and not (inter_mem[1].strip() in calc_memory):
#             print('Unknown variable')
#         elif (not inter_mem[0].strip().isalpha()) and (not inter_mem[1].strip().isalpha()):
#             print('Invalid identifier')
#         else:
#             if inter_mem[1].strip().isalpha() and (inter_mem[1].strip() in calc_memory):
#                 inter_dict = {inter_mem[0].strip(): calc_memory[inter_mem[1].strip()]}
#                 calc_memory.update(inter_dict)
#             elif inter_mem[1].strip().isalpha() and not (inter_mem[1].strip() in calc_memory):
#                 print('Invalid assignment')
#             elif not inter_mem[1].strip().isalpha() and not inter_mem[1].strip().isnumeric():
#                 print('Invalid assignment')
#             else:
#                 inter_dict = {inter_mem[0].strip(): int(inter_mem[1].strip())}
#                 calc_memory.update(inter_dict)
#     return
#
#
# def memory_read(raw_input):
#     if not raw_input.isalpha():
#         print('Invalid identifier')
#     elif raw_input not in calc_memory:
#         print('Unknown variable')
#     else:
#         print(calc_memory[raw_input])
#     return
#
#
# # program main body
# while True:
#     raw_input = input('')
#     if raw_input.startswith('/'):
#         command(raw_input.lstrip('/'))
#     elif '=' in raw_input:
#         memory_store(raw_input)
#     elif raw_input.isalnum():
#         memory_read(raw_input)
#     elif not raw_input:
#         continue
#     else:
#         try:
#             print(operation(raw_input))
#         except:
#             print('Invalid expression 2')


class Calculator:
    variables = dict()

    def calc(self, exp):
        exp = exp.replace('---', '-').replace('--', '+')
        exp = exp.replace('+++', '+').replace('++', '+')
        exp = self.change_vars(exp)
        try:
            return eval(exp)
        except NameError:
            return 'Unknown variable'
        except Exception:
            if exp.startswith('/'):
                return 'Unknown command'
            return 'Invalid Expression'

    def change_vars(self, exp):
        for var in self.variables:
            if var in exp:
                exp = exp.replace(var, self.variables[var])
        return exp

    def var_contains_digit(self, var):
        return any(map(str.isdigit, var))

    def value_is_digit(self, value):
        return value.isdigit()

    def save_var(self, exp):
        exp = exp.replace(' ', '')
        index = exp.index('=')
        var = exp[:index]
        value = exp[index + 1:]

        if self.var_contains_digit(var):
            print('Invalid identifier')
            return
        if not value.isdigit() and value not in self.variables:
            print('Invalid assignment')
            return
        if value.isdigit():
            self.variables[var] = value
        else:
            self.variables[var] = self.variables[value]

    def main(self):
        while True:
            exp = input()
            if exp == '/help':
                print('The program adds and substtracts numbers')
            elif exp == '/exit':
                print('Bye!')
                break
            elif exp == '':
                continue
            elif '=' in exp:
                self.save_var(exp)
            else:
                print(self.calc(exp))


calc = Calculator()
calc.main()
