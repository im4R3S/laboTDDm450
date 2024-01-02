import pytest
from guess_the_number import GuessTheNumber

@pytest.fixture
def game():
    return GuessTheNumber(5)  # Initialize the game with a specific number to guess

def test_guess_too_low(game, capsys):
    # Arrange
    expected_output = "Too low"
    
    # Act
    result = game.check_guess(3)

    # Assert
    assert result == expected_output
    captured = capsys.readouterr()
    assert captured.out == ""  # Ensure no output is printed

def test_guess_too_high(game, capsys):
    # Arrange
    expected_output = "Too high"
    
    # Act
    result = game.check_guess(8)

    # Assert
    assert result == expected_output
    captured = capsys.readouterr()
    assert captured.out == ""  # Ensure no output is printed

def test_correct_guess(game, capsys):
    # Arrange
    expected_output = "Correct guess!"
    
    # Act
    result = game.check_guess(5)

    # Assert
    assert result == expected_output
    captured = capsys.readouterr()
    assert captured.out == ""  # Ensure no output is printed

import pytest
from guess_the_number import GuessTheNumber

@pytest.fixture
def game():
    return GuessTheNumber(5)  # Initialize the game with a specific number to guess

@pytest.mark.parametrize("user_input, expected_output", [
    # Test cases for too low guesses
    (3, "Too low"),    # test case 4
    (1, "Too low"),    # test case 5
    (0, "Too low"),    # test case 6

    # Test cases for too high guesses
    (8, "Too high"),   # test case 7
    (10, "Too high"),  # test case 8
    (100, "Too high"), # test case 9

    # Test case for correct guess
    (5, "Correct guess!")  # test case 10
])
def test_guess_game(game, capsys, user_input, expected_output):
    # Act
    result = game.check_guess(user_input)

    # Assert
    assert result == expected_output
    captured = capsys.readouterr()
    assert captured.out == ""  # Ensure no output is printed
