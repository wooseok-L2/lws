#1. 

#2. 
result=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        result+=i
print(result)

#3. 
def getTotalPage(m,n):
    if m%n==0:
        return m//n
    return m//n+1

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))

#4.
import sys

option=sys.argv[1]

if option=='-a':
    memo=sys.argv[2]
    f=open('memo.txt','w')
    f.write(memo)
    f.write('|n')
    f.close()
elif option=="-v":
    f=open('memo.txt')
    memo=f.read()
    f.close()
    print(memo)

#5. 
import sys

src=sys.argv[1]
dst=sys.argv[2]

f=open('src')

#어렵다.. 정답 코드가 김..ㅜ

#6.
import os

def search(dirname):
    try: 
        filenames=os.listdir(dirname)
        print(filenames)
        for filenames in filenames:
            full_filename=os.path.join(dirname, filenames)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext=os.path.splitext(full_filename)[-1]
                if ext==".py":
                    print(full_filename)
    except PermissionError:
        pass #내용 넘어가서 못 적음


