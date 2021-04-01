#每个工作日进步1%，每个休息日退步1%
dayup=1.0
factor=0.01
for i in range(365):
    if i%7 in [6,0]: #余数为6的时候是星期六，余数为0是星期日
        dayup=dayup*(1-factor)
    else:
        dayup=dayup*(1+factor)
print("Dayup:{:.2f}".format(dayup))