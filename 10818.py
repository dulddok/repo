# cnt = int(input())
# numbers = list(map(int,input().split()))
# max = numbers[0]
# min = numbers[0]
#
# for i in numbers[1:]:
#     if i > max :
#         max = i
#     elif i <min :
#         min =i
#
# print(min,max)

# N = int(input())
# array = list(map(int,input().split()))
# print(min(array), max(array))

N = int(input())
array = list(map(int,input().split()))
array.sort()
print(array[0],array[-1])