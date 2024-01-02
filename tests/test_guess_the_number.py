import pytest
import sys
sys.path.insert(1, '../src/')
from guess_the_number import check_guess

def test_correct_guess():
    # Arrange 
    number_to_guess = 5
    user_input = '5'

    # Act
    result = check_guess(number_to_guess, user_input)
    
    # Assert
    assert result == "Correct guess!"

def test_guess_too_low():
    # Arrange 
    number_to_guess = 5
    user_input = '3'

    # Act
    result = check_guess(number_to_guess, user_input)
    
    # Assert
    assert result == "Too low"

def test_guess_too_high():
    # Arrange 
    number_to_guess = 5
    user_input = '8'
    
    # Act
    result = check_guess(number_to_guess, user_input)
    
    # Assert
    assert result == "Too high"

@pytest.mark.parametrize("number_to_guess, user_input, expected_result", [

    # Arrange
    (5, '5', "Correct guess!"),
    (5, '3', "Too low"),
    (5, '8', "Too high")
])
def test_guesses(number_to_guess, user_input, expected_result):

    # Act
    result = check_guess(number_to_guess, user_input)
    
    # Assert
    assert result == expected_result
