# **Pytest** at its Best!

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

# content of test_class.py
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