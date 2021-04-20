import jieba #中文分词需要引入第三方库jieba
txt=open("threekingdoms.txt","r",encoding="utf-8").read() 
excludes={"将军","却说","荆州","二人","不可","不能","如此"} #不断运行程序找到并排除排名靠前但是确定不是人名的词
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1: #去掉只有一个字的情况
        continue
    elif word=="诸葛亮" or word=="孔明曰":
        rword="孔明"
    elif word=="关公" or word=="云长":
        rword="关羽"
    elif word=="玄德" or word=="玄德曰":
        rword="刘备"
    elif word=="孟德" or word=="丞相":
        rword="曹操"
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1 #对分词进行基数，存入字典
for word in excludes: #从字典中删除需排除的词汇
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))