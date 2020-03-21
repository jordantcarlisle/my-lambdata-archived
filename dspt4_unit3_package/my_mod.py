
# dspt4_unit3_package/my_mod.py


def enlarge(n):
    """
    Multiplies a number by 100

    Param: n (numeric) the number to enlarge

    Return the enlarge number (numeric)
    """
    return n * 100


if __name__ == '__main__':

    print('JUNK')
    print('GLOBAL SCOPE')

    y = float(input("Please input a number to enlarge: "))
    print(enlarge(y))
