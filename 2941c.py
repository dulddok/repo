calpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
alpha = input()

for ca in calpha :
    alpha = alpha.replace(ca,'+')
print(len(alpha))
