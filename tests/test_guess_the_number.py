import pytest
import sys
sys.path.insert(1, '../src/')
from guess_the_number import check_guess

def test_correct_guess():
    # Arrange 
    number_to_guess = 5
    user_input = 5

    # Act
    result = check_guess(number_to_guess, user_input)
    
    # Assert
    assert result == user_input


@pytest.mark.parametrize("number_to_guess, user_input", [

    # Arrange
    (5, '5'),
    (5, 'A'),
    
])
def test_guesses(number_to_guess, user_input):

    # Act
    result = check_guess(number_to_guess, user_input )
    
    # Assert
    assert result == int(user_input)

