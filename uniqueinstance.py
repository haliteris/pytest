class TestClassDemoInstance:
    anyInstance = 0

    def test_one(self):
        self.anyInstance = 1
        assert self.anyInstance == 1

    def test_two(self):
        assert self.anyInstance == 1