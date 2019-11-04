import matplotlib.pyplot as plt
import numpy as np

def simple():
    N = 3
    x = np.array([1, 2, 3])
    y = x + 1
    plt.plot(x, y)
    plt.show()

def hybrid():
    colors = ['red', 'blue', 'green', 'orange']
    for i in range(len(colors)):
        x = np.arange(5)
        y = x + i
        label = str(1948 + i)
        plt.plot(x, y, c=colors[i], label=label)
    #添加图例，loc='upper left表示图例位置在最左侧，一般也可以直接使用loc='best'
    plt.legend(loc='upper left')
    plt.xlabel('Month, Integer')
    plt.ylabel('Unemployment Rate, Percent')
    plt.title('Monthly Unemployment Trends, 1948-1952')
    plt.show()

if __name__ == "__main__":
    # simple()
    hybrid()