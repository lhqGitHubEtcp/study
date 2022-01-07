"""
闭包的前提条件：
1.外部函数中定义了内部函数
2外部函数有返回值
3返回值是内部函数名
4内部函数引用了外部函数的变量

"""
def func(numbers):
    a = 100
    def inner_func():
        nonlocal  a
        nonlocal  numbers
        numbers += 1
        for i in range(numbers):
            a += 1
        print('修改后的a:{}'.format(a))
    return inner_func
closure_sum = func(5)
closure_sum()
