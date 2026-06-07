user_input = '2'
try:
    num = int(user_input)
    print(f'You picked {num}')
except:
	print(f'{user_input} is not a number!')
