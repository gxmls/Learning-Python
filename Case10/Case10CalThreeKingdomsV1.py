import jieba #中文分词需要引入第三方库jieba
txt=open("threekingdoms.txt","r",encoding="utf-8").read() 
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1: #去掉只有一个字的情况
        continue
    else:
        counts[word]=counts.get(word,0)+1 #对分词进行基数，存入字典
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
