#这是一个计算股票价格的程序
Capital=eval(input("请输入持仓成本(元):"))
profit=eval(input("请输入预计盈利百分比(%):"))
print("当盈利{}%时，股票的价格是{:.3f}".format(profit,Capital*(1+profit/100)))