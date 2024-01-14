def check_guess(number_to_guess, user_input):
    
    if(user_input < number_to_guess):
        return "Too low"
    elif(user_input == number_to_guess):
        return user_input
  
 