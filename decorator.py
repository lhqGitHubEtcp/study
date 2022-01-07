'''
装饰器特点：
1.函数A作为参数传递给函数B
2.要有闭包的特点
'''
#定义装饰器
# def decorate(func1):
#     print("测试开始")
#     def wrapper():
#         func1()
#         print("开始装修")
#         print("刷漆")
#         print("我已经不是毛坯房")
#     print("测试结束")
#     return wrapper


#使用装饰器
import time

"""
decorate下的hourse称之为被装饰函数，
将被装饰的函数传给传给装饰器decorate ,
执行decorate 函数（将被装饰函数复制给func1）
将执行装饰器的返回值wrapper赋值给hourse
"""
# @decorate
# def hourse():
#     print("我还是毛坯房")
# hourse()
# print(hourse)
#--------------------------------------装饰器校验登录模拟------------

def decorate(func1):
    def wrapper(*args,**kwargs):  # *args 可变长参数  元组类型，**kargs  指定参数  字典类型
        print("校验中。。。")
        time.sleep(2)
        print("校验通过")
        func1(*args,**kwargs)
    return wrapper
@decorate
def denglu(n):
    print("请登录{}".format(n))

denglu(2)

@decorate
def xuanz(name,age):
    print("_______",name,age)
xuanz("xiaoli","18")

#地方京东客服进度款
@decorate
def students(student_list,ckazz = "3年级"):
    for stu in student_list:
        print(stu)
    print(ckazz)
student_list = [1,2,3,4,5,6]
students(student_list,ckazz = "8年级")