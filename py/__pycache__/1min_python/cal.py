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

def say():
    print('안녕하세요.')