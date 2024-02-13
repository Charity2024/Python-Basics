 #parent/superclass
class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self, amount ,recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount}KES has been sent to {recipient} successfully")
        else:
            print("Insufficient balance")

# child classes
class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number,id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number
    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount}KES has successfully been credited your balance is {self.account_balance}")
        else:
            print("Insufficient balance")

class BusinessMpesa(Mpesa):
    def __init__(self,account_balance, phone_number,business_name):
        super().__init__(account_balance, phone_number)
        self.business_number = business_name

    def receive_payment(self, amount,client):
        self.account_balance =+ amount
        print(f"{amount}KES received from a {client}")

Personal = PersonalMpesa(1450, 722159735, 12591617)
Personal.send_money(1000, 726465162)
Personal.buy_airtime(100)
# instance for business class
Business = BusinessMpesa(1450, 722159735 ,"Candy_Link")
Business.receive_payment(1000, 722159735)
