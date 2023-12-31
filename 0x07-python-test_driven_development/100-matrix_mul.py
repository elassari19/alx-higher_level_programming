#!/usr/bin/python3
"""defines multiplies"""


def matrix_mul(m_a, m_b):
    """Multiplies
    Args:
        m_a: matrix
        m_b: matrix
    Raises:
        TypeError: not a list.
                    not a list of lists.
                    not integer or float.
        ValueError: empty
        TypeError: not rectangle
        ValueError: can’t be multiplied.
    Returns:
        matrrix: matrrix
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        string = "m_a" if not isinstance(m_a, list) else "m_b"
        raise TypeError("{} must be a list".format(string))

    for element in m_a:
        if not isinstance(element, list):
            raise TypeError("{} must be a list of lists".format('m_a'))

    for element in m_b:
        if not isinstance(element, list):
            raise TypeError("{} must be a list of lists".format('m_b'))

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("{} can't be empty".format('m_a'))

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("{} can't be empty".format('m_b'))

    for element in m_a:
        for item in element:
            if not type(item) in (int, float):
                raise TypeError("{} should contain only integers or floats".format('m_a'))

    for element in m_b:
        for item in element:
            if not type(item) in (int, float):
                raise TypeError("{} should contain only integers or floats".format('m_b'))

    len_m_a = len(m_a[0])
    len_m_b = len(m_b[0])

    for element in m_a:
        if len_m_a != len(element):
            raise TypeError("each row of {} must be of the same size".format('m_a'))

    for element in m_b:
        if len_m_b != len(element):
            raise TypeError("each row of {} must be of the same size".format('m_b'))

    if len_m_a != len(m_b):
        raise ValueError("{} and {} can't be multiplied".format('m_a', 'm_b'))

    new_matrix = [[0 for a in m_b[0]] for x in m_a]
    for i in range(len(m_a)):
        for n in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][n] += m_a[i][k] * m_b[k][n]

    return new_matrix
