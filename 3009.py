x_list = []
y_list = []
cnt = 0
xpoint,ypoint=0,0
for i in range(3) :
    a,b = map(int,input().split())
    x_list.append(a)
    y_list.append(b)

if x_list.count(x_list[0]) %2 ==0 :
    for x in x_list[1:] :
        if x !=x_list[0] :
            xpoint = x
else :
    xpoint = x_list[0]

if y_list.count(y_list[0]) %2 ==0 :
    for y in y_list[1:] :
        if y !=y_list[0] :
            ypoint = y
else :
    ypoint = y_list[0]

print(xpoint,ypoint)

# x_nums = []
# y_nums = []
# for _ in range(3):
#     x, y = map(int, input().split())
#     x_nums.append(x)
#     y_nums.append(y)
#
# for i in range(3):
#     if x_nums.count(x_nums[i]) == 1:
#         x4 = x_nums[i]
#     if y_nums.count(y_nums[i]) == 1:
#         y4 = y_nums[i]
# print(x4, y4)