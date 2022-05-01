# def draw_star(n) :
#     global Map
#
#     if n == 3 :
#         Map[0][:3] = Map[2][:3] = [1]*3
#         Map[1][:3] = [1,0,1]
#         return
# # n이 3일때 배열로 9를 만들면 되고 9일때 배열로 27을 만들면 된다 제곱 3이기에
#     a = n//3
#     draw_star(n//3)
#     for i in range(3) :
#         for j in range(3) :
#             if i ==1 and j == 1 :
#                 continue
#             for k in range(a) :
#                 Map[a*i+k][a*j:a(j+1)] = Map[k][:a]
#
# N = int(input())
# # 2차원 배열에서의 1은 별 0은 빈칸
# #메인 데이터 리스트 컴프리헨션 - 2차원 배열 초기화
# Map = [[0 for in range(N)] for i in range(N)]
#
# draw_star(N)
#
# for i in Map :
#     for j in i :
#         if j :
#             print('*',end='')
#         else :
#             print('', end='')
#         print()

def star(x) :
    if x == 1:
        return['*']
    x = x//3
    a = star(x)
    topbotton =[i*3 for i in a]
    middle = [i+' '*x+i for i in a]
    return topbotton + middle + topbotton

n = int(input())
mystar = '\n'.join(star(n)) # join 은 문자열 합치기 함수
print(mystar)