def tri_check(sideOne,sideTwo,sideThree):
    if sideOne == 0 and sideTwo == 0 and sideThree == 0:
        return False
    if sideOne + sideTwo < sideThree:
        return False
    if sideOne + sideThree < sideTwo:
        return False
    if sideThree + sideTwo < sideOne:
        return False
    else:
        return True
