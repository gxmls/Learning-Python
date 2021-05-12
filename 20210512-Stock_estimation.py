'''这是一个简单的股票估值的程序:
市盈率PE(股价/每股收益)：适合对处于成长期的公司进行估值
市净率PB(股价/每股净资产)：适用于钢铁、煤炭、建筑等传统企业
PEG(市盈率/净利率增长率)：PEG越小越好，越安全
市现率(股价/每股现金流)：市现率越低，收回成本的时间越短，越值得投资
'''
price=eval(input("请输入股票当前的价格(元)："))
PE=eval(input("请输入股票的动态市盈率："))
PB=eval(input("请输入股票的市净率："))
earnings=eval(input("请输入每股收益(元)："))
book_value=eval(input("请输入每股净资产(元)："))
growth=eval(input("请输入利润增长率(%)："))
flow=eval(input("请输入每股现金流(元)："))
print("股票当前的价格是：{:.3f}元".format(price))
print("亏损，无法使用市盈率估值") if earnings<=0 else print("市盈率估值：{:.3f}元".format(PE*earnings))
print("亏损，无法使用市净率估值") if book_value<=0 else print("市净率估值：{:.3f}元".format(PB*book_value))
print("负增长，无法使用PEG估值") if growth<=0 else print("PEG：{:.3f}".format(PE/growth))
print("现金流为负，无法使用市现率估值") if flow<=0 else print("市现率：{:.3f}".format(price/flow))