def calculate_factorial(n):
    """
    Функція обчислення факторіалу числа n.
    
    :param n: Ціле число
    :return: Факторіал числа n
    """
    if n < 0:
        raise ValueError("Факторіал визначений тільки для невід'ємних цілих чисел")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)
