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
def peach(day=9, sum=1):
    sum = 2 * (sum + 1)
    day -= 1
    if day == 0:
        return sum
    return peach(day, sum)

def peach1(n):
    if n == 1:
        return 1
    return (peach1(n-1)+1) * 2


print(peach())
print(peach1(10))
