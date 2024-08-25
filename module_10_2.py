import threading
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__} с аргументами {args}: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Каждый рыцарь имеет 100 врагов

    @measure_time
    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name} сражается {days} день(дня)..., осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")