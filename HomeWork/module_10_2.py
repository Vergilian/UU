import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        enemys = 100
        while enemys > 0:
            time.sleep(1)
            days += 1
            enemys -= self.power
            print(f'{self.name} сражается {days} день(дня)..., осталось {enemys} воинов')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
