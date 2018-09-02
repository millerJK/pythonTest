# 字典  dict
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

#清除数据
print(d.clear())


