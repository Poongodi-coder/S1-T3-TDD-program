from main_leap_year import is_leap_year

def test_leap_year_pass():
    assert is_leap_year(2000) == True
    assert is_leap_year(2024) == True
    assert is_leap_year(2028) == True

def test_leap_year_fail():
    assert is_leap_year(2005) == False
    assert is_leap_year(2001) == False
    assert is_leap_year(1900) == False