"""
Test Module for FizzBuzz
========================

This module contain test cases for FizzBuzz.

"""
from katapy.simple.fizzbuzz import fizzbuzz


def test_fizzbuzz_prime_number():
    """
    Test the FizzBuzz function with a prime number.

    This function calls the `fizzbuzz` function with the prime number 7
    and asserts that the result is equal to the string representation of
    the number.

    :return:
    :rtype:
    """
    result = fizzbuzz(7)
    assert result == "7"
