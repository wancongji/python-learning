factorial = 1
sum = 0
for i in range(1,4):
    for j in range(1,i+1):
        factorial *= j
    sum += factorial
    factorial = 1

print(sum)