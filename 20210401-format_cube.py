'''
获得用户输入的一个数字，可能是整数或浮点数，a，计算a的三次方值，并打印输出。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

输出结果采用宽度20个字符、居中输出、多余字符采用减号(-)填充。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

如果结果超过20个字符，则以结果宽度为准。
'''

a=input()
a=str(pow(eval(a),3))
if len(a) >20:
    print(a)
else:
    print(a.center(20,"-"))

'''
参考答案：
a = eval(input())
print("{:-^20}".format(pow(a, 3)))
'''
