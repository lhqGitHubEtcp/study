import  os
import  re
import threading
import  traceback
from lettuce.exceptions import  StepLoadingError

world = threading.local()
world._set = False


# os.path.abspath(__file__) 获取当前运行脚本的完成(绝对)路径
# co_filename 代码对象所在的文件名 co_firstlineno   代码对象的第一行位于所在文件的行号
def _function_matches(one , other):
    return (os.path.abspath(one.__code__.co_filename) == os.path.abspath(other.__code__.co__filename) and
            one.__code__.co_firstlineno == other.__code__.co_firstlineno)

class CallbackDict(dict):
    def append_to(self,where,when,function):
        if not any(_function_matches(o, function) for o in self[where][when]) :
            self[where][when].append(function)


    def clear(self):
        for name, action_dict in self.items():
            for callback_list in action_dict.values():
                callback_list[:] = []