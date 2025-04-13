from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_non_list_input(self):
        # Test with invalid input
        assert CheckoutSolution().checkout("123") == -1
        assert CheckoutSolution().checkout("ABC") == -1
        assert CheckoutSolution().checkout("") == -1

    def test_one_item(self):
        assert CheckoutSolution().checkout(["A"]) == 50

    def test_bulk_discount(self):
        assert CheckoutSolution().checkout(["A, A, A"]) == 130

    def assert_bulk_discount_and_extras(self):
        assert CheckoutSolution().checkout(["A, A, A, A"]) == 180
