N = int(input())

for _ in range(N) :
    student = list(map(int,input().split()))
    number = student[0]
    score = student[1:]
    scores = sum(score)
    average = 0
    highstu = 0
    average = scores/number
    for stu in score :
        if stu > average:
            highstu +=1
    result = highstu/number*100
    print(f'{result:.3f}%')

# n = int(input())
#
# for _ in range(n):
#     nums = list(map(int, input().split()))
#     avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
#     cnt = 0
#     for score in nums[1:]:
#         if score > avg:
#             cnt += 1  # 평균 이상인 학생 수
#     rate = cnt/nums[0] *100
#     print(f'{result:.3f}%')