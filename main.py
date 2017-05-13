from time import sleep
print('Hello annonymous user, let me get to know you.')
sleep(1.5)
name = raw_input('What is your name? ')
print('Hello ' + name + '!')
sleep(1)
print('My name is a secret')
sleep(1)
def askpermission(question):
    answer = raw_input(question).lower()
    if answer == 'yes':
        return True
    else:
        if answer == 'no':
            return False
        else:
            print('Sorry I didn\'t quite understand that!')
            return askpermission(question)
    



if askpermission('Would you mind telling me your age? '):
    print('Thank you!')
    age = raw_input('So, Whats your age? ')
    sleep(1)
    print('Once again, thank you! Your '+ age)
else:
    print('Thats ok!')





