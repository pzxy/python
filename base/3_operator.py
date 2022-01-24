
a = 21
b = 10
c = 0
f = 2.1
s = "abc"
# 31
print(a+b+c)
# 报错，不能拼接字符串 和 java不一样
#print(a+b+s)
# int +float = float
print(b+f)
# f^b，2.1的10次方,都可以为float
print(f**b)
# 会保留小数
print(a/b)
# 相当于int类型在go和java以及c中的意思，会向下取整数。即使是浮点数，也会取整。
print(a//f)
