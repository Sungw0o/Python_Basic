# 컬렉션 타입
# - 변수 하나에 값을 여러개 지정
# - 실질적으로 변수에 컬렉션 1개가 저장
# - 리스트(list) , 튜플(Tuple) ,딕셔너리(Dictionary), 세트(Set)


# 1. 리스트(list)
# - 시퀀스 자료형 (연속 된 값 지정)
# - 대괄호 사용 []
# - 정렬 기능
# - mutable(생성 된 후 변경 가능)
# - index 사용(Slicing 가능)
# - packing unpaking 가능
# - 맴버함수 append(), extend() , insert() , remove(), pop(), index(), sorted() 등등
# - 2차원 리스트는 표(table)과 동일한 형태

# 리스트 초기화(생성)
list_a =[1,2,3]
list_b =[]
list_c = ["Chosun",98,3.14,[1,2,3]]

print(list_c[0]) # 리스트에서 단일 값 추출
print(list_c[1:3]) #리스트 슬라이싱

# 매칭과 언매칭

list_d = ["A","B","C"] #패킹
a,b,c = list_d #언패킹
#a= list_d[0]
#b= list_d[1]
#c= list_d[2]

# append(): 리스트 맨 마지막에 값 추가!
a = [1,2,3,4,5]
a.append(10)
print(a)

# insert(): 원하는 인덱스에 값 추가!
a.insert(1,"A") #인덱스 , 값
print(a)

# extend(): 리스트 병합(List A, List B)
a =[1,2,3]
b=[3,4,5]
a.extend(b) # a를 기준으로 병합
print(a)

# remove(값) : 리스트 내 원소를 값으로 삭제
# pop(인덱스) : 리스트 내 원소를 인덱스로 삭제
abc = [1, 2, 3, 4, 5]
abc.remove(3)  # 3이라는 값
print(abc)
e = abc.pop(0)     # 0번 인덱스
print(abc)
print(e)

# index() : ()안의 값의 인덱스를 출력
a = ["A", "B"]
print(a.index("B"))

# sort() and sorted() : 리스트 안의 원소들을 정렬
#  - sort() : 원본값 자체를 정렬(원본값 상실)   X
#  - sorted() : 원본값을 복제해서 정렬(원본값 유지)
a = [95, 1, 3, 55, 27, 45]
b = sorted(a)  # 디폴트: 오름차순
c = sorted(a, reverse=True)  # 내림차순
print(a)
print(b)
print(c)

print("*" * 100)

# 튜플(Tuple) Ex: 기차
# -list와 대부분 동일
# -시퀸스 자료형 (정렬 불가능)
# -immutable (생성된 후 변경 불가능)
# -index 사용 (Slicing 가능)
# -packing 과 unpacking 가능
# - () 사용 (생략 가능)
# * 여러분이 직접 tuple을 생성하는 경우 X
# -> 파이썬에서 결과값을 받을 때 Tuple로 제공

a = [1,2,3] #list
b = (1,2,3) #Tuple
c = 1,2,3 #Tuple (괄호를 생략 가능하다)

a[0]=99
print(a)

# b[0] = 99 -> 오류 출력 -> Tuple은 값 변경이 불가능함

# Tuple 원소가 1개인 경우, 1개의 값?
a = (1, 2, 3)  # Tuple
b = 1, 2, 3    # Tuple
c = (1)        # Tuple
d = 1          # Int(Tuple이 아닌 Int로 출력)
e = 1,         # Tuple(원소 1개인 경우 원소 뒤에 , 를 붙여주면 Tuple로 출력)
print(type(b))
print(type(d))
print(type(e))

print("=" * 200)

a = 5
b = 8

# 튜플 (Tuple) Ex: 기차
#   - list와 대부분 동일
#   - 시퀀스 자료형 ( 정렬 불가능 )
#   - immutable ( 생성된 후 변경 불가능 )
#   - index 사용 (slicing 가능)
#   - packing 과 unpacking 가능
#   - () 사용 ( 생략 가능)
#   * 여러분이 직접 tuple를 생성하는 경우 X
#   -> 파이썬에서 결과값을 받을 떄 Tuple로 제공

a= [1,2,3] #list
b= (1,2,3) #Tuple
c= 1,2,3   #Tuple ( 괄호 생략 가능 )

a[0]= 99
print(a)

#   b[0] = 99
#   print(b) # Tuple은 값 변경

#   튜플 원소가 1개인 경우
a=(1,2,3)   #Tuple
b=(1,2,3)   #Tuple
c=(1)       #Tuple
d=1         #int
e=1,        #tuple
print(type(b))
print(type(d))
print(type(e))

# a랑 b 바꾸기
a=5
b=8
a,b=b,a #Tuple Packing & unpacking 사용
print(a)
print(b)

#   3. 세트 (set) ex: 복주머니
#   - 수학의 집합 개념
#   - 순서 없음 (index 없음, 정렬 불가능)
#   - 중복값을 허용하지 않음 ( 매우 중요 !!!!! )
#   - 멤버함수 : union(), intersection(), difference() 등등
#   - {} 사용

set_a = {1,2,3}
set_b = {1,1,1,1,2,2,2,3,3,4,5}
print(set_b) #set_b 에서 중복값 제거 해줌

# 중복값 제거 활용 방법
a=["A","A","B","B","B","C","C","D","E"] #List type

a=set(a)  # list type을 set type으로 변환
print(a) # set로 나오게됨

a=list(a)  # set타입을 list타입으로 바꿈
print(a)   # list 타입으로 나오게됨

a=list(set(a)) # set type으로 변환하고 (중복값 제거 위해)-> list type로 다시 변환

#   4. 딕트 (dict) ex: 복주머니
#   - 순서가 없음 ( 인덱스 없음, 정렬 불가능 )
#   - {key : value} 사용  ->  ket, value 1 pair
#   - key는 중복 불가, value 중복 가능
#   - key를 통해서만 value에 접근 가능
#   - 멤버함수 : update(), get(), keys(), values(), items()

#   외부에서 데이터를 받아올 때 대부분 JSON 형식으로 전달
#       - JSON == DICT(동일)

#        key     value
dict_a={"Korea":"Seoul",
        "Canada":"Ottwa",
        "USA":"Washingthon D.C"}
print(dict_a)

#   update() : dict와 dict 병합
a={"a":1,
   "b":2}
b={"b":3,
   "c":5}
a.update(b) # 병합시 중복 key 있는 경우 입력값(b)이 우선
print(a)

# pop() : dict 원소를 key를 통해서 삭제
c = a.pop("a") # -> {"a":1} 지워진닷
print(a)
print(c) # -> 삭제 된 value(key값 X)

# in() : ()안의 key 값이 존재 확인
print("c" in a)
print("f" in a)

# get() : 값 접근
# list, tuple, dict 접근 -> 컬렉션 [index or key] ex: a[2]
print(a["c"]) # dict인 a에서 "c"값의 value 값을 출력함
# print(a["f"])  key값인 "f"가 없으니 error 발생
print(a.get("f"))  # key가 없으면 None 출력 (Error X)

# keys(), values(), items()
print(a.keys())     # key만 추출
print(a.values())   # value만 추출
print(a.items())    # (key,value) 추출

print(list(a.keys())) # key만 추출하는데 list로 바뀌어서 추출한닷!!! >0<

# clear() : dict 초기화
print(a)
a.clear()
print(a)

a={}
print(type(a))

# 컬렉션 타입
# 1.List [] -> 수정 가능
# -sort() - 원만하면 사용 x
# -sorted() 원본값 복사 후 정렬 (오름차순)
# - remove (값)
# 2. Tuple()-> 수정 불가 (입력, 삭제, 정렬 x)
# - ()를 생략
# - (1,2,3) -> 1,2,3
# 1->1,
# 3.Dict{key:value}
# -> JSON(데이터 전송 포맷)
# 4.Set{1,1,1,2,2,3} ->