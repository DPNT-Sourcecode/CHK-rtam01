from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_invalid_input(self):
        # Test with invalid input
        assert CheckoutSolution().checkout("123") == -1
        assert CheckoutSolution().checkout("ABC") == -1
        assert CheckoutSolution().checkout("") == -1