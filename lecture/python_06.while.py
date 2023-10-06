# while 반복문
# - 반복횟수를 모르는 경우
# - 조건이 만족하는 동안 계속 반복
# - 조건 True이면 무한 반복
# - 조건 False이면 반복 종료
# - while문에 조건 True -> 무한 loop문(조심!!)
# - 반드시 break 문과 함께 사용할것!


# while 기본 문법
# while 조건:
# 실행문


"""print("="*100)
a = list(range(1,6))
print(a)
length = len(a)
i =0
while i < len(a):
    print(a[i])
    i+=1

# 문제 7
print("="*100)
count =0
# 사용자가 입력한 값 1,2,3 통과
# 아닌 경우 다시 입력하도록
while True:
    if count >=4:
        print("프로그램을 사용 할 수 없습니다.")
        break;
    num = input("값: ")
    if num in [1,2,3]:
        print(f"{num}을 입력하셨습니다.")
    else:
        print("1,2,3의 값만 입력해주세요")
        count+=1
# 문제 7) 1부터 100까지 총합을 출력하는 코드
# -for문으로 작성
# -while문으로 작성"""

num =1
for i in range(1,101):
    num+=i
print(num)
print("\n")
num2=1
