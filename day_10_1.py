# A more efficient implementation for finding the instr. to switch
# than the recursive one.

f = open("day_10.txt")
#f = open("test.txt")
         
input_volts = [int(l.rstrip()) for l in f.readlines()]
input_volts.sort()

combos = [0] * len(input_volts)

def checkCombo(cur, higher, combo):
    if higher - cur > 3:
        return 0

    return combo

def countCombos(volts):
    volts_len = len(volts)
    combos[volts_len - 1] = 1
    for i in reversed(range(0, volts_len - 1)):
        if i + 1 < volts_len:
            combos[i] = checkCombo(volts[i], volts[i + 1], combos[i + 1])
                     
        if i + 2 < volts_len:
            combos[i] += checkCombo(volts[i], volts[i + 2], combos[i + 2])

        if i + 3 < volts_len:
            combos[i] += checkCombo(volts[i], volts[i + 3], combos[i + 3])

    total = (checkCombo(0, volts[0], combos[0]) +
             checkCombo(0, volts[1], combos[1]) +
             checkCombo(0, volts[2], combos[2]))
    print(total)

countCombos(input_volts)
