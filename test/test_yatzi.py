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