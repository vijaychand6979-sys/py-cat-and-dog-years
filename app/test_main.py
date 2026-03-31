from app.main import get_human_age


def test_less_than_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0], (
        "less than 15 years does not equal [0, 0]"
    )


def test_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1], (
        "first 15 years does not equal [1, 1]"
    )


def test_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2], (
        "24 years does not equal [2, 2]"
    )


def test_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2], (
        "28 years does not equal [3, 2]"
    )


def test_100_years() -> None:
    assert get_human_age(100, 100) == [21, 17], (
        "100 years does not equal [21, 17]"
    )
