"""J3 CCC 2017 - EXACTLY ELECTRICAL """

def main():
    """MAIN"""
    icord_str = input()
    fcord_str = input()
    energy_str = input()

    icord_str_cut  = icord_str.split(' ')
    ixcord_str = icord_str_cut[0]
    iycord_str = icord_str_cut[1]

    fcord_str_cut  = fcord_str.split(' ')
    fxcord_str = fcord_str_cut[0]
    fycord_str = fcord_str_cut[1]

    ixcord = int(ixcord_str)
    iycord = int(iycord_str)
    fxcord = int(fxcord_str)
    fycord = int(fycord_str)
    energy = int(energy_str)

    deltasum = ((fxcord) - (ixcord)) + ((fycord) - (iycord))

    if energy < (fxcord) - (ixcord) or energy < (fycord) - (iycord):
        print("N")
        return main()

    else:
        if deltasum % 2 == 0 and energy % 2 == 0 or deltasum % 2 != 0 and energy % 2 != 0 :
            print("Y")

        if deltasum % 2 == 0 and energy % 2 != 0 or deltasum % 2 != 0 and energy % 2 == 0 :
            print("N")

    return main()
main()