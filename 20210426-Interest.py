'''
计算当日逆回购年化收益率为多少的时候才比添薪宝利息高
添薪宝无交易手续费
1天息国债逆回购手续费为0.001%
'''

def Tian(cap,i,d):
    SumT=cap*i/100*d/365
    return SumT
def Zhai(cap2,i2,d2):
    SumZ=cap2*i2/100*d2/365-cap2*0.001/100
    return SumZ

Capital=eval(input("请输入借出金额（元）："))
tian=eval(input("请输入今日扫单的年化收益（%）："))
zhai=eval(input("请输入今日逆回购的年化收益（%）："))
day=eval(input("请输入今日购买计息天数（天）："))
if Zhai(Capital,zhai,day)>Tian(Capital,tian,day):
    print("逆回购收益大于扫单收益：\n预计逆回购收益：{:.2f}元 预计扫单收益：{:.2f}元".format(Zhai(Capital,zhai,day),Tian(Capital,tian,day)))
else:
    while Zhai(Capital,zhai,day)<Tian(Capital,tian,day):
        zhai+=0.01
    else:
        print("当逆回购年化收益率超过{:.3f}%时，收益高于当日添薪宝扫单收益\n预计逆回购收益：{:.2f}元 预计扫单收益{:.2f}元".format(zhai,Zhai(Capital,zhai,day),Tian(Capital,tian,day)))
    




