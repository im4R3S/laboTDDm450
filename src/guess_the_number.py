def check_guess(number_to_guess, user_input):
    try:
        if not isinstance(user_input, int):
            raise TypeError('Work with Numbers Only')
        if user_input < 0:
            raise ValueError('Work with Positive Numbers Only')


        if user_input < number_to_guess:
            return "Too low"
        elif user_input == number_to_guess:
            return user_input
    except ValueError:
        return 0

    return 0
