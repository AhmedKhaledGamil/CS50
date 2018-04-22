from cs50 import get_int
from math import floor
from math import log10
from math import fabs

def main():
    credit_number = get_int("Number: ")
    no_digits = digits(credit_number)
    if check(no_digits):
        if validity(credit_number):
            type = creditcard_type(credit_number)
            print(type)
        else:
            print("INVALID")
    else:
        print("INVALID")


def digits(n):
    length = floor(log10(fabs(n))) + 1
    return length


def check(n):
    if n == 13 or n == 15 or n == 16:
        return True
    else:
        return False


def validity(n):
    sum = 0
    j = digits(n)
    for i in range(j):
        x = n % 10
        n = floor(n / 10)
        if i % 2:
            product = x * 2
            if product < 10:
                sum = sum + product
            else:
                for k in range(2):
                    y = product % 10
                    product = floor(product / 10)
                    sum = sum + y
        else:
            sum = sum + x

    sum = sum % 10
    if sum == 0:
        return True
    else:
        return False


def creditcard_type(n):
    x = digits(n)
    if x == 15:
        n = floor(n / (10000000000000))
        if n == 34 or n == 37:
            type = "AMEX"
        else:
            type = "INVALID"
    elif x == 13:
        type = "VISA"
    elif x == 16:
        mcard = floor(n / (100000000000000))
        n = floor(n / (1000000000000000))
        if n == 4:
            type = "VISA"
        else:
            if mcard >= 51 and mcard <= 55:
                type = "MASTERCARD"
            else:
                type = "INVALID"
    return type

if __name__ == "__main__":
    main()

