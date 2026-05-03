f_name = '20260503\\10-5\\answers.txt'

with open(f_name, 'w') as f:
    flag = True
    print('Please tell me why you like programming.')
    print('Enter "quit" to end the program.')
    while flag:
        answer = input('Your answer: ')
        if answer == 'quit':
            flag = False
            print('Thank you for your answer!')
            break
        else:
            f.write(answer + '\n')

