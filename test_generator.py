def triangles():
    tri=[1]
    temp=tri
    j=0
    while j<10:
        # print('中断前tri为')
        yield tri#
        for i in range(1,len(tri)):
            # print('j=', j, 'i=', i)
            tri[i]=temp[i]+temp[i-1]
            # print('增加元素后tri为',tri)
        tri.append(1)
        # print('j=',j,'增加末尾1后tri=',tri)
        # print('j=',j,'暂存前temp=',temp)
        temp=tri[:]#传可变对象
        # print('j=',j,'暂存后temp=',temp)
        j=j+1

s=triangles()
for i in s:
    str(i)
    a=len(i)*''
    print(a,i)





