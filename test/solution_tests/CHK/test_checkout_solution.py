import pytest

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    @pytest.mark.parametrize("input_data", [

        123,
        None,
    ])
    def test_non_string_input(self, input_data):
        assert CheckoutSolution().checkout(input_data) == -1

    @pytest.mark.parametrize("input_data", [
        "A1",
        "😄AB",
        "1231"
        "-",
        "A B",
        "ab",
        "AaA",
    ])
    def test_invalid_string_content(self, input_data):
        assert CheckoutSolution().checkout(input_data) == -1

    @pytest.mark.parametrize(
        "input_data, expected_output",
        [
            ("", 0),
            ("A", 50),
            ("C", 20),
            ("AAA", 130),
            ("AAAA", 180),
            ("ABC", 100),
            ("AAABB", 175),
            ("AAAAAAAA", 330),
            ("AAAAAA", 250),
            ("EEB", 80),
            ("EEEEBB", 160),
            ("EE", 80),
            ("EEBBB", 125),
            ("FFF", 20),
            ("FFFFFF", 40),
            ("FFFF", 30),
            ("FF", 20),
            ("PPQR", 180),
            ("RRRRRRRRRQQQ", 450),
            ("UUUU", 120),
            ("SSS", 45),
            ("XYZ", 45),
            ("ZZZYYY", 90),
            ("ZZZXX", 79)

        ],
        ids=[
            "no_items",
            "one_item_has_bulk",
            "one_item_no_bulk",
            "bulk_discount",
            "bulk_discount_and_extras",
            "multiple_items",
            "multiple_bulk_discounts_different_products",
            "multiple_bulk_discounts_same_product",
            "biggest_discount_used",
            "one_freebie",
            "two_freebies",
            "freebie_not_in_basket",
            "freebie_and_discount",
            "buy_three_get_one_free",
            "buy_six_get_two_free",
            "buy_three_get_one_free_plus_one",
            "no_freebies",
            "mix_of_products",
            "discount_fiend",
            "buy_four_get_one_free",
            "group_discount_same_product",
            "group_discount_mixed_products",
            "multiple_group_discounts",
            "Most_expensive_group_discount",
        ],
    )
    def test_checkout(self, input_data, expected_output):
        assert CheckoutSolution().checkout(input_data) == expected_output


