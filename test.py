from code import fizzBuzz

def test_fizz():
    '''teste fizz'''
    assert fizzBuzz(3) == 'Fizz'
    assert fizzBuzz(5) == 'Buzz'
    assert fizzBuzz(15) == 'FizzBuzz'

test_fizz()