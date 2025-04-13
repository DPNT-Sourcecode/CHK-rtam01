import pytest

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    @pytest.mark.parametrize("input_data, expected", [
        ("123", -1),
        ("ABC", -1),
        ("", -1),
    ])
    def test_non_list_input(self, input_data, expected):
        assert CheckoutSolution().checkout(input_data) == expected

    @pytest.mark.parametrize("input_data, expected", [
        (["A", "AB"], -1),
        (["Z", "X"], -1),
        (["A", "1"], -1),
        (["😄", "A" "B"], -1),
    ])
    def test_invalid_list_content(self, input_data, expected):
        assert CheckoutSolution().checkout(input_data) == expected

    def test_no_items(self):
        assert CheckoutSolution().checkout([]) == 0

    def test_one_item(self):
        assert CheckoutSolution().checkout(["A"]) == 50

    def test_bulk_discount(self):
        assert CheckoutSolution().checkout(["A", "A", "A"]) == 130

    def assert_bulk_discount_and_extras(self):
        assert CheckoutSolution().checkout(["A", "A", "A", "A"]) == 180

    def test_multiple_items(self):
        assert CheckoutSolution().checkout(["A", "B", "C"]) == 100

    def test_bulk_discount_multiple_items(self):
        assert CheckoutSolution().checkout(["A", "A", "B", "B"]) == 145

