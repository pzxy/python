# Python 容器类型示例

# 1. 列表 (List) - 有序、可变
from typing import Any


list1 = [1, 2, 3,3, 4, 5]
print("列表:", list1)
list1.append(6)  # 添加元素
print("添加后:", list1)
list1.insert(0, 0)  # 在指定位置插入
print("插入后:", list1)
list1.remove(3)  # 删除元素
print("删除后:", list1)
print("列表长度:", len(list1))
print("切片:", list1[1:4])  # 切片操作

# 2. 元组 (Tuple) - 有序、不可变
tuple1 = (1, 2, 3, "hello", True)
print("\n元组:", tuple1)
print("元组长度:", len(tuple1))
print("访问元素:", tuple1[0], tuple1[-1])  # 索引访问
# tuple1[0] = 10  # 错误！元组不可变

# 3. 字典 (Dict) - 无序、可变、键值对
dict1 = {"name": "Python", "version": 3.9, "type": "language"}
print("\n字典:", dict1)
print("访问值:", dict1["name"])
dict1["year"] = 1991  # 添加键值对
print("添加后:", dict1)
print("所有键:", dict1.keys())
print("所有值:", dict1.values())
print("所有项:", dict1.items())

# 4. 集合 (Set) - 无序、可变、不重复
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("\n集合1:", set1)
print("集合2:", set2)
set1.add(6)  # 添加元素
print("添加后:", set1)
print("交集:", set1 & set2)  # 或 set1.intersection(set2)
print("并集:", set1 | set2)  # 或 set1.union(set2)
print("差集:", set1 - set2)  # 或 set1.difference(set2)

# 5. 字符串 (String) - 有序、不可变
str1 = "Hello Python"
print("\n字符串:", str1)
print("长度:", len(str1))
print("切片:", str1[0:5])  # 切片
print("分割:", str1.split())  # 分割成列表
print("连接:", "-".join(["a", "b", "c"]))

# 6. 容器嵌套
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\n嵌套列表:", nested_list)
print("访问:", nested_list[0][1])  # 访问嵌套元素

nested_dict = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 21}
}
print("嵌套字典:", nested_dict)
print("访问:", nested_dict["student1"]["name"])

# 7. 列表推导式
list_comp = [x * 2 for x in range(5)]
print("\n列表推导式:", list_comp)

# 8. 字典推导式
dict_comp = {x: x**2 for x in range(5)}
print("字典推导式:", dict_comp)

# 9. 集合推导式
set_comp = {x for x in range(10) if x % 2 == 0}
print("集合推导式:", set_comp)

# 10. 键值对动态存储和查找示例
print("\n" + "="*50)
print("键值对动态存储和查找示例")
print("="*50)

# 创建一个空字典，用于动态添加键值对
# 相同键时，新值会覆盖旧值
kv_dict = dict[Any, Any]()    

# 动态添加键值对（模拟从字符串 "1:a", "1:b", "2:bb" 等格式添加）
print("\n动态添加键值对:")
kv_pairs = ["1:a", "1:b", "2:bb", "3:ccc", "2:dd", "4:eeee"]

for kv in kv_pairs:
    k, v = kv.split(":")  # 分割键值对
    kv_dict[k] = v  # 直接赋值，如果键已存在则覆盖，不存在则创建
    print(f"  添加 {kv} -> 当前字典: {kv_dict}")

print(f"\n最终字典: {kv_dict}")

# 通过键查找值
print("\n通过键查找值:")
search_key = "1"
if search_key in kv_dict:
    print(f"键 '{search_key}' 对应的值: {kv_dict[search_key]}")
else:
    print(f"键 '{search_key}' 不存在")

# 继续动态添加（相同键会覆盖）
print("\n继续动态添加:")
kv_dict["5"] = "新值1"
print(f"添加 '5:新值1' 后: {kv_dict}")
kv_dict["5"] = "新值2"  # 覆盖之前的值
print(f"添加 '5:新值2' 后（覆盖）: {kv_dict}")

# 查找新添加的键
print(f"\n查找键 '5': {kv_dict.get('5', '不存在')}")
