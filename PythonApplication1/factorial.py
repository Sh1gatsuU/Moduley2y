def calculate_factorial(n):
    """
    ������� ���������� ��������� ����� n.
    
    :param n: ֳ�� �����
    :return: �������� ����� n
    """
    if n < 0:
        raise ValueError("�������� ���������� ����� ��� ����'����� ����� �����")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)
