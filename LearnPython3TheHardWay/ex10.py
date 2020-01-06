
# ex10 那是什么
# \转义

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# """""" 和''''''功能一致，只是风格问题
custom_cat = '''
something
what
'''

print(custom_cat)
print("转义测试\n响铃符：\a结束点\n退格符：\b结束点")
# \\ 转义成反斜杠（\）
# \' 转义成单引号（'）
# \" 转义成双引号（"）
# \a 转移成响铃符（BEL）
# \b 转义成退格符（BS）
# \f 转义成进纸符（FF）
# \n 转义成换行符（LF）
# \N{name} 转义成数据库中的字符名
# \r 转义成回车符（CR）
# \t 转义成水平制表符（TAB）
# \uxxxx 转义成值为16位十六进制值xxxx的字符
# \Uxxxxxxxx 转义成值为32位十六进制值xxxxxxxx的字符
# \v 转义成垂直制表符（VT）
# \ooo 转义为值为八进制值ooo的字符
# \xhh 转义成值为十六进制值hh的字符
