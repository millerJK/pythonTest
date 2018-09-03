import logging


# try:
#     print("代码正常运行")
#     r = 10 / 2
#     print("result: %f " % r)
# except Exception as e:
#     print(type(e))
#     print("aaa")
#     print(e)
# except ValueError as  e:
#     print('bbb')
#     print(e)
# else:
#     print("没有发生异常")
# finally:
#     print('finally。。。。。')
# print("End")
#
#
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#     print("END")
#
#
# main()
#
#
# #抛出异常
# def test(str):
#     if str == "aaa":
#         raise ValueError("invail str: %s" % str)

# test("aaa");


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise  # 捕获了异常继续向外抛
    # 好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。


bar()
