'''
描述
获得用户输入，去掉其中全部空格，将其他字符按收入顺序打印输出。 
'''

s=input()
sn=''
for c in s:
    if c!=' ':
        sn+=c
    else:
        continue
print(sn)

'''
s = input()
print(s.replace(" ", ""))
'''
