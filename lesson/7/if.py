num = input("Please input numbers(0~99999): ")
val = int(num)
if val <= 99999:
    if val > 9999:
        for i in num:
            print(i)
        print(5)
    else:
        if val > 999:
            print(4)
        else:
            if val > 99:
                print(3)
            else:
                if val > 9:
                    print(2)
                else:
                    print(1)
else:
    print("Please input the right number!")

