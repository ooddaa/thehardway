from nose.tools import *
from game.locations import *


def test_Level1():
    level1 = Level1()
    assert_equal(level1.level_number, 1)
    assert_equal(level1.first_time_visit, True)
