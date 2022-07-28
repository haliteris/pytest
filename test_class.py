# content of test_class.py
class TestClass:
    def test_one(self):
        x = "hello"
        assert "h" in x

    def test_two(self):
        x = "world"
        assert hasattr(x, "check")