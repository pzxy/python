# 猜大小。
import random

for i in range(3):
    print(i)

i = random.randint(0, 100)
while True:
    v = input("请输入一个值:\n")
    if int(v) > i:
        print("输入大了\n")
        continue
    if int(v) < i:
        print("输入小了\n")
        continue
    break
print("当前随机值为:{},输入值为:{}".format(i, v))
print("当前随机值为:%d,输入值为:%s" % (i, v))
print("当前随机值为:{0},输入值为:{1}".format(i, v))
print("当前随机值为:{n1},输入值为:{n3},{n1}".format(n1=i, n3=v))
