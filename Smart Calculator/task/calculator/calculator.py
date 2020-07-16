# # Program Calculator: Jetbrains Hyperskill Hard project
# # (c) JendaKolda 2020
# # Program contains parts of opensource code which I have not coded myself


class infix_to_postfix:
    precedence = {'^': 5, '*': 4, '/': 4, '+': 3, '-': 3, '(': 2, ')': 1}

    def __init__(self):
        self.items = []
        self.size = -1

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pop(self):
        if self.isempty():
            return 0
        else:
            self.size -= 1
            return self.items.pop()

    def isempty(self):
        if self.size == -1:
            return True
        else:
            return False

    def seek(self):
        if self.isempty():
            return false
        else:
            return self.items[self.size]

    def infixtopostfix(self, expr):
        expr = (list(expr.replace('(', ' ( ').replace(')', ' ) ').split()))
        postfix = []
        for i in expr:
            if len(expr) % 2 == 0:
                print("Invalid expression")
                return False
            # elif self.isOperand(i):
            elif i.isnumeric():
                postfix.append(i)
            elif i in '+-*/^':
                while len(self.items) and self.precedence[i] <= self.precedence[self.seek()]:
                    postfix.append(self.pop())
                self.push(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                o = self.pop()
                while o != '(':
                    postfix.append(o)
                    o = self.pop()
            # end of for
        while len(self.items):
            if self.seek() == '(':
                self.pop()
            else:
                postfix.append(self.pop())
        return postfix


class Calculator:
    variables = dict()

    def calc(self, exp):
        exp = exp.replace('---', '-').replace('--', '+')
        exp = exp.replace('+++', '+').replace('++', '+')
        exp = self.change_vars(exp)
        if ('**' in exp) or ('//' in exp):
            return 'Invalid expression'
            pass
        try:
            s = infix_to_postfix()
            postfixed = s.infixtopostfix(exp)
            result = self.evaluate(postfixed)
            # print(result)
            return int(result)
        # except NameError:
        #    return 'Unknown variable'
        except Exception:
            if exp.startswith('/'):
                return 'Unknown command'
            elif exp not in self.variables:
                return 'Unknown variable'
            else:
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

    # tady je funkce na vyhodnoceni postfix notace
    def evaluate(self, postfix):
        stack = []
        for token in postfix:

            if token.strip() == '':
                continue

            elif token == "+":
                stack.append(stack.pop() + stack.pop())

            elif token == "-":
                op2 = stack.pop()
                stack.append(stack.pop() - op2)

            elif token == '*':
                stack.append(stack.pop() * stack.pop())

            elif token == '/':
                op2 = stack.pop()
                if op2 != 0.0:
                    stack.append(stack.pop() / op2)
                else:
                    raise ValueError("division by zero found!")
            elif '**' in token:
                print('Invalid expression')
                break
            elif token.isnumeric():
                stack.append(float(token))

            else:
                raise ValueError("unknown token {0}".format(token))
        return stack.pop()

    def main(self):
        while True:
            exp = input()
            if exp == '/help':
                print('The program adds and substracts numbers')
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
