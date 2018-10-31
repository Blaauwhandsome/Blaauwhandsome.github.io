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