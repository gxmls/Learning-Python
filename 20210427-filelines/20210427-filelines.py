#打印输出附件文件的有效行数，注意：空行不计算为有效行数。
f=open("latex.log",'r')
fo=f.readlines()
s=0
for line in fo:
    line=line.strip("\n") #去掉空行
    if len(line)==0:
        continue
    s+=1
print("共{}行".format(s))
