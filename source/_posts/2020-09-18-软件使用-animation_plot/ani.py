import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

fig, ax = plt.subplots()

# 横坐标取值
m, n = 100, 20
x = np.linspace(0, 4*np.pi, n)

y = np.zeros((m, n))
for i in range(m):
    y[i] = np.sin(x+2*np.pi*i/m)

# 在画纸上画出零时刻第一条线 ln
ln, = ax.plot(x, y[0], 'ro')

def init():
    """FuncAnimation 所需要的动画初始设置, 返回值为零时刻的线 ln"""
    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(i):
    """
    FuncAnimation 所需要的更新函数, 对于第 i 帧, 修改纵轴数据为 y 的第 i 行
    返回值为更新后的第 i 帧对应的线
    """
    ln.set_data(x, y[i])
    return ln,

# 进行绘制. FuncAnimation 的函数文档: https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
my_ani = ani.FuncAnimation(fig=fig, func=update, frames=m, interval=1,
                            init_func=init, blit=False)

# Set up formatting for the movie files (3.7.3 报错, 3.8.5 可以)
writer = ani.FFMpegFileWriter(fps=60, metadata=dict(artist='Me'), bitrate=180)
# 保存图片
# my_ani.save('Harmonic.gif',writer=writer)

plt.show()
