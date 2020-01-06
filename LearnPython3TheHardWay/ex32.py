
# ex32 循环和列表

# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pear', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#
# for number in the_count:
#     print(f"This is count {number}")
#
# for fruit in  fruits:
#     print(f"A fruit of type: {fruit}")
#
# for i in change:
#     print(f"I got {i}")
#
# elements = []
#
# for i in range(0, 6):
#     print(f"Adding {i} to the list.")
#     # 往列表添加数据
#     elements.append(i)
#
# for i in elements:
#     print(f"Element was: {i}")


# ex33 while循环

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now :", numbers)
    print(f"At the bottom i is : {i}")
    print("The numbers:")

for num in numbers:
        print(num)
