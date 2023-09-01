mår = input("Angi menneskeår: ")


def kår(mår):
    if mår == 1:
        return 15
    elif mår == 2:
        return 24
    else:
        kår = 24 + ((mår - 2) * 4)
        return kår


kår = kår(mår)
print(kår)
