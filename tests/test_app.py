from app import calculate_remaining_holiday


def test_calculate_remaining_holiday():
    result = calculate_remaining_holiday(25, 5)

    assert result == 20

def test_no_holiday_taken():
    result = calculate_remaining_holiday(25, 0)

    assert result == 25

def test_all_holiday_taken():
    result = calculate_remaining_holiday(25, 25)

    assert result == 0