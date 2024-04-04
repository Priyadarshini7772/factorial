def facto(num):
    if num>0:
        if num<=1:
            return 1
        else:
            return num*facto(num-1)
num=int(input('enter number: '))
res=facto(num)
print(res)