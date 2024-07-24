import threading
from threading import Thread




class BankAccount(Thread):
    def __init__(self, amount, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.amount = amount

    def deposit_task(amount):
        balance = 1000

        for i in range(5):
            balance = int(balance + amount)
            print(f"Deposited {amount}, new balance is {balance}")

    def withdraw_task(amount):
        balance = 1500

        for i in range(5):
            balance = int(balance - amount)
            print(f"Withdrew {amount}, new balance is {balance}")


deposit_thread = Thread(target=deposit_task)
withdraw_thread = BankAccount(target=withdraw_task, amount=150)

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

print(threading.active_count())