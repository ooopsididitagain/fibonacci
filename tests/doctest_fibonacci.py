import sys
def fibonacci_generator(lenght_of_array: int) -> list:
    '''
    >>> fibonacci_generator(2)
    [1, 1]
    >>> fibonacci_generator('string')
    'Bad input data!'
    '''
    if not isinstance(lenght_of_array, int):
        return 'Bad input data!'
    result = [1, 1, ]
    if lenght_of_array == 1:
        return [1, ]
    elif lenght_of_array == 2:
        return result
    else:
        while (len(result) - 2) != lenght_of_array:
            result.append((result[-1] + result[-2]))
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('Выделено памяти: ',  sys.getsizeof(fibonacci_generator(1)))
    


