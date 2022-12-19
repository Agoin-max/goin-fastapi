from greenlet import greenlet


# 通过greenlet实现协程

def fun1():
    print(1)  # 第1步 输出1
    gr2.switch()  #
    print(2)
    gr2.switch()


def fun2():
    print(3)
    gr1.switch()
    print(4)


gr1 = greenlet(fun1)
gr2 = greenlet(fun2)

gr1.switch()
