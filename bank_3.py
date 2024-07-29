from threading import Thread, Lock

"""Создаём программу, имитирующую банковский счёт с балансом
и методами для пополнения и снятия денег"""


class BankAccount():
    def __init__(self, balance):
        self.balance = balance  # баланс счёта
        self.lock = Lock()  # механизм блокировки потоков

    # метод пополнения баланса:
    def deposit_task(self, amount):
        self.balance = 1000
        with self.lock:  # механизм блокировки потока
            for i in range(5):  # добавляем amount = 100 пять раз
                self.balance = self.balance + amount  # balance = 1000, amount = 100
                print(f"Deposited {amount}, new balance is {self.balance}")

    # метод снятия денег:
    def withdraw_task(self, amount):

        with self.lock:  # механизм блокировки потока
            for i in range(5):
                self.balance = self.balance - amount
                print(f"Withdrew {amount}, new balance is {self.balance}")


# создаём отдельные методы в глобальном пространстве, чтобы сработали отдельные потоки на отдельные методы,
# а именно, чтобы сработали отдельные потоки на методы deposit_task и withdraw_task
def deposit_task(account, amount):
    account.deposit_task(amount)


def withdraw_task(account, amount):
    account.withdraw_task(amount)


# создаём переменную account, которая фигурирует в экземплярах класса deposit_thread и withdraw_thread
account = BankAccount(1000)

# Вызвать метод deposit_task в одном потоке
deposit_thread = Thread(target=deposit_task, args=(account, 100))
# Вызвать метод withdraw_task в другом потоке
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
