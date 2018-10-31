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
