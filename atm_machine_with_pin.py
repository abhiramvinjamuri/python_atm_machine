def deposit(amount):
    if amount > 0:
        print(f'{amount} deposited successfully.')
        return amount 
    else:
        print('Amount must be greater than 20.')
        return 0 
        
def withdraw(amount,balance):
    if amount <= balance:
        print(f'{amount} withdrawn successfully.')
        return amount
    else:
        print('Insufficient Balance')
        return 0 

def check_balance(balance):
    print('Current Balance:',balance)     


def run(balance):
    while True:
        print('1) Deposit')
        print('2) Withdraw')
        print('3) Check Balance')
        print('4) Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            amount = float(input('Enter amount to deposit: '))
            balance += deposit(amount)
            input('Press Enter to continue...')
        elif choice == '2':
            amount = float(input('Enter amount to withdraw: '))
            balance -= withdraw(amount,balance)
            input('Press Enter to continue...')
        elif choice == '3':
            check_balance(balance)
        elif choice == '4':
            print('Thank you for using the ATM. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

balance = 0.00
pin = 7740
attempts = 1
while attempts <= 3:
    user_pin = int(input('Enter your PIN: '))
    if user_pin == pin:
        print('PIN accepted. Welcome!')
        run(balance)
        break
    attempts += 1
    print('Wrong Pin. Try again.')
if attempts == 4:
    print('Too many incorrect attempts. Your account has been locked.')


        