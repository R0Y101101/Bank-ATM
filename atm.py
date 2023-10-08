class Atm:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 1000

    def display_menu(self):
        print("1. Cash Withdrawal")
        print("2. Balance Enquiry")
        print("3. Exit")
 
    def cash_withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful! Remaining balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid amount. Please enter a valid amount.")
        else:
            print("Insufficient funds!")

    def balance_enquiry(self):
        print(f"Your current balance is: ${self.balance}")

# Example usage:
if __name__ == "__main__":
    card_number = input("Enter your ATM card number: ")
    pin = input("Enter your PIN: ")

    # Creating an ATM object
    user_atm = Atm(card_number, pin)

    while True:
        user_atm.display_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter the amount to withdraw: $"))
            user_atm.cash_withdrawal(amount)
        elif choice == '2':
            user_atm.balance_enquiry()
        elif choice == '3':
            print("Exiting ATM ")
            break
        else:
            print("Invalid choice Please enter a valid option")
