# 代码中经常会有变量是否为None的判断，有三种主要的写法：
# 第一种是`if x is None`；
# 第二种是 `if not x：`；
# 第三种是`if  x is  not None`（这句这样理解更清晰`if not (x is None)`）

# 在python中 None, False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False ，即 not None == not False == not '' == not 0 == not [] == not {} == not () =  true
x = 1
print(not x)

x = 0
print(x is not None)

x = [1]
print(not x)

x = []
print(not x)

# not x   在 x 为 None  False ""   0  [] {} () 的时候都为true，所以判断是否为None 最好使用 if  x  is not None   or  if   x is None





