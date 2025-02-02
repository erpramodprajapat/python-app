# Desing pattern in S/W engineering
# Desing pattern in iterator

data=[10,20,30,40]

def ite1():
    for i in data:
        print(i) #iterator


def ite2():
    d=iter(data)
    print(type(d))
    print(d.__next__())
    print(d.__next__())
    print(next(d))
    print(next(d))
    print(next(d))


#custom iterator


if __name__=='__main__':
    ite1()
    ite2()