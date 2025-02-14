#자료형
'''
   문자: 연산x, ' 'or" "
   숫자: 연산가능 / 정수, 실수, 8진수, 16진수수
   불리안: True, False => ex)체크박스
'''
#형변환
'''
   int('2') -> 정수로, int('two')=>변환불가, int('2.5')=>바로 변환불가->int(float('2.5'))->출력 2 
   float('2.5') -> 실수로
   str(2) -> 문자로
'''

#연산자
'''
   % : 나머지            산술 
   // : 몫               산술
   ** : 거듭제곱         산술
   == : 같다             비교 -> 결과값 불리안
   != : 같지않다          비교
   and : 둘다 참->T       논리 -> 결과값 불리안
   or : 둘중 하나 참 ->T   논리
   not : 반전             논리
   in : 포함              멤버 -> 결과값 불리안 ex) print('c' in 'cat')=>True
   not in : 미포함        멤버
'''
#불리안

#리스트 -> 순서o, 중복o, 접근o, 수정o, 추가o, 삭제o
my_list=['오예스','초코파이','몽쉘','초코파이']
your_list=['빅파이']
my_set=set(my_list) #세트로 형변환->중복자료 삭제 하지만 순서가 바뀜
my_list=list(my_set) #리스트로 다시 형변환 -> 중복은 제거 되지만 순서 보장이 안됨
my_dic=dict.fromkeys(my_list) #리스트 값을 key로 변형, value는 none으로 설정됨
my_list=list(my_dic) #딕셔너리의 key를 리스트로 다시 형변환 -> 순서 보장, 중복 제거
#dict(my_list) #사용불가 -> 딕셔너리로 형변환은 안됨

#튜플 -> 순서o, 중복o, 접근o, 추가x, 수정x, 삭제x
my_tuple=('오예스','초코파이','몽쉘') #패킹
(pie1, pie2, pie3)=my_tuple #언패킹
numbers=(1,2,3,4,5,6,7,8,9,10) #패킹
(one, two, *others)=numbers #언패킹, others에 3~10까지 리스트 형식으로 들어감
my_list=list(my_tuple) #리스트로 형변환하면 추가, 수정, 삭제 가능
my_list.append('초코파이') #리스트에 자료 추가
my_tuple=tuple(my_list) #튜플로 다시 형변환환

#딕셔너리 -> 순서o, 중복x(key), 접근o, 수정o, 추가o, 삭제o
person={'이름':'나귀욤','나이':7,'키':120,'몸무게':23} #딕셔너리 생성
person["최종학력"]='유치원' #새로운 데이터 추가
person['키']=150 #기존 데이터 수정
person.update({'키':130,'몸무게':30}) #두 개 이상의 데이터 수정
person.pop('몸무게') #해당 key, value 삭제
person.clear() #모든 key, value 삭제
person.keys() #key만 출력
person.values() #value만 출력
person.items() #key, value 출력 / key,value가 튜플로 묶여서 리스트 형식으로 출력

#참고사항
a=['a','b','c','d'] 
print(','.join(a)) #리스트를 str으로 변환, 형태는 ,로 구분

#조건문 if
today='화요일'
if today=='일요일':
    print('게임한판')
elif today=='토요일':
    print('폰 5분만')
elif today=='수요일':
    print('오늘은 수요일')
else:
    print('물 한 잔')
print('공부시작')
#elif는 if와 else 사이에 와야함

#if 중첩 -> 들여쓰기가 중요!
yellow_card=0
foul=True
if foul:
    yellow_card+=1
    if yellow_card==2:
        print('경고 누적 퇴장')
    else:
        print('휴..조심해야지')
else: 
    print('주의')

#for 반복문 -> for 변수 in 반복 범위 또는 대상:
for x in range(10): 
    print(f'팔 벌려 뛰기 {x+1}회')
#range(10)->0~9 0이상 10미만
#range(start,stop) start이상 stop미만 / range(1,10)->1이상 10미만
#range(start,stop,step) start이상 stop미만 step만큼 증가 range(1,10,2)->1,3,5,7,9

#for 활용문
my_list=[1,2,3,4,5,6]
person={'이름':'나귀욤','나이':7,'키':120,'몸무게':23}
for x in my_list:
    print(x)
for x in person.values():
    print(x)
for x,v in person.items():
    print(x,v)
for x in person.items():  #데이터가 튜플로 나옴옴
    print(x)
fruit='apple'   #숫자는 사용할 수 없음, 숫자를 문자로 사용하면 가능 ex)'350'
for x in fruit:
    print(x)

#while  for(정해진만큼만), while(계속해봐..)
max=25
weight=0
item=3
while weight+item<=max:
    weight+=item
    print('짐을 추가합니다. 현재 무게:{weight}')
print(f'총 무게는{weight}입니다.')

#break -> 반복문 탈출
drama=['시즌1','시즌2','시즌3','시즌4','시즌5']
for x in drama:
    if x=='시즌3':
        print(f'재미 없대, {x} 그만 보자')
        break
    print(f'{x}시청')

#continue -> 다음 반복 수행
for x in drama:
    if x=='시즌3':
        print(f'재미 없대, {x} 건너뛰자')
        continue
    print(f'{x}시청')

#들여쓰기(indent) -> 스페이스 4칸

#리스트 컴프리헨션 -> 새로운 리스트를 간편하게
#new_list=[변수활용 for 변수 in 반복대상 if 조건]
products=['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall=[]  #리콜대상 제품 리스트
for p in products:
    if p.startswith('SIRO'): #제품명이 SIRO로 시작하는가?
        recall.append(p)
recall=[p for p in products if p.startswith('SIRO')]
my_list=[1,2,3,4,5]
new_list=[x for x in my_list if x>3]  #new_list=[4,5]

#함수 
'''
def 함수명(전달값):
    수행할 문장
    return 반환값
'''
def show_price(customer): #함수 정의
    print(f'{customer} 고객님')
    print('커트 가격은 10,000원입니다.')
#함수는 호출을 해야 실행할 수 있다. (호출: 함수명 입력)
#전달값은 여러개 사용가능(콤마로 구분), 함수 내에서만 사용가능
cus1='나장발'
show_price(cus1)
cus2='나수염'
show_price(cus2)
#반환값: 함수 내에서 처리된 결과를 반환, 여러개 반환가능(콤마로 구분, 튜플), 반환되는 즉시 함수 탈출
def get_price(is_vip=False): 
    if is_vip==True: #True=단골손님 False=일반손님
        return 10000 #단골손님
    else:
        return 15000

price=get_price() #기본적으로 False로 작동 -> 기본값=False
print(f'커트 가격은 {price}원 입니다')
#기본값: 전달값에 기본적으로 사용되는 값 
#키워드값: 전달값 종류가 다양할 경우 순서 무관하게 입력하여 사용가능
#키워드값은 is_vip=True와 같이 정확하게 입력해줘야 함수 내 적절한 기능 사용가능
#가변인자(*전달값값): 개수가 바뀔 수 있는 인자, 전달값이 많으면 마지막에 한번만
def visit(today, *customers): #한 개만 *붙여서 사용가능
    print(today) #날짜 출력
    for customer in customers:
        print(customer) #고객이름 출력

visit('2022년06월10일','나장발') #1명 방문
visit('2022년06월10일','나장발','나수염') #2명 방문
visit('2022년06월10일','나장발','나수염','나감리') #3명 방문문

#지역변수: 함수 내에서 정의된 변수, 함수 내에서만 사용가능, 내부에서는 출력 가능
def secret():
    message='이건 나만의 비밀' #secret 함수 내에서 정의
    print(message) #값 출력 가능
    message='함수 내에서는 자유롭게 수정 가능'

def please():
    message='이렇게 하면 되지?'
    print(message) 
#print(message) #오류 발생, 절대 안됨
#위의 두 함수에서 message 변수는 서로 다르다! 개별 함수의 메모리에 저장된 변수임

#전역변수: 어디서든 사용가능
message='나는야 전역변수' #print 함수 사용 전에 전역변수 선언이 되어야함함
print(message) #전역변수 출력 ('나는야 전역변수')
def please2():
    global message #전역변수인 message를 함수 내에서 사용하겠다 선언!
    message='진짜 전역변수' #전역변수 값 수정됨
please2()
print(message) #'진짜 전역변수' 출력

#input()사용자 입력
#input()를 사용하여 입력된 값은 문자열 형태로로 저장됨->형 변환 필요
num=int(input('총 몇 분이신가요?'))
if num>4:
    print('죄송하지만 저희 식당은 최대 4분 까지만 예약가능합니다.')

#파일 입출력
#open(파일명, 열기모드, encoding="인코딩")
#r: read(읽기) / w: write(쓰기) / a: append(이어서 쓰기) 
f = open('list.txt', 'w', encoding='utf8') #파일이 없는 경우 빈파일 생성성
f.write('김xx\n') #문장입력하기
f.write('정xx\n')
f.write('허xx\n')
f.close() #파일 닫기 필수

f = open('list.txt', 'r', encoding='utf8')
contents = f.read() #파일내용 다 읽어오기기
print(contents)
f.close()

f = open('list.txt', 'r', encoding='utf8') #한 줄씩 읽기
for line in f:
    print(line, end='')
f.close()

#with -> 블럭 벗어나면 파일 자동으로 닫음 / 읽기, 쓰기, 이어서 쓰기 모두 해당
with open('list.txt', 'w', encoding='utf8') as f:
    f.write('김xx\n') #문장 입력
    f.write('정xx\n') 
    f.write('허xx\n') 
    #파일 닫기 생략 가능
#챗GPT로 배우는 점프 투 파이썬 / 초보자를 위한 파이썬 300제 -> 문제 풀이 해보면 좋음

#sys 모듈
import sys #sys 모듈을 사용하겠다고 선언
args=sys.argv[1:] #*args로 들어온 인자는 튜플로 저장됨 
for i in args: 
    print(i)
'''sys.argv: 배열입니다. sys.argv[0]에는 기본적으로 파이썬의 실행파일의 경로가 담겨져 있다. 따라서 배열의 길이는 기본적으로 1입니다.
#kwargs -> 매개변수 앞에 별 2개를 붙인 것 / 딕셔너리에 사용
#lambda 예약어 -> add=lambda a,b : a+b  result=add(3,4) => 함수 사용한 것과 동일한 결과 도출
'''

#클래스(객체체)
'''
클래스>함수>변수
파이썬: 대화형 인터프리터, 객체지향추구구 / C: 절차식 언어 / C++, java: 객체지향언어
클래스명의 첫번째 문자는 대문자로(함수는 소문자자)
'''
class BlackBox:
    def __init__(self,name,price):  #__: 더블언더스코어->객체 생성되면 자동 호출됨 / self: b1,b2 등 객체 구별하는 용도
        self.name=name   #self.name->멤버변수 => self가 붙으면 멤버변수가 됨 / self는 객체 자기자신
        self.price=price

b1=BlackBox() #객체생성, b1은 객체 변수가 됨
b2=BlackBox()
b1.name='까망이' #변수선언
print(b1.name)
print(isinstance(b1,BlackBox))

b1=BlackBox('까망이',200000)
print(b1.name,b1.price)
b2=BlackBox('하양이',100000)
print(b2.name,b2.price)
b1.set_travel_mode(20)

#메소드(Methode) => 함수
class BlackBox:
    def __init__(self,name,price):  #__: 더블언더스코어->객체 생성되면 자동 호출됨 / self: b1,b2 등 객체 구별하는 용도
        self.name=name   #self.name->멤버변수 => self가 붙으면 멤버변수가 됨 / self는 객체 자기자신
        self.price=price
    def set_travel_mode(self,min): #여행모드 시간(분)
        print(str(min)+'분 동안 여행모드 on')

b1=BlackBox('까망이',200000)
print(b1.name,b1.price)
b2=BlackBox('하양이',100000)
print(b2.name,b2.price)
b1.set_travel_mode(20)
#or
BlackBox.set_travel_mode(b1,20) #이렇게 사용하는 경우는 거의 없음! 너무 코드가 길어서
##self는 메소드를 정의할 때 처음 전달값은 무조건 self
#        메소드 내에서는 self.name과 같은 형태로 멤버변수를 사용

#상속
class TravelBlackBox(BlackBox): #BlackBox 클래스를 갖다 쓰는 행위
    def set_travel_mode(self,min): #여행모드 시간(분)
        print(str(min)+'분 동안 여행모드 on')
#BlackBox는 부모 클래스, TravelBlackBox는 자식 클래스

b1=BlackBox('까망이',200000)
b2=TravelBlackBox('하양이',100000)
b1.set_travel_mode(20) #사용불가! BlackBox클래스에는 set_travel_mode 함수가 없는 경우를 말함 
b2.set_travel_mode(20)

#super
class TravelBlackBox(BlackBox): 
    def __init__(self,name,price,sd):
        super().__init__(name,price)  #self 사용할 필요 없음. super로 부모클래스의 매게변수 내용만 가져오는 것임
        self.sd=sd
    def set_travel_mode(self,min):
        print(str(min)+'분 동안 여행모드 on')

#다중 상속
class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender:
    def send(self):
        print('메일 발송')

class TravelBlackBox(BlackBox,VideoMaker,MailSender): 
    def __init__(self,name,price,sd):
        super().__init__(name,price)  #self 사용할 필요 없음. super로 부모클래스의 매게변수 내용만 가져오는 것임
        self.sd=sd
    def set_travel_mode(self,min):
        print(str(min)+'분 동안 여행모드 on')

b2=TravelBlackBox('하양이',100000,64)
b2.make()
b2.send()

#메소드 오버라이딩 -> 똑같은 함수를 호출할 경우 자식 클래스에서 정의된 호출이 우선적으로 호출됨
#                    TravelBlackBox에 있는 set_travel_mode 함수는 호출되지 않음음
class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self,min):
        print(str(min)+'분 동안 여행모드 on')
        self.make() #추억용 여행 영상 제작
        self.send() #메일 발송

b2=AdvancedTravelBlackBox('하양이',100000,64)
b2.set_travel_mode(20)

#pass -> 나중에 할게, 일단은 내버려 둬 / if의 조건문으로 사용 불가능능
class BlackBox1:
    def __init__(self):
        pass
    def add():
        pass
    for i in range(10):
        pass
    if 3<5:   #if pass: (x)
        pass
    while True:  #무한루프 주의
        pass
 
 #예외처리
'''
try:
     수행문장 -> 에러가 발생할 가능성이 있는 문장 -> 항상 except 또는 finally와 함께 사용해야함
except:
    에러발생시 수행할 문장 -> 에러 상황이 발생했을때만 수행할 문장
else:
    정상 동작시 수행할 문장 -> 에러가 발생하지 않았을때만 수행할 문장(옵션)
finally:
    마지막으로 수행할 문장 -> 에러 여부 상관없이 항상 수행되는 문장
'''
num1=3
num2=3
try:
    result=num1/num2
    print(f'연산결과는 {result}입니다.')
except:
    print('에러가 발생했어요.')
else:
    print('정상동작')
finally:
    print('수행 완료')   

#에러
try:
    result=num1/num2
    print(f'연산결과는 {result}입니다.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except TypeError:
    print('값이 이상합니다.')
except Exception as err:
    print('에러가 발생했어요.:',err)
else:
    print('정상동작')
finally:
    print('수행 완료')  

#모듈 -> 하나의 파이썬 파일(.py) / 프로그램의 일부분을 담당하는 함수, 클래스, 변수 등의 모임 
'''
import 모듈
from 모듈 import 변수, 함수 또는 클래스스
프로젝트명>패키지>모듈>클래스>함수>변수
'''

#random
import random
my_list=['가위','바위','보']
print(random.choice(my_list))

#패키지(폴더)->안에 모듈(.py)가 존재
#import 폴더명.모듈명.클래스or함수명 으로 호출 가능

#내장함수(Built-in 함수)
'''
abs(), all(), any(), chr(), dir(), divmod(), enumerate()->자주 사용, eval(), filter(함수, 반복가능한 데이터), hex(), id()
instance(object, class), map(함수, 반복가능한 데이터), open(filename,[mode]), ord(), pow(x,y), round()->반올림, sorted()

'''
#glob 라이브러리(중요): 특정 디렉터리 안의 파일 이름을 읽어서 리스트로 리턴
#Faker 라이브러리: 이름 주소 등을 랜덤으로 출력
#생각 보다 많은 외부 라이브러리가 존재함. 유용하게 활용하는 것이 좋음

#파이썬은 동적 프로그래밍 언어 / 자바는 정적 프로그래밍 언어

#객체 참조시 지역->글로벌->빌트인 순 / 빌트인은 print 같은 내장함수

#1분 파이썬 수강 완료!!!!