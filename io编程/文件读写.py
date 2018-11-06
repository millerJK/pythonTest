try:
    f = open("D:/work/python/testfile.txt", 'r')
    print(f.read())
finally:
    f.close()

# 读写文件有可能失败，所以使用了try  catch ,还有一种简便的方法
with open("D:/work/python/testfile.txt", 'r') as f:
    print(f.read())

# read （）如果文件很小一次性将文件中的所有的内容会很方便，如果文件过大一次性读取所有的内容肯定不行，所以使用readline 和 read(size) 进行读取
with open("D:/work/python/testfile.txt", 'r') as f:
    for line in f.readlines():
        print(line.strip())

with open("D:/work/python/testfile.txt", 'r', encoding="utf-8") as f:
    print(f.read())

#以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）
with open("D:/work/python/testfile.txt",'a',encoding="utf-8") as f:
    f.write("你好")


with open("D:/work/python/testfile.txt",'r',encoding="utf-8") as f:
    while True:
        s = f .readline().strip()
        print(s)
        if s == '':
            break

