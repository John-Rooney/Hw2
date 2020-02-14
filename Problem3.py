import random

def game():
    """Dice game, lots of skill required"""
    balance = 100
    print('Your balance is $100')
    print('Place bet of 0 to walk away')
    while balance > 0:
        while True:
            try:
                bet = eval(input('Place a bet: '))
                if bet == 0:
                    print('You walked away with ${}'.format(balance))
                    return
                break
            except:
                print('Numbers Only Please')
        while bet > balance or bet < 0:
            print('Try Again')
            bet = eval(input('Place a bet: '))
        else:
            a = random.randrange(1, 7)
            b = random.randrange(1, 7)
            score = a + b
            if score == 7 or score == 12:
                balance += bet * 2
                print('Die 1: {} Die 2: {}'.format(a, b))
                print('Your balance is ${} after winning ${}'.format(balance, bet * 2))
            else:
                print('Die 1: {} Die 2: {}'.format(a, b))
                yorn = input('Double or nothing? Y/N: ')
                while yorn.lower() not in ['yes', 'y', 'no', 'n']:
                    yorn = input('Double or nothing? Y/N: ')
                else:
                    if yorn.lower() == 'yes' or yorn.lower() == 'y':
                        c = random.randrange(1, 7)
                        if score + c == 7 or score + c == 12:
                            balance += bet * 3
                            print('Die 1: {} Die 2: {} Die 3: {}'.format(a, b, c))
                            print('Your balance is ${} after winning ${}'.format(balance, bet * 3))
                        else:
                            balance -= bet * 2
                            print('Die 1: {} Die 2: {} Die 3: {}'.format(a, b, c))
                            print('Your balance is ${} after losing ${}'.format(balance, bet * 2))
                    else:
                        balance -= bet
                        print('Your balance is ${} after losing ${}'.format(balance, bet))
    else:
        print('You lost all your money :(')
    return

if __name__ == '__main__':
    game()