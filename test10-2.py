'''
描述
关键行指一个文件中包含的不重复行。关键行数指一个文件中包含的不重复行的数量。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬
统计附件文件中与关键行的数量。
'''

f=open("latex.log")
fo=f.readlines()
gf=set(fo)
print("共{}关键行".format(len(gf))) 