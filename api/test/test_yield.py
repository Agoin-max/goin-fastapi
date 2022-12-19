def func1():
    yield 1
    yield from func2()
    yield 2


def func2():
    yield 3
    yield 4


gen_obj = func1()

for item in gen_obj:
    print(item)
