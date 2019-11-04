import numpy as np
import matplotlib.pyplot as plt

def simple():
    N = 3
    x = np.random.randn(N)
    y = np.random.randn(N)
    c = ["r", "g", "b"]
    plt.scatter(x, y, c=c)
    plt.show()

def hybrid():
    data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.show()


if __name__ == "__main__":
    # simple()
    hybrid()
