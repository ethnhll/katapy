def fizzbuzz(number) -> str:
    result = ""
    if number % 3 == 0:
        result += 'fizz'
    if number % 5 == 0:
        result += 'buzz'
    if len(result) == 0:
        result += str(number)
    return result
