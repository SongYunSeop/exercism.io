def is_leap_year(year):
    remainder_is_zero = lambda x, y: x % y == 0

    return remainder_is_zero(year, 4) and (not remainder_is_zero(year, 100) or remainder_is_zero(year, 400))
    
