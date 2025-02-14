#다시 풀어볼 것, 너무 어려웠음 ㅜㅜ
#1.
a='a:b:c:d'
b=a.split(':')
print('#'.join(b))

#2.
a={'A':90,'B':80}
if a.get('C')==None:
    a['C']=70
print(a['C'])

#3. 차이점은 모르겠음...!!!
a=[1,2,3]
b=[1,2,3]
a+=[4,5] #새로운 방을 만들어서 입력함 -> 공간을 두번 만듬듬
print(a)
print(id(a))

print(id(b))
b.extend([4,5]) #원래 있던 방에 값들 추가
print(b)
print(id(b))

#4.
A=[20,55,67,82,45,33,90,87,100,25]
result=0
for x in A:
    if x>=50:
        result+=x
print(result)

#5. 재귀함수 이용
i=int(input('숫자입력:'))

def fib(n):   #함수는 호출하면 return이 무조건 있어야함
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2)+fib(n-1)   #fib(3)=fib(2)+fib(1)=fib(1)+fib(0)+fib(1)

for i in range(input):
    print(fib(i))

def fib(n1):  #재귀 안쓰는 방법 나중에 나머지 작성해 보기기
    result=[]
    a,b=0,1
    while a<=n1:
        result.append(a)
        a, b = b, a+b
    return result

print(fib(15))

#6.
val=input('값을 입력하세요:')
a=map(int, val.split(','))
print(a, type(a))

result=0
for i in a:
    result+=i
print(result)

#7. 
a=int(input('구구단을 출력할 숫자를 입력하시오:'))
result=[a*i for i in range(1,10)]
print(result)

#8.
f=open('abc.txt','w')
f.write('AAA\n')
f.write('BBB\n')
f.write('CCC\n')
f.write('DDD\n')
f.write('EEE')
f.close()

f=open('abc.txt','r')
re=f.read()
f.close()
print(re)

f1=open('abc.txt','r')
lines=f1.readlines()
print(lines, type(lines))
f1.close()
lines.reverse()

f2=open('result_abc.txt','w')
for line in lines:
    line=line.strip()
    f2.write(line)
    f2.write('\n')
f2.close()

#9.
f=open('sample.txt','w')
f.write('70\n')
f.write('60\n')
f.write('55\n')
f.write('75\n')
f.write('95\n')
f.write('90\n')
f.write('80\n')
f.write('80\n')
f.write('85\n')
f.write('100')
f.close()

f1=open('sample.txt')
lines=f1.readlines()
f1.close()

total=0
for line in lines:
    score=int(line)
    total+=score
average=total/len(lines)

f1=open('sample.txt','w')
f1.write(str(average))
f1.close()  

#10.
class calculator():
    def __init__(self,numberlist):
        self.numberlist=numberlist
    def sum(self):
        result=0
        for num in self.numberlist:
            result+=num
        return result
    def avg(self):
        return self.sum()/len(self.numberlist)
    
#11. 검색해볼것

#12. 
result=0
try:
    [1,2,3][3]
    'a'+1
    4/0
except TypeError:
    result+=1
except ZeroDivisionError:
    result+=2
except IndexError:
    result+=3
except Exception as err:
    print(err)
    result+=3
finally:
    result+=4

print(result)

#13.
data=input('숫자를 입력하세요:')
numbers=list(map(int,data))
print(numbers)
result=[]
for i, num in enumerate(numbers):
    result.append(str(num))
    if i<len(numbers)-1:
        is_odd=num%2==1
        is_next_odd=numbers[i+1]%2==1
        if is_odd and is_next_odd:
            result.append('-')
        elif not is_odd and not is_next_odd:
            result.append('*')
print("".join(result))

#14. 
def compress_string(s):
    if not s:
        return ""
    
    compressed=[]
    count=1
    current_char=s[0]
    for i in range(1,len(s)):
        if s[i]==current_char:
            count+=1
        else:
            compressed.append(current_char+str(count))
            current_char=s[i]
            count=1
    compressed.append(current_char+str(count))
    return "".join(compressed)

input_string="aaabbcccccca"
output_string="a3b2c6a1"
print(compress_string(input_string))
print(output_string==compress_string(input_string))


#15.
def chkDupNum(s):
    result=[]
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result)==10

print(chkDupNum("0123456789"))
print(chkDupNum("01234"))
print(chkDupNum("01234567890"))
print(chkDupNum("6789012345"))

#16.
dic={ 
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G', '....':'H','..':'I','.---':'J',
     '-.-':'K','.-..':'L', '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R', '...':'S','-':'T',
     '..-':'U','...-':'V','.--':'W','-..-':'X', '-.--':'Y','--..':'Z' 
}

def morse(src):
    result=[]
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

#정규식 관련 문항 17~20
#17. 
import re
pattern='a[.]{3,}b'
strings=['acccb','a....b','aaab','a.cccb']
maatching_strings=[s for s in strings if re.match(pattern,s)]
print('매치되는 문자열:',maatching_strings)

#18.
import re
p=re.compile('[a-z]+')
m=p.search('5 python')
print(m.start()+m.end())

#19.
import re
text='''
park 010-1234-1234
kim 010-1234-1234
lee 010-1234-1234
'''

modified_text=re.sub(r'(\d{3}-\d{4})-(\d{4})',r'\1-####', text)
print(modified_text)

#20.
import re

emails=['park@naver.com','kim@daum.net','lee@myhome.co.kr']

pattern=r".*[@].*[.](?=com$|net$).*$"

matching_emails=[email for email in emails if re.match(pattern, email)]
print(matching_emails)