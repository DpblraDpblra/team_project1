import matplotlib.pyplot as plt

def plot_data(data):
    '''Функция визуализации'''

    if not data:
        raise ValueError('data не может быть пустым!')
    plt.plot(data)
    plt.show()
