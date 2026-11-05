
import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


# -------------------- ticket_price() tests --------------------

def test_ticket_price_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("visitor", 25, "tuesday", False)


def test_ticket_price_negative_age():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)


@pytest.mark.parametrize("age", [0, 4])
def test_ticket_price_under_five_is_free(age):
    assert ticket_price("adult", age, "tuesday", False) == 0


def test_ticket_price_adult_weekday_without_tour():
    assert ticket_price("adult", 30, "tuesday", False) == 300


def test_ticket_price_monday_half_price():
    assert ticket_price("adult", 30, "monday", False) == 150


@pytest.mark.parametrize("day", ["saturday", "sunday"])
def test_ticket_price_weekend_surcharge(day):
    assert ticket_price("adult", 30, day, False) == 350


def test_ticket_price_student_guided_tour():
    assert ticket_price("student", 20, "tuesday", True) == 200


def test_ticket_price_non_student_guided_tour():
    assert ticket_price("adult", 30, "tuesday", True) == 400


# -------------------- group_discount() tests --------------------

def test_group_discount_invalid_group_size():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)


def test_group_discount_school_group_of_twenty_or_more():
    assert group_discount(20, True) == 40


def test_group_discount_school_group_below_twenty():
    assert group_discount(10, True) == 25


def test_group_discount_non_school_group_of_fifteen_or_more():
    assert group_discount(15, False) == 20


def test_group_discount_non_school_group_of_eight_to_fourteen():
    assert group_discount(8, False) == 10


def test_group_discount_small_non_school_group():
    assert group_discount(4, False) == 0


# -------------------- gallery_entry() tests --------------------

def test_gallery_entry_when_gallery_is_full():
    assert gallery_entry(100, 100, False) == "wait"


def test_gallery_entry_queue_when_at_least_ninety_percent_without_slot():
    assert gallery_entry(90, 100, False) == "queue"


def test_gallery_entry_enter_when_timed_slot_exists():
    assert gallery_entry(95, 100, True) == "enter"


def test_gallery_entry_enter_when_below_ninety_percent():
    assert gallery_entry(80, 100, False) == "enter"
