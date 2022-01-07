# 类名用大驼峰命名规则
# 函数 变量名
import  os
"""
        关键字不能为变量名
        False     None    and   as      assert    break    class    yield
        continue  def     del   elif    else      except   finally  for
        from      global  if    import  in        is       lamba    nonlocal
        not       or      pass  raise   return   try       while    with
"""
# get_name_byline = lambda : 0
# print(get_name_byline.__code__.co_filename)
# print(os.path.abspath(get_name_byline.__code__.co_filename))
#
# def outer():
#     no = 100
#     list1 = [2,4,5,6,2]
#     def inner_func():
#         nonlocal no
#         for index,i in enumerate(list1):
#             list1[index] = i + 5
#         list1.sort()
#         no += 100
#     inner_func()
#     print(list1)
#     print(no)
#
# outer()

"""
闭包的前提条件：
1.外部函数中定义了内部函数
2外部函数有返回值
3返回值是内部函数名
4内部函数引用了外部函数的变量

"""

def  closure():
    a = 2
    def inner_func1():
        b = 4
        print(a,b)
    return inner_func1
#调用closure()函数
x = closure()
#调用返回的内部函数  X就是 inner_func1()
x()
