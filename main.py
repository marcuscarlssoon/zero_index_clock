from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

figure = plt.figure(figsize=(10, 10), dpi=100)
ax = figure.add_subplot(111, polar=True)

pi = np.pi


def time():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    return hour, minute, second


def reset_axes():
    plt.cla()

    plt.setp(ax.get_yticklabels(), visible=False)
    ax.set_xticks(np.linspace(0, 2 * np.pi, 12, endpoint=False))
    ax.set_xticklabels(range(0, 12))
    ax.set_theta_direction(-1)
    ax.set_theta_offset(np.pi / 2)
    ax.grid(False)


def update(*args):
    reset_axes()

    hour, minute, second = time()

    angle_second = (2 * pi * second) / 60
    angle_minute = (2 * pi * minute) / 60
    angle_hour = (2 * pi * hour) / 12

    ax.plot([angle_second, angle_second], [0, 0.9], color="black", linewidth=3, solid_capstyle='round')
    ax.plot([angle_minute, angle_minute], [0, 0.8], color="black", linewidth=4, solid_capstyle='round')
    ax.plot([angle_hour, angle_hour], [0, 0.5], color="black", linewidth=6, solid_capstyle='round')


ani = FuncAnimation(figure, update, interval=100)
plt.show()
