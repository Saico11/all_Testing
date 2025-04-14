#Actividad_2

import math

def isPrime(number):
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):
        if number % check == 0:
            return False
    return True

def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1, 2):
        if number % check == 0:
            return False
    return True

def test():
    # Casos para isPrime (original)
    assert isPrime(1) == False
    assert isPrime(2) == False  # Este fallara porque isPrime no maneja el 2 bien
    assert isPrime(3) == True
    assert isPrime(9) == False  # Este fallara porque isPrime retorna True para 9

    # Casos para isPrime2 (corregida)
    assert isPrime2(1) == False
    assert isPrime2(2) == True
    assert isPrime2(3) == True
    assert isPrime2(9) == False
    assert isPrime2(25) == False
