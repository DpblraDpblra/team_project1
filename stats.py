def calculate_mean(numbers):
    '''Функция для подсчета среднего значения'''
    if not numbers:
        raise ValueError('numbers must be not empty')
    return sum(numbers) / len(numbers)
