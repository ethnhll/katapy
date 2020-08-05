from katapy.fizzbuzz import fizzbuzz


def test_fizzbuzz_prime_number():
    result = fizzbuzz(7)
    assert result == '7'

def test_fizzbuzz_divisible_by_three():
    result = fizzbuzz(7*3)
    assert result == 'fizz'
