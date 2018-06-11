def findMinAndMax(L):
    if len(L)==0:#if L==[]
        min = max= None
    else:
        min=max = L[0]
        for x in L:
            if x < min:
                min = x
            if x > max:
                max = x
    return min, max
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')