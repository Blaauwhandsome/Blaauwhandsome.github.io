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
离散信号的平移
</center>

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

<center>
<img
="pingyi2.png">
离散信号的平移
</center>



```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```