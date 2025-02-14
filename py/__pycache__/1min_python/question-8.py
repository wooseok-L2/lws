
#1.
import re
text='Hello elice!'
p1='e' # p1은 pattern 1의 의미입니다! 정규표현식을 입력해보세요. (ex. "e", "elice")

m1=re.findall(p1,text) # text 문자열 변수에서 정규식 p1로 매칭한 결과를 나타냅니다.
print(m1)
#findall 함수로 추출된 결과는 list로 저장됨.

#2.
import re
text = "abcdefg"

pattern = re.compile("e")

print("정규식 객체의 자료형 : ", type(pattern))

print("정규식 객체 사용하는 경우 : ", pattern.findall(text))

print("객체를 사용하지 않는 경우 : ", re.findall("e", text))

#3.
import re

text = '''&7q:>@6j`~itIghnfHH8=FW7y?<g"lt?=q3*kJdN/bsrF()Z<U$_w2-`KUnyxLB<8uMm%*`"[:%yha[f`bEXHW=qD9K>95K92cvI>Kj51/cy~cwaN[jB'u5<Ix8?;y~g15T_bb2z<uL&xOIaMJFk>s^}nz.sWx<2)R?:x5r9,T_45]zQ>Z|FN%AFf/#@^FR#&wogd@hlk(7&MZqqurTF+V5oy`cpM.iMUBMd#wGs9RTj7J`Q=,AIv3x%&/Q)-jDk'''
          

p = ""  # 9행의 re.compile 함수에 들어갈 문자열 매개변수입니다.

m = re.findall(p, text)
print("결과 : ", m)

#4.
import re

text = '''j<Q'T~K_5f_&VO_):Igq:=8t9qPGVB&-=9;oC7$7bw>I6)=abcQiZ&nNj2J\|0'aE*QyyelicebcW:y`y#Y&nY.gq.-0m\w2m8<1<`P:`OdE{>SF}]4_"8'Ozv:}Pc5@H91j250^H,W$~GD>;K[r_3VW?pS2U*uz`lxne`,ZMeliceFJDhMf$NxcQ[K_o4=Q2z?%[Ak1Do!E!8:>)7abcprcNIelice.mT<Cwy!~T/QfD0L&V&'\$z;7$@By&8L[8?0a4=v4uYY=IK#4{vB46delice$^EI}vD*ndR{F#EJyMHIe2QK,u"c^1d32Cvl%]Hq-;+(O/M8X-ykfelicedll3nfIn>%9i*e!9[u4$W3ASbY!h1elicedg{A|lrKJsSvJ<;A*9f_7K<?elice9MGo1Ngu~5w@EL!QMKaxUS]C6##~OBiduA]wa=pIse%E=PenU<&>w_sd{eaM0elicekr=%C^^@#j[~O!7K(^^LzS(mK"f3?p|C*;`~F|0uMCS1c=Sa-ya7?8j.!9r}YZxv'''
          

p = "t"  # 9행의 re.compile 함수에 들어갈 문자열 매개변수입니다.

m = re.findall(p, text)
print("결과 : ", m)

#5. 
import re

text='Life is short'

p1='^Life'
p2='^is'

m1=re.findall(p1,text)
m2=re.findall(p2,text)
print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

#6.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

p1 = "short$"         # short으로 끝나야 매치
p2 = "short$"         # short으로 끝나야 매치

m1 = re.findall(p1, "Life is short")
m2 = re.findall(p2, "Life is short, art is long")

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

#7.
import re

p1 = "apple"        # apple 포함하면 매치
p2 = "banana"       # banana 포함하면 매치

m1 = re.findall(p1, "I like apple and banana")
m2 = re.findall(p2, "I like apple and banana")

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)


### 아래 p3에 직접 정규표현식을 입력해보세요!

p3 = "apple|banana"             # apple 또는 banana가 포함되면 매치

m3 = re.findall(p3, "I like apple and banana")

print("m3 결과 : ", m3)

#8.
import re

### 아래 p2과 p3에 직접 정규표현식을 입력해보세요.

p1 = "a|e|i|o|u"     # 알파벳 모음에 매치
p2 = "[aeiou]"     # 알파벳 모음에 매치
p3 = "[^aeiou]"     # 알파벳 모음이 아닌 문자(자음)에 매치

m1 = re.findall(p1, "Life is short, art is long")
m2 = re.findall(p2, "Life is short, art is long")
m3 = re.findall(p3, "Life is short, art is long")

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)
print("m3 결과 : ", m3)

#9.
import re

# 임의의 문자열입니다.
text = "vkvJZZjgsr=B5Al83+#@04?+p%x7DI3k"

p1 = "[0-9]"     # 숫자와 매칭됨
p2 = "[a-z]"     # 알파벳 소문자와 매칭됨

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

#10.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

p1 = "\d"         # 숫자만 매치
p2 = "\D"         # 숫자가 아니면 매치

m1 = re.findall(p1, "el_ice%20$19")
m2 = re.findall(p2, "el_ice%20$19")

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

#11.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

p1 = "\w"         # 알파벳 대소문자, 숫자, 밑줄만 매치
p2 = "\W"         # 위위의 조건과 반대 조건

m1 = re.findall(p1, "el_ice%20$19")
m2 = re.findall(p2, "el_ice%20$19")

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

#12.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "cat bat c@t hat cut com cook cant"

p1 = "c.t"        # c로 시작하고 t으로 끝나는, 모든 3글자 단어에 매칭

m1 = re.findall(p1, text)

print("m1 결과 : ", m1)

#13.
import re

text = '''APPLE APPLe APPlE APpLE ApPLE aPPLE APPle APpLe ApPLe aPPLe APplE ApPlE aPPlE AppLE aPpLE apPLE'''
          

p1 = "APPLE"
p2 = "(?i)apple"       # 대소문자를 무시하며 APPLE에 매칭되는 패턴을 작성해보세요.

m1 = re.findall(p1, text)
print("m1 결과 : ", m1)

m2 = re.findall(p2, text)
print("m2 결과 : ", m2)

#14.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

p1 = "\s"         # 공백 문자와 매칭
p2 = "\S"         # 공백이 아닌 문자와 매칭

m1 = re.findall(p1, "Life is short")
m2 = re.findall(p2, "Life is short")

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

#15.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "ct cat caat caaat caaaaat caaaaaat cbt c1t c@t c_t"

p1 = "ca*t"         # c와 t 사이에 'a'가 0개 이상 있는 경우 매칭

m1 = re.findall(p1, text)

print("m1 결과 : ", m1)

#16.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "apple banana carrot rabbit"

p1 = "[a-z]"        # 영어 소문자 매칭
p2 = "[a-z]+"       # 영단어 단위로 매칭

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

#17.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "1 12 102 8948 754 77 3 222"

p1 = "\d+"       # 숫자 매칭
p2 = "\d{3}"         # 세 자리 수 매칭

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

#18.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "9 906 7581 28240 840414 3802773 425624"

p1 = "\d{3,5}"         # 자릿수가 3 이상 5 이하인 수

m1 = re.findall(p1, text)

print("m1 결과 : ", m1)

#19.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "2 96 4019 884863 56635574 946482 95325201 410505 5802 6661337 2937786 31103"

p1 = "\d{7,}"         # 자릿수가 7 이상인 수

m1 = re.findall(p1, text)

print("m1 결과 : ", m1)

#20.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "ac abc abbc abbbc abbbbbc"

p1 = "ab?"         # ac, abc와 매칭

m1 = re.findall(p1, text)

print("m1 결과 : ", m1)

#21.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "<html><head><Title>제목</head></html>"

p1 = "<.*>"
p2 = "<.*?>"         #정규표현식을 이용해보세요.

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)

#22.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "catatatatatat"

p1 = "cat"
p2 = "c(at)+"             # 정규식 패턴 입력!

m1 = re.search(p1, text)
m2 = re.search(p2, text)

print("m1 결과 : ", m1.group())
print("m2 결과 : ", m2.group())

#23.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "tomato"

p1 = "(to)ma\\1"             # 정규식 패턴 입력!

m1 = re.search(p1, text)

print("m1 결과 : ", m1.group())

#24.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = '''
Elice 123456-1234567 010-1234-5678
Cheshire 345678-678901 01098765432
'''

p1 = "(010)\D?\d{4}\D?(\d{4})"          # 정규식 패턴 입력!

print("m1 결과 : ", re.sub(p1, "\g<1>-****-\g<2>", text))

#25.
import re

'''
아래에 정규표현식을 직접 입력해보세요!
'''

text = "tomato potato"

p1 = "(tom|pot)ato"    # tomato 또는 potato와 매칭하자
p2 = "(?:tom|pot)ato"  # 올바른 패턴을 작성해보세요.

m1 = re.findall(p1, text)
m2 = re.findall(p2, text)

print("m1 결과 : ", m1)
print("m2 결과 : ", m2)