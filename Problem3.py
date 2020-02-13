import random

def game():
    balance = 100
    while balance > 0:
        try:
            bet = eval(input('Place a bet: '))
        except:
            print('numbers only please')
        while bet > balance or bet < 0:
            print('Try Again')
            bet = eval(input('Place a bet: '))
        else:
            a = random.randrange(1, 7)
            b = random.randrange(1, 7)
            score = a + b
            if score == 7 or score == 12:
                balance += bet * 2
                print(a, b, balance, bet)
            else:
                print(a, b, balance, bet)
                yorn = input('Double or nothing? Y/N: ')
                while yorn.lower() not in ['yes', 'y', 'no', 'n']:
                    yorn = input('Double or nothing? Y/N: ')
                else:
                    if yorn.lower() == 'yes' or yorn.lower() == 'y':
                        bet *= 2
                        c = random.randrange(1, 7)
                        if score + c == 7 or score + c == 12:
                            balance += bet * 3
                            print(a, b, c, balance, bet)
                        else:
                            balance -= bet
                            print(a, b, c, balance, bet)
                    else:
                        balance -= bet
                        print(a, b, balance, bet)

game()