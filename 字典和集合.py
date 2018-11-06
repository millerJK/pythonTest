# 字典  dict 在其他语言中称之为map，采用键值对的形式进行存储，重复会覆盖，dict 内部存储的顺序和放入顺序是不同的
d = {'Michael': "23", 'Bob': 75, 'Tracy': 85};
print(d["Michael"])

# 增(没有提供插入具体数据)
d['jack'] = 60;
print(d);

# 删除
d.pop("Michael")
print(d)

# 改
d['Michael'] = 23;
print(d)

# 查
print(d['Bob'])
print(d.get('Bobs', -1))

# 清除数据
print(d.clear())

# 辅助API
print("v" in d)  # key值是否存在字典中

# Set 集合 ： 和 java 中的set集合无异
s = set({1, 2, 1, 1, 4, 3})

# 增
s.add(5);
print(s);

# 删
s.pop();
print(s)
s.remove(2);
print(s)

# 改


# 查
