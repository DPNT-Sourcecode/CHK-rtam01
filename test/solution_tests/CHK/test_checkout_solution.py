import pytest

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    @pytest.mark.parametrize("input_data", [
        "123",
        "ABC",
        "",
    ])
    def test_non_list_input(self, input_data):
        assert CheckoutSolution().checkout(input_data) == -1

    @pytest.mark.parametrize("input_data", [
        (["A", "AB"]),
        (["Z", "X"]),
        (["A", "1"]),
        (["😄", "A" "B"]),
    ])
    def test_invalid_list_content(self, input_data):
        assert CheckoutSolution().checkout(input_data) == -1

    def test_no_items(self):
        assert CheckoutSolution().checkout([]) == 0

    def test_one_item_has_bulk(self):
        assert CheckoutSolution().checkout(["A"]) == 50

    def test_one_item_no_bulk(self):
        assert CheckoutSolution().checkout(["C"]) == 20

    def test_bulk_discount(self):
        assert CheckoutSolution().checkout(["A", "A", "A"]) == 130

    def test_bulk_discount_and_extras(self):
        assert CheckoutSolution().checkout(["A", "A", "A", "A"]) == 180

    def test_multiple_items(self):
        assert CheckoutSolution().checkout(["A", "B", "C"]) == 100

    def test_multiple_bulk_discounts_different_products(self):
        assert CheckoutSolution().checkout(["A", "A", "A", "B", "B"]) == 175

    def test_multiple_bulk_discounts_same_product(self):
        assert CheckoutSolution().checkout(["A", "A", "A", "A", "A", "A"]) == 260




