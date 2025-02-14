#1. 점프투
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
       self.value -= val
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) #10에서 7을 뺀  3을 출력

#2. 
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
           print('100이상의 값을 가질 수 없습니다.')
           self.value=100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)

#3 
print(all([1,2,abs(-3)-3])) #abs는 절대값
print(chr(ord('a'))=='a') #ord: 문자를 인자로 받아서 유니코드 정수로 반환
                          #chr: 정수를 인자로 받아서 해당 정수에 해당하는 유니코드 문자 반환

#4. 
print(list(filter(lambda n: n>0, [1,-2,3,-5,8,-3])))

#5 
x=int(0xea)
print(x)
print(int('0xea',16))
print(hex(234))

#6. 
print(list(map(lambda n: n*3,[1,2,3,4])))

#7. 
x=[-8,2,7,5,-3,5,0,1]
print(max(x)+min(x))

#8. 
a=17/3
print(round(a,4))

#9. 터미널에 직접 python 파이썬 파일명 입력값 -> 요런 형태로 작성해줘야함
import sys
num=sys.argv[1:]

result=0

for i in num:
    result+=int(i)
print(result)

#10.
import os

os.chdir('C:\\Users\\dntjr')
f=os.popen('dir')
print(f.read())

#11.
import glob
print(glob.glob('C:\\Users\\dntjr\\*.py'))

#12.
import time
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
x=time.asctime()
print(x)

#13. 
import random

result=[]

while len(result)<6:
    num=random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)
