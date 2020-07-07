# write your code here
x = list(map(int, input("").split()))
total = 0
for element in range(len(x)):
    total = total + x[element]
print(total)