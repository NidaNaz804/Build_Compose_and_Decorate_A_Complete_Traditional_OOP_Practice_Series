# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows 
# changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Meezan Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show(self):
        print(f"Bank Name: {self.bank_name}")

acc1 = Bank()
acc2 = Bank()
acc1.show()
acc2.show()

Bank.change_bank_name("National Bank")
acc1.show()
acc2.show()
