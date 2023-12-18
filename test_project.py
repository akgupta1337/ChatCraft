from project import add, prod, yell


def test_add():
    assert add("!add 2+3+4+5") == 14
    assert add("!add 1+2+ 4   +5") == 12
    assert add("!add abcdef") == 0


def test_prod():
    assert prod("!prod 2*3*4") == 24
    assert prod("!prd 2* 4   *8") == 64
    assert prod("!prod abcdef") == "Please enter integers only."


def test_yell():
    assert yell("!yell shutup") == "ShUtUp"
    assert yell("!yell nice") == "NiCe"
    assert yell("!yell aBcD") == "AbCd"
