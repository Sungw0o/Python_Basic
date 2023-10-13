# 문제1) 입력 된 단수를 출력하는 코드
#dan = int(input("단수: "))
#for i in range(1,10):
#   print(f"{dan}x{i}={dan*i}")

# 문제2) 2단부터 9단까지 출력하는 코드
"""for i in range(2,10):
    print(i,"단\n")
    for j in range (1,10):
        print(i,"*",j,"=",i*j)
# 문제3) list a의 평균 값을 계산하세요.
a = [1,2,3,4,5,99,87,54,2,5,4]
length = len(a)
total =0
for i in a:
    total+=i
result= total / length
# round(값, 소수점숫자): 반올림 
print(round(result,2)) #평균값

# 문제4) list b에서 최소값 찾기!
b = [22,1,4,7,98]
length = len(b)
num_min =b[0]
for num in b:
    if num < num_min:
        num_min= num
print(num_min) # 1 출력"""

# 문제5) list c의 최소값, 최대값 찾기
c =[2,5,7,1,8]
num_max = c[0]
num_min = c[0]
length = len(c)
for num in c:
    if num < num_min:
        num_min=num
    if num>num_max:
        num_max=num

print(num_min)
print(num_max)