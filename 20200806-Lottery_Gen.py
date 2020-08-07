import random
print('This is a Lottery Generator.')
while True:
    go_on=False
    num=int(input('Please enter the number of Lottery tickets: '))
    if num>=1:
        break
    else:
        go_on=False
for num in range (1,num+1):
    print(f'{random.sample(range(1,36),5)} {random.sample(range(1,13),2)}')
    #Note: if using statement'randint(1,36,size=5)' it may generate 5 duplicated random numbers.



