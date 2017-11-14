#二进制
def trans(n):
    if(n>=2):
        trans(n//2)
    print(n%2,end='')


def p(n):
    if(n<0):
        print('-',end='')
        n=-n
    if(n//10):
        p(n//10)
    print(n%10,end='')
p(-130)