import numpy as np
import matplotlib.pyplot as plt #matplotlib.pyplot是调用各种可视化效果的子库
import matplotlib
matplotlib.rcParams['font.family']='SimHei' #pyplot默认不支持中文，需要使用rcParams修改字体
radar_labels=np.array(['研究型(I)','艺术型(A)','社会型(S)',\
    '企业型(E)','常规型(C)','现实型(R)']) #雷达标签
data=np.array([[0.40,0.32,0.35,0.30,0.30,0.88],
    [0.85,0.35,0.30,0.40,0.40,0.30],
    [0.43,0.89,0.30,0.28,0.22,0.30],
    [0.30,0.25,0.48,0.85,0.45,0.40],
    [0.20,0.38,0.87,0.45,0.32,0.28],
    [0.34,0.31,0.38,0.40,0.92,0.28]]) #数据值
data_labels=('艺术家','实验员','工程师','推销员','社会工作者','记事员') #数据标签
angles=np.linspace(0,2*np.pi,6,endpoint=False) #numpy.linspace(start,end,num=num_point)函数用于在线性空间中以均匀步长生成数字序列
                                               #如果不想在序列计算中包括最后一点,增加参数endpoint=False
'''
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
不删掉这两行代码会导致报错：ValueError: The number of FixedLocator locations (7), 
usually from a call to set_ticks, does not match the number of ticklabels (6).
'''
fig=plt.figure(facecolor="white") #设定绘制区域的背景颜色
plt.subplot(111,polar=True) #subplot(nrows,ncols,plotnum)设定子图的行(nrow)，列(ncols),指定子图所在的区域plotnum
                            #如果nrows,ncols,plotnum都小于10可以写成三位数：111表示：1,1,1
                            #polar=True表示使用极坐标绘图
plt.plot(angles,data,'o-',linewidth=1,alpha=0.2) #plot(x,y) x轴，y轴
                                                 #alpha透明度，0-1之间浮点数
                                                 #linewidth线条宽度
                                                 #'0-'表示实心圈标记
plt.fill(angles,data,alpha=0.25) #fill(x,y)对函数与坐标轴之间的区域进行填充
plt.thetagrids(angles*180/np.pi,radar_labels) #matplotlib更新后不需要再加参数frac = 1.2
                                              #thetagrids方法用于设置极坐标角度网格线显示
plt.figtext(0.52,0.95,'霍兰德人格分析',ha='center',size=20) #figtext(x,y,s):向Figure的任意位置添加文本,x,y为坐标(0-1),s为字符串
                                                           #ha or horizontalalignment：对齐方式，center,left or right
legend=plt.legend(data_labels,loc=(0.94,0.80),labelspacing=0.1) #legend()：添加图例
                                                                #loc:图例的位置
                                                                #labelspacing: 图例中条目之间的距离
plt.setp(legend.get_texts(),fontsize='large') #setp()设置图像的属性
                                              #legend.get_texts()：获取并设置图例
plt.grid(True)
plt.savefig('holland_radar.jpg')
plt.show()
