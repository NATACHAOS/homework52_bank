import threading
from threading import Thread, Lock
lock = Lock()

class BankAccount(Thread):

    #метод пополнения баланса
    def deposit_task(account, amount):
        for _ in range(5):
            account.deposit(amount)

    # метод снятия денег
    def withdraw_task(account, amount):
        for _ in range(5):
            account.withdraw(amount)
            account = BankAccount()


deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
