import psutil
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_ylim(0, 100)
ax.set_title('Uso de CPU e Memória')
ax.set_xlabel('Tempo')
ax.set_ylabel('Uso (%)')

cpu_line, = ax.plot([], [], label='CPU', color='#0d0345')
mem_line, = ax.plot([], [], label='Memória', color='#b55b0d')
ax.legend()

cpu_text = ax.text(0.77, 0.7, '', transform=ax.transAxes)
mem_text = ax.text(0.77, 0.6, '', transform=ax.transAxes)

cpu_data = []
mem_data = []
time_data = []

def upd_chart(frame):
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    time_data.append(frame)
    cpu_data.append(cpu_percent)
    mem_data.append(memory_percent)

    cpu_line.set_data(time_data, cpu_data)
    mem_line.set_data(time_data, mem_data)

    ax.set_xlim(0, max(100, frame)) 

    cpu_text.set_text(f'CPU: {cpu_percent:.1f}%')
    mem_text.set_text(f'Memória: {memory_percent:.1f}%')

    return cpu_line, mem_line, cpu_text, mem_text

anim = FuncAnimation(fig, upd_chart, interval=1000)

ax.set_facecolor('#c7c3bf')

plt.show()
