def getText():
    txt=open("hamlet.txt","r").read() #打开txt文本
    txt=txt.lower() #避免大小写造成的干扰，将文本全部转换为小写
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt=txt.replace(ch," ") #去掉特殊符号，用空格替代
    return txt

hamletTxt=getText() #读取并归一化文本
words=hamletTxt.split() #用空格分开的单词，返回列表类型
counts={} #定义一个新字典，表达单词和出现的次数的对应关系
for word in words: #检测counts中是否存在word
    counts[word]=counts.get(word,0)+1 #第一次出现相当与在字典中新增一个元素
items=list(counts.items()) #将字典转换为列表类型便于操作
items.sort(key=lambda x:x[1],reverse=True)
'''列表排序，lambda x:x[1]决定使用哪一个多元选项的列作为排序列,
这里是对键值对2个元素中的第二个元素进行排序
默认是从小到大排序，reverse=True就是从大到小排序'''
for i in range(10): #将排名前10的单词及其对应的次数打印出来
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))

