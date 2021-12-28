import sys
sys.path.append(".")
import pytest
from src.yatzi import Yatzy

@pytest.mark.ChanceSum
def test_chance_scores_sum_of_all_dice():
        assert 15 == Yatzy.chance(2,3,4,5,1)
        assert 16 == Yatzy.chance(3,3,4,5,1)

