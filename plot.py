import matplotlib.pyplot as plt

def plot_data(data):
    '''Функция визуализации'''

    if not data:
        raise ValueError('data не может быть пустым!')
    plt.plot(data)
    plt.show()

if __name__ == "__main__":
    data = [[1,2,3,4],[1,2,3,4]]
    plot_data(data)
    print('End test')
