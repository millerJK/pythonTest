from functools import reduce

print('hello,world');
print(1024*768);


#name = input();
#print("aaa,",name);
#print("aaaaaa",name);



print('''我是传奇
		 我是传奇
		 我是传奇吗''');

print('那是一条神奇的天路','带领人民走向幸福') #多个参数以逗号进行分割， “,”号会被替换为空格


a = 2;
if a > 1:
    print("yes");
else:
    print("no");


a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

a = 1;
a = '123';
print(a);

print("Hi, %s,you have $%d." % ('michael',10000));





#运算符
print(True and False);
print(True and True);
print("" and "".strip());
print(True or False);
print(not True); #false






#占位符
print('%02d-%02d' % (3, 111)) #多个占位符替换
print('%.2f' % 3.1465926) #保存小数点后两位，四舍五入
print('%s' % True);
print('%s食品占总销售额的 %d %%' % ('苹果',12)); # %% 表示 % 类似于转义字符 结果： 苹果食品占总销售额的 12 %






#字符转换
print('中文'.encode('gb2312'));
print('中文'.encode('utf-8'));






print('\n----------------列表和元组-------------------')
#list 列表 获取位置从坐标 0 开始
classes = ['python','java','c','html'];
print(classes);
classes.append('h5'); #追加列表元素
print(classes);
classes.insert(0,'ai'); #第一个位置中插入数据
print(classes);
classes.pop(-2); #删除最后一个元素，倒数第二个一次类推
print(classes);
classes.pop(); #删除列表最后一个元素，列表中元素为空的时候,pop 抛出 indexError 异常
print(len(classes));
classes[0] = 'sara'; #替换值
print(classes);

print(classes[0]);
print(classes[2]);
print(classes[-1]); #下标为-1则表示获取最后一个元素
print(classes[-2]); #获取倒数第二个数据，倒数第三个数据为 -3 ......


#tuple 元组  元祖中的数据不可以重复赋值，不可删除 不可插入
names = ('java','sara','miller');
print(names[0]);
print(len(names));

ints = (1); #不是元组，（）也可以表示运算，所以声明只有一个元素的元组必须在元素后面添加一个逗号
ints = (1,);  #元组
print(ints)






#条件判断

if True:
	print('yes');
else:
	print('false');

a = 65;

if a >= 90 and a <= 100:
	print("你真的很优秀");
elif a > 80 and a <90:
	print('也还不错');
elif a > 60 and a <80:
	print("也行");
else:
	print("不及格");

print(int('1000')>22); #不同数据类型之间不能进行比较，需要先进行转换






#循环
print('----------------循环 for while-------------------')

print(1+1+2);

names = ['Michael', 'Bob', 'Tracy']
for name in names:
	if name == 'Bob':
		continue;
	print(name);


n = 0;
while n < 10:
	if n == 6:
		break;
	n+=2;
	print(n);


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

nums = range(5);
print(nums);
nums = list(range(5));
print(nums);
sum = 0
#不带5，截止到4
for x in range(5):
    sum = sum + x
print(sum)




#dict 字典 dictionary  键值对形式存在, key 值唯一性  集合形式 {，，，，，，}
print('----------------集合 dict------------- ----')
d={'Michael': 95,'Bob':45,'jack':12,'jack':21}; #初始化
print(d);
print(len(d));


print(d['Michael']); #如果key不存在就会报keyError错误，为了避免出现该异常可以提前进行判断 'Michael' in d;
if 'jack' in d:
	print('yes');

print(d.get('miller')); #不存在则返回None
print(d.get('miller',-1)); #可以指定返回不存在值 -1

print(d['Bob']); #查
d['Michael'] = '12'; #改
print(d.pop("jack"));  #删除字典中某个数据

print('----------------集合 set-------------------')
ints = {0,1,2,4,5,7,3,2}; # 初始化赋值
print(ints);
s = set(list(range(0,5))); #赋值
print(s);
s = set([1,2,2,3]); #重复值将会进行过滤
print(s);
s.add(5); #增  s.add(value);
print(s);
s.remove(5); #删  s.remove(value);  若集合中不存在该value则会抛出keyError异常
print(s);


print('----------------系统函数------------------------')
print(abs(100)); #绝对值
print(max(1,-1,-2,-3));#获取最大值
print("----  ----")
print(int('123')) #字符串转换为整数
print(int(12.94)) #字符类型转换为整数(小于等于该值的最小整形) 
print(float('12.34')) #字符串转换为float
print(str(1.23)) #浮点类型转换为字符类型
print(bool(1)); #大于等于1的都是true
print(bool(0));
print(str([1,2,3]));


print('----------------函数类型------------------------')


#位置参数
def max(x,y):
    fx = float(x)
    fy = float(y)
    if(fx > fy):
        return fx
    else:
        return fy


print(max(12.32,"14"));

#写一个大致架构的时候可以使用该方法，先写架构在填内容
def thinking():
	pass

print(thinking());


print('--默认参数--');
#可以设置默认参数   注意：必选参数在前，默认参数在后
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5));


#默认参数，在传入值的时候可以指定传入的默认值
def student_info(name,age,sex='男',country='中国'):
	print(name,"的年龄是",age,"性别:",sex,"来自",country)

student_info('小明',12);
student_info('小花',23,country="美国");


def add_end(L=[]):
	L.append('End');
	print(L);

add_end();
add_end();
add_end();
add_end([1,2,3]);


print('--可变参数--');
#可变参数  numbers 之前添加*
def total(*args):
	s = 1;
	for num in args:
		s = s+num;
	print(s);

total(1,2,3,4,5,6,7,8);
#列表前添加*，可以作为变量参数传入
nums = [1,2,3,4,5,6,7,8,9]
total(*nums);
#元组前添加* 也可以作为变量传入
numss = (1,2,3,4,5,6,7,8,9)
total(*numss);


print('--关键字参数--');
#关键字参数  键值对形式存在
def human(name,age,**kw):
	if 'job' in kw:
		print('this human has job');
		pass
	print(name,age,"sex:",kw);

human('周星驰',12);
human('周星驰',12,sex='男');
human('周星驰',12,sex='男',wife="朱茵");
#也可以直接将集合作为参数传入
extra = {'sex':'男','wife':'朱茵',"job":"导演"};
human('周星驰',12,**extra);

#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法

print('----------------递归函数------------------------')

def fact(n):
    if n == 1:
        return 1;
    return n * fact(n - 1)

print(fact(5));

print('----------------迭代------------------------')

#遍历列表
for number in range(0,5):
	print(number);

nums = list(range(5));

for number in list(range(5)):
	print(number);

#遍历集合
ds = {'a':1,'b':2,'c':3}
for d in ds:
	print(d,"---- %d" % ds[d]);

#遍历字符串
for c in "asdasd":
	print(c);

#遍历set集合
for key in {1,2,3,4}:
	print("set: %d" % key);


print('----------------列表生成式------------------------')

#使用range 便捷生成列表
print(list(range(0,5)));
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x % 2 ==0])



print('----------------切片------------------------')

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)

#包含下标0不包含下标3  L[0] L[1] L[2]
print(L[0:3]);
print(L[:3]);  #实际上获取 L[0] L[1] L[2]
print(L[3:]);  #从下标3开始到列表末尾
print(L[-2:]) #倒数第二个到最后
print(L[-2:-1]) #不包含最后一个
print((0,1,2,3,4,5)[3:]) #元组也可以切片
print('xaerthrt'[2:]) #字符串也可以进行切片
print('xaerthrt'[::-1]) #字符串反向

print('----------------高阶函数 map reduce filter sorted------------------------')

L = [('Bob',12),('jack',23)]
for yuan in L:
	print(yuan);

print('--sorted--')
lists = [36, 5, -12, 9, -21]
print(sorted(lists,key=abs)); 

def by_name(t):
    return t[0];

print(sorted(L,key=by_name));


print('--filter--')
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

print('--map--')
def f(x):
	return x * x;

print(list(map(f,[1,2,3,4,5,6,7])))

print('--reduce--')
def f(x,y):
	return x * x;

print(reduce(f,[1,2,3,4,5,6,7]))
