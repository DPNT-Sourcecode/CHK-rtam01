from lib.solutions.HLO.hello_solution import HelloSolution

class TestHello():
    def test_hello(self):
        assert HelloSolution().hello("John") == "Hello John"
        assert HelloSolution().hello("Jane") == "Hello Jane"
        assert HelloSolution().hello("Alice") == "Hello Alice"
        assert HelloSolution().hello("Bob") == "Hello Bob"
        assert HelloSolution().hello("Charlie") == "Hello Charlie"
