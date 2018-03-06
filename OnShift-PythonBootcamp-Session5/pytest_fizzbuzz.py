# This is the pytest sample
# Good doc on installing pytest: https://docs.pytest.org/en/latest/getting-started.html

from Fizzbuzz import Fizzbuzz

def test_fizzbuzz():
    f = Fizzbuzz()
    assert f.get_fizzbuzz_string(15) == 'Fizzbuzz'

def test_fizz():
    f = Fizzbuzz()
    assert f.get_fizzbuzz_string(6) == 'Fizz'

def test_buzz():
    f = Fizzbuzz()
    assert f.get_fizzbuzz_string(10) == 'Buzz'

def test_empty_string():
    f = Fizzbuzz()
    assert f.get_fizzbuzz_string(14) == ""