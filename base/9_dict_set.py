# 字典
d = {"a": 1, "b": "b2", "c": True}
print(d)
# 集合
s = {1, "2", True}
print(s)
# 可以看出， python 中，变量是以内容为基准而不是像 c 中以变量名为基准，所以只要你的数字内容是5，
# 不管你起什么名字，这个变量的 ID 是相同的，同时也就说明了 python 中一个变量可以以多个名称访问
a = 5
b = 5
c = 6
print(id(a))
print(id(b))
print(id(c))
a = a + 1
print(id(a))
