```markdown
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import matplotlib.ticker as ticker

t=np.linspace(-5,5,50)
y1=np.cos(t)
y2=np.cos(t+1)

fig=plt.figure()
ax=axisartist.Subplot(fig,211)
fig.add_axes(ax)



ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)

ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
ax.set_xlim(-5,5)
ax.set_ylim(-1,1)
plt.title('$x(t)$')
plt.plot(t,y1)

ax=axisartist.Subplot(fig,212)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)

ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
ax.set_xlim(-5,5)
ax.set_ylim(-1,1)
plt.title(r'$x(t+t_0)$')
plt.plot(t,y2)

plt.show()
```
<center>
<img
="pingyi1.png">
连续时间信号的平移
</center>

```markdown
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import matplotlib.ticker as ticker

x=np.linspace(-5,5,50)
y1=np.sin(x)
y2=np.sin(x+1)

fig=plt.figure()
ax=axisartist.Subplot(fig,211)
fig.add_axes(ax)



ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)

ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
ax.set_xlim(-5,5)
ax.set_ylim(-2,2)
plt.title('$x[n]$')
plt.stem(x,y1)

ax=axisartist.Subplot(fig,212)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)

ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
ax.set_xlim(-5,5)
ax.set_ylim(-2,2)
plt.title(r'$x[n-n_0]$')
plt.stem(x,y2)

plt.show()
```
<center>
<img
="pingyi2.png">
离散信号的平移
</center>

```markdown
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import matplotlib.ticker as ticker

x=np.linspace(-5,5,50)
y1=np.e**-x*1*np.cos(5*x+2)
y2=np.e**x*1*np.cos(5*-x+2)

fig=plt.figure()
ax=axisartist.Subplot(fig,211)
fig.add_axes(ax)



ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)

ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
ax.set_xlim(-4,4)
ax.set_ylim(-40,30)
plt.title('$x(t)$')
plt.plot(x,y1)

ax=axisartist.Subplot(fig,212)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)

ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
ax.set_xlim(-4,4)
ax.set_ylim(-40,30)
plt.title(r'$x(-t)$')
plt.plot(x,y2)
plt.show()
```

```markdown
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import matplotlib.ticker as ticker

x=np.linspace(-5,5,30)
y1=(x+2) ** 2
y2=(-x+2) ** 2

fig=plt.figure()
ax=axisartist.Subplot(fig,211)
fig.add_axes(ax)



ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)

ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
ax.set_xlim(-10,10)
ax.set_ylim(-5,50)
plt.title('$x[n]$')
plt.stem(x,y1)

ax=axisartist.Subplot(fig,212)
fig.add_axes(ax)

ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)

ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())
ax.set_xlim(-10,10)
ax.set_ylim(-5,50)
plt.title(r'$x[-n]$')
plt.stem(x,y2)
plt.show()
```

```markdown
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec

x11=np.linspace(0,3,10)
x12=np.linspace(3,6,10)
y1=1/3*x11
y11=-1/3*x12+2

x21=np.linspace(0,1,10)
x22=np.linspace(1,2,10)
y2=x21
y21=-1*x22+2

x31=np.linspace(-2,-1,10)
x32=np.linspace(-1,0,10)
y3=(x31+2)
y31=-1*(x32+2)+2

x41=np.linspace(-1,0,10)
x42=np.linspace(-2,-1,10)
y4=-1*x41
y41=x42+2

x51=np.linspace(1,2,10)
x52=np.linspace(0,1,10)
y5=-1*(x51-2)
y51=(x52-2)+2

fig=plt.figure()
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False

ax=axisartist.Subplot(fig,231)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.set_xlim(-1,7)
ax.set_ylim(-1,2)
plt.title(r'$x(t)$')
plt.plot(x11,y1,color='blue')
plt.plot(x12,y11,color='blue')
plt.xticks([3,6,],['3','6'])

ax=axisartist.Subplot(fig,232)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.set_xlim(-1,3)
ax.set_ylim(-1,2)
plt.title(r'$x(3t)$')
plt.plot(x21,y2,color='blue')
plt.plot(x22,y21,color='blue')
plt.xticks([2,],['2'])
plt.xlabel(r'压缩为$\frac{1}{3}$')

ax=axisartist.Subplot(fig,233)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.set_xlim(-3,1)
ax.set_ylim(-1,2)
plt.title(r'$x(3t+6)$')
plt.plot(x31,y3,color='blue')
plt.plot(x32,y31,color='blue')
plt.xticks([-2,],['-2'])
plt.xlabel('波形左平移2')

ax=axisartist.Subplot(fig,234)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.set_xlim(-3,1)
ax.set_ylim(-1,2)
plt.title(r'$x(-3t)$')
plt.plot(x41,y4,color='blue')
plt.plot(x42,y41,color='blue')
plt.xticks([-2,],['-2'])
plt.xlabel('x(3t)反褶')

ax=axisartist.Subplot(fig,235)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->",size=1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("->",size=1.0)
ax.axis["y"].set_axis_direction("left")
ax.set_xlim(-1,3)
ax.set_ylim(-1,2)
plt.title(r'$x(-3t+6)$')
plt.plot(x51,y5,color='blue')
plt.plot(x52,y51,color='blue')
plt.xticks([2,],['2'])
plt.xlabel('波形右平移2')

plt.show()
```
dsfdfsf