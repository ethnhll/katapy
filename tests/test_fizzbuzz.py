from katapy.fizzbuzz import fizzbuzz


def test_fizzbuzz_prime_number():
    result = fizzbuzz(7)
    assert result == '7'
