#조건문(Condition) : if~elif~else

# - 특정 조건을 만족하는 경우에만 수행할 작업이 있는 경우
# - 모든 조건은 boolean으로 표현 됨
# - 조건문의 경우 if,elif,else 블록 내 종속된 코드 들여쓰기
# - 모든 블록문의 시작점은 마지막에 :(콜론, colon) 추가
# - python에서 블룩내에 코드는 반드시 들여쓰기(Tab) 강제!

# if(조건 1) {        if 조건1:
#    code               code
# } else if(조건 2){  elif 조건2:
#  code                 code
#}

# if 조건 1:
#   code
# elif 조건 2:
#   code
# elif 조건  3:
#   code

# 1.if
# 2.if~elif~elif
# 3.if~eise
# 4.if~elif~else

# 점수 계산기
# 91~100: A
# 81~90: B
# 71~80: C
# 61~70: D
# 60이하 F


"""
score = int(input("점수를 입력하세요: "))
if 91 <= score <= 100:
    grade = "A"
elif 81 <= score <= 90:
    grade = "B"
elif 71 <= score <= 80:
    grade = "C"
elif 61 <= score <=70:
    grade = "D"
else:
    grade = "F"
print(grade)#
"""
# 1.And
# 조건1   조건2     결과
# F   and F         F
# T   and F         F
# F   and T         F
# T   and T         T
# 2.OR
# 조건1   조건2     결과
# F   and F         F
# T   and F         F
# F   and T         F
# T   and T         T
# 3.NOT
# T->F
# F->T

# 문제1. 어떤 종류의 학생인지 맞히기?
#(초등, 중등, 고등 , 대학생 , 학생X)

from datetime import datetime

born = input("당신이 태어난 연도를 입력하세요: ")
print(born)
today = datetime.today().year
age= today - int(born)+1
print(age)
if 8 <= age <= 26:
    if age >= 20:
        print("대학생")
    elif age >=17:
        print("고등학생")
    elif age >=14:
        print("중학생")
    elif age >=8:
        print("초등학생")
    else:
         print("학생이 아닙니다.")