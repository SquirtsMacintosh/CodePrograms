from isTri import tri_check

#################
# unhappy paths #
#################

def test_zeros(sideOne=0,sideTwo=0,sideThree=0):
    """
    Checks if all 0's passes the traingle test
    """
    assert tri_check(sideOne,sideTwo,sideThree) == False # should return false

def test_one_two(sideOne=4,sideTwo=5,sideThree=10):
    """
    Checks a false version on the adding of side one and two
    """
    assert tri_check(sideOne,sideTwo,sideThree) == False # should return false

###############
# happy paths #
###############

def test_equalateral(sideOne=5,sideTwo=5,sideThree=5):
    """
    Checks if an equalateral triangle passes true
    """
    assert tri_check(sideOne,sideTwo,sideThree) == True # should return true

def test_generic_triangle(sideOne=1,sideTwo=2,sideThree=3):
    """
    Checks if a generic 1,2,3 triangle passes true
    """
    assert tri_check(sideOne,sideTwo,sideThree) == True # should return true
