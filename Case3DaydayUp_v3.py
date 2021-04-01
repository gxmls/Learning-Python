#工作日要多努力才能和每天进步1%一样？休息日下降1%
def DayUP(df):
    dayup=1.0
    for i in range(365):
        if i%7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup

factor=0.01
while DayUP(factor) <37.78:
    factor+=0.001
print("Factor={:.3f}".format(factor)) 

