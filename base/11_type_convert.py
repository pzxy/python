# Python 类型转换示例

# 1. int、float、string 互相转换
print("=" * 50)
print("int、float、string 互相转换")
print("=" * 50)

# int() - 转换为整数
print("\n转换为整数:")
print("int(3.14) =", int(3.14))        # 3 (向下取整)
print("int(3.9) =", int(3.9))          # 3
print("int('42') =", int('42'))        # 42
print("int('3.14') =", int(float('3.14')))  # 需要先转float再转int

# float() - 转换为浮点数
print("\n转换为浮点数:")
print("float(42) =", float(42))        # 42.0
print("float('3.14') =", float('3.14'))  # 3.14
print("float('42') =", float('42'))    # 42.0

# str() - 转换为字符串
print("\n转换为字符串:")
print("str(123) =", str(123), type(str(123)))  # '123'
print("str(3.14) =", str(3.14))        # '3.14'
print("str(42) =", str(42))            # '42'

# 2. string 和 bytes 互相转换
print("\n" + "=" * 50)
print("string 和 bytes 互相转换")
print("=" * 50)

# string -> bytes
print("\n字符串转字节:")
text = "Hello, 世界"
print(f"原字符串: {text}")
byte_result = text.encode('utf-8')
print(f"encode('utf-8'): {byte_result}")
print(f"encode('utf-8') 类型: {type(byte_result)}")
print(f"字节数值列表: {list(byte_result)}")  # 显示每个字节的ASCII码/数值
print(f"字节数值列表: {[b for b in byte_result]}")  # 另一种方式

# ASCII字符的字节值
print("\nASCII字符的字节值:")
ascii_text = "Hello"
ascii_bytes = ascii_text.encode('utf-8')
print(f"字符串: {ascii_text}")
print(f"字节对象: {ascii_bytes}")
print(f"字节数值: {list(ascii_bytes)}")
print(f"对应ASCII码: {[ord(c) for c in ascii_text]}")  # 使用ord()获取字符的ASCII码

# bytes -> string
print("\n字节转字符串:")
byte_data = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(f"原字节: {byte_data}")
print(f"字节数值: {list(byte_data)}")  # 显示每个字节的数值
print(f"decode('utf-8'): {byte_data.decode('utf-8')}")
print(f"decode('utf-8') 类型: {type(byte_data.decode('utf-8'))}")

# 访问单个字节（返回整数）
print("\n访问单个字节:")
single_byte = byte_data[0]  # 获取第一个字节
print(f"byte_data[0] = {single_byte}, 类型: {type(single_byte)}")  # 72 (H的ASCII码)
print(f"chr({single_byte}) = {chr(single_byte)}")  # 将ASCII码转回字符
