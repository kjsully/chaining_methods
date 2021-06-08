class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self 

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self 
        
    def display_user_balance(self):
        print(f"User:{self.name},Balance:{self.account_balance}")
        return self





guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
kyle = User('Kyle Sullivan', 'kyle@python.com')

guido.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawal(100).display_user_balance()

monty.make_deposit(200).make_deposit(200).make_withdrawal(100).make_withdrawal(100).display_user_balance()

kyle.make_deposit(100000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()





