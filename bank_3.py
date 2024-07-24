import threading
from threading import Thread




class BankAccount(Thread):
    def __init__(self, amount, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.amount = amount

# метод пополнения баланса:
    def deposit_task(amount):
        balance = 1000

        for i in range(5):
            balance = int(balance + amount)
            print(f"Deposited {amount}, new balance is {balance}")

# метод снятия денег:
    def withdraw_task(amount):
        balance = 1500

        for i in range(5):
            balance = int(balance - amount)
            print(f"Withdrew {amount}, new balance is {balance}")

# Вызвать метод deposit_task в одном потоке
deposit_thread = BankAccount(target=deposit_task)
# Вызвать метод withdraw_task в другом потоке
withdraw_thread = BankAccount(amount=150)

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

# количество потоков:
print(threading.active_count())