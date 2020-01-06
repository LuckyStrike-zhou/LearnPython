
# ex38 列表的操作

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print(" 等一下，这不是十样东西，让我们补充上")

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("添加一个", next_one)
    stuff.append(next_one)
    print(f"现在有{len(stuff)}样东西")


print("现在有：", stuff)

print("让我们用这些东西做些事吧")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))  # join函数用于拼接
print('#'.join(stuff[3:5]))  # [3:5]为列表切片，从3开始依次取出，直到5切不包含5

