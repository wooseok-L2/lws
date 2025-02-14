#1.
def is_odd(number):
    if number%2==1:
        return True
    else:
        return False

#2. 다시 풀어볼 것
def avg_numbers(*numbers): #numbers 값이 튜플로 저장됨
    result=0
    for i in numbers:
        result+=i
    return result/len(numbers)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

#3. input함수로 입력된 값은 문자열 형태로 입력됨 형변환 필요
input1=int(input('첫번째 숫자를 입력하시오:'))
input2=int(input('두번째 숫자를 입력하시오:'))
total=input1+input2
print(f'두 수의 합은 {total}입니다.')

#4.
print('you','need','python')

#5. close로 파일 닫아야 하는데 안닫아서 출력이 안된 것임
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

#6. 
user_input = input("저장할 내용을 입력하세요 : ")
f = open('test.txt', 'a')
f.write('\n')
f.write(user_input)
f.close()

#7. replace 사용가능한지 몰랐음
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java','python')

f = open('test.txt', 'w')
f.write(body)
f.close()