import sys
sys.path.append(".")
from src.yatzi import Yatzy

def test_chance_scores_sum_of_all_dice():
        assert 15 == Yatzy.chance(2,3,4,5,1)
        assert 16 == Yatzy.chance(3,3,4,5,1)

def test_yatzi_same_number():
        assert 50 == Yatzy.yatzy(1,1,1,1,1)
        assert 0 == Yatzy.yatzy(1,2,3,4,5)

def test_ones():
        assert 1 == Yatzy.ones(1,2,3,4,5)
        assert 2 == Yatzy.ones(1,2,1,4,5)
        assert 0 == Yatzy.ones(6,2,2,4,5)
        assert 4 == Yatzy.ones(1,2,1,1,1)
  

def test_twos():
        assert 4 == Yatzy.twos(1,2,3,2,6)
        assert 10 == Yatzy.twos(2,2,2,2,2)
  

def test_threes():
        assert 6 == Yatzy.threes(1,2,3,2,3)
        assert 12 == Yatzy.threes(2,3,3,3,3)
  

def test_fours():
        assert 12 == Yatzy(4,4,4,5,5).fours()
        assert 8 == Yatzy(4,4,5,5,5).fours()
        assert 4 == Yatzy(4,5,5,5,5).fours()
  

def test_fives():
        assert 10 == Yatzy(4,4,4,5,5).fives()
        assert 15 == Yatzy(4,4,5,5,5).fives()
        assert 20 == Yatzy(4,5,5,5,5).fives()
  

def test_sixes():
        assert 0 == Yatzy(4,4,4,5,5).sixes()
        assert 6 == Yatzy(4,4,6,5,5).sixes()
        assert 18 == Yatzy(6,5,6,6,5).sixes()

def test_one_pair():
        assert 6 == Yatzy.score_pair(3,4,3,5,6)
        assert 10 == Yatzy.score_pair(5,3,3,3,5)
        assert 12 == Yatzy.score_pair(5,3,6,6,5)

def test_two_pairs():
        assert 16 == Yatzy.two_pair(3,3,5,4,5)
        assert 18 == Yatzy.two_pair(3,3,6,6,6)
        assert 0 == Yatzy.two_pair(3,3,6,5,4)

def test_three_of_a_kind():
        assert 9 == Yatzy.three_of_a_kind(3,3,3,4,5)
        assert 15 == Yatzy.three_of_a_kind(5,3,5,4,5)
        assert 9 == Yatzy.three_of_a_kind(3,3,3,3,5)

def test_four_of_a_kind():
        assert 12 == Yatzy.four_of_a_kind(3,3,3,3,5)
        assert 20 == Yatzy.four_of_a_kind(5,5,5,4,5)
        assert 12 == Yatzy.four_of_a_kind(3,3,3,3,3)
        assert 0 == Yatzy.four_of_a_kind(3,3,3,2,1)

def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.smallStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.smallStraight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.smallStraight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.smallStraight(1, 2, 3, 4, 6)

def test_largeStraight():
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.largeStraight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.largeStraight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 6)

def test_fullHouse():
    assert 8 == Yatzy.fullHouse(1, 1, 2, 2, 2)
    assert 0 == Yatzy.fullHouse(2, 2, 3, 3, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 4, 4)