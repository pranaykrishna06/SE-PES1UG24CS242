
import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


# ==========================================
# 1. TICKET PRICE - BRANCH COVERAGE
# ==========================================

def test_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("visitor", 25, "tuesday", False)


def test_negative_age():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)


def test_age_below_five():
    assert ticket_price("adult", 3, "tuesday", False) == 0


def test_age_exactly_five():
    assert ticket_price("adult", 5, "tuesday", False) == 300


def test_monday_discount():
    assert ticket_price("adult", 30, "monday", False) == 150


def test_saturday_surcharge():
    assert ticket_price("adult", 30, "saturday", False) == 350


def test_sunday_surcharge():
    assert ticket_price("adult", 30, "sunday", False) == 350


def test_normal_weekday():
    assert ticket_price("adult", 30, "tuesday", False) == 300


def test_guided_tour_for_student():
    assert ticket_price("student", 20, "tuesday", True) == 200


def test_guided_tour_for_non_student():
    assert ticket_price("adult", 30, "tuesday", True) == 400


def test_guided_tour_without_student_category():
    assert ticket_price("senior", 65, "tuesday", True) == 300


def test_guided_tour_disabled():
    assert ticket_price("student", 20, "tuesday", False) == 150


# ==========================================
# 2. GROUP DISCOUNT - BRANCH COVERAGE
# ==========================================

def test_invalid_group_size():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)


def test_school_group_twenty_or_more():
    assert group_discount(20, True) == 40


def test_school_group_below_twenty():
    assert group_discount(10, True) == 25


def test_school_group_exactly_twenty():
    assert group_discount(20, True) == 40


def test_non_school_group_fifteen_or_more():
    assert group_discount(15, False) == 20


def test_non_school_group_below_fifteen():
    assert group_discount(10, False) == 10


def test_non_school_group_exactly_eight():
    assert group_discount(8, False) == 10


def test_non_school_group_below_eight():
    assert group_discount(4, False) == 0


# ==========================================
# 3. GALLERY ENTRY - BRANCH COVERAGE
# ==========================================

def test_gallery_full():
    assert gallery_entry(100, 100, False) == "wait"


def test_gallery_over_capacity():
    assert gallery_entry(110, 100, False) == "wait"


def test_gallery_ninety_percent_without_slot():
    assert gallery_entry(90, 100, False) == "queue"


def test_gallery_above_ninety_percent_without_slot():
    assert gallery_entry(95, 100, False) == "queue"


def test_gallery_ninety_percent_with_timed_slot():
    assert gallery_entry(90, 100, True) == "enter"


def test_gallery_below_ninety_percent():
    assert gallery_entry(80, 100, False) == "enter"


def test_gallery_empty():
    assert gallery_entry(0, 100, False) == "enter"
