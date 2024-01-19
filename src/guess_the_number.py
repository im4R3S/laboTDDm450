def check_guess(number_to_guess, user_input):
    try:
        if user_input < 0:
            raise ValueError('Work with Positive Numbers Only')

        if user_input < number_to_guess:
            print("Too low")
            return user_input
        elif user_input == number_to_guess:
            print("Correct")
            return user_input
    except ValueError:
        raise TypeError('Work with Numbers Only')

    return 0
