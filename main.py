
while True:
    guess = input('Guess a country: ')
    if guess.lower().strip() == 'malawi':
        break
    print('Try again.')

print('Well done!')