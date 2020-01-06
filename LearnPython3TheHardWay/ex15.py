
# ex15 读取文件

# from sys import argv
# script, filename = argv
#
# txt = open(filename)
#
# print(f"Here's your file {filename}.")
# print(txt.read())
# txt.close()
#
# print("Type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)
#
# print(txt_again.read())
# txt_again.close()


# ex16 读写文件

# close 关闭文件
# read 读取文件内容
# readline 只读取文本文件中的一行
# truncate 清空文件
# write('something') 写入文件
# seek(0) 将读写位置移动到文件开头

from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that ,hit CTRL-C(^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w') # 'w'为读写权限参数，w为只写入
print("Truncating the file. Goodbye")
target.truncate()

print("Now I'm going to ask you for three lines")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()