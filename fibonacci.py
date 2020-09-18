def fibonacci_generator(lenght_of_array: int) -> list:
    '''Generate a Fibonacci row, return list.'''
    if not isinstance(lenght_of_array, int) or lenght_of_array <= 0:
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
    print(fibonacci_generator(10))


