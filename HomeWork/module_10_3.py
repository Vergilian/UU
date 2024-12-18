import threading
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = int(0)
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            add = randint(50, 500)
            self.balance += add
            print(f'Пополнение: {add}.Балланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                sleep(0.001)

    def take(self):
        for i in range(100):
            take = randint(50, 500)
            print(f'Запрос на {take}')
            if take <= self.balance:
                self.balance -= take
                print(f'Снятие: {take}.Балланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
