print('Enter a command')
started=False
while True:
    user_command = input('> ').lower()
    if user_command=="start" :
        if started:
            print('car is already started')
        else:
            started= True
            print('car started... Ready to go!!')
    elif user_command=="stop":
        if not started:
            print('car is already stopped')
        else:
            started=False
            print('Car stopped.')
    elif user_command=="help":
        print('use commands start, stop or quit')
    elif user_command=="quit":
        break
    else:
        print('''
you have entered a wrong command 
type "help" to view list of commands''')

print('Thank you, visit again!!!')