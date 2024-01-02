class GuessTheNumber:
    def __init__(self, number):
        self.number_to_guess = number
        self.guess = None

    def check_guess(self, user_input):
        self.guess = int(user_input)

        if self.guess < self.number_to_guess:
            return "Too low"
        elif self.guess > self.number_to_guess:
            return "Too high"
        else:
            return "Correct guess!"
