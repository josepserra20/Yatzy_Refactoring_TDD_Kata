class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        total = 0
        for number in dice:
            total += number
        return total

    @staticmethod
    def yatzy(*dice):
        if len(set(dice)) == 1:
            return 50
        return 0
        
    
    @staticmethod
    def ones(*dice):
        ONE = 1
        return dice.count(ONE) * ONE
    
    @staticmethod
    def twos(*dice):
        TWO = 2 
        return dice.count(TWO) * TWO
    
    @staticmethod
    def threes(*dice):
        THREE = 3
        return dice.count(THREE) * THREE
    
    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) * FOUR

    def fives(self):
        FIVE = 5
        return self.dice.count(FIVE) * FIVE

    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) * SIX
        
    @staticmethod
    def score_pair(*dices):
        sorted_higuest_dice = sorted(dices, reverse=True)
        for number in sorted_higuest_dice:
            if sorted_higuest_dice.count(number) >= 2:
                return number * 2
        return 0

    @staticmethod
    def two_pair(*dice):
        pairs = 0
        number = 1
        result = 0
        while pairs <= 2 and number <= 6:
            if dice.count(number) >= 2:
                pairs += 1
                result += number * 2
            number += 1
        if pairs == 2:
            return result
        else:
            return 0

    @staticmethod
    def three_of_a_kind(*dice):
        for number in dice:
            if dice.count(number) >= 3:
                return number * 3
        return 0

    @staticmethod
    def four_of_a_kind(*dice):
        for number in dice:
            if dice.count(number) >= 4:
                return number * 4
        return 0

    @staticmethod
    def smallStraight(*dice):
        for number in range(1,6):
            if dice.count(number) != 1:
                return 0
        return Yatzy.chance(*dice)
    
    def largeStraight(*dice):
        for number in range(2,7):
            if dice.count(number) != 1:
                return 0
        return Yatzy.chance(*dice)
        
    @staticmethod
    def fullHouse(*dice):
        if Yatzy._pairHouse(*dice) and Yatzy.three_of_a_kind(*dice):
            return Yatzy._pairHouse(*dice) + Yatzy.three_of_a_kind(*dice)
        else:
            return 0


    def _pairHouse(*dice):
        PAIR = 2
        for number in range(6,0,-1):
            if dice.count(number) == PAIR:
                return PAIR * number
        return 0



        
