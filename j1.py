"""J1 CCC 2017 - DETERMINES QUADRANT OF A POINT"""
def main():
    """MAIN"""
    my_x = int(input())
    my_y = int(input())

    if my_x > 0:
        if my_y > 0:
            print("1")
        else:
            print("4")

    if my_x < 0:
        if my_y > 0:
            print("2")
        else:
            print("3")

    return main()
main()
