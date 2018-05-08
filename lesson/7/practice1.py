n = input("Please input a number(n>=0): ")
num = int(n)
if num < 0:
    print("Please input a right number!!")

for i in range(num+1):
    if i == 0 or i == num:
        print('* '*(num+1))
    else:
        print('* ', '  '*(num-2), '* ')