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


def reversal1(n, lst=[]):
    x, y = divmod(n, 10)
    lst.append(y)
    if x == 0:
        return lst
    return reversal1(x, lst)


print(reversal(str(1234)))
print(reversal1(1234))


# 猴子吃桃
def peach(n, count=0):
    count += 1
    x = n // 2 - 1
    if x < 1:
        return x, count
    return peach(x, count)


print(peach(10))
