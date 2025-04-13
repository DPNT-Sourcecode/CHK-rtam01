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
        "ZX",
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

    def test_no_items(self):
        assert CheckoutSolution().checkout("") == 0

    def test_one_item_has_bulk(self):
        assert CheckoutSolution().checkout("A") == 50

    def test_one_item_no_bulk(self):
        assert CheckoutSolution().checkout("C") == 20

    def test_bulk_discount(self):
        assert CheckoutSolution().checkout("AAA") == 130

    def test_bulk_discount_and_extras(self):
        assert CheckoutSolution().checkout("AAAA") == 180

    def test_multiple_items(self):
        assert CheckoutSolution().checkout("ABC") == 100

    def test_multiple_bulk_discounts_different_products(self):
        assert CheckoutSolution().checkout("AAABB") == 175

    def test_multiple_bulk_discounts_same_product(self):
        assert CheckoutSolution().checkout("AAAAAA") == 260



