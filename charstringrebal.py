data = input()
result = []
value = 0

#문자를 하나씩 확인하며
for x in data :
    #알파벳일 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else :
        value +=int(x)
#알파벳 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value!=0 :
    result.append(str(value))

# 최종 결과 출력
print(''.join(result))