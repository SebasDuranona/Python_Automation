# Simple program to verify a password
password = 'password'
tries = 0
print ('Hello, welcome to this app')
print ()
print ('-'*10)
print ('Can I have a name?')

userName = input()

print ('Nice to meet you, ' + userName)
print ()
print ('You see, ' + userName + '... We are not a trustfull bunch...')
print ('I need to confirm you are who you say you are')
print ('PASSWORD???')

userPass = input()

print('-'*10)

if (userPass==password):
    print ('Did not doubt you for a second')
    print()
    print('Welcome to the Criminal Den!')

else:
    print ('No chance in hell you are coming in!')
