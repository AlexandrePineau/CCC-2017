"""J4 CCC 2017 - FAVORITE TIMES"""

def main():
    """MAIN"""
    minutesGoneBy = int(input())

    time = [1, 2, 0, 0]

    faveCounter = 0
    i = 1

    #Loop running for the minutes inserted by the user (Clock function)
    while i <= minutesGoneBy:
        time[3] += 1
        i += 1

        #Turns time[3] into 0 after 10 minutes and time[2] ++
        if time[3] == 10:
            time[3] = 0
            time[2] += 1

        #Turns time to 01:00 when it's 12:60
        if time[0] == 1 and time[1] == 2 and time[2] == 6:
            time[0] = 0
            time[1] = 1
            time[2] = 0
            time[3] = 0

        #Increases hour after 60 minutes up to the 9th hour
        if (time[0] * 10) + time[1] < 9 and time[2] == 6:
            time[2] = 0
            time[1] += 1

        #Hour 9 to 10
        if (time[0] * 10) + time[1] == 9 and time[2] == 6:
            time[2] = 0
            time[1] = 0
            time[0] = 1

        #Hour 10 to 12
        if (time[0] * 10) + time[1] >= 10 and time[2] == 6:
            time[2] = 0
            time[1] += 1

        #Finding the difference between the units of time
        dif2 = [0, 0]
        dif3 = [0, 0, 0]

        dif2[0] = time[2] - time[1]
        dif2[1] = time[3] - time[2]

        dif3[0] = time[1] - time[0]
        dif3[1] = time[2] - time[1]
        dif3[2] = time[3] - time[2]

        #Using the counter for each time there is a constant difference accross each unit of time
        if (time[0] * 10) + time[1] <= 9:
            if dif2[0] == dif2[1]:
                faveCounter += 1

        if (time[0] * 10) + time[1] >= 10:
            if dif3[0] == dif3[1] == dif3[2]:
                faveCounter += 1

    print(time)
    print(faveCounter)
    return main()
main()