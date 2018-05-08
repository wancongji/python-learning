n = int(input("Please input a number: "))
for i in range(2,n):
    if n%i == 0:
        print(i)
        print("The number is SUSHU.")
        break
else:
    print("The number is not SUSHU.")
    
