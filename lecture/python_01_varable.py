# 주석 메모(comment): 단순 메모
#출력 함수(Print)

# - () 안의 값을 입력
# - 변수 값 확인 용도 또는 메세지 출력 용도
print("Hello Python")
print("=" * 200)

# 문자열 타입(String Type)
# - Python: ','"" String
# - C, Java '' (char), ""(String)

# 참고 : Escape code
# - 문법: \(역 슬러쉬) + @
# - 문자열 내의 이룹 문자의 의므를 달리하여 특정한 효과 주기
# - 예) \n : 한 줄 개행, \t: 탭(8칸 공백)
print("Hello \nPython")
print("Hello \nPython")

# 공부 tip
# - 몇 버전 부터 ~ 나온 기술(신기술) -> 신기술 공부, 구기술 공부 X

# 자료형(Type)
# -Python의 모든 자료형은 객체(Object)
# -C, Java 언어 문자형(Char): 'A','E' 키보드 제어!
# 1) 문자열(String): "Hello" , 'Hi'
# 2) 정수형(int): 3,0,-1
# 3) 실수형(float): 3.14, 0.0, -2.2
# 4) 논리형(boolean): True, False

# 예) JAVA 정수형 : byte, short,int ,long
# python 정수형: int
# 만들어진지 오래 된 언어는 다양한 종류의 자료형을 사용!
# 이유는: 자원(메모리)를 효율적으로 사용하기 위해서!
# 예: 자료형은 담을 수 있는 크기의 범위가 지정되어 있음
# 예를 들어서 int는(-10000~10000)까지 담을 수 있다고 가정
# 그런데 우리 회사에서 특정 값이 0~9만 사용
# int를 사용하게 되면 메모리 낭비, 이런 경우 크기의 범위가 더
# 작은 자료형을 사용하면 좋음(short)

# python 동적 타이핑 언어 -> python 실행 될 때 type을 지정!
# type() 함수: ()안의 값의 type을 확인할때 사용
print(type("ABC"))
print(type(123))

#형 변환(Type Casting)
# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
# 1) int(): 정수형으로 변환
# 2) float(): 실수형으로 변환
# 3) str(): 문자열형으로 변환
print("=" * 200)

# Type Casting 실습

# 1) 문자열 정수형("3") -> 정수형(3)

# 2) 문자열 정수형("3") -> 실수형

# 3) 문자열 실수형("9.2") -> 정수형 (Error: X)

# print(int(str_float_b))
# 4) 문자열 실수형("9.2") -> 실수형

# 5) 정수형 -> 실수형

# 6) 정수형 -> 문자열

# 7) 실수형 -> 정수형

# 8) 실수형 -> 문자열

# * float("Hello), int("Hello) 형 변환 불가!

# None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초깃값을 갖지 않게 변수만 생성하고 싶을 때 사용
# - 기타 언어의 Null과 같은 의미로 사용!
# 예) Student_name
print("=" * 200)
student_name = None # 적극 권장 X (절대 사용 금지)
student_name = "" # 적극 권장 O
# 이유 ? Null Pointer Exception Error -> 개발자들 공포의 대상!!

# 기본 자료형(Primitive Type) : 변수에 값이 저장
# - int num = 4;
# 객체 자료형(Reference Type) : 변수에 값의 "주소"가 저장
# - String name = "10";
# * Java: 기본, 객체 모두 사용
# * Python: 객체만 사용

# 변수(Variable)
# - 변수: 하나의 값을 저장할 수 있는 메모리 공간
print("=" * 200)
num = 4
num = 10
print(num) # 출력: 10

# - 변수 생성 및 초기화
# num = 5 # 문법
# 대입연산자(=) : 우측의 값을 좌측에 저장
# 동등연산자(==) : Equal

# name(변수명) , =(대입연산자) , "Sungwo Jang"(값)
name = "Sungwo Jang"

# C 언어 변수 생성 -> int b; (변수 생성, 값 X)
# Python 변수 생성 -> b (변수 호출)

# 명명규칙(Naming Rule)
# - 변수, 함수, 클래스 등의 사용자 정의 이름을 붙일 때 사용!
# - 명확하고 알아보기 쉽게 짓기!


# 1. 영문 대소문자, 숫자, 특수문자(_)만 사용
# 2. 숫자로 시작할 수 없음
# abc1(0) , 1abc(X)
# 3. 영어 대소문자 구별
# 4. 예약어 사용 불가
#   예약어: Python에서 미리 선정하여 사용중인 키워드
#       ex) print, for, while, if, else ,class, try,except,True,False, and, return ,import, def, pass,brea,cotinue,del..
#
#
# Naming Method
# - 변수,함수,클래스 등의 사용자 정의 이름에 사용하는 기법
# - 프로그래밍 언어별로 사용하는 Naming Method가 다름!

# 1. snake_case: 소문자만 사용, 합성어는 (_)사용
#   ex) student_name
# 2. camelCase: 첫 글자 소문자, 합성어 첫글자 대문자
#   ex)studentName
# 3. PascalCase: 첫 글자 대문자, 합성어 첫글자 대문자
#   ex) StudentName

#                   변수                  함수                       클래스
# Java,C            camelCase          camelCase                PascalCase
# Python            snake_case          snake_case              PascalCase

# 개발자: Web(프론트엔드, 백엔드), 앱(Android Apple) , 웹 퍼블리셔
# 웹 디자이너
# 서버 엔지니어(Linux 운영 관리) + 클라우드 개발자
# 네트워크 엔지니어
# 데이터베이스 엔지니어, 데이터베이스 관리자
# SQL 튜너
# 데이터 모델러
# ERP 개발자
# 보안 개발자
# 인공지능, 데이터 사이언티스트 ,프롬포트 엔지니어, 데이터 분석가
# 데이터 엔지니어


# format 출력(동적 출력)
print("=" * 200);
student_num = 20204467
student_name = "Sungwo Jang"
# 출력 예: "조선대학교 20204467, Sungwo Jang 입니다."
print("조선대학교 20204467, Sungwo Jang 입니다") # 하드 코딩 지양!

# 1. format() 함수 - Old한 방법
print("조선대학교 {}, {} 입니다.".format(student_num,student_name))

#2. f-string - new
print(f"조선대학교 {student_num}, {student_name} 입니다.")

# 간단한 사칙연산
# + : 더하기
# - : 빼기
# * : 곱하기
# / : 나누기
# // : 나누기 (몫)
# % : 나누기 (나머지)
# ** :