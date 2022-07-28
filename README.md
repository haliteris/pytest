# **Pytest** at its Best!

Q&A Engineers' best friend. 

This is a key guide which was inspired by PyTest source codes, which are open-source and can be found here: 

https://docs.pytest.org/en/7.1.x/getting-started.html#

------------
**Installation:**
It is easy to install, at your terminal:

$ pip install -U pytest

pytest is functional at your terminal with the keyword 'pytest'.

$ pytest --version

pytest 7.Latest.0


------------
Pytest implements tests at your current directory, using .py files where you used certain keywords or pytest.fuctions.

After you build your code, try pytest at your terminal to start the test. This may require longer time since it tests both the current and sub directories.

**Note:** It is possible to test an exact function with 'quite' reporting mode.

$ pytest -q code_to_test.py

Responds: 1 passed/~~failed~~ in 0.20s.

------------

### **Group multiple tests in a class**

Very basic example including a class to implement multiple test using:

    class TestClass:
        def test_one(self):
            x = "hello"
            assert "h" in x

        def test_two(self):
            x = "world"
            assert hasattr(x, "check")


Pytest finds both test_ prefixed functions. There is no need to subclass anything, but make sure to prefix your class with Test otherwise the class will be skipped. 


As mentioned in source code grouping tests in classes can be beneficial for the following reasons:

- Test organization.

- Sharing fixtures for tests only in that particular class.

- Applying marks at the class level and having them implicitly apply to all tests.

### NOTE:

Pytest users must be aware of that, while testing multiple functions under a class, each test has a unique instance for the class.
To avoid poor test practices, we need to use unique instances. A brief example shows the case:

    class TestClassDemoInstance:
        anyInstance = 0

        def test_one(self):
            self.anyInstance = 1
            assert self.anyInstance == 1

        def test_two(self):
            assert self.anyInstance == 1


While test_one receives a 'pass', second one takes 'fail' since every each test has unique instances.


