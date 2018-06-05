# 求n的阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# 将一个数逆序放入列表中，列入1234=>[4,3,2,1]
def reversal(n, lst=[]):
    if n:
        lst.append(n[len(n) - 1])
        reversal(n[:len(n) - 1])
    return lst


s = input("Please input a number: ")
print(reversal(s))
print(reversal.__defaults__)
