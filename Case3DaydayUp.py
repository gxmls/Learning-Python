#每天进步或退步factor%，一年365累积多少？
factor=input()
dayup=pow(1+eval(factor),365)
daydown=pow(1-eval(factor),365)
print("Dayup:{:.2f},Daydown:{:.2f}".format(dayup,daydown))