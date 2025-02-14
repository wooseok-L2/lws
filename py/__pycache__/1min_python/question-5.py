#1. gpt 점프투 파이썬
class Person:
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def greet(self):
       return(f'{self.name}님이 {self.age}살 입니다.')

person1 = Person("홍길동", 30)
print(person1.greet())  # 출력: 홍길동님이 30살입니다

#2. gpt 점프투 파이썬
class BankAccount:
    def __init__(self,account_number,balance=0,total=0):
        self.account_number=account_number
        self.balance=balance
        self.total=total
        print(f'{self.account_number}의 현재 잔액은 {self.balance}입니다.')
    def deposit(self,amount):
        self.balance+=amount
        self.total=self.balance
        print(f'{self.account_number}계좌에 {amount}만큼 입금을 진행합니다.')
        print(f'{self.account_number}계좌에 {amount}만큼 입금완료했습니다. 잔액은{self.total}입니다.')
    def withdraw(self,amount):
        print(f'{self.account_number}계좌에 {amount}만큼 출금을 진행합니다.')
        if self.balance < amount:
            print(f'{self.account_number}계좌의 잔액이 부족합니다.')
        else: 
            self.balance-=amount
            self.total=self.balance
            print(f'{self.account_number}계좌에서 {amount}만큼 출금합니다.잔액은{self.total}입니다.')
    def transfer(self,amount,target_account):
        if self.balance < amount:
            print(f'{self.account_number}계좌의 잔액이 부족합니다. 현재 잔액은 {self.total}입니다.')
        else:
            print(f'{self.account_number}의 계좌에서 {target_account.account_number}로 {amount}만큼 송금합니다.')
            self.withdraw(amount)
            print(f'{self.account_number}의 계좌에서 {amount}만큼 입금했습니다.')
            target_account.deposit(amount)


account1 = BankAccount(12345, 1000)
account2 = BankAccount(12346, 500)
account1.transfer(100, account2)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)

#3.
def add(num1,num2):
    result=num1+num2
    print(result)

def subtract(num1,num2):
    result=num1-num2
    print(result)

def multiply(num1,num2):
    result=num1*num2
    print(result)
    
def divide(num1,num2):
    if num2==0:
        print('0으로 나눌 수 없습니다.')
    else:
        result=num1/num2
        print(result)

import calculator2
print(calculator2.add(3,4))
print(calculator2.subtract(3,4))
