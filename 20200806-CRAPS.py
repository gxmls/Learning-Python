from random import randint
money=1000
while money>0:
    print(f'You have total assets {money}')
    go_on=False
    while True: #Note: 'while True' means if the condition is true, the circular will be continued until meets break.
        debt=int(input('Please place a bet: '))
        if 0<debt<=money:
            break
    first=randint(1,6)+randint(1,6)
    print(f'Player shook out {first} points')
    if first==7 or first==11:
        print(f'Player Wins!\n')
        money+=debt
    elif first==2 or first==3 or first==12:
        print(f'Dealer Wins!\n')
        money-=debt
    else:
        go_on=True
    while go_on: #Note: go_on=True
        go_on=False
        current=randint(1,6)+randint(1,6) #Note: The next round begins if there was no winner in the first round
        print(f'Player shook out {current} points')
        if current==7:
            print('Dealer Wins!\n')
            money-=debt
        elif current==first:
            print('Player Wins!\n')
            money+=debt
        else:
            go_on=True #Note: Back to the beginning until money <=0
print('Sorry, you are bankrupt!\n')





        


    
