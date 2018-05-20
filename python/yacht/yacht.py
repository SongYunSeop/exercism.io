# Score categories
# Change the values as you see fit
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):

    def get_number_dict(dice):
        result = {}
        for x in dice:
            if str(x) in result:
                result[str(x)] += 1
            else:
                result[str(x)] = 1
        return result

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    elif category == ONES:
        return sum([x for x in dice if x == 1])
    elif category == TWOS:
        return sum([x for x in dice if x == 2])
    elif category == THREES:
        return sum([x for x in dice if x == 3])
    elif category == FOURS:
        return sum([x for x in dice if x == 4])
    elif category == FIVES:
        return sum([x for x in dice if x == 5])
    elif category == SIXES:
        return sum([x for x in dice if x == 6])
    elif category == FULL_HOUSE:
        if len(set(dice)) != 2:
            return 0
        for x in set(dice):
            if len([y for y in dice if y == x]) not in (2,3):
                return 0
        else:
            return sum(dice)
    elif category == FOUR_OF_A_KIND:
        for x in set(dice):
            if len([y for y in dice if y == x]) >= 4:
                return x * 4
        else:
            return 0
    elif category == LITTLE_STRAIGHT:
        return 30 if set(dice) == set([1,2,3,4,5]) else 0
    elif category == BIG_STRAIGHT:
        return 30 if set(dice) == set([2,3,4,5,6]) else 0
    elif category == CHOICE:
        return sum(dice)
    else:
        raise Exception()
