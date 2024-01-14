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
