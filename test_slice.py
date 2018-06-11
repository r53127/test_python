def trim_a(s):
    while s!='' and s[0] == ' ':
        l = len(s)
        print('掐头')
        s = s[1:l]
        l = l - 1
        print('掐头后字符串为%s,长度为%d' %(s,l))
    while s!=''and s[-1] == ' ':
        l = len(s)
        print('去尾')
        s = s[-l:-1]
        l = l - 1
        print('去尾后字符串为%s,长度为%d' % (s, l))
    return s


def trim(s):
    # 必须加上s!='' 因为如果字符串为空，则第一个字符是S[0]是不存在的
    while s!='' and s[0] == ' ':
        s = s[1:]
    while s!=''and  s[-1] == ' ':
        s = s[:-1]
    return s

def trim_c(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')