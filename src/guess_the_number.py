def check_guess(number_to_guess, user_input):
    try:
        user_input = int(user_input)
        if user_input < number_to_guess:
            return "Too low"
        elif user_input == number_to_guess:
            return user_input
    except ValueError:
        return 0
    return 0
