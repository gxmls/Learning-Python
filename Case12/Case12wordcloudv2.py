import jieba
import wordcloud
from imageio import imread #能够读取一个图片文件
mask=imread("heart.png") #词云会生成在有颜色的部位
f=open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
ls2=ls[:]
for word in ls2:
    if len(word)==1:
        ls.remove(word)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",mask=mask,width=1000,height=700,background_color="white",max_words=50,stopwords="的")
w.generate(txt)
w.to_file("grwordcloud_heart.png")
