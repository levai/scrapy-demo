name = "张三"
age = 13
msg = "我的名字是：%s" % name
print(msg)

msg2 = "我的名字是：%s,今年%s岁！" % (name, age)
print(msg2)
'''
格式符号
    %s  将内容转换成字符串，放入占位位置
    %d  将内容转换成整数，放入占位位置
    %f  将内容转换成浮点型，放入占位位置
'''
num = 11
num2 = 11.345

print("数字11宽度限制5，结果是：%5d" % num)
print("数字11宽度限制1，结果是：%1d" % num)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)

# f标记模板

name = "张三"
age = 18
sex = "男"
print(f"我是{name},{age}岁,{sex}")
