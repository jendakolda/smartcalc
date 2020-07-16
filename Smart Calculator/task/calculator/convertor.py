# def postfix(exp):
#     postfix = []
#     stack = []
#     infix = (list(exp.replace('(', ' ( ').replace(')', ' ) ').split()))
#     for i in infix:
#         if i.isnumeric():  # 1
#             postfix.append(i)
#         elif (not stack or stack[-1] == '(') and i in '+-/*':  # 2
#             stack.append(i)
#         elif i in '/*' and stack[-1] in '+-':  # 3
#             stack.append(i)
#         elif i in '+-' and stack[-1] in '+-*/':  # 4
#             while stack[-1] in '+-*/':
#                 postfix.append(stack.pop())
#                 if not stack:
#                     break
#             stack.append(i)
#         elif i in '*/' and stack[-1] in '*/':
#             while stack[-1] in '*/':
#                 postfix.append(stack.pop())
#                 if not stack:
#                     break
#             stack.append(i)
#         elif i == '(':
#             stack.append(i)
#         elif i == ')':
#             while True:
#                 if stack[-1] == '(':
#                     stack.pop()
#                     break
#                 else:
#                     add = stack.pop()
#                     postfix.append(add)
#
#     for _ in stack:
#         postfix.append(stack.pop())
#     postfix.append('-')  # smazat tento radek
#     print(postfix)
#     return postfix

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
                print("Incorrect infix expr")
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
        print(postfix)
        return postfix


def evaluate(postfix):
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

        elif token.isnumeric():
            stack.append(float(token))

        else:
            raise ValueError("unknown token {0}".format(token))
    return stack.pop()


exp = '33 + 20 + 11 + 49 - 32 - 9 + 1 - 80 + 4'

s = infix_to_postfix()
result = s.infixtopostfix(exp)


# post = convert(exp)
print(evaluate(result))
