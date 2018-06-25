"""J2 CCC 2017 - SHIFTY SUM"""

def main():
    """MAIN"""
    num1 = int(input())
    num2 = int(input())

    i = 0
    out = 0

    while i <= num2:
        out += (num1 * (10 ** i))
        i += 1

    print(out)

    return main()
main()
