import jieba
import wordcloud
f=open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
ls2=ls[:] #如果不复制一个列表直接从原始列表中删除元素会出现漏删
for word in ls2:
    if len(word)==1:
        ls.remove(word)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,background_color="white")
w.generate(txt)
w.to_file("grwordcloud.png")
