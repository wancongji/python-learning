# m = int(input("Please input a odd number: "))
# for j in range(1,m+1,2):
#     blk = int((m-j)/2)
#     print(blk*' ','*'*j)

# for i in range(m-2,0,-2):
#     blk = int((m-i)/2)
#     print(blk*' ','*'*i)

n = int(input("Please input a odd number: "))
start = int((n-1)/2)
end = int((n+1)/2)
for i in range(-start, end):
    if i < 0:
        prespace = -i
        print(' '*prespace + '*'*(end-prespace))
    elif i == 0:
        print('*'*n)
    else:
        prespace = i
        print(' '*start + '*'*(end-prespace))
    
    # prespace = -i if i < 0 else i
    # print(' '*prespace + '*'*(7-prespace*2))