import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def display_banner():
    '''Display program name in a banner'''
    msg = "Welcome to the guess the nubmer game!!!"
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n',  stars, '\n')


def configure_range():
    '''Set the high and low values for the random number'''
    x = ''
    y = ''
    print('Select the range you would like to guess between:')
    while True:
        x = input('Lower: ')
        y = input('Upper: ')
        if x.isdigit() and y.isdigit():
            break
        print('Please enter two integers')
    return int(x), int(y)


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''

    #guess = input('Guess the secret number? ')

    while True:

        guess = input('Guess the secret number? ')

        if guess.isdigit():

            break

        else:
            print("that is not a valid entry, please try again.")


    return int(guess)

def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high

def main():
    display_banner()
    guessCount = 0 # Counts the amount of guesses
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()

        result = check_guess(guess, secret)
        guessCount += 1 # Increments each time the user guesses
        print(result)

        if result == correct:
            break
    print('You took ' + str(guessCount) + ' guesses') # Displays the total amount of guesses

if __name__ == '__main__':
    main()
