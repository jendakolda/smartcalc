def postfix(exp):
    postfix = []
    stack = []
    infix = (list(exp.replace('(', ' ( ').replace(')', ' ) ').split()))
    print(infix)
    for i in infix:
        if i.isnumeric():  # 1
            postfix.append(i)
        elif (not stack or stack[-1] == '(') and i in '+-/*':  # 2
            stack.append(i)
        elif i in '/*' and stack[-1] in '+-':  # 3
            stack.append(i)
        elif i in '+-' and stack[-1] in '+-*/':  # 4
            while stack[-1] in '+-*/':
                postfix.append(stack.pop())
                if not stack:
                    break
            stack.append(i)
        elif i in '*/' and stack[-1] in '*/':
            while stack[-1] in '*/':
                postfix.append(stack.pop())
                if not stack:
                    break
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    add = stack.pop()
                    postfix.append(add)

    for _ in stack:
        postfix.append(stack.pop())
    postfix.append('-')
    print(postfix)
    return postfix


def evaluate(postfix):
    s = []
    for symbol in postfix:
        try:
            result = int(symbol)
        except ValueError:
            if symbol not in '+-*/':
                raise ValueError('text must contain only numbers and operators')
            result = eval('%d %s %d' % (s.pop(), symbol, s.pop()))
        s.append(result)
    return s.pop()


exp = '3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)'
postfixed = postfix(exp)
print(evaluate(postfixed))
