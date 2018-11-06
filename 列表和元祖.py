# 列表list  和 元组 tuple之间的异同区别

#相同：
#1.下标都是从0开始

#差异：
#1.列表是有序可变集合，而tuple 则是不可变集合，在初始化一旦设置数据将不再能改动
#2.


classes = [];
print(classes)
classes = ["java", "math", "chinese", "english"];
print(classes)

# 增

# 最后一个列表追加元素
classes.append("android")
print(classes)
# 指定元素插入数据
classes.insert(0, "插入第一个元素");
print(classes)

# 删

# 删除列表最后一个元素
classes.pop();
print(classes)
# 删除列表最后一个元素
classes.pop(-1);
print(classes)
# 删除第一个元素
classes.pop(0);
print(classes)
# 删除“android” 的列表元素
if "android" in classes:
    classes.remove("android")
    print(classes)

# 改
classes[0] = "第一个元素"
classes[1] = "sex";
print(classes)

# 查
print(classes[0])
print(classes[-1])   # -1，-2，-3，-4 一次倒叙查询

#清除数据
classes.clear()
print(classes)



# 元组tuple （）

# 空元组
classes = ();
print(classes)
classes = ("Michael", "Bob", "Tracy");
print(classes)

# 增（元组一旦初始化不能进行修改）

# 删（元组一旦初始化不能进行删除）

# 改（元组一旦初始化不能进行修改）

# 查
print(classes[0]);
print(classes[2]);

#当元组中只有一个数据时，不是元组，如果要设置为元组，在唯一元素后面添加，号
names = (1)
print(names)

students = (1,)
print(students)

