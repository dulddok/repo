# def insert(v) :
#     for i in range(1, len(v)) :
#         j = i-1
#         while(j>=0 and v[i]<v[j]) :
#             j -=1
#         v.insert((j+1),v[i])
#         del v[i+1]
#     return v

x = int(input())
num_list = []
for i in range(x):
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])