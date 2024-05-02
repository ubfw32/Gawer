class Person:
    def __init__(self, name, secondname):
        self.name = name
        self.secondname = secondname


class Client(Person):
    def __init__(self, name, secondname, account, balance=0):
        super().__init__(name, secondname)
        self.account = account
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.secondname} \n your account number is: {self.account} \n your balance is: {self.balance}\n"

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} {self.secondname} \n you deposit {amount}$ \n"
              f"your account N°{self.account} and your total is: {self.balance}$")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} {self.secondname} \n you withdraw {amount}$ \n"
                  f"your account N°{self.account} and your total is: {self.balance}")
        else:
            print("You can't withdraw more than you have")


def new_client():
    name_c = input("Insert your name: \n")
    second_c = input("Insert your second name: \n")
    account_c = input("Insert your 4 digits number: \n")
    client = Client(name_c, second_c, account_c)
    return client


def start():
    my_client = new_client()
    print(my_client)
    ans = 0

    while ans != "4":
        ans = input("Select and option: \n1) DEPOSIT \n2) WITHDRAW \n3)QUIT \n")

        if ans == "1":
            amount_d = int(input("Insert the deposit amount: \n"))
            my_client.deposit(amount_d)

        elif ans == "2":
            amount_r = int(input("Insert the withdraw amount: \n"))
            my_client.withdraw(amount_r)

        elif ans == "3":
            print("Thanks for use our service.")
            break
        else:
            print("Invalid option")


start()
