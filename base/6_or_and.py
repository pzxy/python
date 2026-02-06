print(1 == 2 and 3 > 1) # false
print(1 != 2 and 1) # 1
print(0 and 8) # 0
print("" and 8) #  "" 
print(1 and 8) # 8
print(6 or 9) # 6
print(0 or 9) # 9
# 优先级 not and in
# and 运算符的行为：
# 如果第一个操作数为假值（falsy），返回第一个操作数（不再求值第二个）
# 如果第一个操作数为真值（truthy），返回第二个操作数


# or 运算符的行为：
# 如果第一个操作数为真值（truthy），返回第一个操作数（不再求值第二个）
# 如果第一个操作数为假值（falsy），返回第二个操作数