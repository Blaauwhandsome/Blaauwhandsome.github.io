'''
# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)
plt.title(r'$f(x)=sin(x)$') 
plt.plot(x, y)
#plt.show()

x1 = [t*0.375*np.pi for t in x]
y1 = np.sin(x1)
plt.subplot(1,2,2)
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') 
plt.plot(x1, y1)
plt.show()
'''

# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def u(t,t0):
    n=0
    for i in t:
        if(i<t0):
           t[n]=0
           n+=1
        else:
           t[n]=1
           n+=1
    return t

x0=-1
x1=np.pi
ω=np.pi
t0=1
#ω=π x1(t)=sin(ωt)u(t)
x=np.linspace(x0,x1,1000)
k=np.linspace(x0,x1,1000)
y=np.sin(ω*x)*u(k,0)
plt.figure("x1(t)=sin(ωt)u(t)")
plt.plot(x,y)

#ω=π t0=1 x2(t)=sin(ω(t-t0)u(t)
x=np.linspace(x0,x1,1000)
k=np.linspace(x0,x1,1000)
y=np.sin(ω*(x-t0))*u(k,0)
plt.figure("x2(t)=sin(ω(t-t0)u(t)")
plt.plot(x,y)


#ω=π t0=-1 x3(t)=sin(ωt)u(t-t0)
x=np.linspace(x0,x1,1000)
k=np.linspace(x0,x1,1000)
y=np.sin(np.pi*x)*u(k,t0)
plt.figure("x3(t)=sin(ωt)u(t-t0)")
plt.plot(x,y)


#ω=π t0=-1 x4(t)=sin(ω(t-t0)u(t-t0)
x=np.linspace(x0,x1,1000)
k=np.linspace(x0,x1,1000)
y=np.sin(np.pi*(x-t0))*u(k,t0)
plt.figure("x4(t)=sin(ω(t-t0)u(t-t0)")
plt.plot(x,y)
plt.show()


