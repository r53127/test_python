
def _palindrome(n):
    m=str(n)
    for i in range(int(len(m)/2)):
        if m[i]!=m[len(m)-1-i]:
            return False
    else:
        yield n

 it = filter(_palindrome(n), list(range(1000)))






