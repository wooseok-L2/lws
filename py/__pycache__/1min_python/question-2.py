#1. 
a='Life is too short, you need python'
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'need' in a:
    print('need')
else: 
    print('none')

#2.
a=0
s=0
while a<=1000:
    if a%3==0:
        s+=a
    a+=1
print(s)

#3. 
a=0
while True:
    a+=1
    if a>5:
        break
    print('*'*a)
      
#4. 
for x in range(1,101):
    print(x, end=" ")

#5. 
a=[70,60,55,75,95,90,80,80,85,100]
total=0
for x in a:
    total+=x
    print(total)
ave=total/len(a)
print(ave)

#6.
num=[1,2,3,4,5]
result=[x*2 for x in num if x%2==1]
print(result)