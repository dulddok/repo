mario_mushroom = [int(input()) for i in range(10)]
score = 0
temp = 0
for mario in mario_mushroom :
    score +=mario
    temp = score-mario
    if score == 100 :
        break
    elif score>100 :
        if score -100 <= 100 -temp:
            break
        else :
            score = temp
            break

print(score)


