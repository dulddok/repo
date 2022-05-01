n = int(input())
books = {}
for i in range(n) :
    book = input()
    if book not in books :
        books[book] = 1

    else :
        books[book] +=1

max_freq = max(books.values())

bestseller = []

for book, number in books.items():
#     #(key, value)로 구성된 리스트를 리턴해서 key, value를 바로 뽑아 사용 하는 방식입니다.
#     # key 와 value 를 한 번에 뽑아와야 할 때 가장 좋은 방법으로 보입니다.
     if number == max_freq :
         bestseller.append(book)


print(sorted(bestseller)[0])


# # dict 사용법
# some_dict = {'june':12, 'hello' : 22, 'world' : 33}
# dd = []
# kk = []
# for some , num in some_dict.items():
#     dd.append(some)
#     kk.append(num)
#     print(dd)
#     print(kk)
# for key in some_dict.keys():
#     print(key, ':', some_dict[key])
