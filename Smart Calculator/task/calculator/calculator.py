# write your code here
while True:
    input_line = input('')
    if input_line == '/exit':
        print('Bye!')
        break
    elif input_line == '/help':
        print('The program calculates the sum of numbers')
        pass
    elif not input_line:
        pass
    else:
        x = list(map(int, input_line.split()))
        total = 0
        for element in range(len(x)):
            total = total + x[element]
        print(total)
